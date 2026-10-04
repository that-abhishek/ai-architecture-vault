# Cue cards — ENGINEERING (memory graph vs summary)

One card per take, verbatim. The italic line is what goes on the board during that take.

**1 · Hook (face)**
How do you design a delivery chatbot that doesn't ship to the old address? Summarising the chat is not the answer.

**2 · P1**
At turn five, the customer tells your support bot: deliver to Pune.
_draw: turn strip · t5 Pune · gate: evening_

**3 · P1**
At turn forty, they change it to Chennai.
_draw: t40 Chennai_

**4 · P1**
To save tokens, every ten turns the bot drops old messages and rewrites a summary.
_draw: cross out turns 11-30 · note 'every 10 turns: drop old turns, rewrite the summary (save tokens)' · summary v1 box_

**5 · P1**
After four rewrites, both cities are in it and nothing says which is newer.
_draw: v2, v3 box · v4 box 'Pune ... Chennai' · red ? · 'which one?'_

**6 · P1**
The evening gate time went in the first rewrite.
_draw: red arrow out of v1 · 'gate: evening, dropped'_

**7 · P1**
Rule one: keep the raw turns. The summary only points into them.
_draw: RULE 1 in gold, underlined_

**8 · P1**
For this chat, that's turns five and forty.
_draw: small line under it: 'for this chat: turns 5 and 40'_

**9 · P2**
After every turn, one extra model call writes facts instead of a paragraph.
_draw: 'each turn' arrow '+1 model call' box arrow 'facts'_

**10 · P2**
Turn five becomes order, deliver to, Pune.
_draw: ORDER node · dashed deliver_to · t5 arrow to Pune_

**11 · P2**
Turn forty writes Chennai on the same key, so it wins.
_draw: bold deliver_to · t40 arrow to Chennai · strike Pune, 'old' · 'same key, newer wins'_

**12 · P2**
The gate becomes a fact on the building.
_draw: BUILDING node · gate_closes arrow to evening_

**13 · P2**
The customer's question reads the order, and the driver's reads the building.
_draw: customer question arrow to ORDER · driver question arrow to BUILDING_

**14 · P2**
Rule two: store entity, property, value and a timestamp. The newest value on a key wins.
_draw: RULE 2 in gold, underlined_

**15 · P2**
For this order, that's deliver to, Chennai.
_draw: small line under it: 'for this order: deliver_to = Chennai'_

**16 · P3**
This only works if the model writes the same key every time.
_draw: ORDER node · deliver_to arrow to Pune_

**17 · P3**
At turn forty, it writes shipping city instead.
_draw: shipping_city · t40 arrow to Chennai (red label)_

**18 · P3**
That's a new key, so both cities survive and you're back to two answers.
_draw: red bracket · '2 answers'_

**19 · P3**
Rule three: fix the property names before the first write, and reject the rest.
_draw: allowed properties box, shipping_city struck, 'rejected' · RULE 3 in gold, underlined_

**20 · P3**
For this order, that's deliver to, never shipping city.
_draw: small line under it: 'for this order: deliver_to, never shipping_city'_

**21 · P3**
A refund waiting on a photo isn't a fact, so it stays in a short summary.
_draw: dashed box 'short summary: the thread' · refund, waiting on photo_

**22 · Close (face)**
That's the engineering track, and the key list is in the vault. Next, feeding these facts back into the prompt.
