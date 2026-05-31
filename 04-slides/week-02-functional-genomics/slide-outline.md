# Week 02 — Functional Genomics in Cancer — Slide Outline

> Pilot scaffold. Slide count and source IDs will be refined after validation.

## Deck metadata

- Module: Week 02 — Functional Genomics in Cancer
- Lecture set: three 50–75 minute lectures
- Source lecture plan: `03-lecture-plans/week-02-functional-genomics/lecture-plan.md`
- Validation status: pending

## Lecture 1 — Background & Problem Definition

| Slide | Title | Core takeaway | Visual / asset | Source IDs | Status |
|---|---|---|---|---|---|
| L1-01 | Functional genomics as signal detection | Assays produce biased molecular readouts, not direct biological truth. | Module overview graphic | S001-S007 | draft |
| L1-02 | Why cancer needs regulatory genomics | Regulatory mechanisms explain lineage state, subtype, enhancer dependence, and oncogene activation. | Cancer regulatory mechanism map | S011-S012 | draft |
| L1-03 | Assay families | ChIP-seq, ATAC-seq, CUT&RUN/CUT&Tag, and contact assays measure different objects. | Assay comparison schematic | S001-S006, S010 | draft |
| L1-04 | What is the observed object? | Read pileups, fragment classes, domains, and contact matrices require different models. | Data object grid | S001, S004, S010 | draft |
| L1-05 | Background is structured | Local genomic background and assay bias control false discovery. | Signal/background cartoon | S001, S007 | draft |
| L1-06 | Reproducibility is part of the model | QC and replicate handling are not optional post-processing. | QC pipeline schematic | S002, S007 | draft |
| L1-07 | Lecture 1 synthesis | Before selecting software, define signal, background, and verification. | Three-question framework |  | draft |

## Lecture 2 — Method Development & Verification

| Slide | Title | Core takeaway | Visual / asset | Source IDs | Status |
|---|---|---|---|---|---|
| L2-01 | Peak shape is a modeling choice | Narrow peaks, broad domains, ATAC states, and CUT signal require different callers. | Model comparison grid | S001, S003, S004, S006 | draft |
| L2-02 | MACS-style local enrichment | Dynamic local background solves a central ChIP-seq problem. | MACS cartoon | S001 | draft |
| L2-03 | Cross-correlation and QC | Strand geometry exposes real binding signal and experiment quality. | Cross-correlation plot sketch | S002 | draft |
| L2-04 | Broad domains | Histone domains need spatial clustering/domain models. | Narrow vs broad signal | S003 | draft |
| L2-05 | ATAC fragment structure | Fragment classes encode nucleosome-free and nucleosome-associated states. | HMMRATAC state diagram | S004 | draft |
| L2-06 | Tn5 bias and footprints | Footprints are fragile unless enzyme bias is modeled. | Motif/footprint contrast | S005 | draft |
| L2-07 | Sparse CUT data | Low-background assays change thresholding and peak-calling behavior. | CUT signal cartoon | S006 | draft |
| L2-08 | Contact calls | Distance-aware nulls are essential for loop/contact inference. | Contact matrix null model | S010 | draft |
| L2-09 | Verification toolkit | IDR, benchmarks, orthogonal evidence, and perturbation evidence serve different roles. | Evidence ladder | S007 | draft |

## Lecture 3 — Application & State of the Field

| Slide | Title | Core takeaway | Visual / asset | Source IDs | Status |
|---|---|---|---|---|---|
| L3-01 | From calls to resources | ENCODE/SCREEN and Cistrome convert experiments into reusable regulatory priors. | Resource map | S008, S009 | draft |
| L3-02 | Pan-cancer accessibility | TCGA ATAC illustrates regulatory discovery in primary tumors. | TCGA ATAC schematic | S011 | draft |
| L3-03 | TF cistrome rewiring | Cancer can rewire TF binding without changing the TF itself. | AR cistrome concept figure | TBD | draft |
| L3-04 | Super-enhancer states | Enhancer landscapes can define tumor regulatory identities. | Super-enhancer state map | TBD | draft |
| L3-05 | Enhancer hijacking | SVs can activate oncogenes by rewiring regulatory context. | Enhancer hijacking cartoon | TBD | draft |
| L3-06 | 3D genome connectomes | Contact maps can link regulatory elements but do not prove causality alone. | Enhancer-connectome schematic | S012 | draft |
| L3-07 | Boundaries and handoff | Bulk methods establish principles for later single-cell, spatial, and network weeks. | Module handoff diagram |  | draft |

## Figure / asset requests

| Asset ID | Slide | Asset type | Description | Provenance / source | Status |
|---|---|---|---|---|---|
| W02-A001 | L1-03 | Original schematic | Compare assay chemistries and outputs. | Created in-house | needed |
| W02-A002 | L2-02 | Original schematic | MACS local background / peak-calling concept. | Recreated from validated method description | needed |
| W02-A003 | L2-05 | Original schematic | HMMRATAC fragment classes and states. | Recreated from validated method description | needed |
| W02-A004 | L2-08 | Original schematic | Genomic distance decay and contact significance. | Created in-house | needed |
| W02-A005 | L3-05 | Original schematic | Enhancer hijacking mechanism. | Created in-house with citations | needed |

## Open questions before slide production

- Final slide count per lecture.
- Whether to produce one combined deck or one deck per lecture.
- Which case studies get full slides after validation.
