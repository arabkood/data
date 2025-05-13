#!/bin/bash

export DATABASE_URL=" "

bun run ./scripts/sync/index.ts commit
