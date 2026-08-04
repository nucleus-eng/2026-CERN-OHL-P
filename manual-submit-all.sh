#!/bin/bash
set -uo pipefail
# Deliberately not `set -e` - keep going after a failure so we get a
# full pass/fail summary across every devnote, not just the first one.

# Submits every devnote currently in devnotes/ (any directory with a
# curvenote.yml), directly via the curvenote CLI - no git commits, no
# GitHub Actions. Matches Anton's documented manual-submit command (same
# venue/kind/collection as draft.yml/submit.yml), run from inside each
# devnote's own directory.
#
# Mode defaults to --draft (review/QA build link, not curator-visible).
# Pass --final (or --real) as the first arg, or set MODE=final, to submit
# for real instead - only do that deliberately.
#
#   ./manual-submit-all.sh            # draft (default)
#   ./manual-submit-all.sh --draft    # draft, explicit
#   ./manual-submit-all.sh --final    # real submission, all devnotes
#   MODE=final ./manual-submit-all.sh # same, via env var
#
# Requires `curvenote token set` already run in this shell/machine.
# Uses curvenote@latest explicitly - `submit` enforces a minimum CLI
# version (0.14.2+) that plain `npx curvenote` (which can resolve to an
# older cached/pinned version) doesn't always satisfy.
#
# Runs devnotes concurrently (default 6 at a time, override with
# CONCURRENCY=n) via xargs -P - each submission is an independent CLI
# invocation in its own directory, so there's no shared state to race on
# beyond npx's package cache, which is already warm after the first call.
#
# Run from anywhere inside a clone of nucleus-eng/2026-CERN-OHL-P.
# Written for bash 3.2 (macOS default) - no associative arrays.

MODE="${MODE:-draft}"
case "${1:-}" in
  --final|--real) MODE="final" ;;
  --draft) MODE="draft" ;;
  "") ;;
  *) echo "Usage: $0 [--draft|--final]" >&2; exit 2 ;;
esac

case "$MODE" in
  draft) SUBMIT_FLAG="--draft" ;;
  final) SUBMIT_FLAG="" ;;
  *) echo "Unknown MODE '$MODE' (expected draft or final)" >&2; exit 2 ;;
esac
export SUBMIT_FLAG

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

CONCURRENCY="${CONCURRENCY:-6}"

DEVNOTES=()
for path in devnotes/*/; do
  d="${path%/}"
  d="${d#devnotes/}"
  if [ -f "devnotes/$d/curvenote.yml" ]; then
    DEVNOTES+=("$d")
  fi
done

echo "Found ${#DEVNOTES[@]} devnotes: ${DEVNOTES[*]} (mode=$MODE, concurrency=$CONCURRENCY)"
if [ "$MODE" = "final" ]; then
  echo "*** REAL, CURATOR-VISIBLE SUBMISSION - not a draft ***"
fi

RESULTS_DIR="$(mktemp -d "${TMPDIR:-/tmp}/curvenote-submit-XXXXXX")"
trap 'rm -rf "$RESULTS_DIR"' EXIT

submit_one() {
  d="$1"
  path="devnotes/$d"
  logfile="$path/_build/logs/curvenote.submit.json"
  outlog="$RESULTS_DIR/$d.log"
  rm -f "$logfile"
  (
    cd "$path"
    npx --yes curvenote@latest submit bnext-devnotes --kind devnote --collection developer-cells $SUBMIT_FLAG -y
  ) >"$outlog" 2>&1
  rc=$?
  url=""
  if [ -f "$logfile" ]; then
    url=$(python3 -c "import json;print(json.load(open('$logfile')).get('buildUrl',''))" 2>/dev/null)
  fi
  status="OK"
  [ $rc -eq 0 ] || status="FAILED"
  printf '%s\t%s\t%s\n' "$d" "$status" "$url" >"$RESULTS_DIR/$d.result"
  echo
  echo "==================== $d: $status ===================="
  cat "$outlog"
}
export -f submit_one
export RESULTS_DIR

printf '%s\n' "${DEVNOTES[@]}" | xargs -P "$CONCURRENCY" -I{} bash -c 'submit_one "$@"' _ {}

echo
echo "==================== Summary ===================="
for d in "${DEVNOTES[@]}"; do
  if [ -f "$RESULTS_DIR/$d.result" ]; then
    IFS=$'\t' read -r name status url <"$RESULTS_DIR/$d.result"
    printf "%-30s %-8s %s\n" "$name" "$status" "$url"
  else
    printf "%-30s %-8s %s\n" "$d" "MISSING" ""
  fi
done
