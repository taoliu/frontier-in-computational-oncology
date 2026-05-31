#!/usr/bin/env python3
"""Clean ChatGPT Deep Research citation artifacts from Markdown files.

OpenAI Deep Research exports often contain internal citation markers like:

    citeturn25search3turn13search0

Those markers are useful only inside the original ChatGPT session. They are not
stable public citations and render strangely in Markdown/GitHub. This script can
strip them or replace them with a visible placeholder.

Examples:
    python scripts/clean_openai_citations.py --write \
        '01-deep-research/week-*/deep-research-report.md'

    python scripts/clean_openai_citations.py --check \
        '01-deep-research/week-*/deep-research-*.md'

    python scripts/clean_openai_citations.py --write --mode placeholder \
        '01-deep-research/week-*/deep-research-report.md'
"""

from __future__ import annotations

import argparse
import glob
import re
import sys
from pathlib import Path

# Complete artifacts, e.g. " citeturn1search0turn2view1"
COMPLETE_CITATION_RE = re.compile(r"[ \t]*cite[^\n]*")

# Dangling artifacts introduced by truncation/copying, e.g. " citeturn1"
DANGLING_CITATION_RE = re.compile(r"[ \t]*cite[^\n]*")

# Light cleanup after citation removal.
SPACE_BEFORE_PUNCT_RE = re.compile(r"[ \t]+([.,;:!?])")
TOO_MANY_SPACES_RE = re.compile(r" {2,}")


def clean_text(text: str, mode: str = "strip") -> tuple[str, int]:
    """Return cleaned text and number of citation artifacts changed."""
    placeholder = " [citation pending]" if mode == "placeholder" else ""

    count = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        return placeholder

    text = COMPLETE_CITATION_RE.sub(repl, text)
    text = DANGLING_CITATION_RE.sub(repl, text)

    # Tidy common markdown artifacts left after stripping terminal citations.
    text = SPACE_BEFORE_PUNCT_RE.sub(r"\1", text)
    text = TOO_MANY_SPACES_RE.sub(" ", text)
    text = re.sub(r" +\n", "\n", text)
    return text, count


def expand_patterns(patterns: list[str]) -> list[Path]:
    files: list[Path] = []
    for pattern in patterns:
        matches = [Path(p) for p in glob.glob(pattern, recursive=True)]
        if not matches:
            print(f"warning: no matches for pattern: {pattern}", file=sys.stderr)
        files.extend(matches)
    return sorted({p for p in files if p.is_file()})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("patterns", nargs="+", help="File paths or shell-style globs to clean")
    parser.add_argument(
        "--mode",
        choices=["strip", "placeholder"],
        default="strip",
        help="Strip artifacts entirely or replace them with [citation pending]",
    )
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true", help="Rewrite files in place")
    action.add_argument("--check", action="store_true", help="Exit nonzero if artifacts remain/would change")
    action.add_argument("--dry-run", action="store_true", help="Print files that would change")
    args = parser.parse_args()

    files = expand_patterns(args.patterns)
    changed_files: list[tuple[Path, int]] = []

    for path in files:
        original = path.read_text(encoding="utf-8")
        cleaned, count = clean_text(original, mode=args.mode)
        if cleaned != original:
            changed_files.append((path, count))
            if args.write:
                path.write_text(cleaned, encoding="utf-8")

    for path, count in changed_files:
        print(f"{path}: {count} citation artifact(s)")

    if args.check and changed_files:
        print(f"citation artifacts found in {len(changed_files)} file(s)", file=sys.stderr)
        return 1

    if not changed_files:
        print("No citation artifacts found.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
