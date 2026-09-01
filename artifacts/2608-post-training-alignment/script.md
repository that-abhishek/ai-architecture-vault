# Part 04: Post-Training Alignment

### 1. 🎯 The 1-Sentence Production Paradox
A foundation model trained purely on self-supervised next-token cross-entropy loss behaves as a continuation autocomplete engine with no native concept of conversational turn-taking, safety guardrails, or instruction execution.

### 2. 🔬 Mathematical Invariants
$$\mathcal{L}_{\text{DPO}}(\theta) = -\mathbb{E}_{(x, y_w, y_l)}\left[\log \sigma\left(\beta \log \frac{\pi_\theta(y_w \mid x)}{\pi_{\text{ref}}(y_w \mid x)} - \beta \log \frac{\pi_\theta(y_l \mid x)}{\pi_{\text{ref}}(y_l \mid x)}\right)\right]$$

### 3. 📝 Master Spoken Script
```text
[0:00 – 0:08] HOOK (Talking Head)
"If you spent fifty million dollars pretraining a base LLM and asked it a question, it wouldn’t answer you. It would probably just generate another question. Here’s why."

[0:08 – 0:20] THE BASE PROBLEM (iPad B-Roll)
"A Base Model only minimizes loss to predict the next word on raw internet text. It has no concept of being an assistant—so when you ask a question, it treats it like a quiz sheet and predicts more questions."

[0:20 – 0:35] STEP 1: SFT & MASKING (iPad B-Roll)
"To fix this, Step 1 is Supervised Fine-Tuning. We wrap conversations in Chat Templates using special tags like <user> and <assistant>, calculating loss only on the assistant's answer so it learns the format of following instructions."

[0:35 – 0:47] STEP 2: RLHF & JUDGMENT (iPad B-Roll)
"Step 2 is Preference Alignment. SFT gives the model the right format, but human preference rankings teach it judgment—rewarding helpful, safe answers and penalizing hallucinations."

[0:47 – 0:55] TAKEAWAY & CTA (Talking Head)
"Pretraining builds the raw brain; Post-training builds the actual assistant. Follow @ai.transition for Part 5!"
```
