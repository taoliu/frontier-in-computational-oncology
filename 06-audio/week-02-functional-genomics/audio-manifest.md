# Week 02 — Functional Genomics in Cancer — Audio Manifest

## Voice / generation settings

Preferred pilot settings:

- Provider: OpenAI Audio API via local `speech` skill
- Preferred model: `gpt-4o-mini-tts-2025-12-15` or `gpt-4o-mini-tts`
- Fallback attempted: `tts-1`
- Preferred voice: `cedar`
- Fallback voice attempted: `onyx`
- Output format: `mp3`
- Status: Lecture 1 slides 1–12 generated; slides 1–3 reviewed in pilot

## Attempt log

| Date | Segment(s) | Model | Voice | Result | Notes |
|---|---|---|---|---|---|
| 2026-05-31 | Lecture 1 slides 1–3 | `gpt-4o-mini-tts-2025-12-15` | `cedar` | generated | Generated three MP3 pilot clips after model access was enabled. |
| 2026-05-31 | Lecture 1 slides 4–12 | `gpt-4o-mini-tts-2025-12-15` | `cedar` | generated | Generated remaining Lecture 1 slide-level MP3 clips and added them to HTML export. |
| 2026-05-31 | Lecture 1 slides 1–3 | `gpt-4o-mini-tts` | `cedar` | blocked | OpenAI API returned 403: project lacks access to model. |
| 2026-05-31 | Lecture 1 slides 1–3 | `tts-1` | `onyx` | blocked | OpenAI API returned 403: project lacks access to model. |

## Segments

| Segment ID | Lecture | Script file | Output file | Duration | Status | Regeneration notes |
|---|---|---|---|---|---|---|
| L01-S001 | Lecture 1 slide 1 | `05-scripts/week-02-functional-genomics/lecture-01-script.md` | `06-audio/week-02-functional-genomics/lecture-01/week02_lecture01_L1-01.mp3` | TBD | accepted pilot | Dr. Liu judged pilot audio quality nice; generated with `gpt-4o-mini-tts-2025-12-15`, voice `cedar`. |
| L01-S002 | Lecture 1 slide 2 | `05-scripts/week-02-functional-genomics/lecture-01-script.md` | `06-audio/week-02-functional-genomics/lecture-01/week02_lecture01_L1-02.mp3` | TBD | accepted pilot | Dr. Liu judged pilot audio quality nice; generated with `gpt-4o-mini-tts-2025-12-15`, voice `cedar`. |
| L01-S003 | Lecture 1 slide 3 | `05-scripts/week-02-functional-genomics/lecture-01-script.md` | `06-audio/week-02-functional-genomics/lecture-01/week02_lecture01_L1-03.mp3` | TBD | regenerated | Original pilot clip was truncated before the third question; regenerated full slide audio with `gpt-4o-mini-tts-2025-12-15`, voice `cedar`, on 2026-05-31. |
| L01-S004 | Lecture 1 slide 4 | `05-scripts/week-02-functional-genomics/lecture-01-script.md` | `06-audio/week-02-functional-genomics/lecture-01/week02_lecture01_L1-04.mp3` | TBD | generated | Generated with `gpt-4o-mini-tts-2025-12-15`, voice `cedar`, for full Lecture 1 HTML delivery. |
| L01-S005 | Lecture 1 slide 5 | `05-scripts/week-02-functional-genomics/lecture-01-script.md` | `06-audio/week-02-functional-genomics/lecture-01/week02_lecture01_L1-05.mp3` | TBD | generated | Generated with `gpt-4o-mini-tts-2025-12-15`, voice `cedar`, for full Lecture 1 HTML delivery. |
| L01-S006 | Lecture 1 slide 6 | `05-scripts/week-02-functional-genomics/lecture-01-script.md` | `06-audio/week-02-functional-genomics/lecture-01/week02_lecture01_L1-06.mp3` | TBD | generated | Generated with `gpt-4o-mini-tts-2025-12-15`, voice `cedar`, for full Lecture 1 HTML delivery. |
| L01-S007 | Lecture 1 slide 7 | `05-scripts/week-02-functional-genomics/lecture-01-script.md` | `06-audio/week-02-functional-genomics/lecture-01/week02_lecture01_L1-07.mp3` | TBD | generated | Generated with `gpt-4o-mini-tts-2025-12-15`, voice `cedar`, for full Lecture 1 HTML delivery. |
| L01-S008 | Lecture 1 slide 8 | `05-scripts/week-02-functional-genomics/lecture-01-script.md` | `06-audio/week-02-functional-genomics/lecture-01/week02_lecture01_L1-08.mp3` | TBD | generated | Generated with `gpt-4o-mini-tts-2025-12-15`, voice `cedar`, for full Lecture 1 HTML delivery. |
| L01-S009 | Lecture 1 slide 9 | `05-scripts/week-02-functional-genomics/lecture-01-script.md` | `06-audio/week-02-functional-genomics/lecture-01/week02_lecture01_L1-09.mp3` | TBD | generated | Generated with `gpt-4o-mini-tts-2025-12-15`, voice `cedar`, for full Lecture 1 HTML delivery. |
| L01-S010 | Lecture 1 slide 10 | `05-scripts/week-02-functional-genomics/lecture-01-script.md` | `06-audio/week-02-functional-genomics/lecture-01/week02_lecture01_L1-10.mp3` | TBD | generated | Generated with `gpt-4o-mini-tts-2025-12-15`, voice `cedar`, for full Lecture 1 HTML delivery. |
| L01-S011 | Lecture 1 slide 11 | `05-scripts/week-02-functional-genomics/lecture-01-script.md` | `06-audio/week-02-functional-genomics/lecture-01/week02_lecture01_L1-11.mp3` | TBD | generated | Generated with `gpt-4o-mini-tts-2025-12-15`, voice `cedar`, for full Lecture 1 HTML delivery. |
| L01-S012 | Lecture 1 slide 12 | `05-scripts/week-02-functional-genomics/lecture-01-script.md` | `06-audio/week-02-functional-genomics/lecture-01/week02_lecture01_L1-12.mp3` | TBD | generated | Generated with `gpt-4o-mini-tts-2025-12-15`, voice `cedar`, for full Lecture 1 HTML delivery. |

## TTS instructions for retry

```text
Voice Affect: Calm, clear, lecturer-like, and confident.
Tone: Professional but warm; explain concepts patiently.
Pacing: Moderate and steady, with brief pauses between key ideas.
Pronunciation: ChIP-seq is "chip seek"; ATAC-seq is "attack seek"; Hi-C is "high C"; HiChIP is "high chip"; IDR is "I D R".
Delivery: Natural classroom narration, not an advertisement or audiobook performance.
```

## Pronunciation notes

- ChIP-seq: “chip seek”
- ATAC-seq: “attack seek”
- CUT&RUN: “cut and run”
- CUT&Tag: “cut and tag”
- Hi-C: “high C”
- HiChIP: “high chip”
- PLAC-seq: “plack seek”
- Tn5: “T N five”
- H3K27ac: “H three K twenty-seven A C”
- CTCF: “C T C F”
- cCRE: “candidate cis-regulatory element” or “C C R E” after first definition
- IDR: “I D R”
- FRiP: “frip,” fraction of reads in peaks

## Regeneration note

The local CLI is available at `~/.openclaw/skills/speech/scripts/text_to_speech.py`. Regenerate clips from the Lecture 1 script with the same instructions above if pacing or pronunciation needs revision.
## Lecture 1 production audio — 20-slide export

- Model: `gpt-4o-mini-tts-2025-12-15`
- Voice: `cedar`
- Speed: `0.75`
- Format: MP3
- Generated from: `04-slides/week-02-functional-genomics/html-manifest/lecture-01-pilot.json` transcripts
- HTML export: `08-exports/week-02-functional-genomics/html/lecture-01/`
- Total audio duration: 1778.3 seconds (29:38); about 1797.3 seconds including 19 one-second autoplay pauses

| Slide | File | Duration |
|---|---|---:|
| L1-01 | `lecture-01/week02_lecture01_L1-01.mp3` | 1:35 |
| L1-02 | `lecture-01/week02_lecture01_L1-02.mp3` | 1:41 |
| L1-03 | `lecture-01/week02_lecture01_L1-03.mp3` | 1:29 |
| L1-04 | `lecture-01/week02_lecture01_L1-04.mp3` | 1:26 |
| L1-05 | `lecture-01/week02_lecture01_L1-05.mp3` | 1:27 |
| L1-06 | `lecture-01/week02_lecture01_L1-06.mp3` | 1:18 |
| L1-07 | `lecture-01/week02_lecture01_L1-07.mp3` | 1:20 |
| L1-08 | `lecture-01/week02_lecture01_L1-08.mp3` | 1:33 |
| L1-09 | `lecture-01/week02_lecture01_L1-09.mp3` | 1:24 |
| L1-10 | `lecture-01/week02_lecture01_L1-10.mp3` | 1:25 |
| L1-11 | `lecture-01/week02_lecture01_L1-11.mp3` | 1:21 |
| L1-12 | `lecture-01/week02_lecture01_L1-12.mp3` | 1:20 |
| L1-13 | `lecture-01/week02_lecture01_L1-13.mp3` | 1:23 |
| L1-14 | `lecture-01/week02_lecture01_L1-14.mp3` | 1:35 |
| L1-15 | `lecture-01/week02_lecture01_L1-15.mp3` | 1:29 |
| L1-16 | `lecture-01/week02_lecture01_L1-16.mp3` | 1:42 |
| L1-17 | `lecture-01/week02_lecture01_L1-17.mp3` | 1:17 |
| L1-18 | `lecture-01/week02_lecture01_L1-18.mp3` | 1:44 |
| L1-19 | `lecture-01/week02_lecture01_L1-19.mp3` | 1:32 |
| L1-20 | `lecture-01/week02_lecture01_L1-20.mp3` | 1:35 |

