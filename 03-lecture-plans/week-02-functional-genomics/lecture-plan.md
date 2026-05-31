# Week 02 — Functional Genomics in Cancer — Lecture Plan

> Pilot draft for testing the material-generation workflow. Source validation is still pending; use this as a planning scaffold, not final lecture text.

## Module story

Bulk functional genomics assays do not directly report “enhancers,” “TF binding,” or “loops.” They produce biased readouts — enrichment tracks, accessibility fragments, or contact matrices — whose interpretation depends on assay chemistry, background modeling, peak/domain shape, replicate behavior, and validation strategy. In cancer, those computational choices matter because regulatory mechanisms can explain lineage states, subtype programs, enhancer dependence, enhancer hijacking, and oncogene activation that coding mutations alone do not capture.

The week should teach students to ask three durable questions before choosing tools:

1. What is the observed statistical object?
2. What is signal versus background for this assay?
3. How do we know the call is reproducible and biologically interpretable?

## Lecture 1 — Background & Problem Definition

### Learning goals

- Distinguish the measurement objects produced by ChIP-seq, ATAC-seq, CUT&RUN/CUT&Tag, and chromatin-contact assays.
- Explain why regulatory genomics in cancer is a signal-detection and calibration problem, not just a visualization problem.
- Identify common assay biases: mappability, GC/content effects, local chromatin background, Tn5 bias, sparse tethered-enzyme signal, and genomic-distance decay in contact maps.
- Define the biological cancer questions this module can answer: regulatory states, enhancer activation, super-enhancer dependence, enhancer hijacking, and subtype-specific TF programs.

### Key concepts

- Assay chemistry determines the random variable.
- Enrichment, accessibility, and contact frequency are different data types.
- Background is structured, not flat.
- Regulatory annotation is evidence aggregation, not causal proof.
- Bulk assays remain valuable even in the single-cell/spatial era because they support mature QC, broad cohorts, and regulatory resource construction.

### Suggested flow

1. Start with the cancer problem: coding mutations are not enough to explain many lineage/state and oncogene-regulation questions.
2. Compare assay families:
   - ChIP-seq: target-enriched fragments for TFs or histone marks.
   - ATAC-seq: transposition-accessible fragments carrying nucleosome-scale structure.
   - CUT&RUN/CUT&Tag: low-background tethered cleavage/tagmentation signal.
   - Hi-C/PLAC-seq/HiChIP/capture methods: sparse contact counts with strong distance dependence.
3. Translate each assay into its computational object: counts over genomic intervals, paired fragments, domains, motifs, or contact matrices.
4. Introduce QC and reproducibility as first-class parts of method development.
5. Close with the bridge to Lecture 2: algorithms are different because the assumptions are different.

### Figures/assets needed

- Assay comparison schematic: ChIP-seq / ATAC-seq / CUT&Tag / Hi-C-like contacts.
- “Observed data object” diagram: read pileup, fragment classes, broad domain, contact matrix.
- Bias/background cartoon showing local genomic background versus true enrichment.

### Sources

- S001 MACS
- S002 SPP / cross-correlation
- S004 HMMRATAC
- S006 SEACR / GoPeaks
- S007 ENCODE pipelines

## Lecture 2 — Method Development & Verification

### Learning goals

- Compare narrow-peak, broad-domain, ATAC-specific, and CUT-specific calling models.
- Explain local background modeling, strand cross-correlation, spatial clustering, hidden Markov states, and sparse enrichment logic.
- Separate motif enrichment from footprinting and occupancy inference.
- Explain why replicate concordance, IDR-style thinking, calibration, and benchmark design are core method-development issues.

### Key concepts

- Peak shape is a model choice.
- Candidate selection and significance testing can create calibration problems.
- Motif occurrence, TF binding, and TF activity are related but not equivalent.
- Footprinting requires enzyme-bias correction.
- Loop/contact calls require distance-aware null models and careful interpretation.

### Suggested flow

1. Narrow peaks: MACS-style local background and empirical fragment shift.
2. QC: SPP-style strand cross-correlation; ENCODE-style library complexity, FRiP, TSS enrichment, blacklist filtering, and replicate handling.
3. Broad domains: SICER/SICER2 logic and why histone marks break narrow-peak assumptions.
4. ATAC-specific modeling: HMMRATAC fragment classes and hidden states.
5. CUT&RUN/CUT&Tag: SEACR and GoPeaks as examples of low-background/sparse-signal design.
6. Motifs and footprints: HOMER/MEME-style enrichment versus HINT-ATAC/TOBIAS-style bias-aware footprinting.
7. Contacts: FitHiC2/MAPS as selective examples of distance-aware interaction testing.
8. Verification: benchmarks, orthogonal marks, expression links, CRISPR follow-up when available.

### Figures/assets needed

- Peak-caller model comparison grid.
- MACS local background cartoon.
- HMMRATAC fragment-class/state diagram.
- Motif enrichment versus footprinting schematic.
- Hi-C/HiChIP distance-decay null model cartoon.

### Sources

- S001–S007
- S010 FitHiC2 / MAPS

## Lecture 3 — Application & State of the Field

### Learning goals

- Use public regulatory resources such as ENCODE/SCREEN and Cistrome as examples of scalable regulatory annotation.
- Explain how bulk cancer regulatory genomics has changed interpretation of tumor subtypes, lineage circuitry, and oncogene regulation.
- Evaluate case studies where regulatory data reveal biology missed by mutation-centric analysis.
- Define the limits of bulk functional genomics and the natural handoff to single-cell, spatial, and network modules.

### Key concepts

- Public regulatory atlases turn many experiments into reusable priors.
- Pan-cancer accessibility maps can reveal subtype structure, risk-locus activity, and noncoding regulatory programs.
- Cistrome rewiring and super-enhancer states are cancer mechanisms, not just annotations.
- Enhancer hijacking connects structural variation, chromatin state, and gene activation.
- 3D genome maps add linkage but not automatic causal proof.

### Suggested flow

1. ENCODE/SCREEN/cCREs: rule-based regulatory annotation at scale.
2. Cistrome DB/Cistrome Cancer: public-data reuse for cancer regulatory hypotheses.
3. TCGA pan-cancer ATAC-seq: accessibility elements, subtype programs, risk loci, and regulatory state discovery.
4. Prostate cancer AR cistrome rewiring as a TF-program example.
5. Neuroblastoma super-enhancer states as a regulatory identity example.
6. Enhancer hijacking in medulloblastoma/leukemia as a regulatory SV example.
7. Primary-cancer 3D genome maps as a bridge from peaks to enhancer connectomes.
8. Close with boundaries: Week 3 single-cell chromatin, Week 4 spatial localization, Week 6 network/causal modeling.

### Figures/assets needed

- Resource map: ENCODE/SCREEN, Cistrome, TCGA ATAC, 3D genome resources.
- Pan-cancer ATAC case-study schematic.
- Enhancer hijacking cartoon linking SV, enhancer, oncogene.
- Module boundary diagram showing handoff to Weeks 3, 4, and 6.

### Sources

- S008 ENCODE/cCREs
- S009 Cistrome DB/Cistrome Cancer
- S011 TCGA pan-cancer ATAC
- S012 primary-cancer 3D genome maps

## Assignment / discussion ideas

- Compare two peak callers on the same conceptual assay and identify which assumptions differ.
- Given a peak set and replicate summary, decide whether the result is slide-ready, validation-ready, or unreliable.
- Design a validation plan for a claimed cancer enhancer using accessibility, histone marks, expression, contacts, and perturbation evidence.
- Debate whether a regulatory annotation should be presented as “active enhancer,” “candidate enhancer,” or “regulatory evidence.”

## Open questions before slide generation

- Which Week 02 claims should be lecture-critical versus optional?
- Should chromatin interaction methods receive a full section or only a selective bridge to enhancer connectomes?
- Which cancer case studies should be emphasized: TCGA ATAC, prostate AR, neuroblastoma, enhancer hijacking, or primary-cancer 3D genome maps?
- How much tool detail should be included for student assignments versus conceptual lectures?
