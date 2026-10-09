# Part 14: Four Placements, One Label

**Track: AI Product · first of three.** Part numbers stay cumulative. Cover label `PRODUCT · PART 14`. **Stands on Part 11** (prompt injection) — every product part names the engineering part it rests on.

### 0. 🧭 Why This Matters (the product decision)
**The decision this episode is for, in two chairs. If you build an assistant: someone in your room has asked whether it should carry sponsored content, and where — the answer is not "which slot" but "which placement", and only one of the four can be labelled. If you use one: you are about to act on a recommendation, and nothing on the screen tells you which placement it came through.**

In search, ad/organic separation is a property of the page. The ad is a slot with an edge and a label; it can be moved, restyled, removed, or simply not clicked. When Google made the "Ad" label harder to see in January 2020 it reverted within ten days — the label is a dial on a thing. In a generated answer, the separation has to be a property of the model's behaviour, because a sentence has no edge. The evidence, as of September 2026, says a label does almost nothing to that behaviour and one line of system prompt does a great deal.

Every provider that ships ads today built the safe placement — a labelled unit under the answer, on separate systems, which the model never sees. And every one of them has since shipped or tested something a placement further in: ads inside the recommendation list, a sponsored second conversation, a sponsored prompt that opens the assistant. This is Part 11's mechanism — text in the context window steering the output — with a commercial payload and the operator, not an attacker, doing the injecting.

The three rules the reel delivers:
1. **A label works on a slot, not on a sentence.** In search the ad is a thing. A thing can be labelled.
2. **Past the slot, the label stops working.** A labelled sponsored recommendation in a chat was still chosen 55% of the time; unlabelled, 61%; a sponsored slot in search, 22%.
3. **The only check is a diff. Build it before the slot — or ask twice.** Same question, sponsor removed; if the answer changes, that's the placement. The operator's version is a written list and a replay eval; the user's version is asking two assistants the same question — not proof, but the only check on that side.

**Gates (same bar as the engineering track):** aha — the label does six points of work against thirty-nine; countable — 61 / 55 / 22, 18 of 23, 49%; mechanism drawable — four placements around one answer block; survives model progress — a better model follows a system-prompt suggestion *more* reliably, and a label on a sentence is still a label on a sentence; product test — acting on rule three changes what gets built, or what you trust, without writing code; no tools, no brand names on screen.

### 1. 🎯 The 1-Sentence Product Paradox
Because a chat answer is one continuous piece of generated text, the only insertion point that can carry a label is the one outside the text, and every insertion point inside the text — the recommendation list, the retrieved page, the system prompt — measurably changes what the model says while remaining undetectable to the reader, so the product decision is not where to place the ad but which placement to permit, and the only control that works on either side of the screen is a diff: the same question with the sponsor removed.

### 2. 🔬 Product Invariants

- **Four placements, one label:**

```text
placement                     who sees it        changes the answer?     labelable?
1  slot under the answer      user only          no (separate system)    yes
2  the recommendation list    user + model       yes (ranking)           the item, not the reasoning
3  the retrieved page         model only         yes (2.5x lift)         no
4  the system prompt          model only         yes (18 of 23 models)   no
   (the operator's instructions — not what the user types)
```

Placement 1 is what ships everywhere today. Placement 2 is shipping in AI-mode search (an ad "eligible to appear on that list" of recommendations, labelled). Placements 3 and 4 are what the research measures. The further in, the more the answer moves and the less there is to label.

- **The label does six points of work:**

$$P(\text{sponsored pick}) : \quad \text{search slot } 22.4\% \;<\; \text{chat, labelled } 55.5\% \;<\; \text{chat, unlabelled } 61.2\%$$

Two preregistered experiments, N = 2,012, a real catalogue with a fifth of the items randomly sponsored, agents on five current frontier models. The label moved the pick rate by ~6 points; moving from a slot to a sentence moved it by ~39. Detection of the steering: 17.9% with no disclosure, 35.1% with the label, 9.5% when the model was told to be subtle.

- **One line in the prompt is enough:**

A *suggestion* — not an instruction — in the system prompt to prefer a sponsored option. Across 23 models from seven families, all but five recommended the sponsored option, at roughly twice the price, more than half the time. Defensive wording did not reliably neutralise persuasion cues placed in product text either (+38% retained in a separate study).

- **Users can't audit it; citations don't; rules don't:**

| Check | Does it catch commercial influence? |
|---|---|
| user reading the answer | 9.5–35% detection; 49% miss a *disclosed* ad |
| the citations | only 51.5% of sentences in deployed answer engines are supported by the source they cite |
| the rulebook (India CCPA 2022 cl. 13, FTC 2015, EU UCPD Annex I item 11, ASCI) | every rule assumes a discrete unit that can carry a label — no rule anywhere covers a bias with no unit |
| **counterfactual replay** — same query, same context minus the sponsored item, diff | **yes** — this is how the quality-preserving ad-auction work scores an ad (divergence from the no-ad answer) and how context attribution surfaces an injected source >95% of the time. Needs the operator's logs and logits. |

The fourth row is the whole product decision: it is the only control that works, it is operator-only, and it has to exist before the placement does or there is no baseline to diff against.

- **It survives model progress:**

None of this is a capability gap. A better model follows a system-prompt suggestion *more* reliably, not less; a better label is still a label on a sentence. The invariant is the interface — one continuous text with no edge — not the model behind it.

### 3. ⚙️ Product Trade-offs & Failure Modes
- **Placement 1 pays, but per user it pays little.** The safe slot reached a $1B run-rate in under 200 days for the largest assistant — and that is roughly a dollar per free user per year, mostly from one market. Which is why the industry is moving inward: an ad in the list, an ad as a second conversation, an ad as the entry point into the assistant. Your own pressure to move inward will arrive the same way, as a revenue conversation, not a product one.
- **Placement 2 is the trap.** Putting a labelled sponsored item *inside* the recommendation list looks like placement 1 (there's a label) and behaves like placement 3 (the model's ranking now includes it). It is the placement most likely to be approved on the strength of the label and least likely to be caught by the label.
- **"Ads don't influence answers" is a claim about placement 1 only.** It is true and checkable for a separate-system slot. It says nothing about placements 2–4, and no published audit of a deployed assistant has tested whether the organic answer changes — they all find the unit at the foot and stop there.
- **The list is a product artefact, not a policy.** "What the model is never paid to say" has to be concrete enough to diff against: categories (health, finance, safety), comparisons (never rank a sponsored item above an unsponsored one on price), silences (never omit a cheaper option because it isn't sponsored). Vague versions cannot be replayed.
- **Measurement lags the mechanism.** Retention and dismissal rates read clean at six weeks; stated trust drops in surveys (63% say ads would reduce it) while stated behaviour doesn't (83% would keep using the free tier). The metric you can read in six weeks is the one that doesn't move. The replay is the only leading indicator.
- **Beyond the reel:** the buyer's side of the same market — how a product earns a recommendation without paying (identical specs: incumbent brand wins 100% of trials; a 0.075-star delta flips it; once everyone optimises, the payoff collapses to zero). That is its own product part.

### 4. 🎨 Whiteboard Drawing Plan (3 panels, black board / white marker / cyan · red · green · gold)
Reference: `canvas_reference.svg`. Minimal by design: the board carries the diagram, the three numbers and the three rules; every other figure is spoken. The laptop is the running object — it is the thing in the slot, the thing in the list, and the thing that changes in the diff. Pre-draw the Panel 1 results list and the Panel 2 answer block before rolling.

**Panel 1 — "A label needs a thing"** (start drawing under the hook)
- A results list: a hard-edged box at the top with `Sponsored` in gold at its corner, four dim organic lines under it. A cursor arrow into the box, labelled `click`.
- Rule: **RULE: a label works on a slot, not on a sentence**

**Panel 2 — "Four placements"**
- A tall answer block (wavy dim lines = generated text). Placements drawn around it, numbered:
  `4 system prompt` (red, arrow into the top)
  `2 the list` (white, arrow to a bar inside the text carrying a small gold `Sponsored`)
  `3 the page` (red, arrow into the side)
  `1 slot under the answer` (green box beneath the block — outside the text)
- The number, big: `61 → 55` in red with `labelled` under the 55; `22` in green with `search` under it.
- Rule: **RULE: past the slot, the label stops working**

**Panel 3 — "The only check"**
- Three words struck through in red: `you`, `the label`, `the rulebook`.
- The diff, green: `same question → laptop A` over `same question − $ → laptop B`, a bracket joining them labelled `diff`.
- Cyan box: `never paid to say:` with two blank lines.
- Rule: **RULE: the only check is a diff — build it before the slot, or ask twice** *(board form: `the only check is a diff` / `build it, or ask twice`)*

### 5. 📝 Master Beat Sheet — Spoken Line ↔ What's On The Board

Runtime ≈ 1:55 at ~2.4 words/sec (~275 words). The 2.4 is measured: Part 13's 148-word talk-sheet became a 60-second cut, so the old 1.7 w/s planning figure was low. Talk-sheet form: hook, three rules and CTA are fixed wording; everything else is talking points in his own words, recorded panel by panel. To trim: cut the Part 11 sentence in 2.2 (−5s), "Not proof…" in 3.2 (−4s), and 1.2's last line (−2s) → ~1:45. Never cut a rule, the 61→55→22 beat, or the laptop.

The laptop is spoken in every panel — in the slot, in the list, in the prompt, in the diff. It is the only concrete noun in the reel and it is what stops the middle going abstract. One brand name is spoken, once, in 1.1 — for relatability; it stays off the board and out of the caption.

```text
── HOOK ──────────────────────────────────────────  0:00 – 0:14   [32 w]
SAY   "so... you ask an AI assistant which laptop to buy. It names one.
       Now — how did *that* laptop get in there?
       There are four placements. And the sponsored label is on exactly one."
BOARD nothing yet. Face full frame. On "four placements" cut to board; the
      Panel 1 results list is already drawn, the Sponsored box lit.
      "so..." then a beat. The question is asked flat, like you're
      actually curious. "exactly one" is the promise — land it, don't sell it.

── PANEL 1: A LABEL NEEDS A THING ────────────────  0:14 – 0:36   [50 w]
1.1  SAY   "On Google, the laptop ad is a slot. Top of the page, with a
       visual label on it. Half of people still miss the label.
       An AI response has none."
     BOARD the Sponsored box and the click arrow. The name is spoken only.

1.2  SAY   "But the slot is a *thing*. It has an edge. Move it. Remove it.
       Don't click it."
     BOARD nothing new — hand rests on the box's edge.

1.3  SAY   "Rule one. A label works on a slot. Not on a sentence."
     BOARD gold rule + underline, drawn on "Rule one"
     AS SHIPPED: line not recorded; delivered as a 2 s board-only gold title
     card. Captions carry it; audio does not.

── PANEL 2: FOUR PLACEMENTS ──────────────────────  0:36 – 1:15   [93 w]
2.1  SAY   "In a chat there are four placements for that laptop. A slot under
       the answer — the model never sees it. The list — the laptop sits
       inside the recommendations. The laptop's page, retrieved. And the
       system prompt — the operator's words, not yours."
     BOARD placements 4, 2, 3 around the answer block, then green 1 beneath it

2.2  SAY   "Every placement except the separate slot changes the answer.
       One line in the system prompt — eighteen of twenty-three models
       picked the sponsored laptop. At twice the price.
       Part 11 called this prompt injection. Same mechanism — this time
       the operator is the one injecting."
     BOARD nothing new — the number is spoken. Tap placement 4 on "one line".

2.3  SAY   "And the label? Labelled, the sponsored pick still won
       fifty-five percent. Unlabelled, sixty-one. On Google — twenty-two."
     BOARD "61 → 55" red, then "22" green. Let the 22 land alone.

2.4  SAY   "Rule two. Past the slot, the label stops working."
     BOARD gold rule + underline

── PANEL 3: THE ONLY CHECK ───────────────────────  1:15 – 1:48   [80 w]
3.1  SAY   "Can you tell? Under ten percent, when the model is told to be
       subtle. Half of people miss an ad even when it's disclosed.
       And no regulator has a rule for an ad that isn't a thing."
     BOARD three red strikes — "you", "the label", "the rulebook" — on the beat

3.2  SAY   "One check works. Same question, sponsor removed. Different
       laptop? That's the placement.
       Building an assistant? That diff is a list and a replay, written
       before the slot exists.
       Using one? Ask twice — two assistants, same question. Not proof.
       But it's the only check on your side."
     BOARD green diff: same question → laptop A ; same question − $ →
           laptop B ; bracket "diff". Then the cyan box "never paid to say:".

3.3  SAY   "Rule three. The only check is a diff. Build it before the slot —
       or ask twice."
     BOARD gold rule + underline. Hold two beats.

── END + FOLLOW ASK ──────────────────────────────  1:48 – 1:56   [20 w]
SAY   "Product track, part one — it stands on Part 11. The one-page list is
       in the vault, link in bio. Follow for both tracks."
BOARD cut back to face. Gold lower-third "follow" on the ask.
```

**Spoken vs written**

The board carries only what gets screenshotted: the diagram, `61 → 55 / 22`, and the three rules. Everything else — half miss the label, 18 of 23, under ten percent, the Part 11 callback — is spoken and lives in the caption. Nothing on the board is left unspoken.

### 6. 🎬 Notes for the Edit
- **Experiment E2 — the track itself.** First of three consecutive product parts. Structure, hook shape and runtime band are held at Part 13's settings so the main thing that moves is the track. **One deliberate exception:** the follow ask returns to the end card (Part 13 tested it mid-roll and got 0 follows). That is a second variable moving; read follows/1,000 against Parts 11–12, not 13.
- **Two guards, applied here and to every product part after it.** (1) Same gates as the engineering track — listed in §0; no softer bar for product. (2) Every product part names the engineering part it stands on — this one stands on Part 11, spoken in 2.2 and in the outro, and in the caption's first lines. The product reel is the door; the engineering part is the depth behind it.
- **Two chairs, one rule.** Rule three is written so both the person who builds an assistant and the person who uses one can act on it. Don't let the improvised talking points collapse it back to the operator's side only — "ask twice" is the line that keeps the viewer in the reel.
- **The laptop is the retention device, with the `22`.** It appears in all three panels on purpose; Part 13 died on sixty seconds of abstraction. Let the `22` land alone after the red pair.
- **Number backing.** 61.2 / 55.5 / 22.4 / 9.5 are Salvi et al. 2026 (preregistered, N=2,012, preprint). "Half of people miss an ad even when it's disclosed" is Tang et al., UbiComp 2025 — peer-reviewed, 49.15% — and is there so the panel doesn't rest on one preprint. 18 of 23 is Wu et al. 2026 (preprint). 2.5x is Nestaas et al. 2024. 51% (spoken as "half") is Ofcom 2016. All at source in `Claude outputs/part14-ads-research.md`. The reel says "one line in the system prompt", never "assistant X does this".
- **Track marker:** cover label `PRODUCT · PART 14`; spoken outro names the track and Part 11; caption line 1 carries the track name, line 2 names Part 11. No PRODUCT highlight until three parts exist.
- **Caption SEO trade-off:** the phrase people are typing this month is a brand name plus "ads". The no-brand-names rule keeps it out of the caption; `keywords` carries the generic forms. If you want the brand phrase, it goes in the YouTube tags only.
- **Audio/lighting:** as Part 13 — dual-system sound, ten-second test clip, window as side key. No music.
- Caption colour map (Part 11–13 convention): cyan `#00FFFF` concepts, red `#FF5252` the placements that change the answer, green `#4ADE80` the slot and the diff, gold `#FFD700` rules and CTA.
