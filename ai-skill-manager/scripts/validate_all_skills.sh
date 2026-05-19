#!/usr/bin/env bash
# Validate every skill directory under the repo root that contains SKILL.md.
set -euo pipefail

ROOT="${1:-$(cd "$(dirname "$0")/../.." && pwd)}"
VALIDATOR="${SKILL_VALIDATOR:-$HOME/.claude/skills/skill-creator/scripts/quick_validate.py}"

if [[ ! -f "$VALIDATOR" ]]; then
  echo "error: quick_validate.py not found at $VALIDATOR" >&2
  echo "Set SKILL_VALIDATOR to the skill-creator validate script path." >&2
  exit 1
fi

failed=0
count=0

while IFS= read -r skill_md; do
  dir=$(dirname "$skill_md")
  count=$((count + 1))
  if python3 "$VALIDATOR" "$dir" >/dev/null 2>&1; then
    echo "ok  $(basename "$dir")"
  else
    echo "FAIL $(basename "$dir")"
    python3 "$VALIDATOR" "$dir" || true
    failed=$((failed + 1))
  fi
done < <(find "$ROOT" -mindepth 2 -maxdepth 2 -name SKILL.md | sort)

echo "---"
echo "checked: $count  failed: $failed"
exit "$failed"
