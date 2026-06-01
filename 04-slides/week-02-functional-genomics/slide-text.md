# Week 02 — Functional Genomics in Cancer — Text-Only Slide Content

## Use notes

- Text-only draft for slide production; no final figures are embedded here.
- Visuals are lecturer placeholders or optional prompt-based draft images.
- Keep slide text concise; detailed explanation belongs in lecturer scripts.
- Source IDs refer to `02-source-validation/week-02-functional-genomics/validated-sources.md`.
- Figure placeholders should not be replaced with publication figures until a human reviewer approves license/fair-use context.
- Production delivery target for Lecture 1: about 20 slides, about 90 seconds of narration per slide, about 30 minutes total.

---

## Lecture 1 — Background & Problem Definition

### L1-01 — Functional Genomics in Cancer

**Slide text**

- Bulk regulatory assays are measurement systems, not direct biological labels
- Reads, fragments, domains, and contacts become claims only through models
- Lecture 1 goal: build the assay-aware reasoning framework

**Visual placeholder**

- Title slide with genome track, chromatin accessibility, enhancer, and contact-map icons.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- Module synthesis

### L1-02 — Why mutations are not enough

**Slide text**

- Cancer mechanisms are often regulatory, not coding-only
- Lineage state, enhancer activity, TF binding, and 3D context shape tumor behavior
- Functional genomics asks when and where the genome is active

**Visual placeholder**

- Mechanism map: mutation list plus regulatory state leading to phenotype.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S011, S012, S016-S019

### L1-03 — Three questions before software

**Slide text**

- What is the observed statistical object?
- What is signal versus background?
- What evidence makes the call reproducible and interpretable?

**Visual placeholder**

- Triangle linking assay object, background model, and evidence standard.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S001, S007, S013-S015

### L1-04 — Assay chemistry defines the data object

**Slide text**

- ChIP-seq enriches target-associated fragments
- ATAC-seq samples accessible fragments and fragment lengths
- CUT assays create tethered low-background signal
- Contact assays count pairs of nearby loci

**Visual placeholder**

- Four-panel assay comparison: ChIP-seq, ATAC-seq, CUT&Tag/CUT&RUN, and Hi-C/HiChIP.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S001, S004, S006, S010

### L1-05 — Genome tracks can mislead

**Slide text**

- A browser track is a visualization, not an inference result
- Similar-looking tracks can come from different assays and biases
- Interpretation requires knowing the assay and expected background

**Visual placeholder**

- Two similar genome-browser tracks annotated as different underlying assay objects.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S001, S004, S006, S014

### L1-06 — Enrichment assays ask: enriched over what?

**Slide text**

- ChIP-seq and CUT assays produce target-centered enrichment signal
- Peak calling compares observed signal to an expected background
- The biological claim depends on the background model

**Visual placeholder**

- Signal track over local/input background with called enriched region.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S001, S006, S007

### L1-07 — Peak shape is biological and statistical

**Slide text**

- TF binding often creates narrow focal enrichment
- Histone marks can form broad domains
- The wrong peak-shape model changes the biological story

**Visual placeholder**

- Comparison of narrow TF peak, broad histone domain, and mixed signal track.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S001, S003, S006

### L1-08 — ATAC-seq is accessibility plus fragment structure

**Slide text**

- Tn5 inserts into accessible chromatin
- Fragment lengths separate nucleosome-free and nucleosomal DNA
- Accessibility alone is not proof of regulatory function

**Visual placeholder**

- ATAC fragment-size ladder: short NFR, mononucleosome, dinucleosome fragments.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S004, S005

### L1-09 — Motifs and footprints are not the same as binding

**Slide text**

- Motif occurrence means sequence potential
- Footprints use cut-site patterns around motifs
- Tn5 bias and chromatin context complicate occupancy claims

**Visual placeholder**

- Motif site with ATAC cut-site pattern and bias correction layer.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S005

### L1-10 — Contact assays measure proximity, not causality

**Slide text**

- Hi-C and HiChIP-like assays observe pairs of loci
- Contact frequency is strongly distance-dependent
- A significant contact is spatial evidence, not proof of regulation

**Visual placeholder**

- Contact matrix beside distance-decay curve and enhancer-promoter cartoon.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S010, S012

### L1-11 — Cancer genomes make background harder

**Slide text**

- Copy number and rearrangements alter local signal expectations
- Mappability and blacklist regions can mimic enrichment
- Tumor purity and cell mixture change apparent regulatory state

**Visual placeholder**

- Cancer genome background cartoon: amplified locus, rearrangement, artifact region, mixed cells.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S001, S014, S011

### L1-12 — Controls help, but they are models

**Slide text**

- Input/control tracks estimate non-target signal
- Controls reduce artifacts but introduce assumptions
- Different assay families require different control logic

**Visual placeholder**

- Target signal track aligned with input/control and residual enrichment.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S001, S006, S007

### L1-13 — QC is evidence, not paperwork

**Slide text**

- Library complexity, FRiP, TSS enrichment, and cross-correlation measure data quality
- Blacklist filtering removes recurrent artifacts
- QC determines whether downstream claims are credible

**Visual placeholder**

- QC gate diagram from raw reads to interpretable regulatory calls.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S002, S007, S014

### L1-14 — Replicates test stability of ranked evidence

**Slide text**

- Replicates ask whether calls are stable, not just present
- IDR-style thinking focuses on rank consistency
- A single-sample peak is a candidate, not a durable claim

**Visual placeholder**

- Two replicate ranked peak lists converging into reproducible calls.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S013, S007

### L1-15 — Significance is not always calibrated

**Slide text**

- Peak-caller scores depend on model assumptions
- Nominal P values can be miscalibrated
- Calibration affects how confidently we rank and compare calls

**Visual placeholder**

- Nominal versus calibrated significance curve for peak calls.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S015, S001

### L1-16 — Annotation combines imperfect evidence layers

**Slide text**

- Accessibility, histone marks, motifs, contacts, and expression each answer different questions
- Candidate enhancer is not the same as validated enhancer
- Strong regulatory claims require consistent evidence

**Visual placeholder**

- Evidence stack: accessibility, mark, motif, contact, expression, perturbation.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S008, S009, S010

### L1-17 — Bulk assays still matter in the single-cell era

**Slide text**

- Bulk assays support mature QC, deep coverage, and large cohorts
- They build public regulatory resources and priors
- Single-cell and spatial assays often reuse concepts learned from bulk

**Visual placeholder**

- Bridge diagram from bulk cohorts to single-cell, spatial, and network modules.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S007, S008, S009, S011

### L1-18 — Cancer case studies use the same logic

**Slide text**

- Pan-cancer ATAC-seq links accessibility to subtype programs
- AR cistrome rewiring shows TF binding can change with tumorigenesis
- Enhancer hijacking connects structural variation to regulatory activation

**Visual placeholder**

- Three mini-case panels: pan-cancer ATAC, AR cistrome, enhancer hijacking.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S011, S016, S018, S019

### L1-19 — What not to overclaim

**Slide text**

- Peak ≠ enhancer
- Motif ≠ binding
- Contact ≠ regulation
- Correlation ≠ causal target gene

**Visual placeholder**

- Four caution cards translating common shorthand into careful language.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S005, S008, S010, S015

### L1-20 — Lecture 1 synthesis

**Slide text**

- Define the assay object before choosing a method
- Model signal against structured, assay-specific background
- Require QC, reproducibility, calibration, and evidence integration
- Carry this framework into method development and cancer applications

**Visual placeholder**

- Final framework diagram: assay → model → reproducibility → evidence → claim.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S001-S015

---

## Lecture 2 — Method Development & Verification

