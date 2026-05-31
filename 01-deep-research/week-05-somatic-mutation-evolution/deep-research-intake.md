# Week 05 — Somatic Mutation, Variant Interpretation, and Cancer Evolution — Deep Research Intake

## Source

- Deep Research doc/link: Private Deep Research attachment (not public)
- Date received: 2026-05-31
- Imported by: Claw

## Raw content

Raw file stored at `deep-research-report.md`.

## Raw content excerpt

# Somatic Mutation, Variant Interpretation, and Cancer Evolution

## Module overview

This module should teach a full computational story: how bulk tumor DNA sequencing, usually from paired tumor-normal whole-genome, whole-exome, or targeted-panel data, is converted into somatic SNVs and indels, copy-number states, purity and ploidy estimates, structural variation calls when needed, driver hypotheses, mutational-process assignments, and finally clonal architectures and evolutionary histories. The central method-development lesson is that each step is statistically entangled with the others: variant evidence depends on assay noise and artifact models, observed allele fractions depend on purity and allele-specific copy number, driver discovery depends on robust background-rate modeling, and clonal inference is only as good as the copy-number correction and sampling design that feed it. Good teaching examples therefore come from workflows and benchmarks, not just from headline tools: the current GATK somatic workflow formalizes assembly-based calling plus contamination and orientation-bias filtering, the GDC explicitly publishes multiple pipelines rather than pretending a single best caller exists, SEQC2 and related truth sets expose how assay and pipeline choices change accuracy, and PCAWG and TRACERx show how mutation calling, copy number, signatures, and phylogenetics combine to reveal ongoing selection, whole-genome doubling, and metastatic trajectories.

## Must-read papers and resources

**GATK Somatic Short Variant Discovery with the MuTect lineage.** The Broad workflow is the clearest current teaching resource for Mutect2-era calling: local reassembly in active regions, Pair-HMM read-to-haplotype likelihoods, Bayesian somatic scoring, explicit contamination estimation, orientation-bias learning, probabilistic filtering, and annotation. Pair it with the original MuTect paper to show what problems the field was trying to solve in impure, heterogeneous tumors before assembly-based Mutect2 generalized the approach. Updated June 2024; landmark paper: Cibulskis et al., *Nature Biotechnology* 2013, doi: 10.1038/nbt.2514.

**Strelka2.** Kim et al. made Strelka2 one of the core comparisons for any lecture on somatic SNV and indel detection. It is useful pedagogically because it represents a different design choice from Mutect2, with a fast candidate-generation and scoring framework that remains strong in both germline and somatic settings. Kim et al., *Nature Methods* 2018, doi: 10.1038/s41592-018-0051-x.

**SEQC2 truth sets and best-practice benchmarking.** Fang et al. established the HCC1395/HCC1395BL reference samples and community call sets for benchmarking, while Xiao et al. turned those materials into a systematic assessment of how purity, input, assay type, and pipeline choice affect accuracy and reproducibility. This pair is the best bridge from “algorithm” to “verification.” Fang et al., *Nature Biotechnology* 2021, doi: 10.1038/s41587-021-00993-6; Xiao et al., *Nature Biotechnology* 2021, doi: 10.1038/s41587-021-00994-5.

**dNdScv and modern positive-selection analysis.** Martincorena et al. turned dN/dS ideas into a practical framework for somatic driver discovery, and the dNdScv package remains a strong default for teaching how recurrence is converted into evidence of positive selection after correcting for sequence context and mutation-rate heterogeneity. Martincorena et al., *Cell* 2017, doi: 10.1016/j.cell.2017.09.042.

**Mutational signatures and the COSMIC reference catalog.** Alexandrov et al. is still the landmark reference for SBS, DBS, and indel signatures, and the current COSMIC signatures resource is the operational catalog students will actually use. COSMIC currently serves human cancer signatures version 3.6, including SBS, DBS, ID, CN, SV, and RNA-SBS downloads. Alexandrov et al., *Nature* 2020, doi: 10.1038/s41586-020-1943-3.

**MuSiCal and the newer generation of signature inference.** Jin et al. is a strong modern methods paper because it tackles several practical failures in signature discovery and assignment, and recent benchmarking shows that fitting tools can differ substantially, with SigProfilerSingleSample tending to do well for small mutation counts and SigProfilerAssignment or MuSiCal doing well with larger catalogs. Jin et al., *Nature Genetics* 2024, doi: 10.1038/s41588-024-01659-0.

**HATCHet for allele- and clone-specific copy number.** Zaccaria and Raphael is the right paper to teach why purity, ploidy, whole-genome doubling, and multi-sample CNA deconvolution are hard, and how joint modeling across samples improves identifiability. It also gives a clean entry point into simulation-driven validation with MASCoTE. *Nature Communications* 2020, doi: 10.1038/s41467-020-17967-y.

**PyClone-VI together with MEDICC2.** PyClone-VI is the pragmatic modern teaching paper for bulk clonal clustering from corrected cancer cell fractions, while MEDICC2 shows how phylogenetic inference can be done directly on haplotype-specific copy-number states, including explicit modeling of whole-genome doubling. PyClone-VI: Gillis and Roth, *BMC Bioinformatics* 2020, doi: 10.1186/s12859-020-03919-2. MEDICC2: Kaufmann et al., *Genome Biology* 2022, doi: 10.1186/s13059-022-02794-9.

**PCAWG intra-tumor heterogeneity.** Dentro et al. is the most useful pan-cancer application paper for showing what clonal and subclonal inference can produce at scale: 2,658 whole genomes across 38 cancer types, widespread branching subclones, positive selection on subclonal drivers, and dynamic changes in mutational processes. Dentro et al., *Cell* 2021, doi: 10.1016/j.cell.2021.03.009.

**TRACERx lung evolution.** Frankell et al. is the best single cancer-focused application for linking heterogeneity, copy-number evolution, whole-genome doubling, and patient outcome. It also makes the educational point that multi-region sampling reveals events that single-sample reconstructions miss. Frankell et al., *Nature* 2023, doi: 10.1038/s41586-023-05783-5.


[Truncated here in intake file; see `deep-research-report.md` for full content.]

## Initial triage

- Strongest sections: coherent end-to-end bulk tumor DNA sequencing story; strong linkage between somatic calling, artifact filtering, copy number/purity, driver discovery, signatures, clonal inference, and cancer evolution; good benchmark/dataset orientation via SEQC2, TCGA MC3/GDC, PCAWG, TRACERx, Hartwig, COLO829, and DREAM SMC-Het.
- Weak or missing areas: citation markers are ChatGPT Deep Research internal turn references and are not usable as final citations; several fast-moving resource counts/version claims need current verification; module is broad and may need pruning to keep Week 05 teachable in three lectures.
- Claims requiring validation: all must-read papers/resources and DOIs; GATK/GDC current workflow descriptions; COSMIC/IntOGen/OncoKB version/count claims; benchmark dataset sizes; TRACERx/PCAWG numerical findings; 2025 benchmarking and therapy-driven evolution papers.
- Suggested source-priority level: high — this is a core methods/evolution module and should be validated before lecture-plan and slide generation.

## Extraction checklist

- [ ] Landmark papers
- [ ] Recent reviews
- [ ] Current methods/tools
- [ ] Datasets/benchmarks
- [ ] Cancer case studies
- [ ] Figures/assets to recreate or cite
- [ ] Open problems
- [ ] Lecture 1 material
- [ ] Lecture 2 material
- [ ] Lecture 3 material
