# Part 13: Your Agent's Errors Return 200

### 0. 🧭 Why This Matters (the production decision)
**The decision this episode is for: your agent returned something wrong, and you are about to wrap the call in a retry. It will never fire, because nothing failed — and the check that would catch it costs as much as the call itself.**

Every retry, backoff and circuit breaker you have ever written rests on an assumption you probably never examined: that a failure announces itself. A timeout, a 500, a thrown exception — something arrives, unprompted, to tell you the call went wrong. A hallucination arrives as a success. Right status, right shape, wrong content. There is nothing to catch, so there is nothing to retry.

And it does not improve away. A better model hallucinates less often; it does not hallucinate more loudly. The failures get rarer, which means they are less likely to surface in testing and more likely to reach production unnoticed. The problem gets quieter, not smaller — which is why this is an architectural invariant and not a capability gap waiting on the next release.

The three rules the reel delivers:
1. **The failure looks like a success.** No exception, no status code, nothing to branch on. Retry semantics are inert here.
2. **Detection has a minimum cost.** The only thing that knows the answer is wrong is another model call, so checking costs what producing cost. Everywhere else you have worked, detection was free.
3. **Ground for free, buy truth where it's irreversible.** "Is this true" is the expensive question. "Did this come from the input" is a string operation.

### 1. 🎯 The 1-Sentence Production Paradox
Because a wrong answer and a right answer are indistinguishable at the transport layer — both HTTP 200, both schema-valid, both plausible — the only oracle that can tell them apart is another inference call, which means error *detection* in an agent loop has a cost floor equal to error *production*, and the entire discipline is deciding which calls are worth paying it on.

### 2. 🔬 Systems Invariants

- **The failure has no signal:**

```text
classic    call → 500 → catch → retry          detection cost ≈ 0
agent      call → 200 → valid JSON → wrong     detection cost ≈ 1 model call
```

Nothing in the response carries correctness. Status, schema and plausibility are all satisfied by the wrong answer. This is a property of the interface, not of the model, so no amount of model quality removes it.

- **Detection cost is bounded below by production cost:**

$$C_{\text{verified}} = C_{\text{produce}} + C_{\text{detect}} \approx 2\,C_{\text{produce}}$$

You cannot verify every call and stay solvent, so verification becomes a budgeting decision rather than a hygiene one. That is the shape that has no analogue in conventional systems engineering, where `try/catch` costs nothing to add.

- **Model progress makes it quieter, not smaller:**

Let $p$ be the per-call hallucination rate. A better model lowers $p$. It does not change the *detectability* of the event, which stays at one model call. So expected verification spend is flat in $p$, while your vigilance decays with it — rarer failures mean fewer testing encounters, weaker intuitions, and more of the remaining ones reaching production.

- **Truth is expensive, provenance is cheap:**

| Question | Mechanism | Cost | Catches |
|---|---|---|---|
| "Is this true?" | second model call | 1× production | semantic error, requires world knowledge |
| "Is the shape right?" | schema validation | ~0 | malformed output, missing fields, bad enums |
| "Did every id and number come from the input?" | string containment | ~0 | **invention — an id that was never in the input** |

The third row is the one people skip, and it is the only free check that catches hallucination *specifically*. Fabrication is the failure mode where the model produces a well-formed, plausible identifier that has no source. Grounding catches it mechanically; nothing else does.

- **A green suite means nothing until you know it can go red:**

Non-deterministic output breaks the usual test contract. Comparing against a recorded output flakes constantly; not comparing passes always and catches nothing. The only evidence a suite tests anything is a **kill rate** — deliberately broken versions of the function that your assertions must catch. Flake rate and kill rate are two numbers moving in opposite directions, and both have to be satisfied.

### 3. ⚙️ Production Trade-offs & Failure Modes
- **Verification budget is the real design decision:** you cannot afford 2× on every call, so the question becomes which calls earn it. The defensible line is irreversibility — a reversible action can be corrected after the fact; an irreversible one cannot, so it is where the second model call belongs.
- **Grounding has a precision limit:** string containment catches invented identifiers cleanly, but it will not catch a *correctly copied* value used in the wrong place, and it produces false positives on legitimate paraphrase or unit conversion. It is a high-value cheap check, not a complete one.
- **The evaluator inherits the generator's blind spots:** if the checking call shares the generator's full context, it tends to agree with the reasoning it is reading. Separate context, narrower question, different framing — otherwise you are paying 2× for a rubber stamp.
- **Rarer failures decay your testing:** as $p$ drops, the failures stop appearing in routine work. Mutation testing is what keeps the suite honest once real failures are too rare to encounter naturally.
- **Beyond the reel:** the second injection surface (tool results are untrusted text re-entering the loop on every turn), sampling strategies for verification budgets, and the open question of what to do when the *checking* call is the one that hallucinates.

### 4. 🎨 Whiteboard Drawing Plan (3 panels, black board / white marker / cyan · red · green · gold)
Drawn canvas: `canvas.jpg`. Pre-draw the Panel 1 top row before rolling — it is the heaviest ink in the set and carries no surprise; only the second row is a reveal.

**Panel 1 — "No exception is coming"** (start drawing under the hook — E1b)
- Two four-box chains, stacked. Top, labelled `everything you've built`: `call → 500 → catch → retry`, the `500` in red, `retry` in green.
- Bottom, labelled `your agent`: `call → 200 → valid JSON → wrong`. **The `200` is drawn in green.** That is the joke — let it sit a beat before the red `wrong` lands.
- Red line under: `nothing threw. retry never fired.`
- Silent, small: `better model → rarer, not louder`
- Rule: **RULE: the failure looks like a success**

**Panel 2 — "Detection costs production"**
- Two rows: `classic → detect = the exception = free` in green, `agent → detect = another model call` in red.
- Dashed divider, then the cost bar: `produce 1×` (white box) · `check 1×` (red box) · `= 2×`.
- Under it, the line the reel exists for: `cost of checking = cost of producing`
- Small: `on every call you choose to check`
- Rule: **RULE: detection has a minimum cost**

**Panel 3 — "Truth vs provenance"**
- Red: `"is this true?" → another model call → $$`
- Green, two lines: `"did every id and number come from the input?" → a string op → free`
- White: `grounding catches invention. schema catches shape.`
- Cyan box: `buy truth only where the action is irreversible`
- Silent, small: `a green suite means nothing until you know it can go red`
- Rule: **RULE: ground for free. buy truth rarely** *(board form — say the full line)*

### 5. 📝 Master Beat Sheet — Spoken Line ↔ What's On The Board

Runtime ≈ 1:26 at ~1.7 words/sec (148 words). Written tight, to be improvised over — the beats carry the argument, the phrasing is a floor. The four lines worth protecting word-for-word are the three rules and *cost of checking is equal to cost of producing*, because those are what get screenshotted. To trim: cut the follow ask (−4s) and beat 2.1 (−8s) → ~1:14. Never cut a rule.

Nothing work-identifiable anywhere — no employer, no client, no internal object names. The example objects are generic: ids and numbers.

```text
── HOOK ──────────────────────────────────────────  0:00 – 0:13   [22 w]
SAY   "so... your agent returned a wrong answer. But.. the status is 200.
       the json is valid. And the retry logic never triggered."
BOARD nothing yet. Face full frame. On "the status is 200" cut to board;
      the green 200 is already drawing.
      The pauses are the hook. "so..." then a beat. "But.." then a beat.
      Three flat statements read off a dashboard, not performed.

── PANEL 1: NO EXCEPTION IS COMING ───────────────  0:13 – 0:32   [32 w]
1.1  SAY   "Every retry you've written assumes the failure announces itself."
     BOARD classic row: call → 500 → catch → retry

1.2  SAY   "A hallucination returns success. Right shape, wrong content.
       Nothing to catch."
     BOARD agent row: call → 200 → valid JSON → wrong. Let the green 200 sit
           a beat before the red "wrong". Then "nothing threw. retry never fired."

1.3  SAY   "Rule one. The failure looks like a success."
     BOARD gold rule + underline, drawn on "Rule one"

── FOLLOW ASK ────────────────────────────────────  0:32 – 0:37   [8 w]
SAY   "Building agents? Follow — this is the layer."
BOARD NO cut to face. Gold lower-third over the Panel 1 rule while the hand
      starts Panel 2. The drawing never stops.

── PANEL 2: DETECTION COSTS PRODUCTION ───────────  0:37 – 1:00   [40 w]
2.1  SAY   "Everywhere else, spotting the failure was free. The exception
       arrives on its own."
     BOARD classic: detect = the exception = free

2.2  SAY   "Here, only another model call knows it's wrong. Cost of checking
       is equal to cost of producing."
     BOARD agent: detect = another model call; then produce 1× · check 1× · = 2×;
           then the line "cost of checking = cost of producing"

2.3  SAY   "Rule two. Detection has a minimum cost attached to it."
     BOARD gold rule + underline

── PANEL 3: TRUTH VS PROVENANCE ──────────────────  1:00 – 1:22   [38 w]
3.1  SAY   "Don't ask is this true. That's the expensive question."
     BOARD red: "is this true?" → another model call → $$

3.2  SAY   "Ask whether every id and number came from the input. A string
       operation. Free — and it catches invented objects."
     BOARD green: "did every id and number come from the input?" → a string op
           → free. Under it: grounding catches invention. schema catches shape.

3.3  SAY   "Rule three. Ground for free. Buy truth only where the action is
       irreversible."
     BOARD cyan box, then gold rule + underline. Hold two beats.

── END ───────────────────────────────────────────  1:22 – 1:26   [8 w]
SAY   "Runnable lab in the vault. Link in bio."
BOARD cut back to face.
```

**Spoken vs deliberately silent**

| On the board, never spoken | Why |
|---|---|
| `better model → rarer, not louder` | the invariance argument; reading it lands, saying it sounds defensive |
| `a green suite means nothing until you know it can go red` | a whole second episode; leaving it unspoken is the cheapest tease available |

### 6. 🎬 Notes for the Edit
- **E1b applies** — rerun of Part 12's E1, which came in at 24s against a `>=25` win line. Variable this time is a narrative cold open plus a shorter runtime, so the metric is retention % (avg watch ÷ runtime), not seconds. Baseline 20%, win ≥30%.
- **Three variables moved at once** versus Parts 11/12: hook shape, follow-ask placement (0:32, not the end card), and runtime. Read the result as a package, then hold all three fixed for Part 14 so they become baseline.
- **The follow ask sits after rule one, not at the end.** Average watch was ~24s on the 2:00 cuts, so an end-card ask is spoken to whoever is left. Straight after the first rule puts it just past the drop-off cliff, at the first moment the viewer has been paid.
- **Panel 1's green `200` is the retention device.** Don't smile on it, don't rush it. Let the board do the joke.
- **Audio chain, as shipped:** 85 Hz HPF (24 dB/oct), −3 dB @ 250 Hz Q1.2, +3 dB @ 3 kHz Q0.8, +1.5 dB shelf @ 9 kHz, 3:1 compression, two-pass loudnorm to −14 LUFS / −1.0 dBTP. Measured before: −20.8 LUFS, rumble −1.4 dB @ 20–80 Hz, presence 3.7 dB @ 3–5 kHz. After: −14.0 LUFS, rumble −7.2 dB, presence 15.7 dB. Video stream copied untouched.
- **Not graded.** Face measured 90 luma (~35 IRE) against a 144-luma window — backlit. The fix is the camera position, not four nodes per episode: turn 90° so the window is a side key.
- **No music.** Parts 11 and 12 both run voice and room tone only; Part 12 has a 4.02 s stretch of near-silence a bed would make impossible. If music gets tested, it should be the single variable on a later episode.
- Caption colour map (Part 11/12 convention): cyan `#00FFFF` concepts, red `#FF5252` the failure, green `#4ADE80` the working path (and the deceptive `200`), gold `#FFD700` rules and CTA.
