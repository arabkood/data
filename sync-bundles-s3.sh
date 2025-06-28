#!/bin/bash
set -euo pipefail

echo ">> Starting S3 bundles sync..."

echo ">> Syncing .bundles directory to s3://${S3_BUCKET}..."

# --- Run the s3cmd sync command ---
s3cmd sync /app/.bundles/ s3://${S3_BUCKET}/ \
  --delete-removed \
  --exclude ".*" \
  --exclude "*/.*" \
  --exclude "+*" \
  --exclude "*/+*" \
  --add-header="Cache-Control:max-age=31536000,public"

echo "✅ S3 sync completed successfully."
