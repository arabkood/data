#!/bin/bash

if [[ $# -ne 2 ]]; then
	echo "Usage: $0 <input-yaml> <output-dir>"
	exit 1
fi

FILE=$1
FILENAME=$(basename "$FILE")
FILENAME="${FILENAME%.yml}"
OUTP=$2

OUT="$OUTP/${FILENAME/-/_}"

echo $OUT

# Ensure output directory exists
mkdir -p "$OUT/lesson"

steps_count=$(yq '.steps | length' $FILE)

type=$(yq -r ".type" $FILE)
title=$(yq -r ".title" $FILE)
base_xp=$(yq -r ".base_xp" $FILE)
difficulty=$(yq -r ".difficulty" $FILE)
premium_only=$(yq -r ".premium_only" $FILE)

cat >"$OUT/+item.yml" <<EOL
type: $type
title: $title
base_xp: $base_xp
difficulty: $difficulty
premium_only: $premium_only
EOL

for i in $(seq 0 $((steps_count - 1))); do
	type=$(yq -r ".steps[$i].type" $FILE)
	idx=$(printf "%02d\n" $((i + 1)))

	echo "idx $idx:"
	echo "  Type: $type"

	if [[ $type == "markdown" ]]; then
		filename="$idx"_"$type".md
		yq -r ".steps[$i].content" $FILE >"$OUT/lesson/$filename"
		continue
	fi

	filename="$idx"_"$type".yml
	yq -r ".steps[$i]" $FILE >"$OUT/lesson/$filename"

	echo "done"
done
