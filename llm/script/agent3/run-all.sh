#!/bin/bash

export GOOGLE_API_KEY="AIzaSyALp2SC26f1ghEe0Zbtv6jFg0qu2tPQXG0"
export ANTHROPIC_API_KEY="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"

for MODULE_INDEX in {0..7}; do
  export MODULE_INDEX
  echo "Running for MODULE_INDEX=$MODULE_INDEX"
  bun run ./main.ts
done
