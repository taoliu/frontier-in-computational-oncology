# HTML Slide+Audio Delivery Plan

## Decision

Final course delivery should target a browser-based HTML slide player rather than static slide files alone. Each slide should reveal content step-by-step and play matching slide-level audio.

## Why HTML

- Supports progressive reveal of slide bullets/blocks one by one.
- Supports per-slide or per-step audio with native browser controls.
- Keeps materials portable: can be opened locally, served from GitHub Pages, or embedded in an LMS.
- Avoids locking the course into PowerPoint/Google Slides while preserving the option to export later.
- Fits the tested pipeline: text-only slide content + lecturer scripts + MP3 audio.

## Proposed delivery artifact

For each lecture:

```text
08-exports/week-XX-topic/html/lecture-01/index.html
08-exports/week-XX-topic/html/lecture-01/assets/
```

Each HTML lecture should include:

- slide navigation: previous / next / keyboard arrows
- step navigation within each slide: reveal next bullet/block
- matching audio: one MP3 per slide by default
- optional captions/transcript panel generated from speaker notes
- source/provenance panel with source IDs
- placeholder visuals or generated/approved assets only

## Data flow

```text
validated sources
  → lecture plan
  → slide-text.md
  → lecture script
  → MP3 audio by slide
  → HTML slide manifest
  → HTML lecture player
```

## Recommended content format

Add a machine-readable slide manifest for each lecture:

```text
04-slides/week-XX-topic/html-manifest/lecture-01.json
```

Suggested schema:

```json
{
  "module": "Week XX — Module Title",
  "lecture": "Lecture 1 — Title",
  "slides": [
    {
      "id": "L1-01",
      "title": "Slide title",
      "steps": [
        { "type": "bullet", "text": "First reveal" },
        { "type": "bullet", "text": "Second reveal" }
      ],
      "visual": {
        "type": "placeholder",
        "description": "What visual should show"
      },
      "audio": "../../../06-audio/week-XX-topic/lecture-01/weekXX_lecture01_L1-01.mp3",
      "transcriptSource": "../../../05-scripts/week-XX-topic/lecture-01-script.md",
      "sources": ["S001", "S004"]
    }
  ]
}
```

## Audio convention

- Default: one MP3 per slide.
- Optional future refinement: per-step audio timing if needed.
- Keep source audio outputs ignored by git unless Dr. Liu explicitly approves committing media.
- Store regeneration instructions in `06-audio/week-XX-topic/audio-manifest.md`.

## Implementation recommendation

Use a small static HTML/JS player checked into the repo, not a heavy framework.

Suggested paths:

```text
scripts/build_html_lecture.py
08-exports/shared/html-player/player.js
08-exports/shared/html-player/style.css
```

The builder should read the lecture JSON manifest and produce an `index.html` that can run offline in a browser.

## Updated production pipeline

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

## Pilot recommendation

Use Week 02 Lecture 1 as the HTML pilot because it already has:

- validated source pipeline
- slide text content
- lecturer script
- accepted MP3 audio clips for slides 1–3

Pilot target:

```text
08-exports/week-02-functional-genomics/html/lecture-01/index.html
```

Start with slides 1–3, using the accepted audio clips, then extend to the full lecture after review.


## Current audio availability

As of 2026-05-31, the only accepted generated audio clips are the Week 02 Lecture 1 pilot clips for slides 1–3:

- `06-audio/week-02-functional-genomics/lecture-01/week02_lecture01_L1-01.mp3`
- `06-audio/week-02-functional-genomics/lecture-01/week02_lecture01_L1-02.mp3`
- `06-audio/week-02-functional-genomics/lecture-01/week02_lecture01_L1-03.mp3`

No other lecture audio has been generated yet. The first HTML delivery pilot should therefore use these three clips and treat all later slide audio as pending.


## Lecture timing target

Dr. Liu's revised delivery target for narrated HTML lectures:

- Aim for ~30 minutes per lecture.
- Use roughly 20 slides per lecture.
- Target average narration length: ~1.5 minutes per slide.
- Continuous autoplay should include a short technical pause of about 1 second between slides.
- This 1-second pause is distinct from planned instructional pauses, discussion prompts, or activities.

Implication for Week 02 Lecture 1: the current 12-slide, ~10:40 export is a successful technical/content pilot, but it is too short for the intended final lecture. Next content pass should expand the lecture to about 20 slides and lengthen speaker notes per slide.
