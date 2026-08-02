#!/bin/bash
set -uo pipefail
# Deliberately not `set -e` - keep going after a failure so we get a
# full pass/fail summary across every devnote, not just the first one.

# Submits a DRAFT for every devnote currently in devnotes/ (any directory
# with a curvenote.yml), directly via the curvenote CLI - no git commits,
# no GitHub Actions. Matches Anton's documented manual-submit command
# (same venue/kind/collection as draft.yml/submit.yml), run from inside
# each devnote's own directory.
#
# Uses --draft on purpose - this is for review/QA (getting a build/preview
# link per devnote to manually check notebooks-ran/content/etc against),
# not for real curator-visible submissions. Use a separate, deliberate
# run without --draft when you actually want to submit for real.
#
# Requires `curvenote token set` already run in this shell/machine.
# Uses curvenote@latest explicitly - `submit` enforces a minimum CLI
# version (0.14.2+) that plain `npx curvenote` (which can resolve to an
# older cached/pinned version) doesn't always satisfy.
#
# Run from anywhere inside a clone of nucleus-eng/2026-CERN-OHL-P.
# Written for bash 3.2 (macOS default) - no associative arrays.

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

DEVNOTES=()
for path in devnotes/*/; do
  d="${path%/}"
  d="${d#devnotes/}"
  if [ -f "devnotes/$d/curvenote.yml" ]; then
    DEVNOTES+=("$d")
  fi
done

echo "Found ${#DEVNOTES[@]} devnotes: ${DEVNOTES[*]}"

RESULT_NAMES=()
RESULT_STATUSES=()
RESULT_URLS=()

for d in "${DEVNOTES[@]}"; do
  path="devnotes/$d"
  echo
  echo "==================== $d ===================="
  logfile="$path/_build/logs/curvenote.submit.json"
  rm -f "$logfile"
  (
    cd "$path"
    npx --yes curvenote@latest submit bnext-devnotes --kind devnote --collection developer-cells --draft -y
  )
  rc=$?
  RESULT_NAMES+=("$d")
  if [ $rc -eq 0 ]; then
    RESULT_STATUSES+=("OK")
  else
    RESULT_STATUSES+=("FAILED")
  fi
  url=""
  if [ -f "$logfile" ]; then
    url=$(python3 -c "import json;print(json.load(open('$logfile')).get('buildUrl',''))" 2>/dev/null)
  fi
  RESULT_URLS+=("$url")
done

echo
echo "==================== Summary ===================="
i=0
for d in "${RESULT_NAMES[@]}"; do
  printf "%-30s %-8s %s\n" "$d" "${RESULT_STATUSES[$i]}" "${RESULT_URLS[$i]}"
  i=$((i + 1))
done
