"""
Refund tool for an AI support agent that never pays the same order line twice.

Part 16 · @ai.transition · ai-architecture-vault

Two tickets (an email, then a chat) wake two agent runs. Neither run knows about
the other, and the order page says "not refunded" until the bank settles. A
per-call idempotency key doesn't help: each run builds its own request and key.

Rule 1: key every action on the thing it changes, not the ticket or the run.
        For a refund, that's the order line.
Rule 2: record every action in your own ledger before calling out, and check
        the ledger, not the downstream status.
Rule 3: one automatic run for any action you can't undo.
        A second refund on the same line goes to a human.

Standard library only. Run `python refund_ledger.py` for the self-test.
"""

import sqlite3
from datetime import datetime, timezone

SCHEMA = """
CREATE TABLE IF NOT EXISTS ledger (
    order_line_id TEXT NOT NULL,
    action        TEXT NOT NULL,
    idem_key      TEXT NOT NULL,
    reason        TEXT NOT NULL,
    amount_paise  INTEGER NOT NULL,
    ticket_id     TEXT,
    status        TEXT NOT NULL CHECK (status IN ('started', 'succeeded', 'failed')),
    created_at    TEXT NOT NULL,
    PRIMARY KEY (order_line_id, action)          -- Rule 1 and Rule 3 in one constraint
);
CREATE TABLE IF NOT EXISTS human_queue (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    order_line_id TEXT NOT NULL,
    action        TEXT NOT NULL,
    reason        TEXT NOT NULL,
    amount_paise  INTEGER NOT NULL,
    ticket_id     TEXT,
    created_at    TEXT NOT NULL
);
"""


def connect(path=":memory:"):
    db = sqlite3.connect(path, isolation_level=None)  # explicit transactions below
    db.executescript(SCHEMA)
    return db


def _now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def refund(db, gateway, order_line_id, amount_paise, ticket_id, reason="not_delivered"):
    """The tool the agent calls. Returns a dict the agent can pass straight to the customer."""
    action = "refund"
    key = f"{order_line_id}:{action}"  # Rule 1: the same key from every ticket and every run

    # Rule 2: claim the action in our own ledger BEFORE any money moves.
    try:
        db.execute("BEGIN IMMEDIATE")
        db.execute(
            "INSERT INTO ledger VALUES (?,?,?,?,?,?,'started',?)",
            (order_line_id, action, key, reason, amount_paise, ticket_id, _now()),
        )
        db.execute("COMMIT")
    except sqlite3.IntegrityError:
        db.execute("ROLLBACK")
        status, first_reason, since = db.execute(
            "SELECT status, reason, created_at FROM ledger WHERE order_line_id=? AND action=?",
            (order_line_id, action),
        ).fetchone()
        if reason != first_reason:
            # Rule 3: a different, possibly legitimate second refund (e.g. goodwill). A person decides.
            db.execute(
                "INSERT INTO human_queue (order_line_id, action, reason, amount_paise, ticket_id, created_at)"
                " VALUES (?,?,?,?,?,?)",
                (order_line_id, action, reason, amount_paise, ticket_id, _now()),
            )
            return {"result": "sent_to_human",
                    "message": "A refund was already issued for this item. A teammate will review this one."}
        # The same decision made again by another run: no money moves.
        return {"result": "already_started", "status": status, "since": since,
                "message": f"Your refund was already started on {since[:10]}."}

    # Only the run that won the ledger row reaches the gateway. The gateway gets the
    # same order-line key, so a retry after a timeout is also safe on its side.
    try:
        gateway.refund(idempotency_key=key, order_line_id=order_line_id, amount_paise=amount_paise)
    except Exception:
        db.execute("UPDATE ledger SET status='failed' WHERE order_line_id=? AND action=?", (order_line_id, action))
        raise
    db.execute("UPDATE ledger SET status='succeeded' WHERE order_line_id=? AND action=?", (order_line_id, action))
    return {"result": "started", "message": "Your refund has been started."}


# --- self-test ---------------------------------------------------------------

class FakeGateway:
    """Stands in for the payment provider: it pays on every call it accepts."""
    def __init__(self):
        self.payouts = []
        self.seen_keys = set()

    def refund(self, idempotency_key, order_line_id, amount_paise):
        if idempotency_key in self.seen_keys:  # what a per-call key gives you
            return
        self.seen_keys.add(idempotency_key)
        self.payouts.append((order_line_id, amount_paise))


if __name__ == "__main__":
    db, gw = connect(), FakeGateway()

    # Run one (email ticket) and run two (chat ticket), same order line.
    r1 = refund(db, gw, "ORD-1042:line-1", 120000, ticket_id="email-881")
    r2 = refund(db, gw, "ORD-1042:line-1", 120000, ticket_id="chat-219")
    assert r1["result"] == "started", r1
    assert r2["result"] == "already_started", r2
    assert len(gw.payouts) == 1, gw.payouts  # ₹1200 paid once, not twice

    # A goodwill credit on the same line is a different decision: it goes to a person.
    r3 = refund(db, gw, "ORD-1042:line-1", 20000, ticket_id="chat-220", reason="goodwill")
    assert r3["result"] == "sent_to_human", r3
    assert len(gw.payouts) == 1
    assert db.execute("SELECT COUNT(*) FROM human_queue").fetchone()[0] == 1

    # A different order line refunds normally.
    assert refund(db, gw, "ORD-1042:line-2", 50000, ticket_id="email-882")["result"] == "started"
    assert len(gw.payouts) == 2

    print("ok:", r2["message"], "|", r3["message"])
