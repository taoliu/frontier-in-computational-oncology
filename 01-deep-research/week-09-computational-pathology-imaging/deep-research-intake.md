# Week 09 — Computational Pathology and Cancer Imaging — Deep Research Intake

## Source

- Deep Research doc/link: Private Deep Research attachment (not public)
- Date received: 2026-05-31
- Imported by: Claw

## Raw content

Raw file stored at `deep-research-report.md`.

## Raw content excerpt

# Frontier in Computational Oncology Week 9 Computational Pathology and Cancer Imaging

## Module overview

This module tells a coherent story from digitized tissue images to morphology-derived cancer phenotypes. Its core data modality is the whole-slide image: a multi-resolution, gigapixel tissue representation whose computational structure is very different from a gene-expression matrix. A representative slide scanned at 0.25 μm/pixel can be about 80,000 × 60,000 pixels and ~15 GB uncompressed, which forces algorithm designers to make explicit choices about microns-per-pixel, tiling, context windows, aggregation, storage formats, and visualization. In oncology, this matters because morphology remains central to diagnosis, grading, staging support, prognostication, biomarker quantification, and increasingly to predicting molecular alterations and treatment response directly from H&E, IHC, and multiplex tissue images. The key unmet computational challenges are annotation scarcity, noisy slide-level labels, stain and scanner variation, multiple-instance learning over variable-length bags of tiles, multi-scale representation learning, and the mismatch between excellent retrospective performance and the much harder problem of external, clinical, and regulatory validation. This week should therefore teach not “how to run a pathology model,” but how to formulate, build, benchmark, and validate image-native methods that can turn raw morphology into robust cancer phenotypes.

## Must-read papers and resources

- **Song, Jaume, Williamson, Lu, Vaidya, Miller, Mahmood, 2023, *Nature Reviews Bioengineering*** — likely the best single technical review to assign at the start of the week. It organizes computational pathology by task class, data regime, and deployment challenge, and is especially good for motivating why pathology images are not just another computer-vision benchmark. DOI: **10.1038/s44222-023-00096-8**.

- **Aggarwal, Bharadwaj, Corredor, Pathak, Badve, Madabhushi, 2025, *Nature Reviews Clinical Oncology*** — a valuable “reality check” on what has and has not translated clinically, with attention to validation, regulation, implementation, and economics. It is an excellent capstone reading for the third lecture. DOI: **10.1038/s41571-025-00991-6**.

- **Campanella et al., 2019, *Nature Medicine*** — landmark weak-supervision paper showing that slide-level labels from routine diagnoses can train clinically strong models without dense manual annotation. It is still the canonical entry point for why multiple-instance learning matters in pathology. DOI: **10.1038/s41591-019-0508-1**.

- **Lu et al., 2021, *Nature Biomedical Engineering*** — the CLAM paper. Essential for teaching attention-based MIL, instance-level clustering, data efficiency, and interpretable region discovery under slide-level supervision. DOI: **10.1038/s41551-020-00682-w**.

- **Graham et al., 2019, *Medical Image Analysis*** — HoVer-Net remains a foundational segmentation paper for nuclei instance segmentation plus cell-type classification, and a good bridge between classical segmentation losses and pathology-specific instance reasoning. DOI: **10.1016/j.media.2019.101563**.

- **Bulten et al., 2022, *Nature Medicine*** — the PANDA challenge paper. Essential for benchmarking, reproducibility, and the problem of grading prostate biopsies at international scale. DOI: **10.1038/s41591-021-01620-2**.

- **Coudray et al., 2018, *Nature Medicine*** — the landmark lung cancer paper showing subtype classification and mutation prediction from H&E. Still one of the clearest demonstrations of image–molecular association from routine histology. DOI: **10.1038/s41591-018-0177-5**.

- **Kather et al., 2019, *Nature Medicine*** — the canonical MSI-from-histology paper in gastrointestinal cancer, and one of the cleanest examples of turning routine slides into a screening biomarker for a therapeutically actionable molecular phenotype. DOI: **10.1038/s41591-019-0462-y**.

- **Diao et al., 2021, *Nature Communications*** — important because it tackles interpretability directly through human-interpretable image features rather than only heatmaps, linking morphology and tumor microenvironment structure to molecular phenotypes. DOI: **10.1038/s41467-021-21896-9**.

- **Chen et al., 2024, *Nature Medicine*** — UNI is the clearest entry point into pathology self-supervised learning as an image-specific phenomenon: very large unlabeled WSI corpora, in-domain pretraining, and broad downstream transfer. DOI: **10.1038/s41591-024-02857-3**.

- **Xu et al., 2024, *Nature*** — Prov-GigaPath is important because it moves beyond tile encoders toward whole-slide foundation modeling and demonstrates very strong downstream performance across a broad pathology benchmark. DOI: **10.1038/s41586-024-07441-w**.

- **Neidlinger et al., 2025, *Nature Biomedical Engineering*** — one of the most important recent benchmark papers. It evaluates 19 pathology foundation models on 31 weakly supervised tasks using external cohorts not used for pretraining, making it ideal for teaching the difference between headline accuracy and trustworthy benchmarking. DOI: **10.1038/s41551-025-01516-3**.


[Truncated here in intake file; see `deep-research-report.md` for full content.]

## Initial triage

- Strongest sections: strong image-native framing centered on whole-slide images, tiling, microns-per-pixel, weak slide-level labels, multiple-instance learning, stain/scanner variation, multi-scale representation learning, pathology foundation models, and external/clinical validation.
- Weak or missing areas: citation markers are ChatGPT Deep Research internal turn references and must be replaced with real DOI/URL citations; several foundation-model, product-evidence, and benchmark claims are current/fast-moving and require live verification before lecture-plan generation.
- Claims requiring validation: all must-read papers/resources and DOIs; WSI scale/example size; foundation-model claims for UNI, Prov-GigaPath, CONCH, TITAN, Virchow, CHIEF; benchmark claims for Neidlinger 2025, CAMELYON, PANDA, MoNuSeg/MoNuSAC/CoNIC/NuCLS/MIDOG/TissueNet; product/regulatory evidence claims; NCI 2024 workshop report; commercial pathology AI evidence claims.
- Suggested source-priority level: high — this is a fast-moving imaging/foundation-model module with multiple mutable validation and product-evidence claims.

## Extraction checklist

- [ ] Landmark papers
- [ ] Recent reviews/guidelines
- [ ] Current methods/tools
- [ ] Datasets/benchmarks
- [ ] Cancer case studies
- [ ] Figures/assets to recreate or cite
- [ ] Open problems
- [ ] Lecture 1 material
- [ ] Lecture 2 material
- [ ] Lecture 3 material
