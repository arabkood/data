#!/bin/bash
set -e

echo ">> Starting S3 bundles sync..."

if [ -z "$S3_PV_BUCKET_NAME" ]; then
  echo "❌ ERROR: S3 credentials must be set."
  exit 1
fi

echo ">> Syncing .bundles directory to s3://${S3_PV_BUCKET_NAME}..."

# --- Run the mc mirror command ---
mc mirror /app/.bundles/ myminio/${S3_PV_BUCKET_NAME}/topics/ \
  --overwrite --remove \
  --attr "Cache-Control=max-age=31536000,public"

echo "✅ S3 sync completed successfully."
