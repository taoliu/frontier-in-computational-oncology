# Week 02 — Functional Genomics in Cancer — Audio Manifest

## Voice / generation settings

Preferred pilot settings:

- Provider: OpenAI Audio API via local `speech` skill
- Preferred model: `gpt-4o-mini-tts-2025-12-15` or `gpt-4o-mini-tts`
- Fallback attempted: `tts-1`
- Preferred voice: `cedar`
- Fallback voice attempted: `onyx`
- Output format: `mp3`
- Status: pilot clips generated for Lecture 1 slides 1–3

## Attempt log

| Date | Segment(s) | Model | Voice | Result | Notes |
|---|---|---|---|---|---|
| 2026-05-31 | Lecture 1 slides 1–3 | `gpt-4o-mini-tts-2025-12-15` | `cedar` | generated | Generated three MP3 pilot clips after model access was enabled. |
| 2026-05-31 | Lecture 1 slides 1–3 | `gpt-4o-mini-tts` | `cedar` | blocked | OpenAI API returned 403: project lacks access to model. |
| 2026-05-31 | Lecture 1 slides 1–3 | `tts-1` | `onyx` | blocked | OpenAI API returned 403: project lacks access to model. |

## Segments

| Segment ID | Lecture | Script file | Output file | Duration | Status | Regeneration notes |
|---|---|---|---|---|---|---|
| L01-S001 | Lecture 1 slide 1 | `05-scripts/week-02-functional-genomics/lecture-01-script.md` | `06-audio/week-02-functional-genomics/lecture-01/week02_lecture01_L1-01.mp3` | TBD | accepted pilot | Dr. Liu judged pilot audio quality nice; generated with `gpt-4o-mini-tts-2025-12-15`, voice `cedar`. |
| L01-S002 | Lecture 1 slide 2 | `05-scripts/week-02-functional-genomics/lecture-01-script.md` | `06-audio/week-02-functional-genomics/lecture-01/week02_lecture01_L1-02.mp3` | TBD | accepted pilot | Dr. Liu judged pilot audio quality nice; generated with `gpt-4o-mini-tts-2025-12-15`, voice `cedar`. |
| L01-S003 | Lecture 1 slide 3 | `05-scripts/week-02-functional-genomics/lecture-01-script.md` | `06-audio/week-02-functional-genomics/lecture-01/week02_lecture01_L1-03.mp3` | TBD | regenerated | Original pilot clip was truncated before the third question; regenerated full slide audio with `gpt-4o-mini-tts-2025-12-15`, voice `cedar`, on 2026-05-31. |

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
