#!/bin/bash
set -e

echo ">> Starting S3 bundles sync..."

if [ -z "$S3_PV_BUCKET_NAME" ]; then
  echo "❌ ERROR: S3 credentials must be set."
  exit 1
fi

echo ">> Syncing .bundles directory to s3://${S3_PV_BUCKET_NAME}..."

# --- Run the s3cmd sync command ---
s3cmd sync /app/.bundles/ s3://${S3_PV_BUCKET_NAME}/topics/ \
  --delete-removed \
  --add-header="Cache-Control:max-age=31536000,public" \
  --exclude '*' \
  --include '*bundle.zip' \
  --include '*config.json'

echo "✅ S3 sync completed successfully."
