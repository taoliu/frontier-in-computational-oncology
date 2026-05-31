#!/usr/bin/env python3
"""Create a standardized deep-research intake file for a module."""
from __future__ import annotations
import argparse
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "deep-research-intake-template.md"

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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("week", type=int, choices=range(2, 14))
    parser.add_argument("--source", default="", help="Deep Research doc/link")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    out_dir = ROOT / "01-deep-research" / WEEK_DIRS[args.week]
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "deep-research-intake.md"
    if out_file.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite existing file: {out_file}")

    text = TEMPLATE.read_text()
    text = text.replace("Week XX", f"Week {args.week:02d}")
    text = text.replace("Module Title", MODULE_TITLES[args.week])
    text = text.replace("- Deep Research doc/link:", f"- Deep Research doc/link: {args.source}")
    text = text.replace("- Date received:", f"- Date received: {date.today().isoformat()}")
    text = text.replace("- Imported by:", "- Imported by: Claw")
    out_file.write_text(text)
    print(out_file)

if __name__ == "__main__":
    main()
