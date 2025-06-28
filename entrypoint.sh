#!/bin/bash
set -e

echo "--- Starting Unified Sync Process ---"

# --- Configuration FOR S3 ---
if [ -z "$S3_ACCESS_KEY_ID" ] || [ -z "$S3_SECRET_ACCESS_KEY" ] || [ -z "$S3_PV_BUCKET_NAME" ] || [ -z "$S3_ENDPOINT" ] || [ -z "$S3_REGION" ]; then
  echo "❌ ERROR: S3 credentials must be set."
  exit 1
fi
cat >~/.s3cfg <<EOF
[default]
access_key = $S3_ACCESS_KEY_ID
secret_key = $S3_SECRET_ACCESS_KEY
host_base = $S3_ENDPOINT
host_bucket = %(bucket).$S3_ENDPOINT
bucket_location = $S3_REGION
use_https = True
EOF

cat ~/.s3cfg

exit 0

# Save the current directory
ORIGINAL_DIR=$(pwd)

# Step 1: Run the database sync
echo "--- Step 1: Syncing to Database ---"
cd ./scripts/syncV2
pnpm run sync
echo "✅ Database sync successful."

# Return to the original directory
cd "$ORIGINAL_DIR"

# Step 2: Run the S3 sync
echo "--- Step 2: Syncing to S3 ---"
./sync-bundles-s3.sh
echo "✅ S3 sync successful."

echo "--- Unified Sync Process Complete ---"
