# Part 17: Saved Tokens. Wrong City.

**Track: Engineering.** Cover label `ENGINEERING`, no part number.
Cover title: **SAVED TOKENS. WRONG CITY.**
Spine (Tushar test): *A running summary decides what matters before anyone asks, so a changed address and a dropped detail both go wrong. Store facts as entity, property, value and a timestamp so the newest value on a key wins, and fix the property names so every fact lands on the same key.*
Runtime: 1:24 (speech 0:00–1:24, no outro card). ~260 spoken words.
Text below is what was said on camera (transcribed from the master cut), not the pre-shoot draft. Rule lines were spoken as "One / Two / Three", without "Rule".
Asked for by: a LinkedIn comment on Part 12 ("memory graph vs running summary").

---

## HOOK (talking head)

How do you design a delivery chatbot that does not deliver to an older address? And summarizing the chat is not the answer.

---

## PANEL 1: The running summary

**Board, in order:** turn strip `turns 1-10 … 31-40` with `t5 Pune`, `gate: evening`, `t40 Chennai` · turns 11–30 crossed out, note `every 10 turns: drop old turns, rewrite the summary (save tokens)` · `summary v1` → `v2, v3` → `v4` with `Pune ... Chennai` and red `?` / `which one?` · red arrow out of v1: `gate: evening, dropped` · gold rule, with the chat case under it.

At turn 5, a customer tells your support bot: deliver to Pune. At turn 40, they change it to Chennai. To save tokens, every 10 turns, the bot drops old messages and rewrites a summary. After 4 rewrites, both cities are in it and nothing says which is newer. The evening gate went in the first rewrite.

**T1:** One: keep the raw turns. The summary only points to it. For this chat, that's turn 5 and 40.

---

## PANEL 2: The memory graph

**Board, in order:** `each turn → +1 model call → facts` · **ORDER** node, dashed `deliver_to · t5` → struck `Pune` `old` · bold `deliver_to · t40` → green **Chennai**, `same key, newer wins` · **BUILDING** node, `gate_closes` → `evening` · cyan `customer: "where's it going?"` → ORDER, `driver: "when do I arrive?"` → BUILDING · gold rule, with the order case under it.

After every turn, one extra model call writes facts instead of a paragraph. Turn 5 becomes: order, deliver to, Pune. Turn 40 writes Chennai on the same key, so it wins. The gate becomes a fact on the building. The customer's question reads the order, and the driver's reads the building.

**T2:** Two: store entity, property, value and a timestamp, and the newest value on the key wins. For this order, that's deliver to Chennai.

---

## PANEL 3: Loose keys

**Board, in order:** **ORDER** → `deliver_to` → `Pune` · red `shipping_city · t40` → `Chennai` · red bracket **2 answers** · green box `allowed properties`: `deliver_to`, `gate_closes`, struck `shipping_city` `rejected` · gold rule, with the order case under it · dashed box `short summary: the thread` — `refund in progress, waiting on photo`.

This only works if the model writes the same key every time. At turn 40, it writes shipping city instead. That's a new key, so both cities survive, and you are back to two answers.

**T3:** Three: fix the property name before the first write and reject the rest. For this order, that's deliver to instead of shipping city.

A refund on the photo is not a fact, so it stays in the short summary.

---

## CLOSE (talking head)

The full breakdown is in the vault. Link in the bio. Follow along for more.

---

## The reference code

`memory_store.py` in this folder, standard library only. `running_summary()` stands in for a rolling LLM summary with a length budget: after 40 turns it holds both cities and has lost the gate. `MemoryGraph` stores `(entity, property)` keys with the writing turn as the timestamp, keeps every old value in history, lets the newest value on a key win, and rejects any property not on the fixed list (`order.shipping_city` goes to `rejected`, not into the graph). `python memory_store.py` runs the self-test.

---

## Vault notes (not spoken)

- **Retrieval.** At question time, find the entities the question names and fetch only their edges into the prompt. "Where's my order going" pulls the order node; "when do I arrive" pulls the building.
- **Cost.** One extra model call per turn to extract facts. Cheaper than it sounds next to re-sending a long history (see Part 12), but it is a real per-turn cost.
- **Limit.** A wrong fact written at turn 5 sits in the graph looking exactly like a right one. The graph fixes *which* value is current, not *whether* it was right.
- **Graph and summary together.** Facts about things go in the graph. Where the conversation is (a refund waiting on a photo) is not a fact about a thing, so a short summary stays alongside.
- **On camera "A refund on the photo"** — the cue card said "a refund waiting on a photo". Captions follow what was said.
- **Same scene as Part 16** (delivery support, Pune/Chennai-style details). Fine as a pair; don't add a third part in this scene back to back.

---

## Production notes

- **Hook.** His own line, tightened once: a design question plus "summarizing the chat is not the answer", which rules out the fix every viewer already has in mind.
- **Rules.** General-then-case form, as in Part 16.
- **Canvas.** Explanation written first, board drawn to match it step by step. `canvas_reference.svg` is the pre-shoot reference; `canvas.jpg` is the board as drawn.
- **Audio.** DJI transmitter under the T-shirt again. Fixed in post: high-pass 80 Hz, −2 dB at 250 Hz, +5 dB at 2.8 kHz, downward expander between words, light compression, loudness to −14 LUFS. Before: −15.6 LUFS, −0.1 dBTP, 3.0% of energy in 1–4 kHz, room tail ~0.45 s, gaps 29 dB below speech. After: −14.1 LUFS, −1.3 dBTP, 5.2%, tail ~0.34 s, gaps 37 dB below speech. The final export measures −11.1 LUFS integrated.
- **Captions.** `captions.srt`, 109 tiles of up to 3 words / ~18 characters, timed from the fixed audio with word timestamps (Parakeet TDT via sherpa-onnx, cross-checked with Whisper small.en). The final export is sample-aligned with that audio. Styled in Montserrat ExtraBold.
- **Master cut.** Re-encoded from the 131 MB export to ~5.2 Mbps H.264 (46 MB) to stay under GitHub's 100 MB file limit; audio copied untouched.
- **Cover.** `reel_cover.png` (1080×1920), same layout as Part 16. No outro card on this part: the spoken close does the job, and the reel loops straight back into the hook.
