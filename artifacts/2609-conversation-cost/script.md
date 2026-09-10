# Part 12: Summarising Your Agent's History Can Triple Your Bill

### 0. 🧭 Why This Matters (the production decision)
**The decision this episode is for: your agent's conversations are getting long and expensive, and you are about to summarise the history to shrink them. Done the obvious way, that makes the bill worse, not better.**

Long conversations cost more than people expect, because the API is stateless — the model holds nothing between calls, so the harness resends the entire history every turn. Everyone eventually notices and reaches for compression. But cost is not proportional to tokens sent; it is proportional to *how many of those tokens are cache hits*. Cached prefix tokens read at 0.1x base input price, while fresh tokens written into cache cost 1.25x. That is a 12.5x gap, and rewriting old turns moves tokens across it.

The three rules the reel delivers:
1. **Your bill is cache hit rate, not conversation length.** Measure hit rate before you optimise anything else.
2. **Compression fights caching.** Any edit to the prefix invalidates the cache from that point onward. Rewriting history mid-conversation converts cheap reads into expensive writes — every turn.
3. **Compact at boundaries, never mid-flight.** Append-only until the window forces your hand, then one decisive compaction that becomes the new stable prefix.

### 1. 🎯 The 1-Sentence Production Paradox
Because the API is stateless, an N-turn conversation sends O(N²) tokens — but almost all of them are an unchanged prefix billed at a tenth of the price, so the intuitive fix (summarise the history to send fewer tokens) invalidates that prefix and can triple the bill while halving the tokens.

### 2. 🔬 Systems Invariants
- **Statelessness Makes Conversation Quadratic:**

$$\text{tokens sent} = \sum_{n=1}^{N} n \cdot t = \frac{N(N+1)}{2}\,t$$

With N = 20 turns of t = 1k tokens: 210k tokens sent, not 20k. The "conversation" is an illusion reconstructed from scratch on every call — you are re-buying it each turn.

- **Not All Tokens Cost the Same:**

Cache read = **0.1x** base input price. 5-minute cache write = **1.25x**. 1-hour cache write = **2x**. So the quadratic triangle is affordable precisely because ~90% of it is an identical prefix served at a tenth of the price. Cost tracks hit rate, not length.

- **Cache Invalidation Is Prefix-Structured:**

The hierarchy is `tools` → `system` → `messages`. A change at any level invalidates that level **and everything after it**. Cache writes happen only at your breakpoint, and the system looks back at most 20 blocks for a matching entry. Put `cache_control` on the last block that is byte-identical across requests; max 4 breakpoints per request. Anything volatile — a timestamp, a per-request preamble — placed early in the prompt silently destroys the whole cache behind it.

- **Why Naive Compression Backfires (worked example):**

Assumptions: 20 turns, 1k tokens added per turn, 5-minute TTL held throughout, prices in multiples of base input.

| Strategy | Tokens sent | Cost |
|---|---|---|
| No caching | 210k | 210k × 1.0 = **210 units** |
| Append-only + caching | 210k | reads 190k × 0.1 = 19, writes 20k × 1.25 = 25 → **44 units** |
| Re-summarise every turn (history kept at half size) | ~115k | prefix rewritten each turn, so ~115k × 1.25 → **~144 units** |

Half the tokens. Roughly three times the bill. The compression didn't fail at compressing — it failed by moving every remaining token from the 0.1x column to the 1.25x column, every single turn.

- **Why Boundary Compaction Wins:**

Compacting once pays the 1.25x write on the new prefix a single time; every subsequent turn reads it at 0.1x again. Compacting continuously pays that write on every turn and never gets a hit. Same summarisation technique, opposite economics — the variable is *frequency*, not *ratio*.

### 3. ⚙️ Production Trade-offs & Failure Modes
- **TTL is part of the design:** the default cache lifetime is 5 minutes. A conversation with human-length pauses between turns loses the prefix anyway and the arithmetic above collapses toward the uncached column. The 1-hour TTL costs 2x on writes — worth it only when reads will actually follow.
- **Prompt ordering is a cost decision, not a style decision:** stable content first (tools, system, documents), volatile last (the new message). A single dynamic timestamp near the top is a full-prefix cache miss on every request.
- **Compaction is lossy, and the loss is silent:** the summariser drops what it can't tell is load-bearing, and the agent then reasons from a lossy copy of its own history. Boundary compaction reduces how often you take that loss; it doesn't eliminate it.
- **Minimum cacheable length applies:** short prompts aren't cacheable at all, so none of this matters below the threshold (512–4096 tokens depending on model).
- **Beyond the reel:** cache-aware batching across users, what to pin versus recompute, and measuring hit rate as a first-class production metric next to latency and error rate.

### 4. 🎨 Whiteboard Drawing Plan (3 panels, black board / white marker / cyan · red · green)
Reference render: `canvas_reference.png`. Redraw by hand; the reference fixes layout, not handwriting.

**Panel 1 — "The triangle"** (start drawing under the hook — E1)
- Draw a staircase of widening bars: turn 1, turn 2, turn 3, turn 4, `...`, turn 20. The shape *is* the point — let it build.
- Under it: `20 turns x 1k each` → big red `210k` → `not 20k`.
- Cyan box: `but 90% is the same bytes every turn / so it's a cache read: 0.1x price`.
- Aha (cyan): *you re-buy the conversation every turn* → Rule: **RULE: your bill is cache hit rate, not length**
- Write the rule line on the board on the spoken words "Takeaway one" — the hand and the voice land together.

**Panel 2 — "The trap"**
- Draw the prompt as four blocks: `tools | system | turns 1-10 | turns 11-20`, all marked green `cached`.
- Then redraw the same bar with `turns 1-10` replaced by a red `summary` block. Mark the summary and everything after it red `INVALID`. One red slash from `you rewrite this one...`.
- Line under: `one edit kills the cache from there on`.
- Numbers: `0.1x read → 1.25x write`, green `12x jump`.
- Aha (cyan): *compression fights caching* → Rule: **half the tokens. 3x the bill.**
- Same cue: the rule is written as "Takeaway two" is spoken.

**Panel 3 — "Append only"**
- The correct ordering as one bar: `tools | system | docs | history | new msg` (new msg in green), with a dashed cyan breakpoint line before `new msg` labelled `breakpoint here`. Under it: `last block that never changes. 4 max.`
- Long green arrow: `grow to the right. never edit the left.`
- Bottom: `window nearly full` → cyan `compact ONCE, new prefix`; small: `not every turn. that's the whole difference.`
- Aha (cyan): *a conversation is an append-only log* → Rule: **RULE: compact at boundaries, never mid-flight**
- Same cue: the rule is written as "Takeaway three" is spoken. Hold this frame two beats before the CTA cut.

### 5. 📝 Master Beat Sheet — Spoken Line ↔ What's On The Board

Runtime ≈ 65 s at 3.2 words/sec (~198 words). Every line written on the canvas is either spoken here or deliberately silent — nothing on the board is unaccounted for. To get to 60 s, cut beats 1.2 and 3.4 (both are carried by the drawing anyway). Never cut a takeaway.

```text
── HOOK ──────────────────────────────────────────  0:00 – 0:05
SAY   "You compressed your agent's chat history to save money. Your bill just tripled."
BOARD nothing yet. Face full frame; on "tripled", cut to the board and the first bar starts.

  ALT A: "Your agent re-reads the entire conversation. Every turn. And you're paying for it."
  ALT B: "Two identical tokens. One costs twelve times the other. That's your whole LLM bill."
  Picking rule: "agent" or "LLM" lands inside the first two seconds.

── PANEL 1: THE TRIANGLE ─────────────────────────  0:05 – 0:25   [65 w]
1.1  SAY   "The API is stateless. The model remembers nothing."
     BOARD header "1  The triangle" + subtitle "the API is stateless. you resend everything."

1.2  SAY   "So your harness resends everything. Every single turn."
     BOARD bars for turn 1, turn 2, turn 3, turn 4 — let them build, one per beat of speech

1.3  SAY   "Twenty turns, a thousand tokens each? Not twenty thousand. Two hundred and ten thousand."
     BOARD the "..." then the long turn-20 bar; then "20 turns x 1k each", then big red "210k", then "not 20k"

1.4  SAY   "You survive that because ninety percent is the same bytes every time. Cache read. Tenth of the price."
     BOARD cyan box: "but 90% is the same bytes every turn / so it's a cache read: 0.1x price"

1.5  SAY   "You're re-buying the conversation every turn. Takeaway one — your bill is cache hit rate. Not length."
     BOARD cyan aha line, then the RULE line + underline, drawn on the word "Takeaway"

── PANEL 2: THE TRAP ─────────────────────────────  0:25 – 0:45   [64 w]
2.1  SAY   "So you do the obvious thing. Summarise turns one to ten. Half the history. Done."
     BOARD header "2  The trap"; the four-block bar: tools | system | turns 1-10 | turns 11-20, all green "cached"

2.2  SAY   "And your bill triples."
     BOARD hold. no new ink. let it sit.

2.3  SAY   "The cache is a prefix. Tools and system survive. Everything after your edit doesn't."
     BOARD red slash + "you rewrite this one..."; redraw the bar with the red "summary" block; tools/system stay green "cached", summary and turns 11-20 go red "INVALID"

2.4  SAY   "Those turns were reads at nought-point-one. Now they're writes at one-point-two-five. Twelve times more. Every turn."
     BOARD "one edit kills the cache from there on", then "0.1x read → 1.25x write", then green "12x jump"

2.5  SAY   "Takeaway two — compression fights caching. Half the tokens, three times the bill."
     BOARD cyan aha, then the RULE line + underline

── PANEL 3: APPEND ONLY ──────────────────────────  0:45 – 1:02   [55 w]
3.1  SAY   "So don't rewrite. Append."
     BOARD header "3  Append only" + subtitle "order it: never-changes first, changes-always last"

3.2  SAY   "Never-changes first — tools, system, docs. Then history. Then the new message."
     BOARD the five-block bar, drawn left to right in time with the words; "new msg" in green

3.3  SAY   "Breakpoint on the last thing that never moves."
     BOARD dashed cyan breakpoint line before "new msg" + label; under it "last block that never changes. 4 max."

3.4  SAY   "Grow right. Never edit the left."
     BOARD the long green arrow

3.5  SAY   "Window fills up? Compact once. That's your new prefix. Not every turn — that's the whole difference."
     BOARD "window nearly full" box, arrow, cyan "compact ONCE, new prefix"; then the small line "not every turn. that's the whole difference."

3.6  SAY   "Takeaway three — compact at boundaries. Never mid-flight."
     BOARD cyan aha, then the RULE line + underline. Hold two beats.

── CTA ───────────────────────────────────────────  1:02 – 1:07
SAY   "Full arithmetic's in the vault, link in bio. One blueprint a week. Follow along."
BOARD cut back to face.
```

### 6. 🎬 Notes for the Edit
- E1 applies: the staircase starts drawing under the hook, by 0:10 at the latest. This panel is the best E1 candidate so far — the triangle building bar by bar *is* the retention device.
- If you want one screen-recording cut, put it on Panel 2: a real usage dashboard showing cache-read vs cache-write token columns. Seeing the two columns is worth more than any animation.
- Caption colour map (Part 11 convention): cyan `#00FFFF` concepts (prefix, cache read, breakpoint, append-only), red `#FF5252` the failure (invalid, 1.25x, rewrite), gold `#FFD700` rules and CTA.
- Numbers must match the board: 210k, 0.1x, 1.25x, 12x, "half the tokens, 3x the bill". State the worked example's assumptions if anyone asks in comments — 20 turns, 1k/turn, TTL held. Source: Anthropic prompt caching docs (cache read 0.1x, 5m write 1.25x, 1h write 2x, invalidation hierarchy tools → system → messages, max 4 breakpoints, 20-block lookback).
- Say "cache read" and "cache write", not "prompt caching is a feature of X" — the mechanism is the topic, the vendor is the example.
