# Frontier in Computational Oncology

Teaching material and production workspace for the **Frontier in Computational Oncology** graduate course.

## Production workflow

1. **Course outline**
   - Keep canonical syllabus, week/module plan, assessment design, and lecture map in `00-course-outline/`.

2. **Deep research intake**
   - Store ChatGPT Deep Research outputs from Dr. Liu in `01-deep-research/week-XX-topic/`.
   - Use one file per module unless a module becomes large enough to split by lecture.

3. **Source validation**
   - Validate cited papers, URLs, DOIs, tools, datasets, and claims in `02-source-validation/`.
   - Track source status before using claims in slides or scripts.

4. **Lecture planning**
   - Convert validated research into three-lecture module plans in `03-lecture-plans/`.
   - Each lecture should include learning goals, conceptual arc, methods, figures/assets needed, and assignments/discussion prompts.

5. **Slides**
   - Draft slide outlines and final slide assets in `04-slides/`.
   - Keep source attribution attached to every figure/table/claim.

6. **Scripts**
   - Write lecture narration scripts in `05-scripts/`.
   - Scripts should align with slide IDs and include optional spoken transitions.

7. **Audio**
   - Store generated audio files and voice-generation notes in `06-audio/`.

8. **Assets and exports**
   - Store reusable images, diagrams, reference files, and generated exports in `07-assets/` and `08-exports/`.

## Repository conventions

- Weeks are numbered using `week-02` through `week-13` for deep research modules.
- Use Markdown for research notes, validation logs, lecture plans, and scripts unless another format is required.
- Keep generated binary files out of Git when they are large; use local storage or external Drive links as needed.
- Prefer source-linked claims: every important claim in slides/scripts should trace back to a validated citation or dataset.

## Utility scripts

- `scripts/clean_deep_research_reports.sh` removes ChatGPT/OpenAI Deep Research internal citation artifacts from imported report/intake Markdown files.
- `scripts/clean_openai_citations.py` is the reusable cleaner; use `--check`, `--dry-run`, or `--write`.

## Source documents

Private planning docs and Google Doc links are intentionally not stored in this public repository. Public-facing course materials should be derived from the versioned Markdown files in this repo.
