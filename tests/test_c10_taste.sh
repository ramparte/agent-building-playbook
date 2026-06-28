#!/usr/bin/env bash
# Acceptance test for Task C10 — taste pattern files
# Validates that all 4 required pattern files exist with correct frontmatter and body sections.
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

echo "=== Task C10 — Taste & Expertise Pattern Files ==="
echo "Repo: $REPO"
echo ""

# --- List of required files ---
REQUIRED_FILES=(
    "find-the-hard-stuff.md"
    "develop-your-taste.md"
    "agents-amplify-experience.md"
    "automate-but-avoid-mystery-house.md"
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
echo "--- Dimensions include taste ---"
for f in "${REQUIRED_FILES[@]}"; do
    fp="$PATTERNS/$f"
    [ -f "$fp" ] || continue
    check "$f dimensions include taste" \
        "$(grep -q 'taste' "$fp" && echo ok || echo fail)"
done

echo ""
echo "--- Title checks ---"
check "find-the-hard-stuff.md title is 'Find the Hard Stuff'" \
    "$(grep -q '^title:.*Find the Hard Stuff' "$PATTERNS/find-the-hard-stuff.md" 2>/dev/null && echo ok || echo fail)"
check "develop-your-taste.md title is 'Develop Your Taste'" \
    "$(grep -q '^title:.*Develop Your Taste' "$PATTERNS/develop-your-taste.md" 2>/dev/null && echo ok || echo fail)"
check "agents-amplify-experience.md title is 'Agents Amplify Experience'" \
    "$(grep -q '^title:.*Agents Amplify Experience' "$PATTERNS/agents-amplify-experience.md" 2>/dev/null && echo ok || echo fail)"
check "automate-but-avoid-mystery-house.md title is 'Automate the Easy, Avoid the Mystery House'" \
    "$(grep -q '^title:.*Automate the Easy, Avoid the Mystery House' "$PATTERNS/automate-but-avoid-mystery-house.md" 2>/dev/null && echo ok || echo fail)"

echo ""
echo "--- Multi-dimension check for automate-but-avoid-mystery-house.md ---"
fp="$PATTERNS/automate-but-avoid-mystery-house.md"
if [ -f "$fp" ]; then
    check "automate-but-avoid-mystery-house.md dimensions include workflow-discipline" \
        "$(grep -q 'workflow-discipline' "$fp" && echo ok || echo fail)"
fi

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
    # Check that any URLs that appear are well-known real domains (anthropic.com, github.com)
    # or that there are no URLs at all — either is fine.
    # What we disallow: any URL with a clearly invented domain (placeholder.example.com, etc.)
    if grep -oP 'https?://\S+' "$fp" | grep -vqE '(anthropic\.com|github\.com|arxiv\.org|openai\.com|microsoft\.com)'; then
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
