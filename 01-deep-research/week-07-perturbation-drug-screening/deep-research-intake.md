# Week 07 — Drug Screening, Perturbation Modeling, and Virtual Cell Models — Deep Research Intake

## Source

- Deep Research doc/link: Private Deep Research attachment (not public)
- Date received: 2026-05-31
- Imported by: Claw

## Raw content

Raw file stored at `deep-research-report.md`.

## Raw content excerpt

# Frontier in Computational Oncology Week Seven Drug Screening Perturbation Modeling and Virtual Cell Models

## Module overview

This module should teach students how oncology perturbation experiments become computational objects and, eventually, predictive models: pooled CRISPR knockout/interference/activation screens and legacy RNAi assays turn perturbations into guide-count data; pharmacologic screens turn perturbations into dose–response surfaces; chemogenetic and synthetic-lethality screens ask how genetic context changes drug response; Perturb-seq and related multimodal assays replace scalar phenotypes with transcriptomic, proteomic or chromatin-state readouts; and emerging “virtual cell” efforts try to infer unmeasured perturbation responses in silico. The biological aim is to discover dependencies, rational combinations, resistance mechanisms and context-specific vulnerabilities in cancer, but the computational difficulty is that every stage is noisy and design-dependent: multiplicity of infection, library coverage, controls, guide efficiency, off-target activity, copy-number and proximity artifacts, baseline fitness differences, batch effects, limited dose grids, non-unique synergy null models, noisy single-cell perturbation labels, and poor cross-context generalization can all dominate the signal if they are not modeled explicitly. This week therefore belongs squarely to perturbation-driven response modeling, not to general network inference without interventional data and not to patient-level digital twins.

## Must-read papers and resources

- **Bock et al., _High-content CRISPR screening_ (Nature Reviews Methods Primers, 2022; DOI: 10.1038/s43586-021-00093-4).** The best single methods-oriented primer for designing CRISPR screens, understanding pooled versus high-content phenotypes, and connecting experimental decisions to downstream computation.

- **Bodapati et al., _A benchmark of algorithms for the analysis of pooled CRISPR screens_ (Genome Biology, 2020; DOI: 10.1186/s13059-020-01972-x).** Essential for Lecture Two because it compares algorithmic families under simulation and real-data settings and makes benchmarking logic itself part of the curriculum.

- **Vinceti et al., _A benchmark of computational methods for correcting biases of established and unknown origin in CRISPR-Cas9 screening data_ (Genome Biology, 2024; DOI: 10.1186/s13059-024-03336-1).** A must-read on copy-number and proximity biases, which are now impossible to ignore in cancer dependency analysis.

- **Arafeh et al., _The present and future of the Cancer Dependency Map_ (Nature Reviews Cancer, 2025; DOI: 10.1038/s41568-024-00763-x).** The clearest recent perspective on what dependency maps can support biologically, how they are used in oncology, and what the next generation of perturbation resources needs to add.

- **Pacini et al., _A comprehensive clinically informed map of dependencies in cancer cells and framework for target prioritization_ (Cancer Cell, 2024).** The most directly relevant modern pan-cancer dependency resource paper, linking CRISPR screening with multi-omics and target prioritization across 930 cancer cell lines.

- **Corsello et al., _Discovering the anti-cancer potential of non-oncology drugs by systematic viability profiling_ (2020).** The key PRISM resource paper for pooled-cell-line pharmacologic screening, drug repurposing, and computational prediction of selective response from molecular features.

- **Subramanian et al., _A Next Generation Connectivity Map: L1000 Platform and the First 1,000,000 Profiles_ (Cell, 2017; DOI: 10.1016/j.cell.2017.10.049).** Still the landmark perturbational-transcriptomics paper; assign it to explain why response signatures, not only viability, matter for mechanism-of-action and perturbation matching.

- **Replogle et al., _Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq_ (Cell, 2022).** The definitive genome-scale Perturb-seq paper and a bridge from classical screen analysis to representation learning on high-dimensional perturbation phenotypes.

- **Wei et al., _Benchmarking algorithms for generalizable single-cell perturbation response prediction_ (Nature Methods, 2025; DOI: 10.1038/s41592-025-02980-0).** The benchmark to use when teaching how to evaluate perturbation-response models honestly across unseen cell states and unseen perturbations.

- **Wooten et al., _MuSyC is a consensus framework that unifies multi-drug synergy metrics for combinatorial drug discovery_ (Nature Communications, 2021; DOI: 10.1038/s41467-021-24789-z).** The paper to assign when students ask what “synergy” actually means and why a single scalar answer is usually inadequate.

- **Bunne et al., _How to build the virtual cell with artificial intelligence_ (Cell, 2024; DOI: 10.1016/j.cell.2024.11.015).** The most useful forward-looking paper for ending the module with a rigorous, not hand-wavy, discussion of virtual perturbation concepts.

- **Coelho et al., _Base editing screens define the genetic landscape of cancer drug resistance mechanisms_ (Nature Genetics, 2024; DOI: 10.1038/s41588-024-01948-8).** A strong application paper showing how perturbation design itself changes the computational problem, moving from gene knockout to variant-level resistance mapping.


[Truncated here in intake file; see `deep-research-report.md` for full content.]

## Initial triage

- Strongest sections: strong perturbation-first conceptual boundary; clear separation among pooled CRISPR/RNAi screens, pharmacologic dose–response modeling, chemogenetic/synthetic-lethality screens, Perturb-seq/high-content perturbation readouts, and virtual-cell/virtual-perturbation modeling; good attention to nuisance structure, benchmark realism, and model assumptions.
- Weak or missing areas: citation markers are ChatGPT Deep Research internal turn references and must be replaced with real DOI/URL citations; several 2024–2025 claims are fast-moving and need careful live verification before lecture-plan generation, especially virtual-cell benchmarks, DepMap phase directions, scPerturBench, and recent single-cell perturbation-response benchmarks.
- Claims requiring validation: all must-read papers/resources and DOIs; CRISPR benchmark and bias-correction claims; DepMap/CCLE/Pacini resource details and cell-line counts; GDSC/CTRP/PRISM/PharmacoDB counts; Perturb-seq/scPerturb/PerturbDB/scPerturBench claims; virtual-cell benchmark claims; case-study claims for melanoma Perturb-CITE-seq, base editing resistance maps, SCHEMATIC, and organoid pharmacotyping.
- Suggested source-priority level: high — this is a benchmark- and resource-heavy perturbation module with multiple current claims that should be validated before downstream teaching content.

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
