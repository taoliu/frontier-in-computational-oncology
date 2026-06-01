# Week 02 Pilot Retrospective — Functional Genomics in Cancer

Date: 2026-05-31

## Goal

Test an end-to-end material-generation pipeline on Week 02 before scaling to additional course modules.

## Pipeline tested

```text
Deep Research intake
  → clean OpenAI citation artifacts
  → source validation
  → lecture plan
  → slide-ready outline
  → text-only slide content
  → lecturer script
  → visual prompt/template policy
  → audio pilot
```

## What worked

1. **Deep Research intake can be public-repo safe**
   - Raw reports are stored as Markdown.
   - Private Google Doc links and Telegram attachment UUIDs were removed.
   - ChatGPT/OpenAI internal citation artifacts were stripped using `scripts/clean_deep_research_reports.sh`.

2. **Source validation should be the first real gate**
   - Week 02 now has 19 source groups checked.
   - 18 are verified.
   - 1 remains partial only for citation-date wording nuance: ENCODE/cCRE update (`S008`).
   - Validated source IDs are now used throughout lecture/slide/script files.

3. **Slide text should be generated before visual production**
   - The useful intermediate product is `slide-text.md`: concise slide text, visual placeholder, speaker intent, and source IDs.
   - This is better than jumping directly from outline to PowerPoint.

4. **Visual strategy should be prompt/placeholder first**
   - Human lecturer preference: do not spend much time generating figures.
   - Use placeholders for publication figures.
   - Save optional `gpt-image-2` prompts for generated visual drafts.
   - Do not commit generated images unless explicitly approved.
   - Existing SVGs are rough templates only, not final assets.

5. **Lecturer scripts are feasible and useful**
   - Lecture 1 script was generated as slide-by-slide speaker notes with transitions.
   - Audio pronunciation notes are important for acronyms and assay names.

6. **Audio pilot succeeded after enabling TTS model access**
   - Model: `gpt-4o-mini-tts-2025-12-15`
   - Voice: `cedar`
   - Output: MP3
   - Generated Lecture 1 slides 1–3 as separate clips.
   - Dr. Liu judged the audio quality “really nice.”

## Current Week 02 artifacts

- Deep research intake: `01-deep-research/week-02-functional-genomics/`
- Source validation: `02-source-validation/week-02-functional-genomics/`
- Lecture plan: `03-lecture-plans/week-02-functional-genomics/lecture-plan.md`
- Slide-ready outline: `04-slides/week-02-functional-genomics/slide-outline.md`
- Text-only slide content: `04-slides/week-02-functional-genomics/slide-text.md`
- Lecture 1 script: `05-scripts/week-02-functional-genomics/lecture-01-script.md`
- Audio manifest: `06-audio/week-02-functional-genomics/audio-manifest.md`
- Audio pilot clips:
  - `06-audio/week-02-functional-genomics/lecture-01/week02_lecture01_L1-01.mp3`
  - `06-audio/week-02-functional-genomics/lecture-01/week02_lecture01_L1-02.mp3`
  - `06-audio/week-02-functional-genomics/lecture-01/week02_lecture01_L1-03.mp3`
- Asset/prompt files: `07-assets/images/week-02-functional-genomics/`
- Status: `MATERIALS_STATUS/week-02-functional-genomics.md`

## Repeatable module workflow

For each future week:

1. Import Deep Research report into `01-deep-research/week-XX-topic/`.
2. Run citation cleanup:
   ```bash
   scripts/clean_deep_research_reports.sh --check
   scripts/clean_deep_research_reports.sh
   ```
3. Scaffold downstream files:
   ```bash
   scripts/scaffold_module_materials.py <week>
   ```
4. Validate sources before generating teaching content:
   - update `01-deep-research/.../source-validation.md`
   - update `02-source-validation/.../validated-sources.md`
   - update `02-source-validation/.../source-notes.md`
   - update `07-assets/references/.../source-bibliography.md`
5. Create or revise `03-lecture-plans/.../lecture-plan.md`.
6. Create `04-slides/.../slide-outline.md` with source IDs and placeholders.
7. Create `04-slides/.../slide-text.md` before any deck production.
8. Generate lecturer scripts in `05-scripts/.../`.
9. Generate audio only after scripts are accepted, preferably as slide-level clips first.
10. Use visual placeholders and saved image prompts, not generated/paper figures, unless explicitly requested.
11. Run readiness checks:
    ```bash
    scripts/check_module_ready.py <week>
    scripts/clean_deep_research_reports.sh --check
    ```
12. Commit and push after each stable stage.

## Audio settings that worked

```text
Model: gpt-4o-mini-tts-2025-12-15
Voice: cedar
Format: mp3
Pacing: moderate and steady
Tone: professional, warm, lecturer-like
Strategy: generate separate clips per slide for review/regeneration
```

Instruction block used:

```text
Voice Affect: Calm, clear, lecturer-like, and confident.
Tone: Professional but warm; explain concepts patiently.
Pacing: Moderate and steady, with brief pauses between key ideas.
Pronunciation: ChIP-seq is "chip seek"; ATAC-seq is "attack seek"; Hi-C is "high C"; HiChIP is "high chip"; IDR is "I D R".
Delivery: Natural classroom narration, not an advertisement or audiobook performance.
```

## Decisions to carry forward

- Public repo should remain free of private Google Doc links, Telegram attachment IDs, personal contact data, and extracted copyrighted figures.
- Use source IDs everywhere after validation.
- Prefer text-first production.
- Visuals are placeholders for the lecturer unless explicitly requested.
- Store `gpt-image-2` prompts when useful, but do not generate/commit images by default.
- Audio generation is worth keeping as a later stage because the pilot quality was good.

## Recommended next step

Finish Week 02 text materials:

1. Draft Lecture 2 script.
2. Draft Lecture 3 script.
3. If those scripts are accepted, generate full Lecture 1 audio or continue slide-by-slide audio pilots.

Then apply the same workflow to Week 03.
