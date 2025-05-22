#!/bin/bash
#
# Bundle creation script with bidirectional sync
# Creates bundles from directory structure in ./topics and cleans up orphaned bundles

set -euo pipefail # Exit on error, undefined vars, pipe failures

TOPICS_DIR="./topics"
BUNDLE_DIR="./.bundles"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
  local color=$1
  local message=$2
  echo -e "${color}${message}${NC}"
}

# Check if topics directory exists
if [ ! -d "$TOPICS_DIR" ]; then
  print_status "$RED" "❌ Error: Topics directory '$TOPICS_DIR' does not exist"
  exit 1
fi

# Create bundle directory
mkdir -p "$BUNDLE_DIR"
print_status "$BLUE" "📁 Bundle directory: $BUNDLE_DIR"

# Check if zip is available
if ! command -v zip &>/dev/null; then
  print_status "$RED" "❌ Error: 'zip' command not found. Please install zip utility."
  exit 1
fi

# Initialize counters
files_copied=0
bundles_created=0
bundles_updated=0
bundles_removed=0
files_removed=0
errors=0

# Create associative arrays to track what should exist
declare -A expected_bundles
declare -A expected_files

print_status "$BLUE" "🔍 Scanning source directories..."

# First pass: collect what should exist and process items
find "$TOPICS_DIR" -path "$TOPICS_DIR/*/*/*/*/*" \
  -not -path "$TOPICS_DIR/*/*/*/*/*/*" \
  -not -path "*/.*" \
  -not -path "*/+*" | while read -r path; do

  # Calculate relative path and target directory
  rel_path=$(realpath --relative-to="$TOPICS_DIR" "$(dirname "$path")")
  base_name=$(basename "$path")
  target_dir="$BUNDLE_DIR/$rel_path"

  # Ensure target directory exists
  mkdir -p "$target_dir"

  if [ -d "$path" ]; then
    # Process directory: create bundle zip
    bundle_name="$base_name.bundle.zip"
    target_zip="$target_dir/$bundle_name"

    # Track this bundle as expected
    echo "BUNDLE:$target_zip"

    # Check if bundle needs updating
    needs_update=false
    if [ ! -f "$target_zip" ]; then
      needs_update=true
      print_status "$YELLOW" "📦 Creating new bundle: $path"
    elif [ "$path" -nt "$target_zip" ]; then
      needs_update=true
      print_status "$YELLOW" "📦 Updating bundle: $path (source newer)"
    fi

    if [ "$needs_update" = true ]; then
      # Remove existing bundle if it exists
      [ -f "$target_zip" ] && rm -f "$target_zip"

      # Create zip bundle
      if (cd "$path" && zip -rq "$target_zip" .); then
        if [ ! -f "$target_zip.created" ]; then
          print_status "$GREEN" "✅ Created bundle: $target_zip"
          echo "CREATED" >>"$target_zip.created"
        else
          print_status "$GREEN" "🔄 Updated bundle: $target_zip"
          echo "UPDATED" >>"$target_zip.updated"
        fi
      else
        print_status "$RED" "❌ Failed to create bundle: $target_zip"
        echo "ERROR" >>"$target_zip.error"
      fi
    else
      print_status "$BLUE" "⏭️  Bundle up to date: $target_zip"
    fi

  elif [ -f "$path" ]; then
    # Process file: copy directly
    target_file="$target_dir/$base_name"

    # Track this file as expected
    echo "FILE:$target_file"

    # Check if file needs updating
    needs_update=false
    if [ ! -f "$target_file" ]; then
      needs_update=true
    elif [ "$path" -nt "$target_file" ]; then
      needs_update=true
    fi

    if [ "$needs_update" = true ]; then
      if cp "$path" "$target_file"; then
        print_status "$BLUE" "📎 Copied file: $path → $target_file"
        echo "COPIED" >>"$target_file.copied"
      else
        print_status "$RED" "❌ Failed to copy file: $path"
        echo "ERROR" >>"$target_file.error"
      fi
    else
      print_status "$BLUE" "⏭️  File up to date: $target_file"
    fi

  else
    print_status "$YELLOW" "❓ Unknown item type: $path"
    echo "ERROR" >>"/tmp/unknown_items"
  fi
done >/tmp/expected_items

# Read expected items into arrays
while IFS= read -r line; do
  if [[ $line == BUNDLE:* ]]; then
    bundle_path="${line#BUNDLE:}"
    expected_bundles["$bundle_path"]=1
  elif [[ $line == FILE:* ]]; then
    file_path="${line#FILE:}"
    expected_files["$file_path"]=1
  fi
done </tmp/expected_items

print_status "$PURPLE" "🧹 Cleaning up orphaned bundles and files..."

# Second pass: find and remove orphaned bundles and files
if [ -d "$BUNDLE_DIR" ]; then
  find "$BUNDLE_DIR" -type f | while read -r existing_item; do
    # Skip temporary files created by this script
    [[ "$existing_item" == *.created ]] && continue
    [[ "$existing_item" == *.updated ]] && continue
    [[ "$existing_item" == *.error ]] && continue
    [[ "$existing_item" == *.copied ]] && continue

    should_exist=false
    item_type=""

    if [[ "$existing_item" == *.bundle.zip ]]; then
      # Check if this bundle should exist
      if [[ -n "${expected_bundles[$existing_item]:-}" ]]; then
        should_exist=true
      fi
      item_type="bundle"
    else
      # Check if this regular file should exist
      if [[ -n "${expected_files[$existing_item]:-}" ]]; then
        should_exist=true
      fi
      item_type="file"
    fi

    if [ "$should_exist" = false ]; then
      if rm -f "$existing_item"; then
        print_status "$PURPLE" "🗑️  Removed orphaned $item_type: $existing_item"
        if [ "$item_type" = "bundle" ]; then
          ((bundles_removed++))
        else
          ((files_removed++))
        fi
      else
        print_status "$RED" "❌ Failed to remove orphaned $item_type: $existing_item"
        ((errors++))
      fi
    fi
  done
fi

# Count results from temporary tracking files
bundles_created=$(find "$BUNDLE_DIR" -name "*.created" 2>/dev/null | wc -l)
bundles_updated=$(find "$BUNDLE_DIR" -name "*.updated" 2>/dev/null | wc -l)
files_copied=$(find "$BUNDLE_DIR" -name "*.copied" 2>/dev/null | wc -l)
bundle_errors=$(find "$BUNDLE_DIR" -name "*.error" 2>/dev/null | wc -l)

# Note: bundles_removed and files_removed are counted in the cleanup loop above
# errors includes bundle creation errors but cleanup errors are counted inline

# Cleanup temporary tracking files
find "$BUNDLE_DIR" -name "*.created" -o -name "*.updated" -o -name "*.error" -o -name "*.copied" | xargs rm -f 2>/dev/null || true
rm -f /tmp/expected_items 2>/dev/null || true

# Print summary
echo
print_status "$BLUE" "=== Summary ==="
print_status "$GREEN" "✅ Bundles created: $bundles_created"
print_status "$GREEN" "🔄 Bundles updated: $bundles_updated"
print_status "$GREEN" "📎 Files copied: $files_copied"
print_status "$PURPLE" "🗑️  Bundles removed: $bundles_removed"
print_status "$PURPLE" "🗑️  Files removed: $files_removed"

if [ $errors -gt 0 ]; then
  print_status "$RED" "❌ Errors encountered: $errors"
  exit 1
else
  print_status "$GREEN" "🎉 All operations completed successfully!"
fi
