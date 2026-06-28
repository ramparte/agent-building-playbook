#!/usr/bin/env bash
# Acceptance test for Task A1 - run from repo root
set -euo pipefail

PASS=0
FAIL=0
REPO="${1:-$(pwd)}"

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

echo "=== Task A1 Scaffold Acceptance Tests ==="
echo "Repo: $REPO"

cd "$REPO"

check "patterns/ directory exists" "$([ -d patterns ] && echo ok || echo fail)"
check "scripts/ directory exists" "$([ -d scripts ] && echo ok || echo fail)"
check "tests/ directory exists"   "$([ -d tests ] && echo ok || echo fail)"
check ".github/workflows/ directory exists" "$([ -d .github/workflows ] && echo ok || echo fail)"
check "patterns/.gitkeep exists" "$([ -f patterns/.gitkeep ] && echo ok || echo fail)"
check "docs/seed-research-dump.md exists" "$([ -f docs/seed-research-dump.md ] && echo ok || echo fail)"
check "README.md NOT at repo root" "$([ ! -f README.md ] && echo ok || echo fail)"
check ".gitignore exists" "$([ -f .gitignore ] && echo ok || echo fail)"
check ".gitignore has .DS_Store entry" "$(grep -q '.DS_Store' .gitignore 2>/dev/null && echo ok || echo fail)"
check ".gitignore has .amplifier/ entry" "$(grep -q '.amplifier/' .gitignore 2>/dev/null && echo ok || echo fail)"
check ".gitignore has *.tmp entry" "$(grep -q '\*.tmp' .gitignore 2>/dev/null && echo ok || echo fail)"

echo ""
echo "Results: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] && echo "ALL TESTS PASSED" && exit 0 || echo "TESTS FAILED" && exit 1
