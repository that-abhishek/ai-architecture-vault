# Cue cards — Forty Minutes Across Terminals

One card per take. Words are verbatim from script.md; captions are cut from these. The line under each card says what gets drawn during that take.

---

**HOOK — 1**
Your AI travel agent booked a forty-minute connection across terminals.
_On screen: frame-zero headline, same words, top third._

**HOOK — 2**
The customer missed the flight.
_On screen: headline off, caption tiles start._

---

**P1 — 1**
You have three facts. The first flight lands at two in Terminal 1. The next leaves at two forty from Terminal 3. The transfer takes an hour.
_Drawn: the three fact lines._

**P1 — 2**
Every word you write gets one pass through the model, and your first word was "book".
_Drawn: box "one pass", one arrow per word; "book" circled in red._

**P1 — 3**
To think more, you have to write more.
_Drawn: check lines coming out one under another, each looping back into the box._

**P1 — 4**
Write each check before the answer, and forty minutes fails against an hour. That is all thinking is.
_Drawn: "gap: 40 min", "need: 60 min", 40 less than 60 with a red cross; "book" crossed out._

**P1 — 5**
Rule one: turn thinking on where the answer needs steps. For an AI travel agent, that's the connection check.
_Drawn: gold rule; "AI travel agent: the connection check" smaller under it._

---

**P2 — 1**
Thinking was off for a reason. Every thinking token is billed as output.
_Drawn: nothing new — box from P1 visible._

**P2 — 2**
A three-hundred-token reply with six thousand tokens of thinking is twenty-one times the output, on every call.
_Drawn: short bar "reply 300", long red bar "thinking 6,000", "21x the output", "every call"._

**P2 — 3**
Rule two: set a thinking cap per route, not the maximum the model allows. For the connection check, a few thousand tokens.
_Drawn: route box "connection check — cap: few thousand"; gold rule with the case under it._

---

**P3 — 1**
You can get the steps back without paying for thinking.
_Drawn: "thinking: off", P1 box greyed._

**P3 — 2**
With thinking off, the agent's only working is the reply itself, written in order. Its JSON asked for "book" first and "reason" second.
_Drawn: JSON block, `book: yes` on top in red, `reason: ...` under it._

**P3 — 3**
So it wrote "yes" before a single check existed, and the reason after it defends a decision it never worked out.
_Drawn: arrow "written first" at `book: yes`; red note "no checks yet"._

**P3 — 4**
Rule three: when thinking is off, put the reasoning field before the answer field. For a booking, the checks come before "book: yes".
_Drawn: block redrawn — `checks: gap 40, need 60` on top, `book: no` last; gold rule with the case under it._

---

**CLOSE — 1**
Thinking adds steps, not facts. If the agent has the wrong transfer time, it checks the wrong number very carefully.
_On screen: talking head._

**CLOSE — 2**
Next on the engineering track: [NEXT PART — not decided].
_On screen: outro card._
