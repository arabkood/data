#!/bin/bash

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <input-yaml> <output-dir>"
  exit 1
fi

FILE=$1
OUT=$2

# Ensure output directory exists
mkdir -p "$OUT"

steps_count=$(yq '.steps | length' $FILE)

for i in $(seq 0 $((steps_count - 1))); do
  type=$(yq -r ".steps[$i].type" $FILE)
  idx=$(printf "%02d\n" $((i + 1)))

  echo "idx $idx:"
  echo "  Type: $type"

  if [[ $type == "markdown" ]]; then
    filename="$idx"_"$type".md
    yq -r ".steps[$i].content" $FILE >"$OUT/$filename"
    continue
  fi

  filename="$idx"_"$type".yml
  yq -r ".steps[$i]" $FILE >"$OUT/$filename"

  echo "done"
done
