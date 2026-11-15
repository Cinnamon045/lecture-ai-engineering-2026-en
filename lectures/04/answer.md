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
- What you did:
- Results:
- Observations and questions:
