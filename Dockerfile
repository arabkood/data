FROM node:20-slim

RUN corepack enable && corepack prepare pnpm@latest --activate

WORKDIR /app

COPY ./scripts/syncV2/package.json ./scripts/syncV2/pnpm-lock.yaml ./scripts/syncV2/

WORKDIR /app/scripts/syncV2
RUN pnpm install --frozen-lockfile

WORKDIR /app
COPY . .

WORKDIR /app/scripts/syncV2
CMD ["pnpm", "run", "sync"]
