#!/usr/bin/env bash
# Acceptance test for Task C2 — workflow-discipline pattern files
# Validates that all 9 required pattern files exist with correct frontmatter and body sections.
set -uo pipefail

PASS=0
FAIL=0
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PATTERNS="$REPO/patterns"

check() {
    local desc="$1"
    local result="$2"
    if [ "$result" = "ok" ]; then
        echo "  PASS: $desc"
        PASS=$((PASS+1))
    else
        echo "  FAIL: $desc"
        FAIL=$((FAIL+1))
    fi
}

echo "=== Task C2 — Workflow Discipline Pattern Files ==="
echo "Repo: $REPO"
echo ""

# --- List of required files ---
REQUIRED_FILES=(
    "implement-to-learn.md"
    "keep-specs-in-sync.md"
    "document-intent.md"
    "rebuild-often.md"
    "gate-the-phases.md"
    "prove-on-small-sample.md"
    "decompose-on-timeout.md"
    "bite-sized-tasks.md"
    "clear-stop-condition.md"
)

echo "--- File existence ---"
for f in "${REQUIRED_FILES[@]}"; do
    check "$f exists" "$([ -f "$PATTERNS/$f" ] && echo ok || echo fail)"
done

echo ""
echo "--- Frontmatter fields ---"
for f in "${REQUIRED_FILES[@]}"; do
    fp="$PATTERNS/$f"
    [ -f "$fp" ] || continue
    check "$f has 'title:' in frontmatter"      "$(grep -q '^title:' "$fp" && echo ok || echo fail)"
    check "$f has 'one_liner:' in frontmatter"  "$(grep -q '^one_liner:' "$fp" && echo ok || echo fail)"
    check "$f has 'dimensions:' in frontmatter" "$(grep -q '^dimensions:' "$fp" && echo ok || echo fail)"
done

echo ""
echo "--- Dimensions include workflow-discipline ---"
for f in "${REQUIRED_FILES[@]}"; do
    fp="$PATTERNS/$f"
    [ -f "$fp" ] || continue
    check "$f dimensions include workflow-discipline" \
        "$(grep -q 'workflow-discipline' "$fp" && echo ok || echo fail)"
done

echo ""
echo "--- Required body sections ---"
REQUIRED_SECTIONS=(
    "## What it is"
    "## When to reach for it"
    "## When NOT to"
)
for f in "${REQUIRED_FILES[@]}"; do
    fp="$PATTERNS/$f"
    [ -f "$fp" ] || continue
    for section in "${REQUIRED_SECTIONS[@]}"; do
        check "$f has '$section'" "$(grep -qF "$section" "$fp" && echo ok || echo fail)"
    done
    check "$f has '## Exemplars'" "$(grep -q '^## Exemplars' "$fp" && echo ok || echo fail)"
done

echo ""
echo "--- No fabricated URLs (http patterns in Exemplars) ---"
for f in "${REQUIRED_FILES[@]}"; do
    fp="$PATTERNS/$f"
    [ -f "$fp" ] || continue
    # Provenance patterns cite many legitimate primary sources (blogs, talks,
    # papers, production systems), so an allowlist of domains is untenable.
    # Instead, disallow only clearly-fabricated placeholder domains.
    if grep -oP 'https?://\S+' "$fp" | grep -qiE '(example\.(com|org|net)|placeholder|your-?domain|foo\.bar|localhost|127\.0\.0\.1|todo|xxx+|lorem)'; then
        check "$f has no suspicious URLs" "fail"
    else
        check "$f has no suspicious URLs" "ok"
    fi
done

echo ""
echo "--- Frontmatter is flat (no nested YAML lists with leading -) ---"
for f in "${REQUIRED_FILES[@]}"; do
    fp="$PATTERNS/$f"
    [ -f "$fp" ] || continue
    # Extract frontmatter block (between first pair of ---)
    fm=$(awk '/^---/{count++; if(count==2) exit; next} count==1' "$fp")
    # Flat frontmatter must not have lines starting with '  -' or '- ' indented items
    if echo "$fm" | grep -qP '^\s+-\s'; then
        check "$f frontmatter is flat" "fail"
    else
        check "$f frontmatter is flat" "ok"
    fi
done

echo ""
echo "Results: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] && echo "ALL TESTS PASSED" && exit 0 || echo "TESTS FAILED" && exit 1
