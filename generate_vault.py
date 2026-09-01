import os
import json
from pathlib import Path

# Initialize directories
root = Path(".")
artifacts_dir = root / "artifacts"
artifacts_dir.mkdir(exist_ok=True)

# 1. Root README.md
readme_content = """# AI Architecture & Systems Engineering Vault 🧠⚡
> Open-Source First-Principles Curriculum & Production Systems Engineering Blueprints
> Maintained by [@ai.transition](https://instagram.com/ai.transition)

Welcome to the **AI Architecture & Systems Engineering Vault**. This repository houses complete mathematical derivations, visual architecture schematics, teleprompter scripts, and production trade-offs for foundation model mechanics and distributed AI serving infrastructure.

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

---

## 🛠️ Universal 4-File Standard
Every topic directory adheres to the universal 4-file production standard:
1. `canvas.png` — High-resolution vertical whiteboard architecture diagram.
2. `script.md` — First-principles deep dive, formulas, production trade-offs, and teleprompter script.
3. `master_cut.mp4` — Final rendered reference video cut.
4. `meta.json` — Publishing titles, multi-platform captions, and semantic keyword matrices.
"""

(root / "README.md").write_text(readme_content)

# 2. Module Definitions
modules = [
    {
        "slug": "2608-self-attention",
        "title": "Part 01: Self-Attention Mechanism",
        "paradox": "In isolated token embedding spaces, words have static geometric coordinates, making it impossible for a model to resolve polysemy, syntactic dependencies, or contextual shifts without dynamic, input-conditioned feature deformation.",
        "math": "$$\\text{Attention}(Q, K, V) = \\text{softmax}\\left(\\frac{QK^T}{\\sqrt{d_k}}\\right)V$$",
        "script": """[0:00 – 0:08] HOOK (Talking Head)
"How does an AI model know that the word 'bank' in 'river bank' has nothing to do with money? It happens inside the Self-Attention mechanism."

[0:08 – 0:25] THE MECHANISM: Q, K, V (iPad B-Roll)
"Every token projects three vectors: a Query, a Key, and a Value. The Query asks what context it needs, the Key advertises what information it has, and the Value holds the actual content. When the Query for 'bank' multiplies with the Key for 'river', it scores a high similarity match."

[0:25 – 0:45] THE MATH: SCALING & SOFTMAX (iPad B-Roll)
"To prevent high-dimensional dot products from exploding and flattening our training gradients, we scale the scores by the square root of the dimension size. Softmax converts those scores into percentages that pull eighty-five percent of the meaning directly from 'river'."

[0:45 – 0:58] TAKEAWAY & CTA (Talking Head)
"Attention replaces static dictionary lookups with dynamic contextual routing. Save this breakdown for your next machine learning system design interview, and follow @ai.transition for Part 2!\"""",
        "meta": {
            "title": "How Self-Attention Works in Transformers Explained #shorts",
            "badge": "LLM FOUNDATIONS • PART 01",
            "keywords": ["transformers", "self-attention", "deep learning", "system design", "llm architecture"]
        }
    },
    {
        "slug": "2608-transformer-block",
        "title": "Part 02: Transformer Block Lifecycle",
        "paradox": "Attention alone only computes dynamic linear combinations of prompt tokens; without non-linear parameter-stored memory banks and residual gradient highways, deep networks cannot store static world facts or backpropagate error signals past a few layers.",
        "math": "$$X_1 = X + \\text{MHSA}(\\text{LayerNorm}(X)), \\quad X_2 = X_1 + \\text{FFN}(\\text{LayerNorm}(X_1))$$",
        "script": """[0:00 – 0:08] HOOK (Talking Head)
"How does an LLM turn self-attention into complete, intelligent answers? It all happens inside the Transformer Block across three core steps."

[0:08 – 0:25] STEP 1: PREPARING INPUT (iPad B-Roll)
"Computers don't understand raw words; they understand numbers. When you input 'River Bank', words become embedding vectors, and positional tags are added so the model knows sequence order simultaneously."

[0:25 – 0:50] STEP 2: TRANSFORMER BLOCK CYCLE (iPad B-Roll)
"These vectors pass through a stack of identical Transformer Blocks. Step 1 is Attention, where words share context using Queries and Keys. Step 2 is the Feed-Forward Network, where each token sits in isolation to trigger the model's stored factual memory. Built-in skip connections act as safety rails so core meanings aren't erased."

[0:50 – 1:05] STEP 3: OUTPUT PREDICTION (Talking Head)
"After looping through dozens of blocks, the model scores its final enriched vectors against its entire vocabulary dictionary and predicts the most likely next word.\"""",
        "meta": {
            "title": "Transformer Architecture Explained in 3 Steps #shorts",
            "badge": "LLM FOUNDATIONS • PART 02",
            "keywords": ["transformer architecture", "attention mechanism", "neural networks", "deep learning"]
        }
    },
    {
        "slug": "2608-chinchilla-scaling",
        "title": "Part 03: Chinchilla Scaling Laws",
        "paradox": "Scaling parameter count faster than training token volume creates compute-suboptimal, data-starved architectures that inflate serving infrastructure costs by 400% for equivalent benchmark performance.",
        "math": "$$C \\approx 6ND, \\quad \\text{Optimal Token-to-Parameter Ratio: } D \\approx 20N$$",
        "script": """[0:00 – 0:06] HOOK (Talking Head)
"If you have a fixed compute budget to train an LLM, do you make the model bigger, or feed it more data?"

[0:06 – 0:17] THE HISTORICAL MISTAKE (iPad B-Roll)
"Early scaling laws prioritized model size over dataset size. This led to undertrained giants like Gopher—a massive 280 billion parameters fed only 300 billion tokens."

[0:17 – 0:30] THE CHINCHILLA LAW (iPad B-Roll)
"Then DeepMind’s Chinchilla proved parameters and tokens must scale equally in a 1-to-20 ratio: roughly 20 tokens for every 1 parameter. With the same compute budget, a smaller 70B model trained on 1.4 trillion tokens crushed the 280B monster across the board."

[0:30 – 0:42] PRODUCTION WIN & CTA (Talking Head)
"Smaller, compute-optimal models cost less to deploy and slash production latency and memory by over 70%. Follow @ai.transition for Part 4!\"""",
        "meta": {
            "title": "Why Bigger AI Models Aren't Smarter (Chinchilla Scaling Law) #shorts",
            "badge": "LLM FOUNDATIONS • PART 03",
            "keywords": ["scaling laws", "chinchilla", "llm training", "deep learning"]
        }
    },
    {
        "slug": "2608-post-training-alignment",
        "title": "Part 04: Post-Training Alignment",
        "paradox": "A foundation model trained purely on self-supervised next-token cross-entropy loss behaves as a continuation autocomplete engine with no native concept of conversational turn-taking, safety guardrails, or instruction execution.",
        "math": "$$\\mathcal{L}_{\\text{DPO}}(\\theta) = -\\mathbb{E}_{(x, y_w, y_l)}\\left[\\log \\sigma\\left(\\beta \\log \\frac{\\pi_\\theta(y_w \\mid x)}{\\pi_{\\text{ref}}(y_w \\mid x)} - \\beta \\log \\frac{\\pi_\\theta(y_l \\mid x)}{\\pi_{\\text{ref}}(y_l \\mid x)}\\right)\\right]$$",
        "script": """[0:00 – 0:08] HOOK (Talking Head)
"If you spent fifty million dollars pretraining a base LLM and asked it a question, it wouldn’t answer you. It would probably just generate another question. Here’s why."

[0:08 – 0:20] THE BASE PROBLEM (iPad B-Roll)
"A Base Model only minimizes loss to predict the next word on raw internet text. It has no concept of being an assistant—so when you ask a question, it treats it like a quiz sheet and predicts more questions."

[0:20 – 0:35] STEP 1: SFT & MASKING (iPad B-Roll)
"To fix this, Step 1 is Supervised Fine-Tuning. We wrap conversations in Chat Templates using special tags like <user> and <assistant>, calculating loss only on the assistant's answer so it learns the format of following instructions."

[0:35 – 0:47] STEP 2: RLHF & JUDGMENT (iPad B-Roll)
"Step 2 is Preference Alignment. SFT gives the model the right format, but human preference rankings teach it judgment—rewarding helpful, safe answers and penalizing hallucinations."

[0:47 – 0:55] TAKEAWAY & CTA (Talking Head)
"Pretraining builds the raw brain; Post-training builds the actual assistant. Follow @ai.transition for Part 5!\"""",
        "meta": {
            "title": "Why $50M Base Models Fail: SFT and RLHF Explained #shorts",
            "badge": "LLM FOUNDATIONS • PART 04",
            "keywords": ["post-training", "sft", "rlhf", "dpo", "alignment"]
        }
    },
    {
        "slug": "2608-inference-sampling",
        "title": "Part 05: Inference Sampling & Temperature",
        "paradox": "Always choosing the single highest-probability token (Greedy Argmax Search) pushes autoregressive generation into repetitive degenerative loops and robotic prose.",
        "math": "$$P(w_i) = \\frac{\\exp(z_i / T)}{\\sum_{j=1}^{\vert{}V\vert{}} \\exp(z_j / T)}, \\quad V^{(p)} = \\left\\{ w \\in V \\mid \\sum_{w_i \\in V^{(p)}} P(w_i) \\ge p \\right\\}$$",
        "script": """[0:00 – 0:08] HOOK (Talking Head)
"How does an LLM like ChatGPT actually decide what word to say next? It doesn’t just pick the single most obvious option—here is the exact math."

[0:08 – 0:28] LOGITS & SOFTMAX (iPad B-Roll)
"At the final layer, the model compares its feature vector against its entire dictionary to generate raw similarity scores called Logits. Because raw numbers can't be sampled directly, Softmax exponentiates and normalizes them into clean probabilities that add up to 100%."

[0:28 – 0:48] TEMPERATURE RESHAPING (iPad B-Roll)
"If you always pick the top choice—called Greedy Search—the AI loops and sounds robotic. Temperature divides the logits before Softmax. Low temperature sharpens the top choice for coding; high temperature flattens the distribution for creative writing."

[0:48 – 1:04] TOP-P GUARDRAIL (iPad B-Roll)
"To stop high temperature from picking complete nonsense like 'pizza', Top-P Sampling dynamically cuts off the long tail and only samples from the top cumulative 90%."

[1:04 – 1:15] TAKEAWAY & CTA (Talking Head)
"Logits score words, Softmax creates probabilities, Temperature reshapes them, and Top-P acts as the guardrail. Save this for your next ML interview, and follow for Part 6!\"""",
        "meta": {
            "title": "How LLMs Actually Choose Words: Sampling & Temperature Explained #shorts",
            "badge": "LLM FOUNDATIONS • PART 05",
            "keywords": ["inference", "sampling", "temperature", "top-p", "softmax"]
        }
    },
    {
        "slug": "2608-kv-caching",
        "title": "Part 06: KV Caching & The Memory Wall",
        "paradox": "Autoregressive decoding without state persistence wastes O(N^2) quadratic compute recalculating static historical tokens, but caching Key-Value vectors in VRAM shifts the primary production bottleneck from compute capacity to memory bandwidth and capacity.",
        "math": "$$\\text{Memory}_{\\text{KV}} = 2 \\times n_{\\text{layers}} \\times n_{\\text{heads}} \\times d_k \\times \\text{Seq\\_Len} \\times \\text{Bytes}$$",
        "script": """[0:00 – 0:08] HOOK (Talking Head)
"Why does an AI model slow down and eat all your GPU memory the longer your conversation gets? It comes down to the KV Cache."

[0:08 – 0:26] THE REDUNDANT MATH (iPad B-Roll)
"LLMs generate text token by token. To predict word 100, the attention block needs context from the previous 99. Without caching, the GPU recomputes Keys and Values for all past words at every single step—wasting massive compute."

[0:26 – 0:48] THE COMPUTE-OPTIMAL PATH (iPad B-Roll)
"The fix is KV Caching. We compute Keys and Values once, store them in GPU VRAM, and only compute the new Query vector for the current token. This slashes inference latency from quadratic down to linear."

[0:48 – 1:02] THE MEMORY WALL (iPad B-Roll)
"The catch? It’s a classic space-for-time trade-off. As your prompt length and user concurrency grow, the KV cache expands until it consumes more VRAM than the actual model weights."

[1:02 – 1:12] CTA (Talking Head)
"This is why modern serving engines use PagedAttention to eliminate memory waste. Save this architecture, and follow @ai.transition for Part 7!\"""",
        "meta": {
            "title": "The Hidden Memory Bottleneck in LLMs: KV Caching Explained #shorts",
            "badge": "SERVING & MEMORY • PART 06",
            "keywords": ["kv cache", "gpu memory", "vram", "inference optimization"]
        }
    },
    {
        "slug": "2608-paged-attention",
        "title": "Part 07: PagedAttention & vLLM Memory Paging",
        "paradox": "Traditional serving engines pre-allocate contiguous VRAM chunks based on worst-case sequence lengths, wasting 60% to 80% of GPU memory on internal padding and external fragmentation.",
        "math": "$$\\text{Physical Memory Waste} < 4\\%, \\quad \\text{Throughput Boost: } 2\\times\\text{--}4\\times$$",
        "script": """[0:00 – 0:08] HOOK (Talking Head)
"Traditional AI servers waste up to eighty percent of their GPU memory on empty space. Here is how modern engines solved it using PagedAttention."

[0:08 – 0:25] THE FRAGMENTATION PROBLEM (iPad B-Roll)
"When serving an LLM, the system can't predict how long a response will be. To avoid crashes, it reserves huge, contiguous blocks of VRAM for every user. Most of that reserved memory sits empty, creating massive internal and external fragmentation."

[0:25 – 0:48] THE SOLUTION: OS-STYLE PAGING (iPad B-Roll)
"PagedAttention borrows a page from operating systems. Instead of contiguous memory, it chops the KV cache into fixed pages of sixteen tokens. A dynamic Page Table maps logical tokens to scattered physical slots in VRAM on demand."

[0:48 – 1:00] THE PRODUCTION WIN (Talking Head)
"Memory waste drops below four percent, letting you double your batch sizes and run four times the throughput on the exact same GPU. Follow @ai.transition for Part 8!\"""",
        "meta": {
            "title": "How vLLM and PagedAttention Fixed LLM Memory Waste #shorts",
            "badge": "SERVING & MEMORY • PART 07",
            "keywords": ["pagedattention", "vllm", "memory management", "cuda", "serving"]
        }
    },
    {
        "slug": "2608-remote-mcp-architecture",
        "title": "Part 08: Remote MCP Architecture & Measure.sh Teardown",
        "paradox": "A standard Model Context Protocol (MCP) server running over local stdio takes fewer than 40 lines of code, but deploying remote MCP over public HTTP introduces severe security vectors, statelessness issues, multi-tenant data leaks, and recursive agent loops.",
        "math": "$$\\text{AST Parser} \\longrightarrow \\text{Claim-Injected Predicate} \\longrightarrow \\text{Read Replica}$$",
        "script": """[0:00 – 0:08] HOOK (Talking Head)
"Everyone thinks building a Model Context Protocol server takes 37 lines of code. Over local stdio, sure. But in production over remote HTTP? That myth falls apart."

[0:08 – 0:25] THE PROTOCOL GAP (iPad B-Roll)
"The raw MCP protocol is simple JSON-RPC. But running it remotely requires an auth gateway with OAuth 2.1 and self-revoking one-hour sessions to secure your streaming transport."

[0:25 – 0:45] RECURSION GUARDS & SQL DEFENSE (iPad B-Roll)
"When tools use nested agents like ask_question, you need server-side recursion guards to stop infinite loops. And for text-to-SQL, we enforce four layers of defense: schema pruning, AST syntax parsing for read-only SELECTs, forced tenant-ID injection, and read-replica execution."

[0:45 – 0:58] TAKEAWAY & CTA (Talking Head)
"Real AI engineering isn’t just writing prompts; it’s building enterprise systems defense. Follow @ai.transition for more applied architecture teardowns!\"""",
        "meta": {
            "title": "The 37-Line Remote MCP Myth: Production Architecture Teardown #shorts",
            "badge": "APPLIED SYSTEMS • PART 08",
            "keywords": ["mcp", "model context protocol", "oauth2", "text-to-sql", "agents"]
        }
    }
]

# 3. Create Files
for m in modules:
    mod_dir = artifacts_dir / m["slug"]
    mod_dir.mkdir(exist_ok=True)
    
    # script.md
    script_content = f"# {m['title']}\n\n### 1. 🎯 The 1-Sentence Production Paradox\n{m['paradox']}\n\n### 2. 🔬 Mathematical Invariants\n{m['math']}\n\n### 3. 📝 Master Spoken Script\n```text\n{m['script']}\n```\n"
    (mod_dir / "script.md").write_text(script_content)
    
    # meta.json
    (mod_dir / "meta.json").write_text(json.dumps(m["meta"], indent=2))
    
    # Placeholder assets
    (mod_dir / "canvas.png").touch()
    (mod_dir / "master_cut.mp4").touch()

print("✅ Complete AI Architecture Vault successfully scaffolded across all 8 modules!")
