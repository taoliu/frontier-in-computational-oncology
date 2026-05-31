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

- **Sundaram et al., 2024, *Science*. Single-cell chromatin accessibility reveals malignant regulatory programs in primary human cancers.** The cleanest recent cancer application paper for this module. It shows why malignant-state calling, subclone inference, healthy-reference comparison, and regulatory modeling belong in the same conversation. **DOI:** 10.1126/science.adk9217.

## Computational problems and methods

### Key computational problems and assumptions

- **Cancer cell states are partly biological and partly algorithmic objects.** Tumors contain discrete lineages, continuous programs, patient-specific effects, and mixed malignant and non-malignant ecosystems. Pan-cancer single-cell studies have identified recurrent malignant programs, but recent syntheses emphasize that state naming and separation remain ambiguous, especially when cells sit on continua rather than clean clusters.

- **scRNA-seq modeling should start from count-aware measurement models.** Regularized negative binomial regression remains a strong teaching example because it directly models UMI counts and variance stabilization. At the same time, work separating measurement and expression models argues that UMI measurement is generally not itself zero-inflated, even though both technical and biological zeros are common in practice. This is why indiscriminate imputation should be treated cautiously and as a modeling choice, not a default cleaning step.

- **scATAC-seq feature engineering is a core statistical choice, not just preprocessing.** Accessibility can be summarized on called peaks, genomic windows, cCRE lists, motifs, TSS-centered features, or gene activity matrices. Recent integration benchmarks found that peaks and windows are more informative than gene activity alone for scATAC tasks, and a 2024 benchmark found feature aggregation and SnapATAC-style approaches often outperform classic LSI-based pipelines for clustering and state recovery, even though LSI remains embedded in widely used frameworks such as Signac and ArchR.

- **Cross-modality integration depends on what kind of supervision is available.** WNN assumes paired measurements and learns per-cell modality weights; bridge integration assumes access to an informative multiome bridge; GLUE assumes a useful cross-omic prior graph; scJoint assumes transfer learning can align RNA and ATAC in a shared embedding; LIGER assumes shared and dataset-specific factors can be separated. Benchmarks consistently show there is no universal winner, and the best method depends on whether the task favors batch removal, biological conservation, scale, or handling of unpaired data.

- **Malignant versus non-malignant calling often rests on imperfect genomic surrogates.** A recent review on cancer-cell identification in single-cell data points to three common signals: cell-of-origin markers, inter-patient malignant heterogeneity, and inferred copy-number alterations. CopyKAT and SCEVAN are useful exemplars, but comparison studies show that performance depends strongly on the presence of broad CNAs, reference quality, and platform-specific noise. Near-diploid tumors remain especially difficult.

- **Validation must be matched to the inference target.** Paired multiome gives same-cell cross-modality ground truth for alignment. Controlled cancer cell-line mixtures help validate clustering and annotation. For regulatory inference, the most convincing evidence comes from orthogonal perturbation or functional follow-up, not from co-accessibility alone. That distinction is worth making explicit in lecture two.

### Main algorithms, models, and tools to teach

- **Seurat, Signac, and Azimuth in the R ecosystem.** Seurat is the natural entry point for anchor-based mapping, WNN, and bridge integration; Signac extends this into scATAC and multiome workflows with TF-IDF/LSI, motif analysis, peak-gene linking, and joint RNA-ATAC tutorials; Azimuth shows how reference mapping works in practice for both scRNA and scATAC. Together they make an excellent teaching stack for paired data and reference-based annotation.

- **Scanpy and the broader scverse ecosystem in Python.** Scanpy provides scalable preprocessing, clustering, visualization, trajectory analysis, and differential testing around the AnnData object, and it is the cleanest Python point of entry for graduate students. From there, epiScanpy extends similar ideas to scATAC and single-cell methylation, CellTypist provides practical automated annotation, BBKNN and Harmony illustrate graph-based and embedding-based batch correction, and scVI-tools introduces probabilistic latent-variable modeling for very large cohorts.

- **ArchR and MAESTRO as workflow-first teaching systems.** ArchR is especially good for iterative LSI, doublet handling, gene score calculation, peak-to-gene links, chromVAR deviations, footprinting, trajectories, and scale. MAESTRO is useful because it exposes workflow engineering from FASTQ to interpretation, including cell-type annotation and TF analysis, making it ideal for assignments on reproducibility and implementation choices.

- **Cross-modality alignment methods outside the main analysis suites.** GLUE, scJoint, and LIGER are worth teaching side by side because they embody different views of “shared cell state”: graph-linked integration, transfer-learning-based alignment, and factorization into shared versus dataset-specific components. That comparison helps students see that integration is a modeling problem rather than a generic preprocessing step.

- **Regulatory inference methods should be taught as a ladder of assumptions.** chromVAR estimates motif deviation scores from sparse accessibility profiles; SCENIC infers regulons from expression; ArchR, Signac, and Cicero-style methods use co-accessibility or peak-gene association; SCARlink moves closer to explicit predictive modeling by fitting gene-level regression models on local accessibility tiles. Framing these methods by what they assume about causality, locality, sparsity, and TF binding makes the lecture stronger than a tool-by-tool tour.

- **Trajectory and dynamics methods should be compared, not taught in isolation.** Slingshot, Monocle-style graph learning, diffusion-based pseudotime, and scVelo each solve different parts of the “state transition” problem and each depend on topology assumptions. The classic trajectory benchmark remains useful because it forces students to ask what kind of trajectory structure is being assumed and how one would know it is correct.

- **Cancer-specific state calling should be explicit in the workflow.** inferCNV, CopyKAT, and SCEVAN are important not because they are perfect, but because they show how cancer analysis usually inserts a malignant-calling layer before clustering malignant states, building trajectories, or inferring resistance programs. This is a distinctive oncology-specific teaching point that should not be hidden inside “QC.”

## Datasets and case studies

### Representative datasets and benchmarks

- **10x PBMC multiome datasets.** These are still the cleanest teaching datasets for paired RNA+ATAC because they are public, well documented, and supported across Cell Ranger ARC, Seurat/Signac, and many tutorials. They are best for teaching joint embeddings, label transfer, peak-gene linking, and motif activity before moving into cancer.

- **Bone marrow multiome benchmark from the 2021 NeurIPS challenge.** The GSE194122 BMMC dataset includes 12 healthy donors, nested batch structure across sites, and paired modalities designed for modality prediction, matching, and joint embedding. It is especially useful for showing students what real benchmark design looks like when same-cell pairing is available.

- **Open Problems benchmarks.** Open Problems is now a living benchmark platform for single-cell tasks, including multimodal alignment and batch integration. It is valuable not only as a benchmark source, but also as a teaching aid for how evaluation metrics are formalized and why method rankings depend on the task definition.

- **Controlled lung cancer heterogeneity benchmark.** A 2024 *Scientific Data* study created a 10x scRNA-seq benchmark from lung cancer cell lines carrying different driver alterations, providing a controlled setting to validate clustering, annotation, and heterogeneity methods in an oncology-relevant context. This is a good “middle step” between clean PBMC data and messy patient tumors.

- **Tumor atlas resources for projects and reproducibility.** HTAN provides multi-omic tumor atlases across many tumor sites and biospecimens, including sc/snRNA-seq and scATAC-seq data. TISCH2 remains one of the easiest curated scRNA tumor microenvironment portals for homework and project design, and as of the current site it reports 190 datasets and more than 6.2 million cells.

### Cancer case studies

- **Pan-cancer malignant regulatory programs from scATAC.** Sundaram et al. profiled single-cell chromatin accessibility across eight tumor types and showed that copy-number alterations strongly shape accessibility patterns, enough to identify subclones, while underlying cis-regulatory landscapes still retain cancer-type-specific signals. They also used healthy references to identify nearest healthy counterparts and showed that regulatory models can prioritize functional noncoding mutations near cancer genes. This is the best recent anchor paper for the “malignant state plus regulatory program” story.

- **Melanoma plasticity and immunotherapy resistance.** A 2024 *Cell* paper identified a TCF4-dependent gene regulatory network associated with a mesenchymal-like melanoma state and resistance to immunotherapy. This case study is especially useful because melanoma already has a strong single-cell state literature, so students can connect state plasticity, TF programs, and treatment response within one disease.

- **Breast cancer subtype lineages from paired RNA and chromatin.** In 2024, paired transcription and chromatin-accessibility profiling linked basal-like breast cancers to luminal progenitor-like regulatory programs and luminal tumors to luminal mature-like programs, while also showing enrichment of exhausted CTLA4-expressing CD8 T cells in basal-like disease. This is a strong example of how state inference can bridge malignant lineage questions and immune-state inference in the same dataset.

- **Endocrine resistance in breast cancer.** Integrated scRNA-seq and scATAC-seq analysis of tamoxifen-resistant breast cancer identified resistant cancer-cell states, a 137-gene heterogeneity-guided core signature, enrichment of ESR1, FOXA1, and FOS-family motifs, and experimental support for BMP7 as a resistance factor. This paper is ideal for teaching how computational discovery should be followed by functional verification.

- **Subtype-defining epigenetics and plasticity models beyond breast cancer.** Single-cell chromatin accessibility in colorectal cancer revealed the epigenetic basis and signature transcription factors for major molecular subtypes, including CIMP-related patterns. Separately, multiome work in hepatoblastoma and across cancer cell lines showed how clonal evolution, epigenetic plasticity, ecDNA, stress, and CNV can reshape cell states and therapy response. These are good examples for discussing tumor evolution and resistance programs without relying only on immune-state stories.

## Suggested lecture arc

- **Lecture on background and problem definition.** Start from why cancer requires single-cell resolution: mixed malignant and non-malignant ecosystems, recurrent yet plastic malignant programs, and the fact that transcriptional state and regulatory state are related but not identical. Introduce the assays, the structure of count matrices, and the main statistical difficulties: overdispersion, zeros, extreme sparsity, feature-definition dependence, batch effects, and the difference between same-cell multiome and unpaired integration. Assigned reading should prioritize Heumos et al., Yang et al., and the Tirosh perspective, with a short data walk-through using PBMC multiome and one cancer atlas example.

- **Lecture on method development and verification.** Organize this lecture by inference target rather than by software package: normalization and latent spaces for scRNA; TF-IDF/LSI and feature construction for scATAC; cross-modality integration with WNN, bridge integration, GLUE, scJoint, and LIGER; cell annotation and malignant-cell calling; trajectory and dynamics; and motif or enhancer-gene regulatory inference. Spend explicit time on assumptions, failure modes, and validation design using paired multiome ground truth, benchmark datasets, controlled cancer mixtures, and functional follow-up. The core readings should be Hao 2021, Hao 2023, ArchR, GLUE, Luecken 2022, Luo 2024, and SCARlink.

- **Lecture on application and state of the field.** Use four disease stories: pan-cancer malignant regulatory programs, melanoma resistance states, breast subtype lineage and endocrine resistance, and one additional disease-specific example such as colorectal subtype epigenetics. End with practical resources such as HTAN and TISCH2, then discuss what current tools still cannot do well: unseen disease states, weakly causal enhancer-gene links, fragile malignancy calls in near-diploid tumors, and conservative versus aggressive batch correction in multicenter cohorts.

## Open problems and boundaries

### Open problems and future directions

- **Regulatory causality is still the weak point.** Most current enhancer-gene links remain correlative, local, and highly dependent on feature construction. SCARlink improves on pairwise peak-gene correlations, and newer approaches such as ChromatinHD and sequence-to-function models like scooby point toward stronger multiscale modeling, but causal validation is still the bottleneck.

- **Reference mapping is fragile when disease states are missing from the reference.** Healthy-cell atlases help, but tumors often contain novel malignant or treatment-induced states that should not be forced into healthy ontologies. Methods such as treeArches directly recognize the unseen-state problem, and this is especially relevant for oncology where “unknown” is often the important result.

- **Malignancy inference needs to move beyond broad CNAs alone.** CNV-based methods work best in aneuploid tumors and can degrade badly in near-diploid disease, with weak normal references, or across platforms. Near-future work is likely to combine CNAs with SNVs, fusions, accessibility, and learned tumor-specific signatures.

- **Benchmarks are improving faster than ground truth.** Open Problems and recent multimodal benchmarks are making evaluation more formal, but cancer-specific benchmarks with paired modalities, known clonal truth, and functional validation are still uncommon. This means method papers can still look stronger than they really are when ported into tumors.

- **Perturbational and lineage-aware multiome will likely reshape the field.** Emerging studies combining lineage tracing with multiome and large-scale perturbational multimodal assays suggest that the next wave of methods will estimate not only state and regulation, but also state transition competence and causal regulatory control. That direction matters for cancer resistance and relapse.

### Notes on boundaries

What belongs in this module is single-cell resolution state discovery and regulatory inference without explicit spatial coordinates. That includes scRNA-seq, scATAC-seq, paired multiome, label transfer, batch correction, trajectory inference, motif and enhancer-gene inference, malignant versus non-malignant calling, and cancer-state applications such as tumor evolution, immune states, and resistance programs.

What should be left to other weeks is equally important. Spatial neighborhood structure, tissue architecture, and coordinate-aware models belong to the later spatial module, even if a few papers in this week use spatial data only as orthogonal validation. Bulk peak calling, bulk motif enrichment strategy, and bulk regulatory genomics standards belong to the earlier bulk-regulatory week. General foundation models, broad LLM-based analysis agents, and “omics foundation model” surveys should be saved for the later foundations week, although it is reasonable in this module to briefly mention single-cell sequence-to-function or multiome foundation-style models as emerging directions.