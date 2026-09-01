# Part 02: Transformer Block Lifecycle

### 1. 🎯 The 1-Sentence Production Paradox
Attention alone only computes dynamic linear combinations of prompt tokens; without non-linear parameter-stored memory banks and residual gradient highways, deep networks cannot store static world facts or backpropagate error signals past a few layers.

### 2. 🔬 Mathematical Invariants
$$X_1 = X + \text{MHSA}(\text{LayerNorm}(X)), \quad X_2 = X_1 + \text{FFN}(\text{LayerNorm}(X_1))$$

### 3. 📝 Master Spoken Script
```text
[0:00 – 0:08] HOOK (Talking Head)
"How does an LLM turn self-attention into complete, intelligent answers? It all happens inside the Transformer Block across three core steps."

[0:08 – 0:25] STEP 1: PREPARING INPUT (iPad B-Roll)
"Computers don't understand raw words; they understand numbers. When you input 'River Bank', words become embedding vectors, and positional tags are added so the model knows sequence order simultaneously."

[0:25 – 0:50] STEP 2: TRANSFORMER BLOCK CYCLE (iPad B-Roll)
"These vectors pass through a stack of identical Transformer Blocks. Step 1 is Attention, where words share context using Queries and Keys. Step 2 is the Feed-Forward Network, where each token sits in isolation to trigger the model's stored factual memory. Built-in skip connections act as safety rails so core meanings aren't erased."

[0:50 – 1:05] STEP 3: OUTPUT PREDICTION (Talking Head)
"After looping through dozens of blocks, the model scores its final enriched vectors against its entire vocabulary dictionary and predicts the most likely next word."
```
