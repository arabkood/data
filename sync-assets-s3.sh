#!/bin/bash

# S3_BUCKET="arabkood-public-assets-bucket"
S3_BUCKET=${S3_ASSETS_BUCKET:-"localaws-assets-bucket"}

PUBLISH=${1:-false}
ENVR=${2:-local}
OTHER_ARGS=""

if [ "$PUBLISH" != true ]; then
  OTHER_ARGS="$OTHER_ARGS --dryrun"
fi

AWS="awslocal"
if [ "$ENVR" != local ]; then
  AWS="aws"
fi

# Ensure AWS CLI is installed
if ! command -v $AWS &>/dev/null; then
  echo "AWS CLI not found. Please install it first."
  exit 1
fi

$AWS s3 sync ./public-assets s3://$S3_BUCKET \
  --delete \
  --exclude ".*" \
  --exclude "*/.*" \
  --cache-control "max-age=31536000,public" \
  --content-type auto \
  --metadata-directive REPLACE \
  $OTHER_ARGS
# --acl public-read \

if [ $? -eq 0 ]; then
  echo "Sync to S3 completed successfully."
else
  echo "Sync to S3 failed."
  exit 1
fi
