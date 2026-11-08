# Lecture 03 Answers

## Exercises

- Differences between the Lecture 01 (bare LLM) and agent answers:
- Tool calls shown by `--trace` (tool names and arguments):
- Number of LLM calls for one question (`requests`):
- Tool added and the description in its docstring:

## Homework

- Level attempted: Basic / Implementation / Advanced

I attempted Basic Level

- What you did:

I changed the INSTRUCTIONS part of the of the agent.py and I added the function make_quiz() to tools.py. I register make_quiz function as one of the tools that agent.py can use or call

- Results:

At first when I tried to run the uv run python -m app.agent --list-tools make_ from the unmodified agent.py the function make_quiz is not yet on the list. After committing and pushing the changes, the make_quiz function is added to the tools list that the agent can use.

By adding the make_quiz function, the agent can purposefully make a quiz question(s) and answer(s) based from the topic that was requested to it. 

In addition, by changing the instructions for the agent, the answer that one might get may vary drastically depending on the instructions given.

- Observations and questions:

I learned that an agent’s behavior depends on both INSTRUCTIONS and tool docstrings. Instructions tell the model when to use tools and how to answer, while docstrings describe what each tool does and how to fill its arguments. Rewriting either changes tool selection, arguments, and answer style.