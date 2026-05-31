# Week 02 — Functional Genomics in Cancer — Source Notes

Use this file for evidence snippets, validation reasoning, and source-specific caveats. Keep direct quotes short and cite the source URL/DOI.

## Notes by source ID

### S001 — MACS

- Source: Zhang et al. 2008, Genome Biology, doi:10.1186/gb-2008-9-9-r137.
- What it supports: MACS as the landmark model-based ChIP-seq peak caller; empirical fragment-size/shift modeling; local background reasoning.
- Caveats / wording limits: use MACS as the conceptual baseline for narrow-peak enrichment, not as the only current implementation. Refer to MACS3 docs separately if teaching current command-line details.
- Where used: Lecture 1 assay/background framing; Lecture 2 narrow-peak model.

### S002 — SPP / cross-correlation

- Source: Kharchenko et al. 2008, Nature Biotechnology, doi:10.1038/nbt.1508.
- What it supports: ChIP-seq design and analysis for DNA-binding proteins; strand-shift/cross-correlation style signal and QC framing.
- Caveats / wording limits: use as conceptual and historical QC foundation. Do not overstate as the only replicate strategy.
- Where used: Lecture 1 QC; Lecture 2 cross-correlation slide.

### S003 — SICER

- Source: Zang et al. 2009, Bioinformatics, doi:10.1093/bioinformatics/btp340.
- What it supports: broad/diffuse histone modification signals require domain/spatial clustering models rather than narrow-peak-only logic.
- Caveats / wording limits: SICER is a landmark; if assigning software exercises, check SICER2/current documentation separately.
- Where used: Lecture 2 broad-domain model.

### S004 — HMMRATAC

- Source: Tarbell & Liu 2019, NAR, doi:10.1093/nar/gkz533.
- What it supports: ATAC-seq fragment-size decomposition and a three-state HMM representing open chromatin center, nucleosome regions, and background.
- Caveats / wording limits: present as an ATAC-specific model example; avoid claiming all ATAC peak calling should use HMMRATAC.
- Where used: Lecture 1 data-object comparison; Lecture 2 ATAC model slide.

### S005 — ATAC footprinting / TOBIAS

- Sources: Li et al. 2019, Genome Biology, doi:10.1186/s13059-019-1642-2; Bentsen et al. 2020, Nature Communications, doi:10.1038/s41467-020-18035-1.
- What it supports: footprinting requires bias-aware modeling; TOBIAS is a practical framework for ATAC footprinting and TF binding dynamics.
- Caveats / wording limits: motif occurrence, cut-site depletion, and actual TF occupancy should be taught as separate evidence layers.
- Where used: Lecture 2 motif/footprint section.

### S006 — SEACR and GoPeaks

- Sources: Meers et al. 2019, Epigenetics & Chromatin, doi:10.1186/s13072-019-0287-4; Yashar et al. 2022, Genome Biology, doi:10.1186/s13059-022-02707-w.
- What it supports: low-background CUT&RUN/CUT&Tag data motivates assay-specific peak-calling approaches.
- Caveats / wording limits: GoPeaks paper is specifically framed around CUT&Tag histone modification peak calling; be careful with TF CUT&Tag generalization.
- Where used: Lecture 2 CUT assay slide.

### S007 — ENCODE Uniform Analysis Pipelines

- Source: Hitz et al. 2023, Bioinformatics, doi:10.1093/bioinformatics/btad126.
- What it supports: standardized processing, provenance, QC, and consortium-scale reproducibility.
- Caveats / wording limits: teach as a reproducibility standard and workflow anchor; do not equate with universal optimality.
- Where used: Lecture 1 and 2 QC/provenance sections.

### S008 — ENCODE/cCRE/SCREEN

- Sources: ENCODE Project Consortium et al. 2020, Nature, doi:10.1038/s41586-020-2493-4; Moore et al. 2026, Nature, doi:10.1038/s41586-025-09909-9.
- What it supports: ENCODE expansion; cCRE registry; SCREEN as a practical interface for regulatory annotation.
- Caveats / wording limits: Moore article is a 2026 publication with a 2025 DOI string; cite dates carefully.
- Where used: Lecture 3 resources section.

### S009 — Cistrome DB / Cistrome Cancer

- Sources: Taing et al. 2024, NAR, doi:10.1093/nar/gkad1069; Mei et al. 2017, Cancer Research, doi:10.1158/0008-5472.CAN-17-0327.
- What it supports: Cistrome Data Browser integrates ChIP-seq, ATAC-seq, and DNase-seq data; Cistrome Cancer supports cancer-focused regulatory data reuse.
- Caveats / wording limits: verify current database counts before putting numbers on slides.
- Where used: Lecture 3 resources and public-data reuse.

### S010 — FitHiC2 / MAPS

- Sources: Kaul et al. 2020, Nature Protocols, doi:10.1038/s41596-019-0273-0; Juric et al. 2019, PLOS Computational Biology, doi:10.1371/journal.pcbi.1006982.
- What it supports: FitHiC2 for distance-aware significance estimation in Hi-C; MAPS for PLAC-seq/HiChIP long-range interaction analysis.
- Caveats / wording limits: significant contacts are linkage evidence, not causal enhancer-gene proof.
- Where used: Lecture 2 contact-statistics section; Lecture 3 enhancer-connectome bridge.

### S011 — TCGA pan-cancer ATAC

- Source: Corces et al. 2018, Science, doi:10.1126/science.aav1898.
- What it supports: 410 TCGA tumor samples across 23 cancer types; accessible elements and regulatory interpretation in primary cancers.
- Caveats / wording limits: this is the core cancer case study; keep detailed numerical claims tied to the paper.
- Where used: Lecture 3 pan-cancer accessibility case study.

### S012 — Primary-cancer 3D genome maps

- Source: Yost et al. 2025, Nature Genetics, doi:10.1038/s41588-025-02188-0.
- What it supports: 69 tumors across 15 TCGA cancer types profiled by H3K27ac HiChIP; enhancer connectomes and oncogene enhancer usage categories.
- Caveats / wording limits: frame as a recent state-of-field case study; do not make it the whole module.
- Where used: Lecture 3 3D genome/connectome case study.

## Additional validation needed before final slides

- Prostate cancer AR cistrome rewiring source(s).
- Neuroblastoma super-enhancer state source(s).
- Enhancer hijacking in medulloblastoma/leukemia source(s).
- ENCODE blacklist and IDR papers if those get dedicated method slides.
