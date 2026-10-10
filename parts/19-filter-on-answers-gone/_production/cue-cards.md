# Cue cards — ENGINEERING · PART N (WHERE after LIMIT)

One card per step. Verbatim. Captions are cut from these. The line under each card is what gets drawn during that take.

**1 · Hook (face)**
You added a role filter to your company's AI search agent so interns can't see salaries. Now interns get empty answers.

**2**
An intern asks: can I carry over unused leave?
_Draw: intern · bubble "can I carry over unused leave?"_

**3**
Your agent pulls the five closest documents. All five are manager policies.
_Draw: agent → search → stack of 5 docs "top 5" · each tagged red MGR_

**4**
The role filter removes them, and the agent says no policy found.
_Draw: role filter gate · all 5 crossed out · empty tray · red "no policy found"_

**5**
In SQL, that is LIMIT before WHERE.
_Draw: red "LIMIT 5" then "WHERE role" (drawn arrow)_

**6**
Rule one: put the role filter inside the first query, before any top-k. For the intern, WHERE runs before LIMIT.
_Draw: RULE 1 — general, then intern: WHERE before LIMIT_

**7**
Move the filter first. The intern's leave policy survives, and it ranks eleventh.
_Draw: WHERE role = intern gate at the front · ranked list 1–12, leave policy at #11_

**8**
The search turned every document into a vector before anyone asked.
_Draw: doc → vector · stamp "made before the question"_

**9**
Carry-over and encashment read as leave, so they sit together. LIMIT five cuts it again.
_Draw: dot map, "carry over" and "encashment" touching inside "leave" · red cut line under #5_

**10**
Rule two: fetch wide with the cheap search, then sort again before the cut. For the intern, fifty in, five out.
_Draw: RULE 2 — general, then intern: 50 in, 5 out_

**11**
The second sort is the reranker. It reads the question and one document together.
_Draw: cyan "reranker" box, "top 50" in · card with question + doc side by side_

**12**
It sees carry over in both. The policy moves to the top.
_Draw: "carry over" underlined in both · green arrow #11 to #1_

**13**
It costs one model call per document, so it only sees fifty. A policy below fifty never reaches it.
_Draw: "1 call per doc", "50 calls" · doc at #60 crossed red: never reaches it_

**14**
Rule three: log the cited document's rank before reranking. For the leave policy, that's eleventh.
_Draw: RULE 3 — general, then leave policy: 11th_

**15 · Close (face)**
The blueprint is in the vault, link in bio. This was the engineering track. Next, we make the agent smarter without retraining.
