FROM node:20-slim

# Install core dependencies: curl, bun, and enable pnpm
RUN apt-get update && apt-get install -y curl \
  && corepack enable && corepack prepare pnpm@latest --activate \
  && curl -fsSL https://bun.sh/install | bash \
  && apt-get purge -y curl && apt-get autoremove -y && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Add bun to PATH
ENV PATH="/root/.bun/bin:$PATH"

# Set working directory
WORKDIR /app

# Pre-copy lock and package files for caching install
COPY ./scripts/syncV2/package.json ./scripts/syncV2/pnpm-lock.yaml ./scripts/syncV2/

# Install dependencies using pnpm
WORKDIR /app/scripts/syncV2
RUN pnpm install --frozen-lockfile

# Copy full project (including the rest of scripts and data)
WORKDIR /app
COPY . .

# Final working dir and command
WORKDIR /app/scripts/syncV2
CMD ["pnpm", "run", "sync"]
