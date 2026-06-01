# Material Generation Workflow

This repository treats each weekly module as a reproducible production pipeline:

```text
Deep Research intake
  → source validation
  → lecture plan
  → slide outline / figure plan
  → text-only slide content
  → speaker scripts
  → audio notes / generated audio
  → HTML slide manifest
  → HTML lecture export
```

## Principles

1. **Do not use Deep Research claims directly in slides.** Treat them as leads until validated.
2. **Source validation comes first.** Each high-value claim should have a DOI, stable URL, dataset page, or tool documentation link.
3. **Lecture plans should use only validated or explicitly marked provisional sources.**
4. **Slides should be generated from lecture plans, not from the raw Deep Research report.**
5. **Every figure or asset needs provenance.** Record whether it is recreated, original, generated, adapted, or cited.
6. **Scripts and audio follow slide IDs.** This keeps later regeneration targeted.
7. **Keep private source links out of the public repository.** Public files should not include private Google Docs, Telegram attachment IDs, or personal contact details.
8. **Close every lecture with forward context.** The final slide script of each lecture should end with a short preview of what comes next. If another lecture remains in the same week, preview the next lecture. If it is the final lecture of the week, preview the next module instead.


## Figure policy for public materials

- Store original/generated schematics in the public repository when possible.
- For publication figures that may be useful in live teaching, store a **placeholder** instead of the extracted figure.
- Each placeholder should include source ID, suggested paper/figure target when known, what the figure should demonstrate, and this note: “Human reviewer may insert original publication figure if license/fair-use context is appropriate.”
- Do not commit extracted copyrighted publication figures to the public repository unless the license is clearly reusable.

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

### 6. Audio

Outputs:
- `06-audio/week-XX-topic/audio-manifest.md`

Gate:
- Regeneration notes exist for any audio segments.
- Audio segments follow slide IDs.
- Default delivery uses one MP3 per slide unless a later step requires finer timing.

### 7. HTML slide/audio delivery

Outputs:
- `04-slides/week-XX-topic/html-manifest/lecture-XX.json`
- `08-exports/week-XX-topic/html/lecture-XX/index.html`

Gate:
- HTML player supports slide navigation, step-by-step reveal, matching slide audio, transcript/source panels, and local browser playback.
- Export records which slide text, script, audio, and asset versions were used.
- Visuals remain placeholders unless generated/approved assets are explicitly available.

## Week 02 pilot

Use Week 02 Functional Genomics as the pilot module before scaling to the remaining weeks. The pilot should test:

- Whether the validation table has the right fields.
- How many sources can be validated per pass.
- Whether the lecture-plan template is detailed enough for slide generation.
- Whether figure/asset manifest fields catch provenance and copyright risks early.
- How much script detail is needed before audio generation.
- Whether the HTML slide/audio player can deliver slide-by-slide content with synchronized audio comfortably.
