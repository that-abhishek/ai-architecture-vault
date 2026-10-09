# Part 15: $33,000 to Say Yes

**Track: Engineering.** Cover label `ENGINEERING · PART 15`. Stands on Part 13 (detection cost: a check costs about as much as producing the answer; this part is how to make the check cheap).
Cover title: **$33,000 TO SAY YES**
Cover title alt: **ONE WORD, TWO PRICES**
Spine (Tushar test): *A yes-or-no check doesn't need a model that writes. Use one that picks a box and gives you a probability, and always give it a "none of these" box.*
Target: ~90 s (~230 spoken words). Takeaways T1–T3 are spoken and go on the board word for word.
Vendor naming: Jev and TypeSafe are named on the board and in the caption (editorial change, 24 Sep 2026: a vendor is fine when it's a utility with a real production optimization). The frontier judge is called "a frontier model" on the board. Its name goes in the caption only.

---

## HOOK (talking head)

Your app sends out a million AI answers. Before each one ships, a second model reads it and says yes or no. At frontier prices, that one word costs you thirty-three thousand dollars.

---

## PANEL 1: The judge

**Board:** `answer + source` → big box **FRONTIER JUDGE** → `yes`. Below it, red: **$33,000 / 1M checks**. On the right, two identical `yes` words side by side, one labelled `sure` and one `coin toss`, both with an arrow into `if (yes)`.

You are the judge. An answer comes in with its source, and you check whether it stays inside the source. You run on a frontier model, so you pay frontier price for one word.

There are two problems. a) The bill grows with every answer you check. b) Your yes carries no weight. A sure yes and a coin-toss yes look the same to the code that reads it.

**T1:** Move yes-or-no checks off the frontier model.

---

## PANEL 2: A model that only picks

**Board:** `question` → two boxes with bars: **yes 0.93** / **no 0.07**. Under them a scale 0 → 1 with a line at **0.95**: above = `ship`, 0.6–0.95 = `person`. Corner, green: **Jev · 91.5% agree · $160** against a struck-out red **$33,000**.

Now you are not allowed to write. You get two boxes, yes and no, and you put a number on each. Yes 0.93, no 0.07.

That is a System One model, and Jev from TypeSafe is the first one. You declare the boxes up front, and every box comes back with a probability in one pass.

On six thousand checks of financial research answers, Jev agreed with the frontier judge 91.5 percent of the time. At that rate, a million checks cost a hundred and sixty dollars instead of thirty-three thousand. A cheap open model costs two hundred and sixty, so most of the saving is leaving the frontier model. What Jev adds is the number on each box.

Draw a line at 0.95. Above it ships, and between 0.6 and 0.95 goes to a person.

**T2:** Route on the probability, not on the word.

---

## PANEL 3: The cake recipe

**Board:** a drawn cake → three boxes `billing` / **`technical 0.94`** (red) / `account`. Red: **0 / 30 flagged**. Below, a green dashed box: **none of these**.

It always picks one of your boxes. Testers sent a ticket classifier thirty messages that fit no box. A cake recipe came back as a technical issue at 0.94. Not one of the thirty was flagged.

It cannot return a wrong type. It can return a wrong answer in the right type, with 0.94 on it.

**T3:** Give every question a "none of these" box.

---

## CLOSE (talking head)

How many labelled examples you need to place that line is the next part. Engineering track, vault link in bio.

---

## Verification (checked 24 Sep 2026)

| Claim | Status | Source |
|---|---|---|
| 6,003 rubric checks on financial-research answers; Jev agreed with the frontier judge (Claude Fable 5.1) 91.5% of the time | solid (one study) | Good Start Labs, *Verification is the bottleneck*, 15 Sep 2026, goodstartlabs.com/research/verification-is-the-bottleneck |
| $160 (Jev) vs $33,000 (Fable 5.1) per million graded answers | solid as quoted; extrapolated from 6,003 checks, not a million observed, hence "at that rate" on camera | same; restated in Langfuse, 18 Sep 2026, langfuse.com/blog/2026-09-18-using-typesafes-jev-for-evals |
| Cheap open model (DeepSeek V4.1 Flash) $260, 93.5% agreement | solid as quoted, secondary (Langfuse citing the same study) | Langfuse, 18 Sep 2026 |
| Fields and allowed values declared up front, filled in one pass, probability per value; can't return outside the schema | solid (vendor description; schema compliance also held in independent runs, 23,703 calls, 0 invalid) | typesafe.ai/blog/introducing-system-one-models-and-jev (15 Sep 2026); dev.to independent-tests roundup |
| "First System One model" | vendor's own framing; spoken as "the first one" | TypeSafe launch post |
| 30 out-of-scope messages, 0 flagged without a "none of these" option; cake recipe → technical issue at 0.94 | solid (pre-registered, small n = 30), 20 Sep 2026, model jev-1.13-20260917 | github.com/priorbench/jev |
| Available now, not waitlist-only | solid: model id `typesafe/jev-1.13` on OpenRouter | openrouter.ai/labs/jev |
| 0.95 line, 0.6–0.95 band, yes 0.93 / no 0.07 | illustrative, not measured | — |
| $33,000 in the hook = a million checks on the frontier judge | solid as quoted (same study) | Good Start Labs |

**Dropped:** the "32.5% of answers flip when yes/no are swapped" figure. It came from a secondary roundup and conflicts with a direct option-swap audit that flipped 0 of 400 (jujumilk3/jev-calibration-audit). Not used.
**Kept off camera:** the vendor's "193.6x faster / 444.6x cheaper". Independent testers couldn't find its comparators.
**Couldn't read:** arXiv 2609.24574 (the text-annotation study). The fetch was rate-limited on 24 Sep. Nothing in the script depends on it.

---

## Production notes (24 Sep 2026)

- Shot and cut 24 Sep 2026. Runtime 2:06 (2:04 of speech + 2.5 s silent end card: FRONTIER WRITES / JEV PICKS / A SYSTEM ONE MODEL).
- The three takeaways and the limit line were delivered on camera, not as screen + voice-over. The cards were read word for word.
- The board was hand-drawn as "per 1M tokens" under the $33,000. It was wrong (the figure is per 1M checks) and was removed in the edit.
- "0 / 30 flagged" and rule 3 were spoken but not written on the board in panel 3.
- Audio normalised to −14 LUFS (source was −26 LUFS).
- captions.srt: forced-aligned against the cue cards per speech run. Two stretches (0:31–0:36 and 1:55–end) are proportionally timed, not word-aligned.
