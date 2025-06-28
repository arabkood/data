#!/bin/bash
set -e

echo ">> Starting S3 Public Assets bundles sync..."

if [ -z "$S3_PV_BUCKET_NAME" ]; then
  echo "❌ ERROR: S3 credentials must be set."
  exit 1
fi

echo ">> Syncing public-assets directory to s3://${S3_PV_BUCKET_NAME}..."

# --- Run the s3cmd sync command ---
s3cmd sync /app/public-assets/ s3://${S3_PV_BUCKET_NAME}/public/ \
  --delete-removed \
  --add-header="Cache-Control:max-age=31536000,public" \
  --content-type auto

echo "✅ S3 Public Assets Sync completed successfully."
