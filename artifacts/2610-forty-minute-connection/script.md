# Part 18: Thinking Off. Flight Missed.

**Track: Engineering.** Cover label `ENGINEERING`, no part number.
Cover title: **THINKING OFF. FLIGHT MISSED.**
Spine (Tushar test): *A model gets one pass per token, so it can only think more by writing more. Turn thinking on only where the answer needs steps, cap it per route because thinking bills as output, and when it's off, put the reasoning field before the answer field so the steps still come first.*
Runtime: 1:35 (speech 0:00–1:35, spoken close, no outro card). ~250 spoken words.
Text below is what was said on camera (transcribed from the master cut), not the pre-shoot draft. Rule lines were spoken as "One / Two / Three", without "Rule".
Topic question: "How would you make your AI agent smarter without training a new model?" Answer taken: make it think longer.

---

## HOOK (talking head)

**On screen 0:00–4:50:** frame-zero headline, the first sentence as text (`headline` image, mid-frame over the shirt, "40-minute" in red). Caption tiles start at sentence two.

Your AI travel agent booked a 40-minute connection across terminals. The customer missed the flight.

---

## PANEL 1: One pass per word

**Board, in order:** `lands 2:00, T1` · `next 2:40, T3` · `transfer: 1 hr` → **one pass** box → first word `book`, circled red · cyan `to think more, write more` · checks out of the box, each looping back in: `gap: 40 min`, `need: 60 min`, red `40 less than 60 ✗` · `book` struck · gold rule, with the travel-agent case under it.

You have three facts. The first flight lands at 2 in Terminal 1. The next leaves at 2:40 from Terminal 3. The transfer takes an hour. Every word you write gets one pass through the model, and your first word was book. To think more, you have to write more. Write each check before the answer, and 40 minutes fails against an hour. That is all thinking is.

**T1:** One: turn thinking on where the answer needs steps. For an AI travel agent, that's connection check.

---

## PANEL 2: What thinking costs

**Board, in order:** short bar `reply 300` · long red bar `thinking 6,000` · red **21x** `the output, every call` · box `connection check` / cyan `cap: few thousand` · gold rule, with the route case under it.

Thinking was off for a reason. Every thinking token is billed as output. A 300-token reply with 6,000 tokens of thinking is 21 times the output, on every call.

**T2:** Two: set a thinking cap per route, not what the model allows. For a connection check, a few thousand tokens.

---

## PANEL 3: The steps, for free

**Board, in order:** dashed grey `one pass` / `thinking: off` · JSON `{ book: yes` (red) `reason: ... }` · red arrow `written first` / `no checks yet` · JSON redrawn `{ checks: gap 40, need 60` (cyan) `book: no` (green) `}` ✓ · gold rule, with the booking case under it.

You can get the same steps back without paying for thinking. With thinking off, the agent's only working is the reply itself, written in order. Its JSON asked for book first and reason second. So it wrote yes before a single check existed, and the reason after it defends a decision it never worked out.

**T3:** Three: when the thinking is off, put the reasoning field before the answer field. For a booking, the connection check comes before book: yes.

---

## CLOSE (talking head)

Thinking adds steps, not facts. If the agent has wrong transfer time, it checks the wrong number very carefully. The full breakdown is in the vault. Link in bio. Follow along for more such breakdowns.

---

## The reference code

`thinking_router.py` in this folder, standard library only. `ROUTES` holds a thinking cap per route, with fact lookups at 0 and unknown routes falling back to 0, not the model maximum. `output_multiple(300, 6000)` returns 21. `connection_checks()` writes the agent's skipped checks out one per line and ends on `book: no`. `reasoning_first()` flags a JSON schema whose answer field comes before its reasoning field. `python thinking_router.py` runs the self-test.

---

## Vault notes (not spoken)

- **Why writing more is thinking more.** A transformer spends a fixed amount of compute per generated token, and each new token can read every token before it. Writing intermediate steps buys more passes and gives later passes something to read. Thinking modes are the same mechanism with the steps hidden from the reply.
- **Why field order stops mattering when thinking is on.** Hidden thinking is generated before any visible output, so the decision is already worked out by the time the JSON starts. Rule 3 is only for the thinking-off path.
- **Billing.** Thinking tokens are billed at the output-token rate across the major providers, including when only a summary of the thinking is returned. Checked against secondary sources on 5 Oct 2026; the provider pricing pages are the primary source. 300 / 6,000 / 21x is a scene number: (300 + 6,000) / 300.
- **Limit.** Thinking adds steps, not facts. If the transfer time in context is wrong, more thinking checks the wrong number more carefully. Said on camera in the close.
- **Not used on camera:** research showing longer thinking can lower accuracy on simple tasks. It supports Rule 1, but it's a study result, so it stays here.
- **Wider, not longer.** The other no-retraining lever is sampling several answers and picking one with a checker (code, SQL, schema). Considered for this part and dropped for one mechanism per part; a candidate for a later one.

---

## Production notes

- **Hook.** Wrong-answer scene with the surprise in sentence one. "How would you…" was rejected for the hook as leaning on Paid Twice.
- **Frame-zero headline.** First part with the hook's first sentence as on-screen text from frame zero (`headline` image, 0–4.5 s), placed mid-frame over the shirt because the top third covered his face. Caption tiles hand over at 4.56 s. This is the part's experiment variable (see `meta.json`).
- **Rules.** General-then-case form, as in Parts 16 and 17.
- **Canvas.** Explanation written first, board drawn to match it step by step. `canvas_reference.svg` is the pre-shoot reference; `canvas.jpg` is the board as drawn.
- **Audio.** Came in quiet this time (DJI transmitter under the T-shirt). Fixed in post: high-pass 80 Hz, +5 dB at 2.8 kHz, +2 dB shelf at 6 kHz, downward gate between words, loudness to −14 LUFS. Before: −28.4 LUFS, −11.1 dBTP, 2.8% of energy in 1–4 kHz, gaps 23 dB below speech. After: −14.3 LUFS, −1.0 dBTP, 3.8%, gaps 36 dB below speech. The final export measures −11.3 LUFS integrated, −0.9 dBTP.
- **Captions.** `captions.srt`, 106 tiles of up to 3 words / ~18 characters, starting at 4.56 s (sentence one is the headline). Timed from the fixed audio with word timestamps (Parakeet TDT via sherpa-onnx, cross-checked with Whisper small.en); five random tiles spot-checked by re-transcription. Both models heard "needs step"; captions show "needs steps".
- **On-camera deviations from the cue cards:** "One / Two / Three" without "Rule"; "not what the model allows" (card: "not the maximum the model allows"); "that's connection check"; "the same steps back"; "When the thinking is off"; "the connection check comes before book: yes" (card: "the checks come before"); "has wrong transfer time"; close is the vault / link in bio / follow line instead of a bridge to the next part.
- **Master cut.** Final export with headline and captions burnt in, 66 MB, H.264 ~5.5 Mbps; under GitHub's 100 MB limit, so not re-encoded.
- **Cover.** `reel_cover.png` (1080×1920), same layout as Parts 16 and 17.
- **Posting.** Posted from the phone so the Meta AI voice-translation toggle (Portuguese) was available; the desktop upload flow doesn't show it.
