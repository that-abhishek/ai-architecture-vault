"""
Thinking budget per route, and the reasoning field before the answer field.

Part 18 · @ai.transition · ai-architecture-vault

An AI travel agent booked a 40-minute connection across terminals. It had every
fact: lands 2:00 in T1, next leaves 2:40 from T3, transfer takes an hour. With
thinking off, its first written word was "book". A model gets one pass per
token, so the only way it thinks more is by writing more.

Rule 1: turn thinking on where the answer needs steps, off where it needs a fact.
        For a travel agent, that's the connection check.
Rule 2: set a thinking cap per route, not the maximum the model allows.
        Thinking tokens are billed as output: 300 reply + 6,000 thinking = 21x.
Rule 3: when thinking is off, put the reasoning field before the answer field.
        For a booking, the checks come before "book".

Standard library only. Run `python thinking_router.py` for the self-test.
"""

from datetime import datetime

# Rule 1 + Rule 2: thinking is a per-route decision with its own cap.
# 0 means thinking off. Numbers are illustrative; set them from your own evals.
ROUTES = {
    "order_status":     {"thinking_tokens": 0},     # a fact lookup: no steps
    "baggage_policy":   {"thinking_tokens": 0},     # a fact lookup: no steps
    "connection_check": {"thinking_tokens": 3000},  # several dependent checks
    "rebooking":        {"thinking_tokens": 4000},  # checks plus a choice
}


def thinking_budget(route: str) -> int:
    """Cap for a route. Unknown routes get no thinking, not the model maximum."""
    return ROUTES.get(route, {"thinking_tokens": 0})["thinking_tokens"]


def output_multiple(reply_tokens: int, thinking_tokens: int) -> float:
    """How many times the reply's output you pay for, since thinking bills as output."""
    return (reply_tokens + thinking_tokens) / reply_tokens


# The checks the agent skipped, written out one per line.
def connection_checks(lands: str, lands_terminal: str, departs: str,
                      departs_terminal: str, transfer_minutes: int) -> list[str]:
    fmt = "%H:%M"
    gap = int((datetime.strptime(departs, fmt) - datetime.strptime(lands, fmt)).seconds / 60)
    need = transfer_minutes if lands_terminal != departs_terminal else 30
    return [
        f"gap: {gap} min",
        f"need: {need} min ({lands_terminal} to {departs_terminal})",
        f"{gap} {'>=' if gap >= need else '<'} {need}",
        f"book: {'yes' if gap >= need else 'no'}",
    ]


# Rule 3: with thinking off, the reply is the only working the model gets,
# and it is written in schema order. Answer first means decided before checked.
ANSWER_FIELDS = {"book", "answer", "decision", "approved"}
REASONING_FIELDS = {"checks", "reasoning", "reason", "steps"}


def reasoning_first(schema: dict) -> bool:
    """True if every reasoning field comes before every answer field."""
    keys = list(schema["properties"])
    reasoning = [i for i, k in enumerate(keys) if k in REASONING_FIELDS]
    answers = [i for i, k in enumerate(keys) if k in ANSWER_FIELDS]
    if not reasoning or not answers:
        return True
    return max(reasoning) < min(answers)


BAD_SCHEMA = {"type": "object", "properties": {
    "book": {"type": "boolean"},
    "reason": {"type": "string"},
}}

GOOD_SCHEMA = {"type": "object", "properties": {
    "checks": {"type": "array", "items": {"type": "string"}},
    "book": {"type": "boolean"},
}}


def _self_test() -> None:
    assert thinking_budget("order_status") == 0
    assert thinking_budget("connection_check") > 0
    assert thinking_budget("something_new") == 0, "unknown routes must not get max thinking"

    assert output_multiple(300, 6000) == 21.0

    steps = connection_checks("14:00", "T1", "14:40", "T3", 60)
    assert steps[0] == "gap: 40 min"
    assert steps[-1] == "book: no"
    assert connection_checks("14:00", "T1", "15:30", "T3", 60)[-1] == "book: yes"

    assert not reasoning_first(BAD_SCHEMA)
    assert reasoning_first(GOOD_SCHEMA)

    print("connection check:", " | ".join(steps))
    print("21x:", output_multiple(300, 6000))
    print("self-test passed")


if __name__ == "__main__":
    _self_test()
