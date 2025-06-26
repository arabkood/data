#!/bin/bash
#
# Bundle creation script with bidirectional sync
# Creates bundles from directory structure in ./topics and cleans up orphaned bundles

set -euo pipefail

TOPICS_DIR="./topics"
BUNDLE_DIR="./.bundles"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
NC='\033[0m'

# Counters
bundles_created=0
bundles_updated=0
files_copied=0
bundles_removed=0
files_removed=0
errors=0

# Function to print colored output
print_status() {
  local color=$1
  local message=$2
  echo -e "${color}${message}${NC}"
}

# Check prerequisites
check_prerequisites() {
  if [ ! -d "$TOPICS_DIR" ]; then
    print_status "$RED" "❌ Error: Topics directory '$TOPICS_DIR' does not exist"
    exit 1
  fi

  if ! command -v zip &>/dev/null; then
    print_status "$RED" "❌ Error: 'zip' command not found. Please install zip utility."
    exit 1
  fi

  if ! command -v realpath &>/dev/null; then
    print_status "$RED" "❌ Error: 'realpath' command not found. Please install it (usually in coreutils)."
    exit 1
  fi
}

# Create bundle directory
setup_bundle_dir() {
  mkdir -p "$BUNDLE_DIR"
  print_status "$BLUE" "📁 Bundle directory: $BUNDLE_DIR"
}

# Process a directory into a bundle
process_directory() {
  local source_path=$1
  local target_dir=$2
  local base_name=$3

  local bundle_name="$base_name.bundle.zip"
  local target_zip="$target_dir/$bundle_name"

  # Track as expected
  expected_bundles["$target_zip"]=1

  local needs_update=false
  local is_new=false

  if [ ! -f "$target_zip" ]; then
    needs_update=true
    is_new=true
  elif [ "$source_path" -nt "$target_zip" ] || find "$source_path" -type f -newer "$target_zip" -print -quit 2>/dev/null | grep -q '.'; then
    needs_update=true
  fi

  if [ "$needs_update" = true ]; then
    if [ "$is_new" = true ]; then
      print_status "$YELLOW" "📦 Creating new bundle for: $source_path"
    else
      print_status "$YELLOW" "📦 Updating bundle for: $source_path"
    fi

    rm -f "$target_zip"
    local absolute_target=$(realpath -m "$target_zip")

    if (cd "$source_path" && zip -rq "$absolute_target" .); then
      if [ "$is_new" = true ]; then
        print_status "$GREEN" "✅ Created bundle: $target_zip"
        bundles_created=$((bundles_created + 1))
      else
        print_status "$GREEN" "🔄 Updated bundle: $target_zip"
        bundles_updated=$((bundles_updated + 1))
      fi
    else
      print_status "$RED" "❌ Failed to create bundle: $target_zip"
      errors=$((errors + 1))
    fi
  else
    print_status "$BLUE" "⏭️  Bundle up to date: $target_zip"
  fi
}

# Process a file
process_file() {
  local source_path=$1
  local target_dir=$2
  local base_name=$3

  local target_file="$target_dir/$base_name"

  # Track as expected
  expected_files["$target_file"]=1

  local needs_update=false

  if [ ! -f "$target_file" ] || [ "$source_path" -nt "$target_file" ]; then
    needs_update=true
  fi

  if [ "$needs_update" = true ]; then
    if cp "$source_path" "$target_file"; then
      print_status "$BLUE" "📎 Copied/Updated file: $source_path → $target_file"
      files_copied=$((files_copied + 1))
    else
      print_status "$RED" "❌ Failed to copy file: $source_path"
      errors=$((errors + 1))
    fi
  else
    print_status "$BLUE" "⏭️  File up to date: $target_file"
  fi
}

# Main processing function
process_source_items() {
  print_status "$BLUE" "🔍 Scanning source directories and processing items..."

  # Use process substitution to avoid subshell issues
  while read -r path; do
    local rel_path_parent_dir=$(realpath --relative-to="$TOPICS_DIR" "$(dirname "$path")")
    local base_name=$(basename "$path")
    local target_dir="$BUNDLE_DIR/$rel_path_parent_dir"

    mkdir -p "$target_dir"

    if [ -d "$path" ]; then
      process_directory "$path" "$target_dir" "$base_name"
    elif [ -f "$path" ]; then
      process_file "$path" "$target_dir" "$base_name"
    else
      print_status "$YELLOW" "❓ Unknown item type: $path"
    fi
  done < <(find "$TOPICS_DIR" -path "$TOPICS_DIR/*/*/*/*/*" \
    -not -path "$TOPICS_DIR/*/*/*/*/*/*" \
    -not -path "*/.*" \
    -not -path "*/+*")
}

# Clean up orphaned items
cleanup_orphaned_items() {
  print_status "$PURPLE" "🧹 Cleaning up orphaned bundles and files..."

  if [ ! -d "$BUNDLE_DIR" ]; then
    print_status "$YELLOW" "⚠️ Bundle directory $BUNDLE_DIR does not exist, skipping cleanup."
    return
  fi

  # Use process substitution to avoid subshell issues
  while read -r existing_item; do
    local should_exist=false
    local item_type=""

    if [[ "$existing_item" == *.bundle.zip ]]; then
      item_type="bundle"
      if [[ -n "${expected_bundles[$existing_item]:-}" ]]; then
        should_exist=true
      fi
    else
      item_type="file"
      if [[ -n "${expected_files[$existing_item]:-}" ]]; then
        should_exist=true
      fi
    fi

    if [ "$should_exist" = false ]; then
      if rm -f "$existing_item" 2>/dev/null; then
        print_status "$PURPLE" "🗑️  Removed orphaned $item_type: $existing_item"
        if [ "$item_type" = "bundle" ]; then
          bundles_removed=$((bundles_removed + 1))
        else
          files_removed=$((files_removed + 1))
        fi
      else
        print_status "$RED" "❌ Failed to remove orphaned $item_type: $existing_item"
        errors=$((errors + 1))
      fi
    fi
  done < <(find "$BUNDLE_DIR" -type f)
}

# Print summary
print_summary() {
  echo
  print_status "$BLUE" "=== Summary ==="
  print_status "$GREEN" "✅ Bundles created: $bundles_created"
  print_status "$GREEN" "🔄 Bundles updated: $bundles_updated"
  print_status "$GREEN" "📎 Files copied/updated: $files_copied"
  print_status "$PURPLE" "🗑️  Bundles removed: $bundles_removed"
  print_status "$PURPLE" "🗑️  Files removed: $files_removed"

  if [ $errors -gt 0 ]; then
    print_status "$RED" "❌ Errors encountered: $errors"
    exit 1
  else
    print_status "$GREEN" "🎉 All operations completed successfully!"
  fi
}

# Declare associative arrays for tracking expected items (global scope)
declare -A expected_bundles
declare -A expected_files

# Main execution
main() {
  check_prerequisites
  setup_bundle_dir
  process_source_items
  cleanup_orphaned_items
  print_summary
}

# Run main function
main "$@"
