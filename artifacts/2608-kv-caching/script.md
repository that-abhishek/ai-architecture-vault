# Part 06: KV Caching & The Memory Wall

### 1. 🎯 The 1-Sentence Production Paradox
Autoregressive decoding without state persistence wastes O(N^2) quadratic compute recalculating static historical tokens, but caching Key-Value vectors in VRAM shifts the primary production bottleneck from compute capacity to memory bandwidth and capacity.

### 2. 🔬 Mathematical Invariants
$$\text{Memory}_{\text{KV}} = 2 \times n_{\text{layers}} \times n_{\text{heads}} \times d_k \times \text{Seq\_Len} \times \text{Bytes}$$

### 3. 📝 Master Spoken Script
```text
[0:00 – 0:08] HOOK (Talking Head)
"Why does an AI model slow down and eat all your GPU memory the longer your conversation gets? It comes down to the KV Cache."

[0:08 – 0:26] THE REDUNDANT MATH (iPad B-Roll)
"LLMs generate text token by token. To predict word 100, the attention block needs context from the previous 99. Without caching, the GPU recomputes Keys and Values for all past words at every single step—wasting massive compute."

[0:26 – 0:48] THE COMPUTE-OPTIMAL PATH (iPad B-Roll)
"The fix is KV Caching. We compute Keys and Values once, store them in GPU VRAM, and only compute the new Query vector for the current token. This slashes inference latency from quadratic down to linear."

[0:48 – 1:02] THE MEMORY WALL (iPad B-Roll)
"The catch? It’s a classic space-for-time trade-off. As your prompt length and user concurrency grow, the KV cache expands until it consumes more VRAM than the actual model weights."

[1:02 – 1:12] CTA (Talking Head)
"This is why modern serving engines use PagedAttention to eliminate memory waste. Save this architecture, and follow @ai.transition for Part 7!"
```
