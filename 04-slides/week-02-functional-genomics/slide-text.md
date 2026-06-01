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

### L2-01 — Method development follows the assay

**Slide text**

- Different assays produce different statistical objects
- Peak callers encode assumptions about signal shape and background
- Lecture 2 goal: choose methods by evidence logic, not habit

**Visual placeholder**

- Opening framework: assay object → model assumption → call → verification.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- Module synthesis, S001-S007

### L2-02 — Four modeling questions

**Slide text**

- What signal shape is expected?
- What background should be subtracted or modeled?
- How are scores calibrated and ranked?
- What verification turns a call into usable evidence?

**Visual placeholder**

- Four-question checklist surrounding a candidate regulatory region.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S001, S003, S013, S015

### L2-03 — Narrow TF peaks: why MACS mattered

**Slide text**

- TF ChIP-seq often creates focal enrichment
- MACS models local bias/background and fragment shift
- The output is a candidate binding event, not functional proof

**Visual placeholder**

- MACS-style diagram: plus/minus strand reads, shifted fragment pileup, local background.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S001

### L2-04 — Local background is a biological safeguard

**Slide text**

- Global background can miss regional biases
- Local background helps control copy number, mappability, and open chromatin context
- Cancer data make local expectations especially important

**Visual placeholder**

- Same peak under global background versus local background at amplified/copy-variable locus.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S001, S014

### L2-05 — ChIP-seq QC: strand cross-correlation

**Slide text**

- True protein-binding ChIP-seq creates shifted strand patterns
- Cross-correlation summarizes signal structure and fragment length
- QC tells us whether peak calls deserve trust

**Visual placeholder**

- Plus/minus strand cross-correlation curve with fragment-length peak and background shoulder.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S002, S007

### L2-06 — ENCODE-style pipelines as provenance systems

**Slide text**

- Standardized pipelines record processing choices and QC outputs
- FRiP, library complexity, TSS enrichment, and blacklist filtering support interpretation
- A pipeline is not a universal best method, but it improves auditability

**Visual placeholder**

- Pipeline provenance ladder: raw data → alignment → filtering → QC → calls → reports.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S007, S014

### L2-07 — Broad domains break narrow-peak assumptions

**Slide text**

- Some histone marks form diffuse enriched regions
- Spatial clustering can detect domains rather than focal summits
- Method choice changes whether biology appears fragmented or continuous

**Visual placeholder**

- Narrow peak caller splitting broad histone mark versus SICER-style enriched domain.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S003

### L2-08 — ATAC-seq requires fragment-aware modeling

**Slide text**

- ATAC reads contain both accessibility and nucleosome-scale information
- Short and nucleosomal fragments should not always be pooled blindly
- HMMRATAC models fragment classes as chromatin states

**Visual placeholder**

- Three ATAC fragment coverage tracks feeding into hidden chromatin-state path.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S004

### L2-09 — CUT assays change the background problem

**Slide text**

- CUT&RUN and CUT&Tag create tethered, often low-background signal
- Sparse enrichment can make standard ChIP assumptions mismatched
- SEACR and GoPeaks illustrate assay-specific caller design

**Visual placeholder**

- CUT&RUN sparse peaks and CUT&Tag histone-mark signal compared with ChIP-seq background.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S006

### L2-10 — Motif enrichment is sequence evidence

**Slide text**

- Motif enrichment asks which sequence patterns are overrepresented
- It suggests candidate TF families, not direct occupancy
- Background sequence choice strongly affects results

**Visual placeholder**

- Peak set → motif enrichment → candidate TF family, with matched background sequence.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S005

### L2-11 — Footprinting asks a stronger question

**Slide text**

- Footprints use cut-site patterns around motifs
- Bias correction is essential for ATAC-seq footprinting
- Footprint ≠ guaranteed binding; it is occupancy-like evidence

**Visual placeholder**

- Motif-centered ATAC cut profile before and after Tn5 bias correction.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S005

### L2-12 — Contact calling needs a distance-aware null

**Slide text**

- Contact frequency decays with genomic distance
- FitHiC2 models statistical confidence for Hi-C contacts
- MAPS models PLAC-seq/HiChIP long-range interactions

**Visual placeholder**

- Contact count plotted against distance-decay background with significant outlier interaction.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S010

### L2-13 — Replicates are about ranked stability

**Slide text**

- Reproducibility is more than overlap between peak lists
- IDR-style analysis asks whether ranks are consistent
- Stable high-ranking calls are better candidates for interpretation

**Visual placeholder**

- Two replicate ranked lists feeding into reproducible high-confidence calls.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S013, S007

### L2-14 — Calibration affects prioritization

**Slide text**

- Peak-caller P values depend on model assumptions
- RECAP shows nominal significance can be miscalibrated
- Poor calibration can distort top-candidate selection

**Visual placeholder**

- Nominal P values versus calibrated empirical significance; top candidates reshuffled.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S015

### L2-15 — Benchmark design must match the claim

**Slide text**

- Gold standards are often incomplete or biased
- Simulations test assumptions, not full biological truth
- Benchmarks should evaluate the decision the method will support

**Visual placeholder**

- Benchmark triangle: simulated truth, orthogonal assays, perturbation-supported examples.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S007, S013, S015

### L2-16 — Orthogonal evidence strengthens weak labels

**Slide text**

- Different assays answer different parts of the regulatory question
- Concordant evidence supports annotation; discordance reveals uncertainty
- Perturbation is strongest when causal claims are needed

**Visual placeholder**

- Evidence ladder from peak call to orthogonal mark, expression link, contact, perturbation.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S008, S009, S010

### L2-17 — Cancer-specific verification adds extra checks

**Slide text**

- Copy number and purity can distort read depth and apparent accessibility
- Subtype and cell-mixture effects can masquerade as tumor-intrinsic programs
- Verification should consider tumor context, not only assay QC

**Visual placeholder**

- Cancer-specific QC overlay: copy number, purity, subtype, mixture, regulatory call.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S011, S012, S014

### L2-18 — Choosing a method is choosing a claim

**Slide text**

- Narrow peak, broad domain, footprint, state, and contact calls support different statements
- Tool choice should be explained in biological language
- The output label should match the evidence strength

**Visual placeholder**

- Method-to-claim map: MACS peak, SICER domain, HMMRATAC state, TOBIAS footprint, FitHiC2 contact.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S001, S003, S004, S005, S010

### L2-19 — A practical verification checklist

**Slide text**

- Assay-object match: does the method fit the data?
- QC and filtering: is the experiment interpretable?
- Replicates and calibration: are rankings stable and scores meaningful?
- Biological integration: what evidence supports the claim?

**Visual placeholder**

- Checklist card for reviewing a functional-genomics method section.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S001-S015

### L2-20 — Lecture 2 synthesis

**Slide text**

- Methods differ because assay assumptions differ
- Verification is part of method development, not an afterthought
- Careful claims connect computational calls to cancer biology
- Next: applying regulatory resources and case studies

**Visual placeholder**

- Final synthesis: method families feeding into verified regulatory evidence and cancer interpretation.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S001-S015

---

## Lecture 3 — Application & State of the Field
### L3-01 — From methods to cancer insight

**Slide text**

- Lecture 3 asks how functional genomics changes cancer interpretation
- Public resources convert many assays into reusable regulatory priors
- Case studies show regulatory mechanisms missed by mutation-only views

**Visual placeholder**

- Opening map: methods from Lecture 2 flowing into resources, cancer case studies, and future single-cell/spatial/network modules.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- Module synthesis, S008-S012, S016-S019

### L3-02 — The application checklist

**Slide text**

- What resource or cohort produced the regulatory evidence?
- What assay object and model created the feature?
- What cancer claim is justified by the evidence?

**Visual placeholder**

- Three-step checklist card: resource/cohort → assay/model → cancer claim.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S008-S012

### L3-03 — Public atlases are reusable priors

**Slide text**

- ENCODE and related resources organize functional elements across biosamples
- cCREs summarize candidate regulatory evidence, not validated causal function
- Atlases help interpret new cancer datasets, but context still matters

**Visual placeholder**

- Regulatory atlas schematic: many assays and biosamples feeding a reusable candidate-element registry.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S008

### L3-04 — SCREEN and cCRE language

**Slide text**

- SCREEN exposes candidate cis-regulatory elements for search and reuse
- Labels reflect evidence combinations such as accessibility and histone marks
- The word candidate should stay visible in interpretation

**Visual placeholder**

- Browser-style cCRE card showing accessibility, enhancer-like mark, promoter-like mark, and candidate label.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S008

### L3-05 — Cistrome turns public data into hypotheses

**Slide text**

- Cistrome resources collect and process public chromatin datasets
- Cistrome Cancer links regulatory profiles to cancer questions
- Reuse is powerful when metadata, QC, and biological context are checked

**Visual placeholder**

- Resource workflow: public ChIP-seq/ATAC-seq/DNase-seq → curated database → cancer hypothesis.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S009

### L3-06 — Resource use is not shortcut biology

**Slide text**

- Public tracks provide priors, not automatic answers
- Biosample match, antibody/assay quality, and processing choices affect interpretation
- Good reuse asks whether the prior fits the cancer context

**Visual placeholder**

- Decision tree for using a public regulatory track: match, quality, evidence type, context.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S007-S009, S014

### L3-07 — Pan-cancer ATAC-seq maps regulatory state

**Slide text**

- TCGA ATAC-seq profiled chromatin accessibility across primary tumors
- Accessibility patterns reveal tumor-type and subtype regulatory programs
- Noncoding regulatory features can become cohort-level biological variables

**Visual placeholder**

- Cohort schematic: many tumor samples → ATAC peak matrix → cancer-type/subtype regulatory map.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S011

### L3-08 — What pan-cancer accessibility adds

**Slide text**

- Accessibility can highlight active regulatory elements beyond coding mutations
- Risk loci and noncoding elements can be linked to tumor regulatory programs
- The output is a map of candidate regulatory activity across cancers

**Visual placeholder**

- Three-panel schematic: subtype-specific peak, risk-locus accessibility, candidate enhancer near gene.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S011

### L3-09 — AR cistrome rewiring in prostate cancer

**Slide text**

- The same transcription factor can bind different sites in tumor versus normal context
- AR binding is extensively reprogrammed during prostate tumorigenesis
- Cofactors and chromatin context help reshape the regulatory program

**Visual placeholder**

- Normal versus tumor AR binding map with shifted enhancer usage and cofactor icons.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S016

### L3-10 — The lesson from TF rewiring

**Slide text**

- TF activity is not determined by motif sequence alone
- Cancer state can redirect binding and target genes
- Cistrome rewiring turns regulatory data into a mechanism hypothesis

**Visual placeholder**

- Motif availability plus chromatin context plus cofactors leading to tumor-specific TF targets.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S005, S016

### L3-11 — Super-enhancers as regulatory identity markers

**Slide text**

- Clusters of enhancer activity can mark core transcriptional circuitry
- Neuroblastoma studies revealed super-enhancer-associated cell states
- Regulatory identity can explain tumor heterogeneity beyond mutation lists

**Visual placeholder**

- Super-enhancer landscape separating two neuroblastoma regulatory states.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S017

### L3-12 — Interpreting super-enhancer claims carefully

**Slide text**

- Super-enhancer calls depend on ranking and stitching choices
- A strong enhancer cluster suggests regulatory importance, not automatic dependency
- Perturbation or convergent evidence strengthens the claim

**Visual placeholder**

- Ranked enhancer signal curve with cutoff, stitched cluster, and validation evidence ladder.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S017, S015

### L3-13 — Enhancer hijacking: structural variation meets regulation

**Slide text**

- Structural variants can reposition enhancers near oncogenes
- Medulloblastoma enhancer hijacking activates GFI1-family oncogenes
- The mechanism requires integrating SV, enhancer evidence, and expression

**Visual placeholder**

- Before/after genome cartoon: rearrangement moves active enhancer beside oncogene.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S018

### L3-14 — BCL11B enhancer hijacking in leukemia

**Slide text**

- Enhancer hijacking can activate oncogenes in lineage-ambiguous leukemia
- BCL11B deregulation illustrates allele-specific regulatory activation
- This is a regulatory mechanism, not a coding-mutation mechanism

**Visual placeholder**

- Leukemia example schematic: rearranged enhancer neighborhood causing BCL11B activation.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S019

### L3-15 — 3D genome maps add enhancer-connectome evidence

**Slide text**

- H3K27ac HiChIP can connect active enhancers with promoter neighborhoods
- Primary-cancer 3D maps reveal static, gained, and rewired enhancer usage
- Contacts add linkage evidence, not automatic causal proof

**Visual placeholder**

- Enhancer-connectome diagram: active enhancer loops to promoter across cancer contexts.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S012, S010

### L3-16 — From peaks to enhancer connectomes

**Slide text**

- Accessibility and histone marks identify candidate regulatory elements
- Contact maps suggest which promoters they may influence
- Expression and perturbation decide how strong the target-gene claim can be

**Visual placeholder**

- Evidence chain: peak/mark → contact → expression link → perturbation-supported target.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S010, S012

### L3-17 — Bulk functional genomics still has limits

**Slide text**

- Bulk profiles mix tumor, stromal, immune, and lineage states
- Rare subclones and spatial niches can be averaged away
- Regulatory maps often identify candidates, not complete causal circuits

**Visual placeholder**

- Bulk signal decomposition cartoon showing tumor, immune, stromal, and rare-state contributions.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S011, S012

### L3-18 — Natural handoff to single-cell and spatial modules

**Slide text**

- Single-cell assays separate regulatory programs across cell states
- Spatial methods ask where those states and signals occur in tissue
- Network models ask how regulatory elements and genes form systems

**Visual placeholder**

- Module bridge: bulk regulatory map → single-cell resolution → spatial context → network/causal model.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- Module synthesis, S011, S012

### L3-19 — A reading checklist for cancer papers

**Slide text**

- Translate each claim back to the assay evidence
- Separate candidate, linked, active, and validated regulatory elements
- Ask what would change the authors’ conclusion if removed

**Visual placeholder**

- Paper-reading checklist with graded claim language: candidate, linked, active, validated.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S001-S019

### L3-20 — Week 2 synthesis

**Slide text**

- Functional genomics turns molecular readouts into regulatory evidence
- Cancer applications reveal subtype programs, TF rewiring, enhancer activation, and 3D linkage
- Strong interpretation requires assay-aware methods, reproducibility, and graded claims
- Next: higher-resolution regulatory biology in later modules

**Visual placeholder**

- Final Week 2 synthesis: assay → method → resource/case study → careful cancer mechanism claim.

**Speaker intent**

- Production slide with approximately 90 seconds of narration.

**Sources**

- S001-S019

