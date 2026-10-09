"""Part 17 reference code: running summary vs memory graph with fixed keys.

Standard library only. `python memory_store.py` runs the self-test.

Scene: a delivery support chat. Turn 5 says "deliver to Pune", turn 8 says the
building gate closes in the evening, turn 40 says "make it Chennai".
"""
from dataclasses import dataclass

# Rule 3: the property list is fixed before the first write.
ALLOWED = {
    "order": {"deliver_to"},
    "building": {"gate_closes"},
}


@dataclass
class Fact:
    entity: str
    prop: str
    value: str
    turn: int  # timestamp: the turn that wrote it


class MemoryGraph:
    """Rule 2: entity, property, value, with a timestamp. Newest value on a key wins."""

    def __init__(self):
        self.current = {}   # (entity, prop) -> Fact
        self.history = []   # every write, old values kept and marked by turn
        self.rejected = []  # writes outside the allowed list

    def write(self, fact):
        if fact.prop not in ALLOWED.get(fact.entity, set()):
            self.rejected.append(fact)  # e.g. order.shipping_city
            return False
        self.history.append(fact)
        key = (fact.entity, fact.prop)
        old = self.current.get(key)
        if old is None or fact.turn >= old.turn:
            self.current[key] = fact
        return True

    def read(self, entity):
        """A question reads only the node it names."""
        return {p: f.value for (e, p), f in self.current.items() if e == entity}


def running_summary(turns, every=10, keep_chars=60):
    """Old way: every N turns, drop the messages and rewrite a summary.

    Stands in for an LLM rewrite with a length budget: it keeps what looks
    important and appends new text. Nothing marks one line as replacing another.
    """
    summary, buffer = "", []
    for i, text in enumerate(turns, 1):
        buffer.append(text)
        if i % every == 0:
            important = [t for t in buffer if "deliver" in t or "Chennai" in t]
            summary = (summary + " " + " ".join(important)).strip()[-keep_chars:]
            buffer = []
    return summary


def self_test():
    turns = ["hi"] * 40
    turns[4] = "deliver to Pune"
    turns[7] = "the building gate closes in the evening"
    turns[39] = "actually, make it Chennai"

    s = running_summary(turns)
    assert "Pune" in s and "Chennai" in s, s       # both cities survive
    assert "gate" not in s, s                        # dropped at the first rewrite

    g = MemoryGraph()
    g.write(Fact("order", "deliver_to", "Pune", 5))
    g.write(Fact("building", "gate_closes", "evening", 8))
    g.write(Fact("order", "deliver_to", "Chennai", 40))
    assert g.read("order") == {"deliver_to": "Chennai"}        # same key, newer wins
    assert g.read("building") == {"gate_closes": "evening"}    # nobody had to rank it
    assert [f.value for f in g.history if f.prop == "deliver_to"] == ["Pune", "Chennai"]

    # Loose keys: the extractor writes a new property at turn 40.
    loose = MemoryGraph()
    loose.write(Fact("order", "deliver_to", "Pune", 5))
    ok = loose.write(Fact("order", "shipping_city", "Chennai", 40))
    assert not ok and loose.rejected[0].prop == "shipping_city"  # rejected, not stored
    assert loose.read("order") == {"deliver_to": "Pune"}        # fix the extractor, re-run

    print("summary :", repr(s))
    print("graph   :", g.read("order"), g.read("building"))
    print("rejected:", [(f.entity, f.prop, f.value) for f in loose.rejected])
    print("ok")


if __name__ == "__main__":
    self_test()
