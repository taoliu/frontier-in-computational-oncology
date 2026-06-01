# Source Validation Log — Module 9 / Week 09 — Computational Pathology and Cancer Imaging

Raw Deep Research file: `deep-research-report.md`

Note: Dr. Liu labeled this as **Week 9**. In the course outline this corresponds to **Week 09 — Computational Pathology and Cancer Imaging**.

## Priority validation queue

| ID | Claim / Item | Source | DOI/URL | Status | Notes |
|---|---|---|---|---|---|
| S001 | Computational pathology technical review by task class, data regime, and deployment challenge | Song et al. 2023, Nature Reviews Bioengineering | 10.1038/s44222-023-00096-8 | pending | Verify title, author list, and scope. |
| S002 | Clinical translation/reality-check review for pathology AI validation, regulation, implementation, economics | Aggarwal et al. 2025, Nature Reviews Clinical Oncology | 10.1038/s41571-025-00991-6 | pending | Current; verify publication details and claims. |
| S003 | Weak supervision from slide-level labels for pathology models | Campanella et al. 2019, Nature Medicine | 10.1038/s41591-019-0508-1 | pending | Verify canonical weak-supervision/MIL framing. |
| S004 | CLAM attention-based MIL with instance clustering and interpretable regions | Lu et al. 2021, Nature Biomedical Engineering | 10.1038/s41551-020-00682-w | pending | Verify method details. |
| S005 | HoVer-Net nuclei instance segmentation and classification | Graham et al. 2019, Medical Image Analysis | 10.1016/j.media.2019.101563 | pending | Verify segmentation/cell-type framing. |
| S006 | PANDA prostate grading challenge | Bulten et al. 2022, Nature Medicine | 10.1038/s41591-021-01620-2 | pending | Verify benchmark and international grading claims. |
| S007 | Lung cancer subtype and mutation prediction from H&E | Coudray et al. 2018, Nature Medicine | 10.1038/s41591-018-0177-5 | pending | Verify subtype/mutation prediction claims. |
| S008 | MSI prediction from gastrointestinal histology | Kather et al. 2019, Nature Medicine | 10.1038/s41591-019-0462-y | pending | Verify biomarker-screening framing. |
| S009 | Interpretable image features linked to molecular/TME phenotypes | Diao et al. 2021, Nature Communications | 10.1038/s41467-021-21896-9 | pending | Verify human-interpretable feature claims. |
| S010 | UNI pathology self-supervised learning foundation model | Chen et al. 2024, Nature Medicine | 10.1038/s41591-024-02857-3 | pending | Verify corpus, model claims, and downstream transfer. |
| S011 | Prov-GigaPath whole-slide foundation modeling | Xu et al. 2024, Nature | 10.1038/s41586-024-07441-w | pending | Verify whole-slide modeling and benchmark claims. |
| S012 | External benchmark of 19 pathology foundation models on 31 weakly supervised tasks | Neidlinger et al. 2025, Nature Biomedical Engineering | 10.1038/s41551-025-01516-3 | pending | Current; verify exact model/task counts and conclusions. |
| S013 | WSI scale/format claims: 0.25 μm/pixel, 80k×60k, ~15GB uncompressed, DICOM-WSI/vendor formats | Reviews/standards | DOI/URL TBD | pending | Validate representative example and avoid overgeneralizing. |
| S014 | Stain normalization/domain generalization: Macenko, recent reviews, no universal recipe | Multiple papers | DOI/URL TBD | pending | Verify classic method and recent survey conclusions. |
| S015 | MIL and spatial/transformer variants: attention MIL, TransMIL, Patch-GCN, survival heads | Multiple papers | DOI/URL TBD | pending | Validate method distinctions and assumptions. |
| S016 | Infrastructure tools: TIAToolbox, Slideflow, PathML, QuPath | Tool docs/papers | DOI/URL TBD | pending | Verify current names, capabilities, and citation details. |
| S017 | Segmentation lineage: U-Net, HoVer-Net, Mesmer/TissueNet; segmentation metrics Dice/AJI/PQ/F1 | Multiple papers/resources | DOI/URL TBD | pending | Validate method roles and benchmark pair. |
| S018 | Pathology representation/foundation models: HIPT, UNI, CONCH, TITAN, Virchow, Prov-GigaPath, CHIEF | Multiple papers | DOI/URL TBD | pending | Current; verify exact claims and avoid broad foundation-model theory. |
| S019 | Public datasets/benchmarks: TCGA, CDSA, TCIA, CPTAC, CAMELYON16/17, PANDA, MoNuSeg, MoNuSAC, CoNIC, NuCLS, MIDOG, TissueNet, BigPicture | Multiple resources | DOI/URL TBD | pending | Verify current dataset/resource claims and task definitions. |
| S020 | Validation/reporting frameworks: TRIPOD+AI, SPIRIT-AI, CONSORT-AI, NCI 2024 workshop report | Guidelines/reports | DOI/URL TBD | pending | Validate scope for pathology AI studies/trials. |
| S021 | Clinical/product evidence: commercial pathology AI products, FDA AI-enabled device list, Europe/GB approvals | Reviews/regulatory pages | DOI/URL TBD | pending | Mutable; verify live before final materials. |
| S022 | Cancer case-study claims: breast/CAMELYON, colorectal MSI/multistain biomarkers, lung image-genomics, IHC H-score quantification, CoNIC immune-cell morphometrics | Multiple papers | DOI/URL TBD | pending | Identify exact papers and validate claims. |

## Notes

- The original Deep Research output contained internal ChatGPT citation tokens; imported report/intake Markdown has been cleaned, but final materials still need real DOI/URL citations.
- Validation should prioritize foundation-model and external-validation claims before lecture-plan generation.
- Keep boundaries explicit: spatial omics molecular neighborhood analysis belongs to Week 4; clinical EHR/outcome modeling belongs to Week 8; general foundation-model theory belongs to Week 10.
