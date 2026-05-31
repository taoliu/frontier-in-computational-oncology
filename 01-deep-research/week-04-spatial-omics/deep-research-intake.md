# Week 04 — Spatial Omics of the Tumor Microenvironment — Deep Research Intake

## Source

- Deep Research doc/link: Private Deep Research attachment (not public)
- Date received: 2026-05-31
- Imported by: Claw

## Raw content

Raw file stored at `deep-research-report.md`.

## Raw content excerpt

# Spatial Omics of the Tumor Microenvironment

## Module overview

This module should tell a clear methodological story: dissociated single-cell atlases explain *who* is present in tumors, but spatial omics is needed to explain *where* cells, states, and signals are organized, and how that organization shapes invasion, immune exclusion, stromal barriers, hypoxia, and therapy response. Compared with dissociated single-cell assays, spatial molecular profiling introduces new computational problems tied to assay physics and geometry: mixed spots in sequencing-based assays, sparse molecule counts at very high resolution, cell segmentation and transcript-to-cell assignment in imaging assays, registration across serial sections, reference-based deconvolution, spatial statistics, neighborhood and niche detection, and cell-cell communication constrained by distance and tissue architecture. Across transcriptomics, proteomics, and emerging spatial epigenomics, the main teaching goal is not tool operation but model design: which assumptions are imposed by each assay, how those assumptions enter algorithms, and how one can verify that inferred spatial biology is real rather than an artifact of resolution, panel design, segmentation, or reference mismatch.

## Must-read papers and resources

- **Elhanani, Ben-Uri, Keren. *Spatial profiling technologies illuminate the tumor microenvironment*. Cancer Cell, 2023. DOI: 10.1016/j.ccell.2023.01.010.** A strong entry-point review for the oncology framing of spatial technologies, what types of biological questions they answer, and where the field was heading in cancer by 2023.

- **You et al. *Systematic comparison of sequencing-based spatial transcriptomic methods*. Nature Methods, 2024. DOI: 10.1038/s41592-024-02325-3.** Essential for teaching assay tradeoffs. It benchmarked 11 sequencing-based methods across 35 experiments from three reference tissues and showed that effective resolution depends not only on feature size but also on diffusion and capture behavior.

- **Wang et al. *Systematic benchmarking of imaging spatial transcriptomics platforms in FFPE tissues*. Nature Communications, 2025. DOI: 10.1038/s41467-025-64990-y.** A head-to-head comparison of Xenium, MERSCOPE, and CosMx on matched FFPE tissue microarrays, valuable for discussing sensitivity, specificity, concordance with orthogonal data, and platform choice in cancer studies.

- **Moncada et al. *Integrating microarray-based spatial transcriptomics and single-cell RNA-seq reveals tissue architecture in pancreatic ductal adenocarcinomas*. Nature Biotechnology, 2020. DOI: 10.1038/s41587-019-0392-8.** A landmark cancer paper for the “from dissociated cells back to tissue” narrative, and still a good teaching case for reference-guided deconvolution and spatial mapping in a stromal-rich tumor.

- **Cable et al. *Robust decomposition of cell type mixtures in spatial transcriptomics*. Nature Biotechnology, 2022. DOI: 10.1038/s41587-021-00830-w.** The canonical RCTD paper. A must-read for statistical modeling of spot mixtures, technology effects, and reference-based decomposition.

- **Kleshchevnikov et al. *cell2location maps fine-grained cell types in spatial transcriptomics*. Nature Biotechnology, 2022. DOI: 10.1038/s41587-021-01139-4.** A key Bayesian method paper for fine-grained abundance mapping that explicitly models technical variation and borrows strength across locations, widely used in tumor microenvironment studies.

- **Petukhov et al. *Cell segmentation in imaging-based spatial transcriptomics*. Nature Biotechnology, 2022. DOI: 10.1038/s41587-021-01044-w.** The Baysor paper. This is the right paper for teaching why segmentation is not a preprocessing footnote but a core inferential problem in imaging-based assays.

- **Singhal et al. *BANKSY unifies cell typing and tissue domain segmentation for scalable spatial omics data analysis*. Nature Genetics, 2024. DOI: 10.1038/s41588-024-01664-3.** Important for the current shift from “cell typing first, domains second” toward models that learn cell identity together with neighborhood context.

- **Varrone et al. *CellCharter reveals spatial cell niches associated with tissue remodeling and cell plasticity*. Nature Genetics, 2024. DOI: 10.1038/s41588-023-01588-4.** A leading computational paper for scalable niche discovery and cross-sample niche comparison, directly relevant to tumor-immune-stromal neighborhood analysis.

- **Cang et al. *Screening cell-cell communication in spatial transcriptomics via collective optimal transport*. Nature Methods, 2023. DOI: 10.1038/s41592-022-01728-4.** A strong methods paper for teaching how spatial constraints change ligand-receptor inference, especially under competition among ligands and receptors.

- **Keren et al. *A Structured Tumor-Immune Microenvironment in Triple Negative Breast Cancer Revealed by Multiplexed Ion Beam Imaging*. Cell, 2018. DOI: 10.1016/j.cell.2018.08.039.** Older than the preferred window, but still a landmark cancer application showing that spatial organization itself carries prognostic information beyond cell counts.

- **Schürch et al. *Coordinated Cellular Neighborhoods Orchestrate Antitumoral Immunity at the Colorectal Cancer Invasive Front*. Cell, 2020.** Another landmark application, foundational for the cellular-neighborhood concept in oncology and still highly teachable for neighborhood graphs and spatial ecosystems.


[Truncated here in intake file; see `deep-research-report.md` for full content.]

## Initial triage

- Strongest sections: strong methodological framing that spatial omics complements dissociated single-cell atlases by adding tissue geometry; clear separation of sequencing-based, imaging-based, proteomic, and emerging spatial epigenomic regimes; useful emphasis on deconvolution, segmentation, niche/domain detection, spatial statistics, cell-cell communication, registration, and benchmark instability.
- Weak or missing areas: citation markers are ChatGPT Deep Research internal turn references and are not usable as final citations; several fast-moving platform/resource claims need current verification, especially 2025 imaging benchmarks, HTAN release counts, Visium HD case studies, and spatial epigenomics claims.
- Claims requiring validation: all must-read papers/resources and DOIs; benchmark sizes and platform comparisons; HTAN counts and assay list; tumor case-study details; claims about best-performing methods in deconvolution/domain/registration benchmarks; boundaries versus Week 3 single-cell and Week 9 pathology imaging.
- Suggested source-priority level: high — this is a core spatial module with many platform-specific and fast-moving claims that should be validated before lecture-plan generation.

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
