# Week 02 — Functional Genomics in Cancer — Slide-Ready Outline

## Deck metadata

- Module: Week 02 — Functional Genomics in Cancer
- Lecture set: three lectures, 12 slides each
- Source lecture plan: `03-lecture-plans/week-02-functional-genomics/lecture-plan.md`
- Validation status: first-pass source validation complete; S008 partial/date wording nuance
- Production status: slide-ready outline; assets still need generation

## Lecture 1 — Background & Problem Definition

**Lecture thesis:** bulk functional genomics assays are measurement systems with assay-specific signal, background, and verification problems. Before choosing a tool, define the observed object.

| Slide | Title | Core takeaway | Visual / asset | Source IDs | Status |
|---|---|---|---|---|---|
| L1-01 | Title: Functional Genomics in Cancer | This week is about converting biased regulatory readouts into defensible biological claims. | Title card with assay icons |  | slide-ready |
| L1-02 | Why mutations are not enough | Cancer phenotypes often depend on regulatory state, lineage circuitry, enhancer activation, and 3D regulatory context. | Cancer regulatory mechanism map | S011, S012, S016-S019 | slide-ready |
| L1-03 | Three questions before software | Ask: what is observed, what is background, and how is reproducibility shown? | Three-question framework | S001, S007, S013-S015 | slide-ready |
| L1-04 | Assay families and outputs | ChIP-seq, ATAC-seq, CUT&RUN/CUT&Tag, and contact assays measure different statistical objects. | W02-A001 assay comparison schematic | S001, S004, S006, S010 | slide-ready |
| L1-05 | ChIP-seq and CUT assays | Enrichment assays depend on target specificity, fragmentation/cleavage chemistry, controls, and local genomic background. | Enrichment-track schematic | S001, S006, S007 | slide-ready |
| L1-06 | ATAC-seq as accessibility plus structure | ATAC-seq reads encode accessibility and fragment-size/nucleosome structure, not just “open chromatin.” | ATAC fragment-size cartoon | S004, S005 | slide-ready |
| L1-07 | Contact assays as sparse matrices | Hi-C/HiChIP-like assays require distance-aware interpretation because nearby loci contact more often by default. | Contact matrix with distance decay | S010, S012 | slide-ready |
| L1-08 | Background is structured | Mappability, GC bias, local chromatin context, and blacklist regions can look like biological signal. | W02-A006 bias/background schematic | S001, S014 | slide-ready |
| L1-09 | Controls are models, not magic | Input/control tracks and panels of filters reduce artifacts but encode assumptions about expected background. | Control-vs-signal schematic | S001, S006, S007 | slide-ready |
| L1-10 | Reproducibility is part of the claim | Replicate consistency, library complexity, FRiP/TSS enrichment, blacklist filtering, and IDR-like logic determine whether calls are trustworthy. | W02-A007 QC gate diagram | S002, S007, S013, S014 | slide-ready |
| L1-11 | Regulatory annotation is evidence aggregation | Peaks, motifs, histone marks, contacts, and expression are evidence layers; none alone proves causality. | Evidence stack graphic | S008-S010 | slide-ready |
| L1-12 | Lecture 1 synthesis | Assay-aware thinking is the foundation for method choice and cancer interpretation. | Summary triangle: assay → model → evidence | S001-S015 | slide-ready |

## Lecture 2 — Method Development & Verification

**Lecture thesis:** peak and loop callers are not interchangeable because they encode different assumptions about peak shape, background, replicate behavior, and calibration.

| Slide | Title | Core takeaway | Visual / asset | Source IDs | Status |
|---|---|---|---|---|---|
| L2-01 | Title: From reads to regulatory calls | The computational task is to convert read-level evidence into calibrated peaks, domains, footprints, or contacts. | Pipeline overview | S001-S010 | slide-ready |
| L2-02 | Peak shape is a modeling choice | Narrow TF peaks, broad histone domains, ATAC states, and sparse CUT signals require different model classes. | W02-A008 model comparison grid | S001, S003, S004, S006 | slide-ready |
| L2-03 | MACS: local enrichment and fragment shift | MACS is the clean teaching example for narrow-peak local background modeling. | W02-A002 MACS local background schematic | S001 | slide-ready |
| L2-04 | Cross-correlation and experiment quality | Strand-shift/cross-correlation links the geometry of binding events to QC. | W02-A009 cross-correlation sketch | S002 | slide-ready |
| L2-05 | Broad domains: SICER-style clustering | Diffuse histone marks need spatial clustering/domain models, not only narrow-peak callers. | Narrow-vs-broad signal | S003 | slide-ready |
| L2-06 | ATAC-specific modeling: HMMRATAC | Fragment classes can support a hidden-state model of open chromatin and nucleosome context. | W02-A003 HMMRATAC fragment/state diagram | S004 | slide-ready |
| L2-07 | Motifs are not footprints | Motif enrichment, TF binding, and TF activity are related but separable claims. | Motif-to-occupancy ladder | S005 | slide-ready |
| L2-08 | Footprinting needs bias correction | Tn5 sequence/protocol bias can mimic footprints if not modeled. | Bias-corrected footprint cartoon | S005 | slide-ready |
| L2-09 | CUT&RUN/CUT&Tag sparse enrichment | Low-background tethered-enzyme assays change peak-calling behavior and parameter expectations. | CUT signal vs ChIP signal comparison | S006 | slide-ready |
| L2-10 | Contact calls need distance-aware nulls | Contact significance must account for genomic-distance decay and assay-specific capture design. | W02-A004 distance-decay/contact null schematic | S010 | slide-ready |
| L2-11 | Verification toolkit | IDR, blacklist filtering, benchmarks, recalibration, orthogonal marks, expression, and perturbation each answer different validation questions. | W02-A010 evidence/verification ladder | S007, S013-S015 | slide-ready |
| L2-12 | Lecture 2 synthesis | Methods differ because assays differ; verification is not optional decoration. | Method-selection decision tree | S001-S015 | slide-ready |

## Lecture 3 — Applications & State of the Field

**Lecture thesis:** bulk regulatory genomics becomes powerful in cancer when validated calls are connected to public resources, subtype programs, enhancer states, enhancer hijacking, and 3D regulatory architecture — while keeping causal claims appropriately bounded.

| Slide | Title | Core takeaway | Visual / asset | Source IDs | Status |
|---|---|---|---|---|---|
| L3-01 | Title: From regulatory calls to cancer biology | Validated regulatory calls can explain tumor states and oncogene regulation that mutation lists miss. | Title card / cancer regulatory map | S011-S019 | slide-ready |
| L3-02 | Public regulatory resources | ENCODE/SCREEN and Cistrome turn many experiments into reusable regulatory priors. | W02-A011 resource map | S008, S009 | slide-ready |
| L3-03 | Pan-cancer ATAC as discovery engine | TCGA ATAC shows how accessibility maps reveal subtype programs, regulatory elements, and noncoding hypotheses in primary tumors. | W02-A012 TCGA ATAC schematic | S011 | slide-ready |
| L3-04 | Case study: AR cistrome rewiring | The same transcription factor can bind a different regulatory landscape during tumorigenesis. | AR cistrome rewiring concept | S016 | slide-ready |
| L3-05 | Case study: neuroblastoma enhancer states | Super-enhancer landscapes can define regulatory identities and plastic cell states. | Super-enhancer state schematic | S017 | slide-ready |
| L3-06 | Case study: enhancer hijacking | Structural variants can activate oncogenes by moving them into active enhancer neighborhoods. | W02-A005 enhancer hijacking mechanism | S018, S019 | slide-ready |
| L3-07 | From peaks to enhancer connectomes | H3K27ac HiChIP and related assays connect active enhancers to candidate target genes across primary tumors. | Enhancer-connectome schematic | S012 | slide-ready |
| L3-08 | What contacts can and cannot prove | Physical proximity is regulatory evidence, not causal proof by itself. | Contact-evidence ladder | S010, S012 | slide-ready |
| L3-09 | Clinically realistic future | Low-input, FFPE-compatible, and primary-tumor regulatory assays are improving, but routine clinical use still needs robust QC and interpretation. | Timeline / translation funnel | S007, S012 | slide-ready |
| L3-10 | Boundaries with later weeks | Bulk methods establish assay-aware principles that single-cell, spatial, and network modules will extend. | W02-A013 module handoff diagram |  | slide-ready |
| L3-11 | Discussion prompt | How much evidence is enough to call an element an enhancer, a target gene, or an oncogenic regulatory mechanism? | Evidence-threshold prompt | S008-S012, S018-S019 | slide-ready |
| L3-12 | Week synthesis | The durable lesson: model the assay, validate the call, then interpret regulatory evidence carefully. | Final summary triangle | S001-S019 | slide-ready |

## Figure / asset requests

| Asset ID | Slide | Asset type | Description | Provenance / source | Status |
|---|---|---|---|---|---|
| W02-A001 | L1-04 | Original schematic | Compare ChIP-seq, ATAC-seq, CUT&RUN/CUT&Tag, and chromatin-contact assay outputs. | Created in-house; cite S001/S004/S006/S010 | needed |
| W02-A002 | L2-03 | Original schematic | MACS local background / peak-calling concept. | Recreated from validated method description S001 | needed |
| W02-A003 | L2-06 | Original schematic | HMMRATAC fragment classes and HMM states. | Recreated from validated method description S004 | needed |
| W02-A004 | L2-10 | Original schematic | Genomic distance decay and contact significance. | Created in-house; cite S010 | needed |
| W02-A005 | L3-06 | Original schematic | Enhancer hijacking mechanism using medulloblastoma and leukemia examples. | Created in-house; cite S018/S019 | needed |
| W02-A006 | L1-08 | Original schematic | Structured background and blacklist-region artifact cartoon. | Created in-house; cite S001/S014 | needed |
| W02-A007 | L1-10 | Original schematic | QC gate diagram: library complexity, FRiP/TSS, blacklist, replicate/IDR. | Created in-house; cite S002/S007/S013/S014 | needed |
| W02-A008 | L2-02 | Table/diagram | Model comparison grid for MACS/SICER/HMMRATAC/SEACR/GoPeaks. | Created in-house; cite S001/S003/S004/S006 | needed |
| W02-A009 | L2-04 | Original schematic | Strand cross-correlation conceptual plot. | Recreated conceptually from S002 | needed |
| W02-A010 | L2-11 | Original schematic | Evidence/verification ladder from computational QC to perturbation. | Created in-house; cite S007/S013-S015 | needed |
| W02-A011 | L3-02 | Original schematic | Resource map linking ENCODE/SCREEN, Cistrome, TCGA ATAC, and 3D resources. | Created in-house; cite S008/S009/S011/S012 | needed |
| W02-A012 | L3-03 | Original schematic | TCGA ATAC workflow and discoveries in primary cancers. | Created in-house; cite S011 | needed |
| W02-A013 | L3-10 | Original schematic | Handoff diagram from bulk functional genomics to single-cell, spatial, and network modules. | Created in-house | needed |

## Open questions before slide production

- Should Week 02 be one combined 36-slide deck or three separate 12-slide decks?
- Should Lecture 3 keep all five case-study slides, or should some become backup/appendix slides after Dr. Liu reviews pacing?
- Should we generate simple original schematics first, then revise into polished slides, or draft full PowerPoint directly?
