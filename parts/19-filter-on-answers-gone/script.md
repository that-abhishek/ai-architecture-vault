# Part 19: Filter On. Answers Gone.

**Track: Engineering.** Cover label `ENGINEERING`, no part number.
Cover title: **FILTER ON. ANSWERS GONE.** (alt: WHERE AFTER LIMIT.)
Spine (Tushar test): *The role filter ran after the top-five cut, so an intern got an empty list. Filter first, fetch fifty with the cheap search, and let a reranker, which reads the question and each document together, pick the five.*
Target: about 80 s spoken (budget set for 90 s at 2.5 words/s; you ran ~2.8 on Paid Twice).

**Word count (counted):** hook 21 · panel 1 60 · panel 2 60 · panel 3 60 · close 22 · **total 223**
**Numbers spoken:** five, eleventh, fifty. Nothing else.

---

## HOOK (talking head)

You added a role filter to your company's AI search agent so interns can't see salaries. Now interns get empty answers.

---

## PANEL 1: The filter ran last

An intern asks: can I carry over unused leave? Your agent pulls the five closest documents. All five are manager policies. The role filter removes them, and the agent says no policy found. In SQL, that is LIMIT before WHERE.

**R1:** Rule one: put the role filter inside the first query, before any top-k. For the intern, WHERE runs before LIMIT.

**Drawn, in order:**
1. Intern stick figure, bubble: *can I carry over unused leave?*
2. Agent → search box → a stack of five docs, label `top 5`
3. Each of the five tagged red `MGR` (top one reads `MGR: leave encashment`)
4. A `role filter` gate; all five crossed out on the far side, empty tray
5. Red bubble from the agent: **no policy found**
6. Red, under the flow: `LIMIT 5` then `WHERE role` (drawn arrow, not a glyph)
7. Gold **RULE 1**: filter inside the first query, before any top-k · smaller under it: *intern: WHERE before LIMIT*

---

## PANEL 2: Right filter, still cut

Move the filter first. The intern's leave policy survives, and it ranks eleventh. The search turned every document into a vector before anyone asked. Carry-over and encashment read as leave, so they sit together. LIMIT five cuts it again.

**R2:** Rule two: fetch wide with the cheap search, then sort again before the cut. For the intern, fifty in, five out.

**Drawn, in order:**
1. The `WHERE role = intern` gate redrawn at the front of the flow, before search
2. A ranked list 1 … 12, the leave policy written at **#11**
3. A document → small vector, stamped `made before the question`
4. A 2-D dot map: `carry over` and `encashment` as two dots almost touching, both inside a circle labelled `leave`
5. Red cut line under #5, slicing the list above #11, label `LIMIT 5`
6. Gold **RULE 2**: fetch wide with the cheap search, sort again before the cut · smaller: *intern: 50 in, 5 out*

---

## PANEL 3: The second sort

The second sort is the reranker. It reads the question and one document together. It sees carry over in both. The policy moves to the top. It costs one model call per document, so it only sees fifty. A policy below fifty never reaches it.

**R3:** Rule three: log the cited document's rank before reranking. For the leave policy, that's eleventh.

**Drawn, in order:**
1. Second box after the list, labelled `reranker` (cyan), with `top 50` going in
2. One card holding question + document side by side, `carry over` underlined in both
3. Curved arrow lifting the leave policy from #11 to #1, green
4. Under the reranker: `1 call per doc` and `50 calls` (write "x" out; no × glyph in Caveat)
5. A doc at #60, outside the 50 line, crossed red: `never reaches it`
6. Gold **RULE 3**: log the cited doc's rank before reranking · smaller: *leave policy: 11th*

---

## CLOSE (talking head)

The blueprint is in the vault, link in bio. This was the engineering track. Next, we make the agent smarter without retraining.

---

## Hook candidates (for the record)

- **B, chosen:** You added a role filter to your company's AI search agent so interns can't see salaries. Now interns get empty answers.
- A: Your HR bot tells the intern "no policy found". The policy exists, and the intern is allowed to read it.
- C: Your document bot found the right policy and ranked it eleventh. The model only reads the top five.

Panel order changed from the approved spine: the filter now comes first. Hook B promises the filter, so paying it off in panel 1 keeps viewers past second twelve; the reranker follows as the fix for the problem the filter exposes.

---

## Vault notes (not spoken)

- **Why WHERE after LIMIT happens (solid).** Many RAG apps call vector search for top-k, then run a permission check on the results as a separate step. Vector indexes that apply a metadata filter after the approximate search have the same failure: fewer than k results, sometimes zero. Pre-filtering or filtered search inside the index avoids it.
- **Why manager docs crowd the top five (illustrative).** In the scene, managers have more leave documents (encashment, approvals, team calendars), so the closest five are all theirs. Real ratio depends on the corpus.
- **Bi-encoder vs cross-encoder (solid).** The first search embeds query and document separately; the document vector exists before the question. A cross-encoder reranker takes the (question, document) pair as one input and scores it in one forward pass, so cost is linear in candidates. That's why it runs on tens, not the library.
- **Limit (spoken).** Anything ranked below the first-stage cut never reaches the reranker. Rule 3's log is how you notice the cut is too tight.
- **Still check access on the final five.** Pre-filtering decides what gets ranked; the answer step should still re-check the role. Defense in depth, kept out of the reel because it maps to a known principle.
- **Long context.** On a small library you can skip the reranker and put all fifty in the prompt. The filter placement holds either way.

---

## Production notes (final cut, Oct 10 2026)

- **Audio.** Came in quiet this time (−30.8 LUFS, −12.4 dBTP, 2.5% of energy in 1–4 kHz). Chain: high-pass 80 Hz, +4.5 dB at 2.8 kHz, +1.5 dB at 5.5 kHz, +16 dB gain, light FFT denoise, downward expander, two-pass loudness to −14 LUFS / −1 dBTP. After: −14.0 LUFS, −1.3 dBTP, 3.1% in 1–4 kHz, room floor between words 10 dB lower relative to speech. The fixed WAV and remux are in `raw/` (not in the repo).
- **Captions.** `captions.srt`, 89 tiles, ≤3 words / ~18 characters, timed from the fixed cut (Parakeet TDT word timestamps, cross-checked with Whisper small.en). Five tiles spot-checked by re-transcription.
- **On-camera deviations from the cue cards:** "salary" (not salaries) · "unused leaves" · "pulls five closest documents" (no "the") · "One / Two / Three" without "Rule" · "A policy *before* fifty never reaches it" (script: below) · close changed to "Follow along for more such breakdowns", dropping the track line and the bridge.
- **Talking-head animations (Oct 10 2026).** One board-style card (1000×340, top band, at x 40 / y 100) per talking head, timed to word timestamps: hook = only a red "no policy found" card slamming in on "empty answers" (6.64 s; the funnel version was rejected); rule 1 = LIMIT 5 → WHERE role swaps to WHERE role → LIMIT 5; rule 2 = 50 bars, #11 jumps to #1 on "sort again", all but 5 dim on "5 out"; rule 3 = typed log line, 11 circled on "11th". Close left plain. Overlays (PNG-in-MOV with alpha, 30 fps; placed at 6.6 s, 22.1 s, 45.4 s, 69.1 s) are in `raw/19-filter-on-answers-gone/animation/`. SFX synthesised (buzz, pop, whoosh, ding, soft typing), peaks at −9 to −12 dBFS (the first pass at −20 was barely audible), in the same raw folder. The composite is `_production/master_cut.mp4`, the cut to post.
