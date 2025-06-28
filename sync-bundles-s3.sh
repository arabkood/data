#!/bin/bash
set -e

echo ">> Starting S3 bundles sync..."

echo ">> Syncing .bundles directory to s3://${S3_BUCKET}..."

# --- Run the s3cmd sync command ---
s3cmd sync /app/.bundles/ s3://${S3_BUCKET}/ \
  --dry-run \
  --delete-removed \
  --add-header="Cache-Control:max-age=31536000,public" \
  --exclude '*' \
  --include '*bundle.zip' \
  --include '*config.json'

echo "✅ S3 sync completed successfully."
