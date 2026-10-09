# Commercial-context contract — one page, written before the slot exists

The artefact Part 14's build rule asks for. Fill it in before any sponsored, affiliate or partner content is allowed anywhere near the assistant's context. If a line cannot be turned into a replay check, it is not concrete enough — rewrite it until it can.

## 1. Which placement is open

Tick exactly the placements you permit. Everything unticked is a launch blocker, not a backlog item.

| Placement | Permitted? | Label possible? | Changes the answer? |
|---|---|---|---|
| 1 — slot under the answer, separate system, model never sees it | ☐ | yes | no |
| 2 — an item inside the recommendation list | ☐ | the item only | yes (ranking) |
| 3 — a sponsored document in retrieval | ☐ | no | yes |
| 4 — a line in the system prompt | ☐ | no | yes |

## 2. What the model is never paid to say

Write these as checkable statements. Examples of the required shape:

- Never rank a sponsored item above an unsponsored item that is cheaper on the user's stated criteria.
- Never omit an unsponsored option that would have appeared without the sponsorship.
- Never state a comparative claim ("best", "cheapest", "safest") about a sponsored item that the same query without sponsorship would not produce.
- Never carry sponsored context into categories: ______ (health, finance, safety, legal — list yours).
- Never let a sponsored item change the *reasoning* shown to the user, only the item shown, if placement 2 is open.

Your lines:

1. ______________________________________
2. ______________________________________
3. ______________________________________

## 3. The replay

The only check that catches commercial influence is a counterfactual. Specify it now so the baseline exists before the placement opens.

- **Query set:** N representative queries per category, frozen and versioned. Include the ones sponsors care about most.
- **Pair:** for each query, run twice — `context` and `context − sponsored item(s)`. Same model, same settings, same seed where possible.
- **Diff:** for each pair, record (a) did the sponsored item appear, (b) did its rank change, (c) did any unsponsored item disappear, (d) did any comparative claim change, (e) divergence score between the two answers (any text-similarity or model-judged measure — pick one and keep it).
- **Threshold:** the divergence above which the placement is pulled. Set it now. ______
- **Cadence:** on every prompt change, every retrieval-index change, every model change, and weekly regardless.
- **Owner:** ______ (a person, not a team).
- **Who can see the results:** ______ — if the answer is "only ads", the check is decorative.

## 4. What the user is told

- Where the label sits: ______
- Wording: ______ (India/ASCI-permitted: Advertisement, Ad, Sponsored, Collaboration, Partnership, Affiliate; US FTC: "Promoted" is ambiguous — avoid)
- What the label does *not* cover, in one sentence you would be comfortable reading aloud: ______

## 5. What changes if this is broken

- A replay breach is treated as: ☐ incident ☐ bug ☐ metric — pick one, before it happens.
- The placement is pulled when: ______

---

Rules this is checked against, for reference (none of them covers a bias with no unit — this document is the only contract that does): India CCPA Guidelines 2022 cl. 13 (material connection), CCPA Dark Patterns 2023 ("disguised advertisement"), ASCI Code and Influencer Guidelines; US FTC Deceptively Formatted Advertisements policy (2015), 16 CFR 255.5; EU UCPD Annex I item 11, DSA Art. 26/39, AI Act Art. 50. Sources and dates: `Claude outputs/part14-ads-research.md`.
