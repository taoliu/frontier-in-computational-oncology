# Week 02 — Functional Genomics in Cancer — Text-Only Slide Content

## Use notes

- Text-only draft for slide production; no final figures are embedded here.
- Visuals are lecturer placeholders or optional prompt-based draft images.
- Keep slide text concise; detailed explanation belongs in lecturer scripts.
- Source IDs refer to `02-source-validation/week-02-functional-genomics/validated-sources.md`.
- Figure placeholders should not be replaced with publication figures until a human reviewer approves license/fair-use context.

---

## Lecture 1 — Background & Problem Definition

### L1-01 — Functional Genomics in Cancer

**Slide text**

- Week 02: bulk regulatory assays as computational measurement systems
- From biased molecular readouts to defensible regulatory claims
- Core question: what can we infer from peaks, fragments, domains, and contacts?

**Visual placeholder**

- Title slide with simple icons for sequencing reads, chromatin, enhancer, and contact map.

**Speaker intent**

- Set the tone: this is a method-development week, not a software tour.

**Sources**

- Module synthesis; no single source required.

### L1-02 — Why mutations are not enough

**Slide text**

- Many cancer mechanisms are regulatory, not coding-only
- Lineage state, enhancer activation, TF rewiring, and 3D regulatory context can shape tumor behavior
- Functional genomics helps explain *when* and *where* the genome is active

**Visual placeholder**

- Regulatory mechanism map: mutation list → regulatory state → phenotype.

**Speaker intent**

- Motivate why a computational oncology course needs bulk regulatory genomics before single-cell/spatial/network modules.

**Sources**

- S011, S012, S016-S019

### L1-03 — Three questions before software

**Slide text**

1. What is the observed statistical object?
2. What is signal versus background?
3. How do we know the call is reproducible and biologically interpretable?

**Visual placeholder**

- Three-question triangle: assay → model → evidence.

**Speaker intent**

- Give students a reusable framework for the entire week.

**Sources**

- S001, S007, S013-S015

### L1-04 — Assay families produce different objects

**Slide text**

- ChIP-seq: target-enriched fragments
- ATAC-seq: accessible fragments with nucleosome-scale structure
- CUT&RUN/CUT&Tag: tethered low-background signal
- Hi-C/HiChIP-like assays: sparse chromatin contact counts

**Visual placeholder**

- W02-A001 / prompt-based visual draft: assay comparison.

**Speaker intent**

- Make clear that assay chemistry defines the downstream statistical model.

**Sources**

- S001, S004, S006, S010

### L1-05 — ChIP-seq and CUT assays are enrichment experiments

**Slide text**

- ChIP-seq enriches DNA fragments associated with a target protein or mark
- CUT assays localize cleavage or tagmentation near the target
- Both produce genomic signal tracks that must be compared against expected background

**Visual placeholder**

- Enrichment track with target-bound loci and background reads.

**Speaker intent**

- Explain why enrichment tracks are not self-interpreting.

**Sources**

- S001, S006, S007

### L1-06 — ATAC-seq measures accessibility and structure

**Slide text**

- Tn5 inserts preferentially into accessible chromatin
- Paired-end fragment lengths encode nucleosome-free and nucleosome-associated DNA
- Accessibility is a measurement, not automatically a regulatory function

**Visual placeholder**

- Fragment-size ladder: short, mono-nucleosome, di-nucleosome fragments.

**Speaker intent**

- Prepare students for HMMRATAC and footprinting later.

**Sources**

- S004, S005

### L1-07 — Contact assays are sparse and distance-biased

**Slide text**

- Contact assays observe pairs of genomic loci, not direct regulatory causality
- Nearby loci contact more often by default
- Distance-aware null models are essential for loop interpretation

**Visual placeholder**

- Contact matrix plus genomic-distance decay curve.

**Speaker intent**

- Prevent students from reading every loop as an enhancer-gene mechanism.

**Sources**

- S010, S012

### L1-08 — Background is structured

**Slide text**

- Genomic background varies by mappability, GC content, chromatin state, and local copy/context
- Some regions repeatedly show anomalous signal across assays
- Filtering and background modeling are part of the biological claim

**Visual placeholder**

- Structured background cartoon with blacklist-like artifact region.

**Speaker intent**

- Explain why “flat background” is usually a bad assumption.

**Sources**

- S001, S014

### L1-09 — Controls are models, not magic

**Slide text**

- Input/control tracks estimate expected non-target signal
- Controls reduce artifacts but introduce their own assumptions
- Assay-specific controls differ across ChIP-seq, CUT assays, ATAC-seq, and contact assays

**Visual placeholder**

- Signal track over control/background track.

**Speaker intent**

- Teach control choice as a modeling decision.

**Sources**

- S001, S006, S007

### L1-10 — Reproducibility is part of the model

**Slide text**

- QC: library complexity, FRiP, TSS enrichment, cross-correlation, blacklist filtering
- Replicate consistency asks whether ranked calls are stable
- A peak without reproducibility evidence is only a candidate

**Visual placeholder**

- QC gate diagram.

**Speaker intent**

- Make quality control feel central rather than administrative.

**Sources**

- S002, S007, S013, S014

### L1-11 — Regulatory annotation is evidence aggregation

**Slide text**

- Peaks, motifs, histone marks, accessibility, expression, and contacts are evidence layers
- Candidate regulatory elements are not automatically causal enhancers
- Strong claims require multiple consistent evidence types

**Visual placeholder**

- Evidence stack: peak → mark → motif → contact → expression → perturbation.

**Speaker intent**

- Set up careful language for later case studies.

**Sources**

- S008-S010

### L1-12 — Lecture 1 synthesis

**Slide text**

- Define the assay object
- Model signal against structured background
- Require reproducibility before biological interpretation
- Carry these rules into every method and case study

**Visual placeholder**

- Summary triangle: assay → model → evidence.

**Speaker intent**

- Close Lecture 1 with the framework students will reuse in Lectures 2 and 3.

**Sources**

- S001-S015

---

## Lecture 2 — Method Development & Verification

### L2-01 — From reads to regulatory calls

**Slide text**

- Goal: convert read-level evidence into peaks, domains, footprints, or contacts
- Each output is a statistical claim
- The correct model depends on assay design and expected signal shape

**Visual placeholder**

- Pipeline: reads/fragments → model → calls → validation.

**Speaker intent**

- Introduce Lecture 2 as the algorithmic core of the week.

**Sources**

- S001-S010

### L2-02 — Peak shape is a modeling choice

**Slide text**

- Narrow TF peaks: local enrichment
- Broad histone domains: spatial clustering
- ATAC peaks: fragment-structure-aware states
- CUT signals: sparse low-background enrichment

**Visual placeholder**

- Model comparison grid: MACS, SICER, HMMRATAC, SEACR/GoPeaks.

**Speaker intent**

- Explain why one peak caller cannot be the universal answer.

**Sources**

- S001, S003, S004, S006

### L2-03 — MACS: local enrichment over background

**Slide text**

- MACS models ChIP-seq enrichment using local background estimates
- Empirical fragment shift helps align read evidence to binding events
- Teaching lesson: a peak is enrichment over an expected background

**Visual placeholder**

- W02-A002 / prompt-based visual draft: MACS local background.

**Speaker intent**

- Use MACS as the clean baseline for narrow-peak calling.

**Sources**

- S001

### L2-04 — Cross-correlation connects geometry and QC

**Slide text**

- True binding events create characteristic strand-shift patterns
- Cross-correlation summarizes that geometry
- QC metrics can reflect whether the assay captured real binding structure

**Visual placeholder**

- Positive/negative strand cross-correlation sketch.

**Speaker intent**

- Show that QC can emerge from assay physics.

**Sources**

- S002

### L2-05 — Broad domains need different models

**Slide text**

- Some histone marks form diffuse domains rather than sharp summits
- Spatial clustering methods detect enriched regions across neighboring windows
- Peak shape should follow expected biology and assay signal

**Visual placeholder**

- Narrow TF peak versus broad histone domain.

**Speaker intent**

- Contrast broad-domain logic with MACS-style narrow peaks.

**Sources**

- S003

### L2-06 — HMMRATAC: fragment lengths become states

**Slide text**

- ATAC fragment classes separate nucleosome-free and nucleosome-associated signal
- HMMRATAC uses hidden states to model accessible chromatin structure
- ATAC-specific information can improve assay-aware peak calling

**Visual placeholder**

- W02-A003 / prompt-based visual draft: ATAC fragments → HMM states.

**Speaker intent**

- Use HMMRATAC to demonstrate assay-specific model design.

**Sources**

- S004

### L2-07 — Motifs are not footprints

**Slide text**

- Motif occurrence: sequence could bind a TF
- Motif enrichment: sites are overrepresented in a region set
- Footprint/occupancy: local cut pattern suggests binding
- TF activity: requires broader functional evidence

**Visual placeholder**

- Ladder from motif to activity.

**Speaker intent**

- Stop students from collapsing motif, binding, and activity into one claim.

**Sources**

- S005

### L2-08 — Footprinting needs bias correction

**Slide text**

- Enzyme sequence bias can mimic or obscure footprints
- Tn5 insertion patterns must be corrected before occupancy interpretation
- Differential footprinting is a model-sensitive inference

**Visual placeholder**

- Biased versus bias-corrected cut-site profile.

**Speaker intent**

- Explain why footprint plots are attractive but fragile.

**Sources**

- S005

### L2-09 — CUT&RUN/CUT&Tag change the operating regime

**Slide text**

- Tethered assays often have lower background than ChIP-seq
- Sparse signal changes thresholding and caller behavior
- Assay-specific tools can outperform generic assumptions

**Visual placeholder**

- ChIP-like broad background versus CUT-like localized signal.

**Speaker intent**

- Teach students to revisit assumptions when protocols change.

**Sources**

- S006

### L2-10 — Contact calls need distance-aware null models

**Slide text**

- Contact frequency decays with genomic distance
- Significant contacts are deviations from expected contact behavior
- Capture design and mark anchoring alter the null model

**Visual placeholder**

- Contact matrix with distance-decay baseline.

**Speaker intent**

- Give students a compact statistical intuition for chromatin interaction calling.

**Sources**

- S010

### L2-11 — Verification toolkit

**Slide text**

- Blacklist filtering reduces recurrent artifacts
- IDR asks whether ranked calls reproduce across replicates
- Recalibration checks whether reported significance is trustworthy
- Orthogonal marks, expression, and perturbation test biological interpretation

**Visual placeholder**

- Verification ladder from computational QC to perturbation.

**Speaker intent**

- Separate computational reproducibility from biological validation.

**Sources**

- S007, S013-S015

### L2-12 — Lecture 2 synthesis

**Slide text**

- Peak/domain/contact calling is model choice
- Model choice follows assay physics and expected signal shape
- Verification determines how strong the claim can be

**Visual placeholder**

- Decision tree: assay → signal shape → caller → validation evidence.

**Speaker intent**

- Prepare students to interpret application papers in Lecture 3.

**Sources**

- S001-S015

---

## Lecture 3 — Applications & State of the Field

### L3-01 — From regulatory calls to cancer biology

**Slide text**

- Validated regulatory calls can reveal tumor states and oncogene regulation
- The biological endpoint is not a peak list
- The endpoint is a defensible model of regulatory mechanism

**Visual placeholder**

- Title slide: peaks → regulatory programs → cancer mechanism.

**Speaker intent**

- Shift from methods to interpretation without losing methodological caution.

**Sources**

- S011-S019

### L3-02 — Public resources convert experiments into priors

**Slide text**

- ENCODE/SCREEN: candidate regulatory elements and annotation layers
- Cistrome: reusable ChIP-seq, ATAC-seq, and DNase-seq profiles
- Public resources help generate hypotheses but still require context-specific validation

**Visual placeholder**

- Resource map: ENCODE/SCREEN, Cistrome, TCGA ATAC, 3D genome resources.

**Speaker intent**

- Show how validated individual assays scale into reusable infrastructure.

**Sources**

- S008, S009

### L3-03 — Pan-cancer ATAC as discovery engine

**Slide text**

- Primary-tumor ATAC-seq can expand the cancer regulatory catalog
- Accessibility can reveal subtype programs and noncoding regulatory hypotheses
- Case-study message: bulk assays still matter in real tumor cohorts

**Visual placeholder**

- Publication figure placeholder W02-P001 or original schematic W02-A012.

**Speaker intent**

- Use TCGA ATAC as the central bulk cancer regulatory genomics example.

**Sources**

- S011

### L3-04 — Case study: AR cistrome rewiring

**Slide text**

- Tumorigenesis can reprogram where a lineage TF binds
- Same TF, different cistrome, different regulatory interpretation
- Regulatory state change can be a cancer mechanism

**Visual placeholder**

- Publication figure placeholder W02-P002 or simplified before/after cistrome schematic.

**Speaker intent**

- Give a concrete TF-program example.

**Sources**

- S016

### L3-05 — Case study: neuroblastoma enhancer states

**Slide text**

- Super-enhancer landscapes can define tumor regulatory identities
- Regulatory circuitry helps explain cell-state plasticity
- Enhancer state can be a more informative axis than mutation status alone

**Visual placeholder**

- Publication figure placeholder W02-P003 or two-state enhancer-circuit schematic.

**Speaker intent**

- Show enhancer profiling as a way to define cancer cell states.

**Sources**

- S017

### L3-06 — Case study: enhancer hijacking

**Slide text**

- Structural variants can move oncogenes into active enhancer neighborhoods
- The coding sequence may be unchanged, but regulatory context changes
- Functional genomics links SVs to oncogene activation mechanisms

**Visual placeholder**

- W02-A005 / prompt-based enhancer hijacking visual draft; optional publication examples W02-P004? for specific loci if reviewer wants.

**Speaker intent**

- Connect regulatory genomics to structural variation and cancer mechanism.

**Sources**

- S018, S019

### L3-07 — From peaks to enhancer connectomes

**Slide text**

- H3K27ac HiChIP and related assays connect active enhancers to candidate target genes
- 3D maps can reveal static, gained, or rewired enhancer architectures
- Contact evidence strengthens hypotheses but does not prove causality alone

**Visual placeholder**

- Publication figure placeholder W02-P004 or generic enhancer-connectome schematic.

**Speaker intent**

- Present 3D regulatory maps as the state-of-field bridge from peaks to mechanisms.

**Sources**

- S012

### L3-08 — What contacts can and cannot prove

**Slide text**

- Contact: physical proximity evidence
- Co-accessibility / histone mark: regulatory-state evidence
- Expression association: target-gene evidence
- Perturbation: stronger causal evidence

**Visual placeholder**

- Evidence ladder for enhancer-gene claims.

**Speaker intent**

- Reinforce careful language around enhancer-target assignment.

**Sources**

- S010, S012

### L3-09 — Clinically realistic future

**Slide text**

- Low-input and primary-tumor regulatory assays are improving
- FFPE-compatible and 3D methods are moving closer to clinical specimens
- Routine use still needs robust QC, interpretation standards, and validation

**Visual placeholder**

- Translation funnel: assay feasibility → reproducibility → interpretation → clinical use.

**Speaker intent**

- Give a forward-looking but not overhyped summary.

**Sources**

- S007, S012

### L3-10 — Boundaries with later weeks

**Slide text**

- Week 03: single-cell and multimodal regulatory states
- Week 04: spatial localization of cells, states, and signals
- Week 06: networks, systems modeling, and causal regulation
- Week 02 gives the assay-aware statistical foundation

**Visual placeholder**

- Course handoff diagram.

**Speaker intent**

- Place this module within the larger course architecture.

**Sources**

- Course outline.

### L3-11 — Discussion prompt

**Slide text**

- When is a region only accessible?
- When is it a candidate enhancer?
- When is it a target-linked enhancer?
- When is it an oncogenic regulatory mechanism?

**Visual placeholder**

- Four-step evidence threshold prompt.

**Speaker intent**

- Turn source validation logic into student discussion.

**Sources**

- S008-S012, S018-S019

### L3-12 — Week synthesis

**Slide text**

- Model the assay
- Validate the call
- Integrate evidence layers
- Interpret regulatory mechanisms with appropriate caution

**Visual placeholder**

- Final summary: assay → model → validated evidence → cancer mechanism.

**Speaker intent**

- End with durable habits students can carry to later modules.

**Sources**

- S001-S019
