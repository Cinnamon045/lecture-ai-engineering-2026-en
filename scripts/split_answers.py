import json, pathlib

questions = [q.strip() for q in open("my_questions.txt") if q.strip()]
rows = []
for i, q in enumerate(questions, 1):
    raw = pathlib.Path(f"my_eval/raw_{i}.txt").read_text()
    answer, _, trace = raw.partition("--- trace ---")
    answer = "\n".join(l for l in answer.splitlines() if not l.startswith("[model]")).strip()
    rows.append({"id": f"{i:02d}", "question": q, "answer": answer, "trace": trace.strip()})

json.dump(rows, open("my_eval/answers.json", "w"), ensure_ascii=False, indent=2)
print(f"saved {len(rows)} rows")