#!/usr/bin/env bash
# scripts/build-index.sh — generate INDEX.md from patterns/*.md frontmatter
set -euo pipefail

# Pin collation so sort order is identical on every machine (macOS UTF-8
# locales fold case differently than CI's C locale, causing INDEX churn).
export LC_ALL=C

PATTERNS_DIR="${1:-patterns}"
OUTPUT_FILE="${2:-INDEX.md}"

# Validate input
if [[ ! -d "$PATTERNS_DIR" ]]; then
    echo "ERROR: not a directory: $PATTERNS_DIR" >&2
    exit 1
fi

# Temp files — cleaned up on exit
rows="$(mktemp)"
tmp_out="$(mktemp)"
trap 'rm -f "$rows" "$tmp_out"' EXIT

# extract_field FIELD FILE
# Prints the trimmed value of a flat frontmatter field.
# Scans only the frontmatter block (NR==1 '---' to next '---').
extract_field() {
    local field="$1"
    local file="$2"
    awk -v field="$field" '
        NR==1 && /^---/ { in_front=1; next }
        in_front && /^---/ { exit }
        in_front {
            if ($0 ~ ("^" field ":")) {
                val = $0
                sub("^" field ":[[:space:]]*", "", val)
                gsub(/[[:space:]]+$/, "", val)
                print val
            }
        }
    ' "$file"
}

# Gather pattern files
shopt -s nullglob
files=("$PATTERNS_DIR"/*.md)
if [[ ${#files[@]} -eq 0 ]]; then
    echo "ERROR: no pattern files found in $PATTERNS_DIR" >&2
    exit 1
fi

# Build rows: tag TAB title TAB path TAB one_liner
for file in "${files[@]}"; do
    path="$file"
    title="$(extract_field title "$file")"
    one_liner="$(extract_field one_liner "$file")"
    dimensions="$(extract_field dimensions "$file")"

    if [ -z "$title" ] || [ -z "$one_liner" ] || [ -z "$dimensions" ]; then echo "ERROR: $file is missing one or more required frontmatter fields (title, one_liner, dimensions)" >&2; exit 1; fi

    # Split dimensions on comma
    IFS=',' read -ra tags <<< "$dimensions"

    for tag in "${tags[@]}"; do
        # Trim whitespace
        tag="$(printf '%s' "$tag" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
        # Skip empty
        [[ -z "$tag" ]] && continue
        # Append row: tag TAB title TAB path TAB one_liner
        printf '%s\t%s\t%s\t%s\n' "$tag" "$title" "$path" "$one_liner" >> "$rows"
    done
done

# Write header to tmp_out
{
    echo '# INDEX — Agent-Building Playbook'
    echo ''
    echo '> GENERATED FILE — do not edit by hand. Regenerate with `scripts/build-index.sh`.'
    echo '> Dense, skim-and-select pattern list. Patterns appear under every tag they carry.'
} > "$tmp_out"

# Compute sorted unique tags from rows
tags_sorted="$(cut -f1 "$rows" | sort -u)"

# Emit one section per tag
while IFS= read -r tag; do
    printf '\n## %s\n' "$tag" >> "$tmp_out"
    # Find matching rows, sort by title (field 2), emit list items
    awk -F'\t' -v tag="$tag" '$1 == tag { print }' "$rows" \
        | sort -t$'\t' -k2,2 \
        | while IFS=$'\t' read -r _tag row_title row_path row_one_liner; do
            printf -- '- [%s](%s) — %s\n' "$row_title" "$row_path" "$row_one_liner"
          done >> "$tmp_out"
done <<< "$tags_sorted"

# Atomically write output
mv "$tmp_out" "$OUTPUT_FILE"
echo "Wrote $OUTPUT_FILE" >&2
