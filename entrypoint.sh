#!/bin/bash
set -e

echo "--- Starting Unified Sync Process ---"

# --- Configuration FOR S3 ---
S3_ACCESS_KEY="${S3_ACCESS_KEY_ID:-}"
S3_SECRET_KEY="${S3_SECRET_ACCESS_KEY:-}"
S3_ENDPOINT="${S3_ENDPOINT:-}"
S3_BUCKET="${S3_PV_BUCKET_NAME:-}"
S3_REGION="${S3_REGION:-us-east-1}"
if [ -z "$S3_ACCESS_KEY" ] || [ -z "$S3_SECRET_KEY" ] || [ -z "$S3_BUCKET" ]; then
  echo "❌ ERROR: S3 credentials (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_BUCKET_NAME) must be set."
  exit 1
fi
cat >~/.s3cfg <<EOF
[default]
access_key = $S3_ACCESS_KEY
secret_key = $S3_SECRET_KEY
host_base = $S3_ENDPOINT
host_bucket = %(bucket).$S3_ENDPOINT
bucket_location = $S3_REGION
use_https = True
EOF

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
