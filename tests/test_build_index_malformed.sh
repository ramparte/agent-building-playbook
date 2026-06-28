#!/usr/bin/env bash
# Malformed-input test for scripts/build-index.sh
# Verifies that build-index.sh exits non-zero and names the offending file
# when a pattern is missing required frontmatter fields (one_liner absent).
set -uo pipefail

# -- helpers ------------------------------------------------------------------

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD="$REPO_ROOT/scripts/build-index.sh"

fail() {
    echo "FAIL: $*" >&2
    exit 1
}

# -- temp workspace with cleanup ----------------------------------------------

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

# -- fixture: pattern missing one_liner (only title + dimensions) -------------

PATTERNS="$WORK/patterns"
mkdir -p "$PATTERNS"

cat > "$PATTERNS/broken-pattern.md" <<'EOF'
---
title: Broken Pattern
dimensions: taste
---

# Broken Pattern

Body text here.
EOF

OUT="$WORK/INDEX.md"

# -- invoke build, capture combined output and RC -----------------------------

RC=0
ERROUT=$("$BUILD" "$PATTERNS" "$OUT" 2>&1) || RC=$?

# -- assertions ---------------------------------------------------------------

[ "$RC" -ne 0 ] \
    || fail "build-index.sh should exit non-zero on a pattern missing required fields (got RC=$RC)"

echo "$ERROUT" | grep -q 'broken-pattern.md' \
    || fail "error output should name the offending file 'broken-pattern.md' (got: $ERROUT)"

echo "MALFORMED-INPUT TEST PASSED"
