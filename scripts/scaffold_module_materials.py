#!/usr/bin/env python3
"""Create the reusable material-generation scaffold for a course week.

This does not generate final teaching content. It creates the production files
for source validation, lecture planning, slide outlining, scripts, audio notes,
assets, and exports so a week can move through the pipeline consistently.
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

WEEK_DIRS = {
    2: "week-02-functional-genomics",
    3: "week-03-single-cell-multimodal",
    4: "week-04-spatial-omics",
    5: "week-05-somatic-mutation-evolution",
    6: "week-06-networks-systems-oncology",
    7: "week-07-perturbation-drug-screening",
    8: "week-08-clinical-informatics",
    9: "week-09-computational-pathology-imaging",
    10: "week-10-foundation-models",
    11: "week-11-generative-ai-agents",
    12: "week-12-digital-twins",
    13: "week-13-clinical-translation",
}

MODULE_TITLES = {
    2: "Functional Genomics in Cancer",
    3: "Single-Cell and Multimodal Regulatory Genomics",
    4: "Spatial Omics of the Tumor Microenvironment",
    5: "Somatic Mutation, Variant Interpretation, and Cancer Evolution",
    6: "Gene Regulation, Networks, and Systems Oncology",
    7: "Drug Screening, Perturbation Modeling, and Virtual Cell Models",
    8: "Clinical Informatics and Outcome Prediction",
    9: "Computational Pathology and Cancer Imaging",
    10: "Foundation Models for Biomedical and Cancer Data",
    11: "Generative AI, Agents, and Knowledge Systems for Oncology",
    12: "Digital Twins: Virtual Cell, Virtual Tumor, and Virtual Patient",
    13: "Clinical Translation of Computational Methods in Oncology",
}

TEMPLATES = {
    "02-source-validation/{week}/validated-sources.md": "validated-sources-template.md",
    "02-source-validation/{week}/source-notes.md": "source-notes-template.md",
    "03-lecture-plans/{week}/lecture-plan.md": "lecture-plan-template.md",
    "04-slides/{week}/slide-outline.md": "slide-outline-template.md",
    "05-scripts/{week}/lecture-01-script.md": "script-template.md",
    "05-scripts/{week}/lecture-02-script.md": "script-template.md",
    "05-scripts/{week}/lecture-03-script.md": "script-template.md",
    "06-audio/{week}/audio-manifest.md": "audio-manifest-template.md",
    "07-assets/images/{week}/asset-manifest.md": "assets-manifest-template.md",
    "07-assets/references/{week}/source-bibliography.md": "validated-sources-template.md",
    "08-exports/{week}/.gitkeep": None,
    "08-exports/{week}/README.md": None,
    "MATERIALS_STATUS/{week}.md": "module-status-template.md",
}


def render_template(text: str, week_num: int, week_slug: str, title: str, lecture: str | None = None) -> str:
    text = text.replace("Week XX", f"Week {week_num:02d}")
    text = text.replace("Module Title", title)
    text = text.replace("week-XX-topic", week_slug)
    text = text.replace("- Last updated:", f"- Last updated: {date.today().isoformat()}")
    text = text.replace("- Module:", f"- Module: Week {week_num:02d} — {title}")
    if lecture:
        text = text.replace("- Lecture:", f"- Lecture: {lecture}")
    return text


def write_file(path: Path, content: str, force: bool) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    existed = path.exists()
    if existed and not force:
        return "exists"
    path.write_text(content)
    return "overwritten" if existed else "created"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("week", type=int, choices=range(2, 14))
    parser.add_argument("--force", action="store_true", help="Overwrite existing scaffold files")
    args = parser.parse_args()

    week_slug = WEEK_DIRS[args.week]
    title = MODULE_TITLES[args.week]
    template_dir = ROOT / "templates"

    for rel_pattern, template_name in TEMPLATES.items():
        rel = rel_pattern.format(week=week_slug)
        out = ROOT / rel
        if template_name is None:
            content = "" if out.name == ".gitkeep" else f"# Week {args.week:02d} — {title} — Exports\n\nGenerated exports for this module.\n"
        else:
            content = (template_dir / template_name).read_text()
            lecture = None
            if "lecture-01" in rel:
                lecture = "Lecture 1 — Background & Problem Definition"
            elif "lecture-02" in rel:
                lecture = "Lecture 2 — Method Development & Verification"
            elif "lecture-03" in rel:
                lecture = "Lecture 3 — Application & State of the Field"
            content = render_template(content, args.week, week_slug, title, lecture)
        status = write_file(out, content, args.force)
        print(f"{status}: {rel}")


if __name__ == "__main__":
    main()
