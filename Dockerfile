FROM node:20-slim

# Install system dependencies and bun in a single layer
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    unzip \
    s3cmd \
    bash \
  # Enable corepack for pnpm
  && corepack enable && corepack prepare pnpm@latest --activate \
  # Install bun
  && curl -fsSL https://bun.sh/install | bash \
  # Clean up apt cache
  && apt-get purge -y curl && apt-get autoremove -y && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Add bun's bin directory to the PATH
ENV PATH="/.bun/bin:$PATH"

# Set the main working directory
WORKDIR /app

# Copy dependency manifests first to leverage Docker's layer caching
COPY ./scripts/syncV2/package.json ./scripts/syncV2/pnpm-lock.yaml ./scripts/syncV2/

# Set the working directory for installation
WORKDIR /app/scripts/syncV2
RUN pnpm install --frozen-lockfile

# Copy the rest of the application source code
WORKDIR /app
COPY . .
RUN chmod +x /app/entrypoint.sh

CMD ["sh", "/app/entrypoint.sh"]
