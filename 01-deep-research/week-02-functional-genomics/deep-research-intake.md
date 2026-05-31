# Week 02 — Functional Genomics in Cancer — Deep Research Intake

## Source

- Deep Research doc/link: Private Deep Research attachment (not public)
- Date received: 2026-05-30
- Imported by: Claw

## Raw content

Raw file stored at `deep-research-report.md`.

## Raw content excerpt

# Functional Genomics in Cancer

## Module overview

This module should teach students how bulk functional genomics assays become computational signal-detection problems in cancer. The core story is that ChIP-seq, ATAC-seq, CUT&RUN, CUT&Tag, and bulk chromatin interaction assays do not directly “find enhancers” or “find TF binding.” They generate assay-specific count tracks or contact matrices whose structure is set by chemistry, fragment size, local background, sequence bias, mappability, antibody performance, and replicate quality. The computational task is therefore to turn biased readouts into calibrated peaks, domains, footprints, motifs, chromatin contacts, and finally regulatory annotations that are useful for cancer biology. In oncology, this matters because many clinically important mechanisms are regulatory rather than coding: lineage-state switching, enhancer activation, super-enhancer dependence, and enhancer hijacking can change subtype definitions, oncogene assignment, and therapeutic hypotheses even when DNA mutations alone are not enough. The module should stay focused on bulk assays and regulatory element discovery in tumors and model systems, treating single-cell and spatial assays only as short transition points to later weeks. citeturn25search3turn13search0turn12search12turn8search0turn15search1turn35search0

## Must-read papers and resources

1. **Zhang et al., 2008, *Model-based analysis of ChIP-Seq (MACS)*, *Genome Biology*. DOI: 10.1186/gb-2008-9-9-r137.** The landmark narrow-peak caller. Students should read it for empirical fragment-shift estimation, local background modeling, and the basic logic behind enrichment testing that still shapes MACS3 usage. citeturn40search0turn40search2turn40search17

2. **Kharchenko et al., 2008, *Design and analysis of ChIP-seq experiments for DNA-binding proteins*, *Nature Biotechnology*. DOI: 10.1038/nbt.1508.** The classic SPP-style paper for strand cross-correlation, experiment design, and replicate-aware thinking in TF ChIP-seq. It remains one of the clearest method papers for linking assay design to statistical processing. citeturn40search1

3. **Zang et al., 2009, *A clustering approach for identification of enriched domains from histone modification ChIP-Seq data*, *Bioinformatics*; plus SICER2 documentation.** This is the broad-domain counterpoint to MACS. It is essential for teaching why histone marks such as H3K27me3 and H3K36me3 violate narrow-peak assumptions and need spatial clustering or domain models. citeturn41search5turn41search4

4. **Tarbell and Liu, 2019, *HMMRATAC: A Hidden Markov ModeleR for ATAC-seq*, *Nucleic Acids Research*. DOI: 10.1093/nar/gkz533.** The most teachable dedicated bulk ATAC-seq peak caller because it uses paired-end fragment classes and a three-state HMM to model open chromatin, flanking nucleosomes, and background. citeturn5search1turn5search12

5. **Li et al., 2019, *Identification of transcription factor binding sites using ATAC-seq*, *Genome Biology*. DOI: 10.1186/s13059-019-1642-2, and Bentsen et al., 2020, *TOBIAS*, *Nature Communications*.** Read these together for the core footprinting lesson: footprint calling only works when protocol-specific Tn5 bias is modeled, and even then occupancy inference is not identical to motif occurrence. citeturn6search12turn6search0turn21search0

6. **Meers et al., 2019, *Peak calling by Sparse Enrichment Analysis for CUT&RUN chromatin profiling*, and Yashar et al., 2022, *GoPeaks*, *Genome Biology*. DOI: 10.1186/s13059-022-02707-w.** These are the best pair for teaching low-background enrichment in CUT&RUN and CUT&Tag, including why sparse signal and assay geometry change the operating characteristics of peak callers. citeturn12search1turn12search5turn12search24

7. **Hitz et al., 2023, *The ENCODE Uniform Analysis Pipelines*.** This is the methods-and-infrastructure paper students should read to understand modern standardized processing, provenance, QC, peak outputs, and why consortium pipelines matter for benchmarking and reproducibility. It reads well with the ENCODE blacklist paper and the IDR framework. citeturn8search0turn8search8turn28search0turn27search2

8. **ENCODE Project Consortium et al., 2020, *Expanded encyclopaedias of DNA elements in the human and mouse genomes*, *Nature*. DOI: 10.1038/s41586-020-2493-4, and Moore et al., 2026, *An expanded registry of candidate cis-regulatory elements*.** These are the right entry points for ENCODE-style regulatory annotation, especially how accessibility anchors, histone marks, and CTCF are integrated into cCRE classes and exposed through SCREEN. citeturn9search4turn9search0turn32search8turn32search14

9. **Taing et al., 2024, *Cistrome Data Browser: integrated search, analysis and visualization of chromatin data*, *Nucleic Acids Research*. DOI: 10.1093/nar/gkad1069, plus Mei et al., 2017, *Cistrome Cancer*. DOI: 10.1158/0008-5472.CAN-17-0327.** This pair is ideal for public-data reuse in cancer regulatory genomics, including TF target prediction, enhancer profiles, sample metadata, and hypothesis generation from public ChIP-seq and ATAC-seq compendia. citeturn8search11turn33search0turn33search3

10. **Kaul et al., 2020, *FitHiC2*, and Juric et al., 2019, *MAPS*.** These are the most useful statistical readings for chromatin interaction analysis in this module: FitHiC2 for distance-aware significance estimation in Hi-C, and MAPS for PLAC-seq or HiChIP-style contact calling when protein- or mark-anchored loops are the biological target. citeturn7search0turn14search6

11. **Corces et al., 2018, *The chromatin accessibility landscape of primary human cancers*, *Science*. DOI: 10.1126/science.aav1898.** This is the core cancer application paper for the module. It shows how bulk ATAC-seq in TCGA tumors can expand the cis-regulatory catalog, define subtype-relevant chromatin states, and connect cancer risk loci to active regulatory DNA. citeturn1

[Truncated here in intake file; see `deep-research-report.md` for full content.]

## Initial triage

- Strongest sections: clear module overview, must-read source list, computational assumptions, tool categories, datasets/case studies, and 3-lecture outline.
- Weak or missing areas: citation markers are ChatGPT Deep Research internal turn references and are not usable as final citations; all sources need DOI/URL validation before slide/script use.
- Claims requiring validation: all numbered papers/resources, especially recent/forward-looking items (ENCODE cCRE 2026, Yost 2025 3D genome landscape, WACS, RECAP, benchmarks, FFPE-compatible 3D methods).
- Suggested source-priority level: high — this is a foundational Tao-led module and should be validated before lecture-plan generation.

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
