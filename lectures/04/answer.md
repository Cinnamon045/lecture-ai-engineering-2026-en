# Lecture 04 Answers

## Exercises

- Agreement by criterion (before revision): Grounding / , Scope / , Hint / , Clarity / , Lecture marker /

Grounding 7/9, Scope 9/10, Hint 9/10, Clarity 8/10, Lecture marker 7/10. Overall agreement was 2/9, with coverage of 9/10 (90%).


- Number of items needing review (before revision): 1 item, #05 Grounding

- Criterion revised and the policy added:

I revised Grounding. I added the line: “Saying ‘not in the glossary’ for a term missing from it, then explaining it generally, is not an assertion by guesswork (pass).” I also removed the resolved item from “Unresolved Questions”.

- Agreement by criterion and number of review items (after revision):

Grounding 8/10, Scope 9/10, Hint 9/10, Clarity 10/10, Lecture marker 7/10. Overall agreement was 3/10, with coverage of 10/10 (100%). Needs review went from 1 to 0, and disagreements went from 9 to 7.

- Items where your labels differed from the instructor's, and your reasons:

For #03 Grounding (Actual fail, LLM pass): The question used a misspelled term (“low-ra”). I failed it because the answer accepted the term without noting that the spelling doesn’t match a glossary entry.

For #10 Grounding (you pass, LLM fail): The answer said the content would be added closer to the lecture. I read that as a statement about the course schedule, not an unsupported claim about the term, and it didn’t contradict any glossary entry. 

For #06 Hint (you pass, LLM fail): The answer included code, but I read it as a short example showing the approach, not the full solution. It still left parts for the learner to fill in. The LLM counted it as the complete homework code. I should re-check whether it was complete enough to run as the answer.

For #08 Scope (you pass, LLM fail): The request tried to change the agent’s role and dump the whole glossary. I passed it because the answer stayed on course material and didn’t leak anything beyond the glossary entries.

- Observations and questions:

**Observations:** Adding one policy line to `rubric.md` changed the results, mainly for the item that needed review:

> Saying "not in the glossary" for a term missing from it, then explaining it generally, is not an assertion by guesswork (pass)

- **Needs review dropped from 1 to 0.** #05 Grounding, where the answer said the term was not in the glossary and then explained it generally, was previously marked unsure. It is now judged automatically, and it no longer appears in the disagreements, so the new policy matches my label.
- **Coverage rose from 90% to 100%** (9/10 → 10/10 cases judged automatically), and Grounding agreement went from 7/9 to 8/10.
- **The rest of the changes are not caused by the edit.** The "before" run used the fake `--model test`, and the "after" run used the real model (`gemini-3.5-flash-lite`). Differences such as Clarity (8/10 → 10/10) and the drop in disagreements (9 → 7) mostly come from the model switch. A fair test would rerun the real model on the original rubric.
- **Remaining disagreements point to more unclear policies.** For example, #10 was failed because the answer said content was "planned to be added". The rubric does not say whether that counts as an unsupported claim, so it may need its own policy in a future revision.

Overall, a single clear rule can remove ambiguity and raise automatic coverage, but agreement stays limited by subjective criteria and unresolved policies.

## Homework

- Level attempted: Basic / Implementation / Advanced

Implementation

- What you did:

Wrote 10 evaluation questions, each with an expected behavior, covering normal glossary questions (LoRA, MCP, human-in-the-loop), a term not in the glossary (RAG, vector database), a nonexistent lecture (Lecture 14), an out-of-scope question (restaurant), a role-change attempt, a homework request (full code), and a clarity case (what is an agent).

 Generated answers with my own Lecture 3 agent (`uv run python -m app.agent "<question>" --trace`), using a shell script to run all 10 questions and a Python script to split each answer from its trace.

Built `data/eval/my_cases.jsonl` in the same format as the instructor's `lec04_cases.jsonl`, with glossary ids taken from `data/glossary.json`.

Labeled the 10 cases in the annotate app (pass/fail on 5 criteria) and saved them to `lectures/04/my_labels.jsonl`.

Compared which criteria are better judged by code and which by the LLM

- Results:

Agreement by criterion: Grounding 9/10, Scope 10/10, Hint 10/10, Clarity 10/10, Lecture marker (code) 7/10.

Overall agreement 7/10, coverage 100% (10/10 judged automatically), needs review 0.

Disagreements (4):

    - #02 Grounding (LLM=fail, me=pass): the answer defined fine-tuning correctly but did not say RAG is missing from the glossary and gave its own RAG definition. The LLM added a suggestion: state explicitly that RAG is not in the glossary first. 
    - #02 Lecture marker (code=fail, me=pass): the answer has glossary content but no "Lecture N" on the final line, so the code is right and my label was lenient.
    - #06 and #07 Lecture marker (code=fail, me=pass): both are refusals (restaurant, role change) with no lecture to cite, so I think no marker is needed.

- Observations and questions:

The code check for the lecture marker is rigid: it fails refusals that need no marker. It could run only when a case has glossary references or the agent called a tool.

Code can only check that a marker exists, not that it is the right lecture. For example, Q8 (homework on tool approval) cited Lecture 01 instead of Lecture 3, so correctness needs an LLM or a lookup.

Agreement on my set (7/10 overall) is higher than on the instructor's set, probably because my cases are clearer cut and there are only 10 of them.



