#!/usr/bin/env bash
mkdir -p my_eval
export PYDANTIC_AI_NO_BANNER=1
i=1
while IFS= read -r q; do
  echo "Running Q$i: $q"
  uv run python -m app.agent "$q" --trace > "my_eval/raw_$i.txt" 2>&1
  i=$((i+1))
  sleep 5
done < my_questions.txt
echo "done"