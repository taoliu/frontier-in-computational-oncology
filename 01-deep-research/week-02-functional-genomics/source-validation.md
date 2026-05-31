# Source Validation Log — Week 02 — Functional Genomics in Cancer

Raw Deep Research file: `deep-research-report.md`

## Priority validation queue

| ID | Claim / Item | Source | DOI/URL | Status | Notes |
|---|---|---|---|---|---|
| S001 | MACS landmark narrow-peak caller; empirical fragment-shift and local background modeling | Zhang et al. 2008, Model-based analysis of ChIP-Seq, Genome Biology | 10.1186/gb-2008-9-9-r137 | verified | Citation and conceptual claims verified; current MACS3 command details should be checked separately if used in assignments. |
| S002 | SPP/cross-correlation framework for ChIP-seq design/QC | Kharchenko et al. 2008, Nature Biotechnology | 10.1038/nbt.1508 | verified | Supports ChIP-seq design/analysis and cross-correlation-style QC framing. |
| S003 | SICER broad-domain ChIP-seq caller | Zang et al. 2009, Bioinformatics; SICER2 docs | 10.1093/bioinformatics/btp340 | verified | DOI found; supports broad/diffuse histone-domain spatial clustering. Current SICER2 docs still optional for software exercises. |
| S004 | HMMRATAC bulk ATAC-seq HMM peak caller | Tarbell & Liu 2019, Nucleic Acids Research | 10.1093/nar/gkz533 | verified | Title and model details verified: ATAC fragment decomposition plus three-state HMM. |
| S005 | ATAC footprinting requires Tn5/protocol bias correction | Li et al. 2019 Genome Biology; Bentsen et al. 2020 TOBIAS | 10.1186/s13059-019-1642-2; 10.1038/s41467-020-18035-1 | verified | TOBIAS DOI found; wording should distinguish motif occurrence, footprint pattern, and TF occupancy. |
| S006 | CUT&RUN/CUT&Tag low-background peak calling; SEACR and GoPeaks | Meers et al. 2019; Yashar et al. 2022 Genome Biology | 10.1186/s13072-019-0287-4; 10.1186/s13059-022-02707-w | verified | SEACR and GoPeaks claims verified; avoid overgeneralizing GoPeaks beyond histone-modification CUT&Tag. |
| S007 | ENCODE Uniform Analysis Pipelines and reproducibility/QC standards | Hitz et al. 2023, Bioinformatics | 10.1093/bioinformatics/btad126 | verified | Supports standardized processing/provenance/QC; use as workflow standard, not universal best method. |
| S008 | ENCODE expanded encyclopedia and cCRE registry/SCREEN | ENCODE Project Consortium 2020 Nature; Moore et al. 2026 Nature | 10.1038/s41586-020-2493-4; 10.1038/s41586-025-09909-9 | partial | 2026 item exists; cite carefully because DOI string contains 2025 but article was published in 2026. |
| S009 | Cistrome Data Browser and Cistrome Cancer for public cancer regulatory data reuse | Taing et al. 2024 NAR; Mei et al. 2017 Cancer Research | 10.1093/nar/gkad1069; 10.1158/0008-5472.CAN-17-0327 | verified | Supports ChIP-seq/ATAC-seq/DNase-seq data reuse and cancer regulatory hypothesis generation; current database counts should be rechecked before slides. |
| S010 | Chromatin interaction methods FitHiC2 and MAPS | Kaul et al. 2020; Juric et al. 2019 | 10.1038/s41596-019-0273-0; 10.1371/journal.pcbi.1006982 | verified | FitHiC2 and MAPS citations verified; emphasize contacts as evidence, not causal proof. |
| S011 | TCGA/pan-cancer ATAC-seq core case study | Corces et al. 2018 Science | 10.1126/science.aav1898 | verified | Core case-study claims verified: 410 tumors, 23 cancer types, regulatory discovery framing. |
| S012 | Primary cancer 3D genome maps / enhancer connectomes | Yost et al. 2025, Nature Genetics | 10.1038/s41588-025-02188-0 | verified | Recent source verified: 69 tumors, 15 primary cancer types, H3K27ac HiChIP enhancer-connectome framing. |

## Notes

- The original Deep Research output contained internal ChatGPT citation tokens; imported report/intake Markdown has been cleaned, and final materials still need real DOI/URL citations.
- Validation should replace those tokens with real DOI/URL citations and mark unsupported claims for revision.
