#!/usr/bin/env python3
"""Check whether a module has the expected production scaffold files."""

from __future__ import annotations

import argparse
from pathlib import Path

from scaffold_module_materials import WEEK_DIRS, MODULE_TITLES

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "01-deep-research/{week}/deep-research-report.md",
    "01-deep-research/{week}/deep-research-intake.md",
    "01-deep-research/{week}/source-validation.md",
    "02-source-validation/{week}/validated-sources.md",
    "02-source-validation/{week}/source-notes.md",
    "03-lecture-plans/{week}/lecture-plan.md",
    "04-slides/{week}/slide-outline.md",
    "05-scripts/{week}/lecture-01-script.md",
    "05-scripts/{week}/lecture-02-script.md",
    "05-scripts/{week}/lecture-03-script.md",
    "06-audio/{week}/audio-manifest.md",
    "07-assets/images/{week}/asset-manifest.md",
    "07-assets/references/{week}/source-bibliography.md",
    "08-exports/{week}/README.md",
    "MATERIALS_STATUS/{week}.md",
]

CITATION_ARTIFACTS = ("cite", "turn", "")


def has_artifacts(path: Path) -> bool:
    if path.suffix.lower() not in {".md", ".txt"}:
        return False
    text = path.read_text(errors="ignore")
    return any(marker in text for marker in CITATION_ARTIFACTS)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("week", type=int, choices=range(2, 14))
    args = parser.parse_args()

    week = WEEK_DIRS[args.week]
    title = MODULE_TITLES[args.week]
    print(f"Week {args.week:02d} — {title}")

    missing = []
    artifact_files = []
    for pattern in REQUIRED:
        path = ROOT / pattern.format(week=week)
        if not path.exists():
            missing.append(path)
            print(f"MISSING  {path.relative_to(ROOT)}")
        else:
            print(f"OK       {path.relative_to(ROOT)}")
            if has_artifacts(path):
                artifact_files.append(path)

    if artifact_files:
        print("\nCitation artifacts remain:")
        for path in artifact_files:
            print(f"ARTIFACT {path.relative_to(ROOT)}")

    if missing or artifact_files:
        return 1
    print("\nModule scaffold looks ready.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
