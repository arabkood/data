#!/bin/bash
set -e

echo ">> Starting S3 Public Assets bundles sync..."

if [ -z "$S3_PV_BUCKET_NAME" ]; then
  echo "❌ ERROR: S3 credentials must be set."
  exit 1
fi

echo ">> Syncing public-assets directory to s3://${S3_PV_BUCKET_NAME}..."

# --- Run the mc mirror command ---
mc mirror /app/public-assets/ myminio/${S3_PV_BUCKET_NAME}/public/ \
  --overwrite --remove \
  --attr "Cache-Control=max-age=31536000,public"

echo "✅ S3 Public Assets Sync completed successfully."
