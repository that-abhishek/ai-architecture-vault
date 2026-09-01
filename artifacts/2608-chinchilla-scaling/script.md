# Part 03: Chinchilla Scaling Laws

### 1. 🎯 The 1-Sentence Production Paradox
Scaling parameter count faster than training token volume creates compute-suboptimal, data-starved architectures that inflate serving infrastructure costs by 400% for equivalent benchmark performance.

### 2. 🔬 Mathematical Invariants
$$C \approx 6ND, \quad \text{Optimal Token-to-Parameter Ratio: } D \approx 20N$$

### 3. 📝 Master Spoken Script
```text
[0:00 – 0:06] HOOK (Talking Head)
"If you have a fixed compute budget to train an LLM, do you make the model bigger, or feed it more data?"

[0:06 – 0:17] THE HISTORICAL MISTAKE (iPad B-Roll)
"Early scaling laws prioritized model size over dataset size. This led to undertrained giants like Gopher—a massive 280 billion parameters fed only 300 billion tokens."

[0:17 – 0:30] THE CHINCHILLA LAW (iPad B-Roll)
"Then DeepMind’s Chinchilla proved parameters and tokens must scale equally in a 1-to-20 ratio: roughly 20 tokens for every 1 parameter. With the same compute budget, a smaller 70B model trained on 1.4 trillion tokens crushed the 280B monster across the board."

[0:30 – 0:42] PRODUCTION WIN & CTA (Talking Head)
"Smaller, compute-optimal models cost less to deploy and slash production latency and memory by over 70%. Follow @ai.transition for Part 4!"
```
