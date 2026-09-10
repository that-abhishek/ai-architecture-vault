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

---

## 🛠️ Directory Standard
Every topic directory contains:

1. `script.md` — First-principles deep dive, formulas, production trade-offs, and teleprompter script.
2. `meta.json` — Publishing title, badge, caption, and semantic keywords.
3. `master_cut.mov` / `master_cut.mp4` — Final rendered reference video cut.

Where available: `canvas.png` / `canvas.jpg` (vertical iPad whiteboard diagram) and `captions.srt` (styled subtitle track).
