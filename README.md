# AI Architecture & Systems Engineering Vault 🧠⚡
> Open-Source First-Principles Notes & Production Systems Engineering Breakdowns
> Maintained by [@ai.transition](https://instagram.com/ai.transition)

Welcome to the **AI Architecture & Systems Engineering Vault**. This repository holds the material behind each [@ai.transition](https://instagram.com/ai.transition) episode — the core formula, whiteboard schematic, and teleprompter script for foundation model mechanics and distributed AI serving infrastructure. Some parts go deeper into production trade-offs and failure modes; all of them are first-principles, short, and built to be read alongside the video.

---

## 📚 Curriculum Syllabus

### Volume I: Transformer Foundations & Macro Architecture
* **[Part 01: Self-Attention Mechanism](./artifacts/2608-self-attention/)**
* **[Part 02: Transformer Block Lifecycle](./artifacts/2608-transformer-block/)**

### Volume II: Scaling Laws, Alignment & Inference Mechanics
* **[Part 03: Chinchilla Scaling Laws](./artifacts/2608-chinchilla-scaling/)**
* **[Part 04: Post-Training Alignment](./artifacts/2608-post-training-alignment/)**
* **[Part 05: Inference Sampling & Temperature](./artifacts/2608-inference-sampling/)**

### Volume III: Serving, Memory & Applied Production Systems
* **[Part 06: KV Caching & The Memory Wall](./artifacts/2608-kv-caching/)**
* **[Part 07: PagedAttention & vLLM Memory Paging](./artifacts/2608-paged-attention/)**
* **[Part 08: Remote MCP Architecture & Measure.sh Teardown](./artifacts/2608-remote-mcp-architecture/)**
* **[Part 09: The Context Distraction Paradox & RAG](./artifacts/2609-context-distraction/)**
  * *Keywords:* Softmax Attention Dilution, "Lost in the Middle" Degradation, Parametric Memory Collisions, Cross-Encoder Re-ranking, Context Budgeting.
* **[Part 10: Mobile Systems → AI Systems](./artifacts/2609-mobile-to-ai-systems/)**
  * *Keywords:* LMK ↔ KV Cache Preemption, Virtual Memory ↔ PagedAttention, 16ms Frame Budget ↔ TTFT, Reactive Streams ↔ Token Streaming, On-Device Inference (ExecuTorch / CoreML / NPUs).
* **[Part 11: Prompt Injection — No Patch, Just Blast Radius](./artifacts/2609-promp-injection/)**
  * *Keywords:* One-String Context (No Privilege Boundary), SQL Parameterization vs. No-Grammar LLMs, Blacklist Futility, Indirect Injection, Least-Privilege Tools, Human-in-the-Loop Confirmation, Dual-LLM (Privileged / Quarantined) Pattern.
* **[Part 12: Summarising Your Agent's History Can Triple Your Bill](./artifacts/2609-conversation-cost/)**
  * *Keywords:* Stateless API & Quadratic Conversation Cost, Cache Read vs. Write Economics, Prefix-Structured Invalidation, Rolling-Summary Trap (Re-compression), Breakpoint Placement, Boundary Compaction.
* **[Part 13: Your Agent's Errors Return 200](./artifacts/2609-detection-cost/)**
  * *Keywords:* Success-Shaped Failure (No Exception to Catch), Inert Retry Semantics, Detection Cost Floor (Check ≈ Produce), Truth vs. Provenance, Grounding Assertions for Invention, Schema vs. Semantic Checks, Irreversibility as the Verification Budget, Mutation Testing Non-Deterministic Output.

### Track 2 — AI Product (runs alongside Track 1; part numbers stay cumulative)
Product seen from the room where "what gets built" is decided. Same rule: one visual blueprint per part. Test for the track: if acting on the takeaway changes code inside a system already decided on, it's engineering; if it changes what gets built, or whether, it's product. Same gates as Track 1 — an aha, something countable, a drawable mechanism, survives model progress — and every product part names the engineering part it stands on.

* **[Part 14: Four Placements, One Label](./artifacts/2609-ads-in-the-answer/)**
  * *Stands on:* Part 11 (prompt injection — same mechanism, commercial payload, operator as injector).
  * *Keywords:* Slot vs. Sentence (a Label Needs a Thing), Four Placements (UI Slot, Recommendation List, Retrieved Page, System Prompt), Label Efficacy (61 → 55 vs. 22), Prompt-Level Commercial Steering (18 of 23 Models), Reader Undetectability, Counterfactual Diff as the Only Control (Build It, or Ask Twice), The "Never Paid to Say" Contract.

---

## 🛠️ Directory Standard
Every topic directory contains:

1. `script.md` — First-principles deep dive, formulas, production trade-offs, and teleprompter script.
2. `meta.json` — Publishing title, badge, caption, and semantic keywords.
3. `master_cut.mov` / `master_cut.mp4` — Final rendered reference video cut.

Where available: `canvas.png` / `canvas.jpg` (vertical iPad whiteboard diagram) and `captions.srt` (styled subtitle track).
