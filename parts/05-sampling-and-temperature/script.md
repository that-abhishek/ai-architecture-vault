# Part 05: Inference Sampling & Temperature

### 1. 🎯 The 1-Sentence Production Paradox
Always choosing the single highest-probability token (Greedy Argmax Search) pushes autoregressive generation into repetitive degenerative loops and robotic prose.

### 2. 🔬 Mathematical Invariants
$$P(w_i) = \frac{\exp(z_i / T)}{\sum_{j=1}^{ert{}Vert{}} \exp(z_j / T)}, \quad V^{(p)} = \left\{ w \in V \mid \sum_{w_i \in V^{(p)}} P(w_i) \ge p \right\}$$

### 3. 📝 Master Spoken Script
```text
[0:00 – 0:08] HOOK (Talking Head)
"How does an LLM like ChatGPT actually decide what word to say next? It doesn’t just pick the single most obvious option—here is the exact math."

[0:08 – 0:28] LOGITS & SOFTMAX (iPad B-Roll)
"At the final layer, the model compares its feature vector against its entire dictionary to generate raw similarity scores called Logits. Because raw numbers can't be sampled directly, Softmax exponentiates and normalizes them into clean probabilities that add up to 100%."

[0:28 – 0:48] TEMPERATURE RESHAPING (iPad B-Roll)
"If you always pick the top choice—called Greedy Search—the AI loops and sounds robotic. Temperature divides the logits before Softmax. Low temperature sharpens the top choice for coding; high temperature flattens the distribution for creative writing."

[0:48 – 1:04] TOP-P GUARDRAIL (iPad B-Roll)
"To stop high temperature from picking complete nonsense like 'pizza', Top-P Sampling dynamically cuts off the long tail and only samples from the top cumulative 90%."

[1:04 – 1:15] TAKEAWAY & CTA (Talking Head)
"Logits score words, Softmax creates probabilities, Temperature reshapes them, and Top-P acts as the guardrail. Save this for your next ML interview, and follow for Part 6!"
```
