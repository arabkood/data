#!/bin/bash
set -e

echo "--- Starting Unified Sync Process ---"

# --- Configuration FOR S3 ---
if [ -z "$S3_ACCESS_KEY_ID" ] || [ -z "$S3_SECRET_ACCESS_KEY" ] || [ -z "$S3_PV_BUCKET_NAME" ] || [ -z "$S3_ENDPOINT" ]; then
	echo "❌ ERROR: S3 credentials must be set."
	exit 1
fi

# Ensure endpoint has a scheme
ENDPOINT="$S3_ENDPOINT"
if ! [[ "$ENDPOINT" =~ ^https?:// ]]; then
	ENDPOINT="https://$ENDPOINT"
fi

mc alias set myminio "$ENDPOINT" "$S3_ACCESS_KEY_ID" "$S3_SECRET_ACCESS_KEY"

# Step 1: Run the S3 Topics sync
echo "--- Step 1: Syncing topics to S3 ---"
./sync-bundles-s3.sh
echo "✅ S3 topics sync successful."

# Step 2: Run the S3 Public Assets sync
echo "--- Step 2: Syncing public-assets to S3 ---"
./sync-assets-s3.sh
echo "✅ S3 sync public-assets successful."

# Save the current directory
ORIGINAL_DIR=$(pwd)

# Step 3: Run the database sync
echo "--- Step 3: Syncing to Database ---"
cd ./scripts/syncV2
pnpm run sync
echo "✅ Database sync successful."

# Return to the original directory
cd "$ORIGINAL_DIR"

echo "--- Unified Sync Process Complete ---"
