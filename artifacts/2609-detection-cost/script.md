# Part 13 — Your Agent's Errors Return 200
**Badge:** RELIABILITY • PART 13 · **Cover:** YOUR AGENT'S ERRORS RETURN 200 · *alt:* TRUTH IS EXPENSIVE. PROVENANCE IS CHEAP.
**Runtime:** ≈ 1:26 at ~1.7 words/sec · 148 words · **Experiment:** E1b — narrative cold open, follow ask after rule one

Tight base, written to be improvised over. The beats carry the argument; the phrasing is a floor, not a script. Say it your way on the take — the only lines worth protecting word-for-word are the three rules and *cost of checking is equal to cost of producing*, because those are what get screenshotted.

Nothing work-identifiable anywhere — no employer, no client, no internal object names. The example objects are generic: ids and numbers.

To trim: cut the follow ask (−4s) and beat 2.1 (−8s) → ~1:14. Never cut a rule.

---

## HOOK — 0:00–0:13 · 22 w

> **"so... your agent returned a wrong answer. But.. the status is 200. the json is valid. And the retry logic never triggered."**

`BOARD` Nothing yet. Face full frame. On **"the status is 200"** cut to board; the green `200` is already drawing.

The pauses are the hook. `so...` then a beat. `But..` then a beat. Three flat statements read off a dashboard, not performed.

---

## PANEL 1 — NO EXCEPTION IS COMING — 0:13–0:32 · 32 w

**1.1** — "Every retry you've written assumes the failure announces itself."
`BOARD` Classic row: `call → 500 → catch → retry`, the `500` in red, `retry` in green.

**1.2** — "A hallucination returns success. Right shape, wrong content. Nothing to catch."
`BOARD` Agent row: `call → 200 → valid JSON → wrong`. `200` in **green** — let it sit a beat before the red `wrong` lands. Then: `nothing threw. retry never fired.`

**1.3** — "Rule one. The failure looks like a success."
`BOARD` Gold rule + underline, drawn on "Rule one".

---

## FOLLOW ASK — 0:32–0:37 · 8 w

> **"Building agents? Follow — this is the layer."**

`BOARD` No cut to face. Gold lower-third over the Panel 1 rule while the hand starts Panel 2. The drawing never stops.

---

## PANEL 2 — DETECTION COSTS PRODUCTION — 0:37–1:00 · 40 w

**2.1** — "Everywhere else, spotting the failure was free. The exception arrives on its own."
`BOARD` `classic: detect = the exception = free`

**2.2** — "Here, only another model call knows it's wrong. Cost of checking is equal to cost of producing."
`BOARD` `agent: detect = another model call`, the bar `produce 1× · check 1× · = 2×`, then `cost of checking = cost of producing`

**2.3** — "Rule two. Detection has a minimum cost attached to it."
`BOARD` Gold rule + underline.

---

## PANEL 3 — TRUTH VS PROVENANCE — 1:00–1:22 · 38 w

**3.1** — "Don't ask is this true. That's the expensive question."
`BOARD` Red: `"is this true?" → another model call → $$`

**3.2** — "Ask whether every id and number came from the input. A string operation. Free — and it catches invented objects."
`BOARD` Green: `"did every id and number come from the input?" → a string op → free`. Under it: `grounding catches invention. schema catches shape.`

**3.3** — "Rule three. Ground for free. Buy truth only where the action is irreversible."
`BOARD` Cyan: `buy truth only where the action is irreversible`, then gold rule + underline. **Hold two beats.**

---

## END — 1:22–1:26 · 8 w

> **"Runnable lab in the vault. Link in bio."**

`BOARD` Cut to face.

---

## The three rules, for the board

1. **RULE: the failure looks like a success**
2. **RULE: detection has a minimum cost**
3. **RULE: ground for free. buy truth rarely** *(board form — the cyan box above carries the "where". Say the full line.)*

## Spoken vs silent

| On the board, never spoken | Why |
|---|---|
| `better model → rarer, not louder` | the invariance argument; reading it lands, saying it sounds defensive |
| `a green suite means nothing until you know it can go red` | a whole second episode; leaving it unspoken is the cheapest tease you have |

## Room to improvise

- **1.1 and 2.1** are the two setup beats. They exist to be said loosely — stretch them, add the aside about backoff or circuit breakers if it comes out naturally. They're also the first things to cut if the take runs long.
- **1.2** — say `right shape` and `wrong content` as two sentences with a real gap. The gap is where the viewer gets it.
- **2.2** is the line the reel exists for. Slow down and land it clean.
- **3.2** — "invented objects" means an id that was never in the input at all. If it needs a concrete example on the take, invent a neutral one; don't reach for anything from work.
- Don't smile on the `200`. Let the board do the joke.

## Colour map
`#00FFFF` cyan concepts · `#FF5252` red the failure · `#4ADE80` green the working path (and the deceptive `200`) · `#FFD700` gold rules, follow ask, CTA
