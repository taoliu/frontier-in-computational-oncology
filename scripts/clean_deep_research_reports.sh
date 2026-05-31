#!/usr/bin/env bash
set -euo pipefail

# Clean OpenAI/ChatGPT Deep Research internal citation markers from imported
# deep-research Markdown reports and intake excerpts.
#
# Usage:
#   scripts/clean_deep_research_reports.sh          # rewrite files in place
#   scripts/clean_deep_research_reports.sh --check  # fail if artifacts remain
#   scripts/clean_deep_research_reports.sh --dry-run

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

ACTION="${1:---write}"

python3 scripts/clean_openai_citations.py "$ACTION" \
  '01-deep-research/week-*/deep-research-report.md' \
  '01-deep-research/week-*/deep-research-intake.md'
