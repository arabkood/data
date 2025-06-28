FROM node:20-slim

# Install system dependencies in a single layer for efficiency
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    unzip \
    s3cmd \
  # Install bun and enable pnpm
  && corepack enable && corepack prepare pnpm@latest --activate \
  && curl -fsSL https://bun.sh/install | bash \
  # Clean up apt cache to keep the image small
  && apt-get purge -y curl && apt-get autoremove -y && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Add bun to the system's PATH
ENV PATH="/root/.bun/bin:$PATH"

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
