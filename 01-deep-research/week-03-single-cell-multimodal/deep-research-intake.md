# Week 03 — Single-Cell and Multimodal Regulatory Genomics — Deep Research Intake

## Source

- Deep Research doc/link: Private Deep Research attachment (not public)
- Date received: 2026-05-30
- Imported by: Claw

## Raw content

Raw file stored at `deep-research-report.md`.

## Raw content excerpt

# Single-Cell and Multimodal Regulatory Genomics in Cancer

## Module overview

This module centers on a simple but important idea: cancer cell states and their regulatory programs are often cell-state-specific, therapy-responsive, and mixed with diverse non-malignant immune and stromal populations, so bulk assays miss key biology by averaging across cells. Recent single-cell RNA-seq, single-cell ATAC-seq, and paired RNA+ATAC multiome assays make it possible to define malignant and non-malignant states, link transcription to chromatin accessibility, infer candidate transcription factor programs, and study resistance trajectories at single-cell resolution. The computational challenge is not only large sample size, but also the statistical form of the data: scRNA-seq counts are overdispersed with many zeros, scATAC-seq matrices are even sparser and depend strongly on feature construction, and cross-modality integration must balance batch removal against preservation of subtle biology. For cancer, the key teaching goal is to show students how modeling choices around normalization, feature engineering, latent spaces, label transfer, trajectory inference, regulatory inference, and malignant-state calling change the biological story they recover.

## Must-read papers and resources

The list below leans recent, but it keeps a few older landmarks because they still define how the field thinks.

- **Heumos et al., 2023, *Nature Reviews Genetics*. Best practices for single-cell analysis across modalities.** A high-value review for setting the full workflow, including where unimodal and multimodal analyses differ, how benchmarks should inform method choice, and how to reason about integration, annotation, and trajectory claims. **DOI:** 10.1038/s41576-023-00586-w.

- **Yang et al., 2024, *Life Medicine*. Integration of single-cell transcriptome and chromatin accessibility and its application on tumor investigation.** A module-specific review focused on exactly the RNA-plus-ATAC integration problem in tumors, with a useful summary of computational methods and cancer use cases. **DOI:** 10.1093/lifemedi/lnae015.

- **Hao et al., 2021, *Cell*. Integrated analysis of multimodal single-cell data.** The core Seurat multimodal paper. It introduces weighted nearest neighbor analysis and multimodal reference mapping, both of which are central for teaching paired-modality integration and state definition. **DOI:** 10.1016/j.cell.2021.04.048.

- **Hao et al., 2023, *Nature Biotechnology*. Dictionary learning for integrative, multimodal and scalable single-cell analysis.** The Seurat v5 “bridge integration” paper. This is essential for teaching how RNA-only references can still annotate non-RNA modalities through a paired multiome bridge. **DOI:** 10.1038/s41587-023-01767-y.

- **Granja et al., 2021, *Nature Genetics*. ArchR is a scalable software package for integrative single-cell chromatin accessibility analysis.** Still one of the clearest end-to-end scATAC papers, and one of the best ways to teach iterative LSI, gene scores, peak-to-gene links, TF footprinting, and RNA integration inside a single framework. **DOI:** 10.1038/s41588-021-00790-6.

- **Cao and Gao, 2022, *Nature Biotechnology*. Multi-omics single-cell data integration and regulatory inference with graph-linked embedding.** GLUE is one of the key unpaired integration papers because it makes prior regulatory graphs part of the alignment model instead of treating feature spaces as unrelated. **DOI:** 10.1038/s41587-022-01284-4.

- **Mitra et al., 2024, *Nature Genetics*. Single-cell multi-ome regression models identify functional and disease-associated enhancers and enable chromatin potential analysis.** SCARlink is important because it moves enhancer-gene inference beyond simple peak-gene correlation and uses regularized Poisson regression on tile-level accessibility. **DOI:** 10.1038/s41588-024-01689-8.

- **Schep et al., 2017, *Nature Methods*. chromVAR: inferring transcription-factor-associated accessibility from single-cell epigenomic data.** An older landmark, but still foundational for motif deviation analysis in scATAC-seq and in tools such as ArchR and Signac. **DOI:** 10.1038/nmeth.4401.

- **Aibar et al., 2017, *Nature Methods*. SCENIC: single-cell regulatory network inference and clustering.** Another older landmark that remains central for teaching regulon-based state identification from expression alone and for comparing RNA-only versus RNA+ATAC regulatory inference. **DOI:** 10.1038/nmeth.4463.

- **Luecken et al., 2022, *Nature Methods*. Benchmarking atlas-level data integration in single-cell genomics.** A required benchmark paper because it makes the overcorrection versus bio-conservation tradeoff concrete, and it includes both RNA and ATAC integration scenarios. **DOI:** 10.1038/s41592-021-01336-8.

- **Luo et al., 2024, *Genome Biology*. Benchmarking computational methods for single-cell chromatin data analysis.** A very useful scATAC benchmark paper for lecture two, especially because it challenges the idea that the most popular pipelines are always the strongest performers. **DOI:** 10.1186/s13059-024-03356-x.

- **Sundaram et al., 2024, *Science*. Single-cell chromatin accessibility reveals malignant regulatory programs in primary human cancers.** The cleanest recent cancer application paper for this module. It shows why malignant-state calling, subclone inference, healthy-reference comparison, and regulatory modeling belong in the same conversation. **DO

[Truncated here in intake file; see `deep-research-report.md` for full content.]

## Initial triage

- Strongest sections: strong single-cell/multiome module overview, recent must-read list with DOIs, method assumptions, tools/workflows, datasets/benchmarks, cancer case studies, lecture arc, and clear boundaries.
- Weak or missing areas: citation markers are ChatGPT Deep Research internal turn references and are not usable as final citations; cancer case-study details and recent/fast-moving methods need DOI/URL verification.
- Claims requiring validation: all must-read papers/resources, benchmark claims, HTAN/TISCH2 counts, cancer case-study claims, and emerging methods such as ChromatinHD/scooby/treeArches.
- Suggested source-priority level: high — this is core material for the single-cell/multimodal regulatory genomics module and should be validated before lecture-plan generation.

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
