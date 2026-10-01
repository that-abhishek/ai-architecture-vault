# Cue cards — ENGINEERING · PART N (paid twice)

One card per step. Verbatim. Captions are cut from these. The line under each card is what gets drawn during that take.

**1 · Hook (face)**
How would you design a refund agent that doesn't do multiple refunds? And an idempotency key isn't enough.

**2**
The customer emails about a missing parcel. Run one refunds it.
_Draw: email → run 1 → refund() → ORDER_

**3**
She asks again on chat. Run two starts, knowing nothing about run one.
_Draw: chat → run 2 · crossed link to run 1_

**4**
It refunds again. You have paid twelve hundred rupees twice.
_Draw: run 2 → refund() → ORDER · Rs 1200 × 2_

**5**
Rule one: key every action on the thing it changes, not the ticket or the run. For a refund, that's the order line.
_Draw: RULE 1 — general, then refund: order line_

**6**
Your key catches a double click, one request sent twice.
_Draw: double click: key A, key A → blocked ✓_

**7**
Run two sends its own request and key.
_Draw: run 2: key A, key B → passes ✗_

**8**
Run two checks the order. It says not refunded until the bank settles.
_Draw: check order → NOT REFUNDED · bank: still settling ✗_

**9**
The key catches repeated requests. This is a repeated decision.
_Draw: request ≠ decision_

**10**
Rule two: record every action yourself before calling out, and check your record. For a refund, that's your ledger.
_Draw: RULE 2 — general, then refund: your ledger_

**11**
Run two calls refund. The ledger already has this order line.
_Draw: run 2 → refund() → LEDGER · order line ✓_

**12**
The tool moves zero rupees and replies: already started. The agent passes that on.
_Draw: already started → customer · Rs 0 moved_

**13**
The ledger also blocks a real second refund, like a goodwill credit.
_Draw: goodwill credit → human_

**14**
Rule three: one automatic run for any action you can't undo. For refunds, a second one goes to a human.
_Draw: RULE 3 — general, then refund: a 2nd one → human_

**15 · Close (face)**
The ledger code is in the vault, link in bio. This was the engineering track.
