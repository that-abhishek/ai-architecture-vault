# Part 10: Mobile Systems → AI Systems

### 1. 🎯 The 1-Sentence Production Paradox
Mobile engineers assume AI infrastructure demands a math PhD, but production AI serving is an operating-systems problem — memory pressure, preemption, paging, frame-budget latency, and streaming state machines — which is exactly the discipline they have already spent a decade building.

### 2. 🔬 Systems Invariants (Mobile ↔ AI Serving Mapping)
- **Low-Memory Killer ↔ Request Preemption:**

When the GPU exhausts its KV cache budget, the serving engine evicts (preempts) an in-flight request and recomputes or swaps it later — structurally identical to Android's LMK / iOS Jetsam killing a backgrounded app under memory pressure.

- **Virtual Memory Paging ↔ PagedAttention:**

$$\text{KV}_{\text{block}} = \text{block\_size} \times 2 \times L \times d_{\text{model}} \times \text{bytes/param}$$

PagedAttention allocates KV cache in fixed-size non-contiguous blocks with a block table per sequence — the same page-table indirection that lets an app touch more address space than physical RAM without crashing, and the same fix for fragmentation.

- **16 ms Frame Budget ↔ Time-to-First-Token (TTFT):**

Both are hard, user-perceptible latency budgets. The discipline is identical: instrument, profile, and find where the budget went (prefill compute, scheduler queueing, tokenizer, network), rather than guessing.

- **Reactive Streams & Retry State Machines ↔ Token Streaming & Model Fallbacks:**

SSE/WebSocket token streams with partial-output handling, disconnect recovery, and provider fallback are the same state machines as Rx/Flow pipelines with offline-first retry logic.

- **On-Device Constraint Intuition ↔ Edge Inference:**

ExecuTorch, CoreML, and phone NPUs bring thermal throttling, battery, and memory-ceiling trade-offs into model serving — the constraint intuition mobile engineers already own and backend engineers are still acquiring.

### 3. ⚙️ The Real Gap (What Mobile Engineers Must Learn)
- **Non-deterministic outputs:** Testing and observability when the same input yields different outputs (sampling, temperature — see Part 05).
- **Embeddings & vector retrieval:** A new primitive with no mobile analogue (see Part 09).
- **Cost per call as a first-class design constraint:** Token economics shape architecture the way battery and data caps once did — but priced per request.

### 4. 📝 Master Spoken Script
```text
[0:00 – 0:08] HOOK (A-Roll: Talking Head)
"If you're a mobile engineer feeling intimidated by AI — thinking you need a math PhD — here's the reality: you already understand most of AI serving infrastructure. Let me show you exactly which parts."

[0:08 – 0:24] LOOP 1: MEMORY (B-Roll: iPad Panel 1)
"Production AI isn't calling a Python API. It's an operating systems problem.
Fought Android and iOS low-memory killers? That's preemption: when a GPU runs out of KV cache, the serving engine evicts a request exactly the way the OS kills your backgrounded app.
And virtual memory paging — the reason your app doesn't crash when it touches more memory than exists — that's PagedAttention. Same page tables, same fix for fragmentation."

[0:24 – 0:38] LOOP 2: LATENCY & STREAMING (B-Roll: iPad Panel 2)
"Ever chased a sixteen-millisecond frame drop on the main thread? Same discipline as Time-to-First-Token: a hard budget the user can feel, and profiling until you find where it went.
Reactive streams, network drops, retry state machines? That's token streaming and model fallbacks."

[0:38 – 0:48] LOOP 3: THE EDGE (B-Roll: iPad Panel 3)
"And as models move on-device — ExecuTorch, CoreML, phone NPUs — the constraint intuition you've built for thirteen years becomes the advantage. Backend folks are the ones catching up here."

[0:48 – 0:58] THE GAP & CTA (A-Roll: Talking Head)
"What you don't have yet: non-deterministic outputs, embeddings, and cost per call as a design constraint. That's the real gap — and it's learnable.
I've built mobile platforms since 2013 and still lead a mobile team. Same mental models. Share this with a mobile engineer who feels late, grab the open-source Vault in my bio, and follow @ai.transition."
```
