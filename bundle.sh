#!/bin/bash

#
TOPICS_DIR="./topics"
BUNDLE_DIR="./.bundles"

mkdir -p "$BUNDLE_DIR"

find "./topics" -path "./topics/*/*/*/*/*" \
  -not -path "./topics/*/*/*/*/*/*" \
  -not -path "*/.*" \
  -not -path "*/+*" | while read path; do

  rel_path=$(realpath --relative-to="$TOPICS_DIR" "$(dirname "$path")")
  base_name=$(basename "$path")

  target_dir="$BUNDLE_DIR/$rel_path"
  mkdir -p "$target_dir"

  if [ -d "$path" ]; then
    # It's a directory: create a .bundle.zip
    bundle_name="$base_name.bundle.zip"
    target_zip=$(realpath "$target_dir/$bundle_name")

    echo "$path => $target_zip"

    rm -f "$target_zip"
    (
      cd "$path" &&
        zip -r "$target_zip" .
    )

    if [ $? -eq 0 ]; then
      echo "✅ Created bundle: $target_zip"
    else
      echo "❌ Failed to create bundle: $target_zip"
    fi

  elif [ -f "$path" ]; then
    # It's a file: just copy it
    target_file="$target_dir/$base_name"

    cp "$path" "$target_file"
    echo "📎 Copied file: $path => $target_file"

  else
    echo "❓ Unknown type: $path"
  fi

done
