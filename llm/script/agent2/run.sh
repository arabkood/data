#!/bin/bash

export GOOGLE_API_KEY="AIzaSyALp2SC26f1ghEe0Zbtv6jFg0qu2tPQXG0"
export ANTHROPIC_API_KEY="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"
export TARGET_LESSON=30
export VARIANTS=1

bun run ./main.ts
