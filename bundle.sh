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

# Check if essential commands are available
if ! command -v zip &>/dev/null; then
  print_status "$RED" "❌ Error: 'zip' command not found. Please install zip utility."
  exit 1
fi
if ! command -v realpath &>/dev/null; then
  print_status "$RED" "❌ Error: 'realpath' command not found. Please install it (usually in coreutils)."
  exit 1
fi

# Initialize counters for the summary section (these are re-calculated later from files)
bundles_removed=0
files_removed=0
errors=0 # For cleanup errors in this script version

# Create associative arrays to track what should exist (populated from /tmp/expected_items_bundler)
declare -A expected_bundles
declare -A expected_files

# Define temporary file names to avoid conflicts
EXPECTED_ITEMS_TMP_FILE="/tmp/expected_items_bundler_$$" # $$ makes it unique per script run
UNKNOWN_ITEMS_TMP_FILE="/tmp/unknown_items_bundler_$$"

print_status "$BLUE" "🔍 Scanning source directories and processing items..."

# First pass: collect what should exist and process items.
# The while loop runs in a subshell due to the pipe `|` and redirection `>`.
find "$TOPICS_DIR" -path "$TOPICS_DIR/*/*/*/*/*" \
  -not -path "$TOPICS_DIR/*/*/*/*/*/*" \
  -not -path "*/.*" \
  -not -path "*/+*" | while read -r path; do

  # Calculate relative path and target directory
  rel_path_parent_dir=$(realpath --relative-to="$TOPICS_DIR" "$(dirname "$path")")
  base_name=$(basename "$path")
  target_dir_for_item="$BUNDLE_DIR/$rel_path_parent_dir"

  # Ensure target directory exists for the item and its tracking files
  mkdir -p "$target_dir_for_item" || {
    print_status "$RED" "❌ Subshell Error: Failed to create target directory $target_dir_for_item"
    exit 1
  }

  if [ -d "$path" ]; then
    # Process directory: create bundle zip
    bundle_name="$base_name.bundle.zip"
    target_zip_relative="$target_dir_for_item/$bundle_name" # Relative to script CWD

    # Track this bundle as expected (output to temp file)
    echo "BUNDLE:$target_zip_relative"

    # Check if bundle needs updating
    needs_update=false
    bundle_was_new=false # Flag to distinguish for messaging/tracking file
    if [ ! -f "$target_zip_relative" ]; then
      needs_update=true
      bundle_was_new=true
      # Message moved to just before zipping
    # Check if source dir itself is newer OR any file *inside* source dir is newer
    elif [ "$path" -nt "$target_zip_relative" ] ||
      (find "$path" -type f -newer "$target_zip_relative" -print -quit 2>/dev/null || true) | grep -q '.'; then
      needs_update=true
      # Message moved to just before zipping
    fi

    if [ "$needs_update" = true ]; then
      if [ "$bundle_was_new" = true ]; then
        print_status "$YELLOW" "📦 Creating new bundle for: $path"
      else
        print_status "$YELLOW" "📦 Updating bundle for: $path (source or contents newer)"
      fi

      # Remove existing bundle if it exists (for updates)
      rm -f "$target_zip_relative" # Safe, rm -f doesn't error if file not found

      # Get ABSOLUTE path for zip command's output file
      absolute_target_zip_path=$(realpath -m "$target_zip_relative")

      # Create zip bundle. `zip` failure is handled by `else`.
      if (cd "$path" && zip -rq "$absolute_target_zip_path" .); then
        if [ "$bundle_was_new" = true ]; then
          print_status "$GREEN" "✅ Created bundle: $target_zip_relative"
          echo "CREATED" >>"$target_zip_relative.created"
        else
          print_status "$GREEN" "🔄 Updated bundle: $target_zip_relative"
          echo "UPDATED" >>"$target_zip_relative.updated"
        fi
      else
        print_status "$RED" "❌ Failed to create bundle: $target_zip_relative (from $path)"
        echo "ERROR" >>"$target_zip_relative.error"
      fi
    else
      print_status "$BLUE" "⏭️  Bundle up to date: $target_zip_relative"
    fi

  elif [ -f "$path" ]; then
    # Process file: copy directly
    target_file_relative="$target_dir_for_item/$base_name" # Relative to script CWD

    # Track this file as expected (output to temp file)
    echo "FILE:$target_file_relative"

    needs_update=false
    if [ ! -f "$target_file_relative" ]; then
      needs_update=true
    elif [ "$path" -nt "$target_file_relative" ]; then
      needs_update=true
    fi

    if [ "$needs_update" = true ]; then
      # `cp` failure is handled by `else`.
      if cp "$path" "$target_file_relative"; then
        print_status "$BLUE" "📎 Copied/Updated file: $path → $target_file_relative"
        echo "COPIED" >>"$target_file_relative.copied"
      else
        print_status "$RED" "❌ Failed to copy file: $path to $target_file_relative"
        echo "ERROR" >>"$target_file_relative.error"
      fi
    else
      print_status "$BLUE" "⏭️  File up to date: $target_file_relative"
    fi
  else
    print_status "$YELLOW" "❓ Unknown item type: $path"
    echo "UNKNOWN_TYPE: $path" >>"$UNKNOWN_ITEMS_TMP_FILE" || print_status "$RED" "Failed to log unknown item to $UNKNOWN_ITEMS_TMP_FILE"
  fi
done >"$EXPECTED_ITEMS_TMP_FILE" # End of the `find | while` subshell

# Check if the primary temporary file was created and has content.
if [ ! -s "$EXPECTED_ITEMS_TMP_FILE" ] &&
  ! (find "$TOPICS_DIR" -path "$TOPICS_DIR/*/*/*/*/*" \
    -not -path "$TOPICS_DIR/*/*/*/*/*/*" \
    -not -path "*/.*" \
    -not -path "*/+*" -print -quit | grep -q '.'); then
  print_status "$YELLOW" "⚠️  No source items found or processing loop failed to produce $EXPECTED_ITEMS_TMP_FILE."
  # If no source items, this might be normal. If source items exist but file is empty/missing, it's an error.
fi

# Read expected items into arrays
while IFS= read -r line; do
  if [[ $line == BUNDLE:* ]]; then
    bundle_path="${line#BUNDLE:}"
    expected_bundles["$bundle_path"]=1
  elif [[ $line == FILE:* ]]; then
    file_path="${line#FILE:}"
    expected_files["$file_path"]=1
  fi
done <"$EXPECTED_ITEMS_TMP_FILE"

print_status "$PURPLE" "🧹 Cleaning up orphaned bundles and files..."

# Second pass: find and remove orphaned bundles and files
# This loop also runs its `while` in a subshell due to the pipe.
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
      item_type="bundle"
      if [[ -n "${expected_bundles[$existing_item]:-}" ]]; then
        should_exist=true
      fi
    else # A non-bundle file
      item_type="file"
      if [[ -n "${expected_files[$existing_item]:-}" ]]; then
        should_exist=true
      fi
    fi

    if [ "$should_exist" = false ]; then
      # `rm` failure handled by `else`.
      if rm -f "$existing_item"; then
        print_status "$PURPLE" "🗑️  Removed orphaned $item_type: $existing_item"
        if [ "$item_type" = "bundle" ]; then
          ((bundles_removed++)) # This counter is in the main shell.
        else
          ((files_removed++)) # This counter is in the main shell.
        fi
      else
        print_status "$RED" "❌ Failed to remove orphaned $item_type: $existing_item"
        ((errors++)) # This counter is in the main shell.
      fi
    fi
  done
else
  print_status "$YELLOW" "⚠️ Bundle directory $BUNDLE_DIR does not exist, skipping cleanup."
fi

# Count results from temporary tracking files
bundles_created_count=$(find "$BUNDLE_DIR" -name "*.created" 2>/dev/null | wc -l)
bundles_updated_count=$(find "$BUNDLE_DIR" -name "*.updated" 2>/dev/null | wc -l)
files_copied_count=$(find "$BUNDLE_DIR" -name "*.copied" 2>/dev/null | wc -l)
logged_item_processing_errors=$(find "$BUNDLE_DIR" -name "*.error" 2>/dev/null | wc -l)
unknown_types_logged=$( ([ -f "$UNKNOWN_ITEMS_TMP_FILE" ] && wc -l <"$UNKNOWN_ITEMS_TMP_FILE") || echo 0)
logged_item_processing_errors=$((logged_item_processing_errors + unknown_types_logged))

# Cleanup temporary tracking files
(find "$BUNDLE_DIR" -maxdepth 10 -type f \( -name "*.created" -o -name "*.updated" -o -name "*.error" -o -name "*.copied" \) -print0 | xargs -0 --no-run-if-empty rm -f) || true
rm -f "$EXPECTED_ITEMS_TMP_FILE" "$UNKNOWN_ITEMS_TMP_FILE" 2>/dev/null || true

# Print summary
echo
print_status "$BLUE" "=== Summary ==="
print_status "$GREEN" "✅ Bundles created: $bundles_created_count"
print_status "$GREEN" "🔄 Bundles updated: $bundles_updated_count"
print_status "$GREEN" "📎 Files copied/updated: $files_copied_count"
print_status "$PURPLE" "🗑️  Bundles removed: $bundles_removed"
print_status "$PURPLE" "🗑️  Files removed: $files_removed"

total_errors=$((errors + logged_item_processing_errors))

if [ $total_errors -gt 0 ]; then
  print_status "$RED" "❌ Errors reported: $total_errors (Processing: $logged_item_processing_errors, Cleanup: $errors)"
  exit 1
else
  print_status "$GREEN" "🎉 All operations completed successfully!"
fi
