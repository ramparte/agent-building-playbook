#!/usr/bin/env bash
# Happy-path test for scripts/build-index.sh (TDD red — build-index.sh does not exist yet)
set -uo pipefail

# ── helpers ─────────────────────────────────────────────────────────────────

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD="$REPO_ROOT/scripts/build-index.sh"

fail() {
    echo "FAIL: $*" >&2
    exit 1
}

# ── temp workspace with cleanup ──────────────────────────────────────────────

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

# ── fixture patterns ─────────────────────────────────────────────────────────

PATTERNS="$WORK/patterns"
mkdir -p "$PATTERNS"

cat > "$PATTERNS/alpha-pattern.md" <<'EOF'
---
title: Alpha Pattern
one_liner: Alpha does the first thing clearly.
dimensions: meta-principles, reliability
---

# Alpha Pattern

Alpha body text.
EOF

cat > "$PATTERNS/beta-pattern.md" <<'EOF'
---
title: Beta Pattern
one_liner: Beta handles the second case.
dimensions: reliability
---

# Beta Pattern

Beta body text.
EOF

cat > "$PATTERNS/gamma-pattern.md" <<'EOF'
---
title: Gamma Pattern
one_liner: Gamma covers the third path.
dimensions: orchestration
---

# Gamma Pattern

Gamma body text.
EOF

OUT="$WORK/INDEX.md"

# ── invoke build ─────────────────────────────────────────────────────────────

"$BUILD" "$PATTERNS" "$OUT" \
    || fail "build-index.sh exited non-zero on valid fixtures"

# ── assertions ───────────────────────────────────────────────────────────────

[ -f "$OUT" ] \
    || fail "INDEX.md was not created at $OUT"

grep -q '^## meta-principles' "$OUT" \
    || fail "heading '## meta-principles' missing from INDEX.md"

grep -q '^## reliability' "$OUT" \
    || fail "heading '## reliability' missing from INDEX.md"

grep -q '^## orchestration' "$OUT" \
    || fail "heading '## orchestration' missing from INDEX.md"

# Alpha carries two dimension tags so its title must appear at least twice
alpha_count="$(grep -c 'Alpha Pattern' "$OUT" || true)"
[ "$alpha_count" -ge 2 ] \
    || fail "Alpha Pattern should appear at least twice (multi-tag); found $alpha_count"

grep -q 'Alpha does the first thing clearly\.' "$OUT" \
    || fail "one_liner for Alpha Pattern missing from INDEX.md"

grep -q 'Beta handles the second case\.' "$OUT" \
    || fail "one_liner for Beta Pattern missing from INDEX.md"

grep -q 'Gamma covers the third path\.' "$OUT" \
    || fail "one_liner for Gamma Pattern missing from INDEX.md"

grep -q 'alpha-pattern\.md' "$OUT" \
    || fail "link 'alpha-pattern.md' missing from INDEX.md"

echo "HAPPY-PATH TEST PASSED"
