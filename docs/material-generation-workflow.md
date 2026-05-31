# Material Generation Workflow

This repository treats each weekly module as a reproducible production pipeline:

```text
Deep Research intake
  → source validation
  → lecture plan
  → slide outline / figure plan
  → speaker scripts
  → audio notes / generated audio
  → assets and exports
```

## Principles

1. **Do not use Deep Research claims directly in slides.** Treat them as leads until validated.
2. **Source validation comes first.** Each high-value claim should have a DOI, stable URL, dataset page, or tool documentation link.
3. **Lecture plans should use only validated or explicitly marked provisional sources.**
4. **Slides should be generated from lecture plans, not from the raw Deep Research report.**
5. **Every figure or asset needs provenance.** Record whether it is recreated, original, generated, adapted, or cited.
6. **Scripts and audio follow slide IDs.** This keeps later regeneration targeted.
7. **Keep private source links out of the public repository.** Public files should not include private Google Docs, Telegram attachment IDs, or personal contact details.

## Stage gates

### 1. Deep Research intake

Inputs:
- `01-deep-research/week-XX-topic/deep-research-report.md`
- `01-deep-research/week-XX-topic/deep-research-intake.md`
- `01-deep-research/week-XX-topic/source-validation.md`

Gate:
- OpenAI/ChatGPT citation artifacts removed with `scripts/clean_deep_research_reports.sh --check`.
- Source-validation queue exists.

### 2. Source validation

Outputs:
- `02-source-validation/week-XX-topic/validated-sources.md`
- `02-source-validation/week-XX-topic/source-notes.md`

Gate:
- Required sources are marked `verified` or `partial` with careful wording.
- Unsupported or weak claims are marked `replace` or `reject`.
- Lecture-critical numerical claims are checked against primary sources.

### 3. Lecture plan

Output:
- `03-lecture-plans/week-XX-topic/lecture-plan.md`

Gate:
- Three-lecture arc is coherent.
- Learning goals, methods, case studies, assignments, and figure needs are explicit.
- Source list points back to validated source IDs.

### 4. Slide outline and figure plan

Outputs:
- `04-slides/week-XX-topic/slide-outline.md`
- `07-assets/images/week-XX-topic/asset-manifest.md`

Gate:
- Every slide has a purpose, takeaway, source IDs, and figure/asset status.
- Any generated or recreated figure has a clear design brief.

### 5. Speaker scripts

Outputs:
- `05-scripts/week-XX-topic/lecture-01-script.md`
- `05-scripts/week-XX-topic/lecture-02-script.md`
- `05-scripts/week-XX-topic/lecture-03-script.md`

Gate:
- Scripts match slide IDs.
- Technical claims remain source-traceable.
- Pronunciation notes are captured for audio generation.

### 6. Audio and exports

Outputs:
- `06-audio/week-XX-topic/audio-manifest.md`
- `08-exports/week-XX-topic/`

Gate:
- Regeneration notes exist for any audio segments.
- Exported slide/script versions are recorded.

## Week 02 pilot

Use Week 02 Functional Genomics as the pilot module before scaling to the remaining weeks. The pilot should test:

- Whether the validation table has the right fields.
- How many sources can be validated per pass.
- Whether the lecture-plan template is detailed enough for slide generation.
- Whether figure/asset manifest fields catch provenance and copyright risks early.
- How much script detail is needed before audio generation.
