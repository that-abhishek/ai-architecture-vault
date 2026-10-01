# Part 16: Paid Twice, Key and All

**Track: Engineering.** Cover label `ENGINEERING`. The cover carries no part number from this part on.
Cover title: **PAID TWICE. KEY AND ALL.**
Spine (Tushar test): *Two support tickets wake two agent runs, and a per-call idempotency key can't see that they're the same decision. Key the refund on the order line, record it in your own ledger first, and send a second refund to a human.*
Runtime: 1:17 (speech 0:00–1:14, outro card after). ~208 spoken words.
Text below is what was said on camera (transcribed from the master cut), not the pre-shoot draft. Rule lines were spoken as "One / Two / Three", without "Rule".

---

## HOOK (talking head)

How would you design a refund AI agent that doesn't do multiple refunds? And an idempotency key is not enough.

---

## PANEL 1: Two tickets, two runs

**Board, in order:** `email` → `run 1` → `refund()` → **ORDER** · `chat` → `run 2`, with a crossed-out link between run 1 and run 2 · `run 2` → `refund()` → **ORDER** · red **Rs 1200 × 2** · gold rule, with the refund case under it.

The customer emails about a missing parcel. Run 1 refunds it. She asks again on chat. Run 2 starts, knowing nothing about run 1. It refunds again. You have paid 1200 rupees. Twice.

**T1:** One: key every action on the thing that it changes, not on the run or the ticket ID. For a refund, that's your original order line.

---

## PANEL 2: Why your key missed

**Board, in order:** `double click` → `key A` `key A` → green **blocked ✓** · `run 2` → `key A` red `key B` → red **passes ✗** · `check order` → order page **NOT REFUNDED**, red `bank: still settling` ✗ · cyan **request ≠ decision** · gold rule, with the refund case under it.

Your key catches a double click. One request sent twice. Run 2 sends its own request and key. Run 2 checks the order. It says not refunded until the bank settles. The key catches repeated requests. This is a repeated decision.

**T2:** Two: record your every action before calling out, and check your records. For a refund, that's your ledger.

---

## PANEL 3: The tool says no

**Board, in order:** `run 2` → `refund()` → **LEDGER** with `order line ✓` · green `already started` → `customer` · green **Rs 0 moved** · `goodwill credit` → dashed → gold `human` · gold rule, with the refund case under it.

Run two calls refund. The ledger already has this order ID. The tool moves zero rupees and replies: already started. The agent passes that on. The ledger also blocks a real second refund, like a goodwill credit.

**T3:** Three: one automatic action for anything that you cannot undo. For refunds, a second run goes to a human.

---

## CLOSE (talking head)

The ledger code is in the vault. Link in the bio. Follow along for more such breakdowns.

---

## The ledger code

`refund_ledger.py` in this folder: a refund tool for a support agent, standard library only. One ledger row per `(order_line_id, action)` claimed before the gateway is called; the gateway gets the same order-line key; a same-reason repeat returns "already started", a different reason (goodwill) goes to a human queue. `python refund_ledger.py` runs the self-test (two runs → one payout).

---

## Vault notes (not spoken)

- **Why the per-call key misses.** The key is usually derived per request or per run. Two agent runs from two tickets build two different requests, so the gateway sees two new keys. The fix is not "no key", it's the key's scope: the ledger row is an idempotency key on the order line, not on the call.
- **"Not refunded until the bank settles"** is illustrative. Many payment gateways expose a pending-refund state; the failure is real when the agent reads an order status that only flips on settlement. Hence "the order page", not "the gateway", on camera and on the board.
- **Limit.** The ledger blocks a legitimate second refund too (a goodwill credit after the first refund). That is the point of Rule 3: a person decides it.
- **Same scene as the memory-graph draft** (delivery support). Switch one of them if both ship close together.

---

## Production notes

- **Hook.** Chosen from three candidates. Says "isn't enough", not "isn't the answer", because the ledger itself is a key, scoped to the order line.
- **Rules.** First part with general-then-case rules (general rule, then "For a refund, that's …").
- **Audio.** Recorded with the DJI transmitter under the T-shirt. Fixed in post: high-pass 80 Hz, +4.5 dB at 2.8 kHz, +1.5 dB at 5.5 kHz, gentle downward expander, loudness to −14 LUFS / −1 dBTP. Before: −17.1 LUFS, −0.1 dBTP, 2.3% of energy in 1–4 kHz. After: −14.2 LUFS, −1.0 dBTP, 3.1%, room floor between words 5.6 dB lower. The final export measures −11.2 LUFS integrated.
- **Captions.** `captions.srt`, 89 tiles of up to 3 words / ~18 characters, timed from the master cut with word timestamps (Parakeet TDT via sherpa-onnx, cross-checked with Whisper small.en). Styled in Kohinoor Devanagari Bold.
- **Cover and outro.** `reel_cover.png`, `reel_outro.png` (1080×1920), from the reusable cover/outro card. The title and label sit inside the 3:4 profile-grid crop.
