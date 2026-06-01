# Source Validation Log — Module 10 / Week 10 — Foundation Models for Biomedical and Cancer Data

Raw Deep Research file: `deep-research-report.md`

Note: Dr. Liu labeled this as **Week 10**. In the course outline this corresponds to **Week 10 — Foundation Models for Biomedical and Cancer Data**.

## Priority validation queue

| ID | Claim / Item | Source | DOI/URL | Status | Notes |
|---|---|---|---|---|---|
| S001 | Cancer-focused foundation-model overview and translational framing | Tsang et al. 2025, Annual Review of Biomedical Data Science | DOI/URL TBD | pending | Verify publication details and scope. |
| S002 | Critical review of EHR/clinical foundation-model evaluation limitations | Wornow et al. 2023, npj Digital Medicine | 10.1038/s41746-023-00879-8 | pending | Verify evaluation criteria and claims. |
| S003 | ESM-2 protein language model and atomic-level structure prediction scaling | Lin et al. 2023, Science | 10.1126/science.ade2574 | pending | Verify model/paper title and scaling claims. |
| S004 | ProteinGym benchmark for protein design and fitness prediction | Notin et al. 2023 | DOI/URL TBD | pending | Verify benchmark scope and citation details. |
| S005 | Nucleotide Transformer model sizes, pretraining data, and downstream genomics evaluation | Dalla-Torre et al. 2025, Nature Methods | 10.1038/s41592-024-02523-z | pending | Verify 50M–2.5B parameters, 3,202 genomes, 850 species. |
| S006 | Geneformer transfer learning for network biology | Theodoris et al. 2023, Nature | 10.1038/s41586-023-06139-9 | pending | Verify contextual gene-embedding framing. |
| S007 | scGPT single-cell multi-omics foundation model | Cui et al. 2024, Nature Methods | 10.1038/s41592-024-02201-0 | pending | Verify generative pretraining and downstream claims. |
| S008 | Zero-shot limitations of single-cell foundation models | Kedzierska et al. 2025, Genome Biology | 10.1186/s13059-025-03574-x | pending | Verify conclusions and baseline comparisons. |
| S009 | UNI pathology foundation model | Chen et al. 2024, Nature Medicine | 10.1038/s41591-024-02857-3 | pending | Verify frozen-embedding reuse and broad downstream claims. |
| S010 | Virchow clinical-grade pathology foundation model and rare-cancer detection | Vorontsov et al. 2024, Nature Medicine | 10.1038/s41591-024-03141-0 | pending | Verify pan-cancer/rare-cancer performance claims. |
| S011 | Benchmarking pathology foundation models as feature extractors | Neidlinger et al. 2025, Nature Biomedical Engineering | 10.1038/s41551-025-01516-3 | pending | Verify 19 FMs, 13 cohorts, external testing, diversity > volume claim. |
| S012 | EHRSHOT few-shot benchmark and CLMBR-T-base | Wornow et al. 2023 | 10.52202/075280-2933 | pending | Verify benchmark tasks and structured EHR model claims. |
| S013 | Biological sequence FMs: ProtTrans, DNABERT, DNABERT-2, HyenaDNA, RNA-FM, ERNIE-RNA | Multiple papers | DOI/URL TBD | pending | Validate tokenization/objective/context-length claims. |
| S014 | Single-cell FMs/tools: scFoundation, SCimilarity, Nicheformer, BioLLM, CZI Virtual Cells Platform | Multiple papers/resources | DOI/URL TBD | pending | Current; verify names, availability, and claims. |
| S015 | Pathology/image FMs: CHIEF, Prov-GigaPath, CONCH, TITAN, Virchow, UNI | Multiple papers | DOI/URL TBD | pending | Validate design distinctions and external benchmark results. |
| S016 | Clinical text/structured EHR models: ClinicalBERT, GatorTron, BEHRT, Med-BERT, CLMBR | Multiple papers | DOI/URL TBD | pending | Validate input modalities and transfer/continued pretraining claims. |
| S017 | Cross-modal adaptation methods: frozen linear probes, full fine-tuning, continued pretraining, LoRA/adapters | Methods papers/resources | DOI/URL TBD | pending | General methods; cite selectively if needed. |
| S018 | Datasets/benchmarks: CELLxGENE, CELLxGENE Census, HCA, MIMIC-IV, eMERGE, TCGA, CPTAC, CDSA, PANDA, ClinVar, GUE | Resource docs/papers | DOI/URL TBD | pending | Verify current names and scope. |
| S019 | Single-cell perturbation benchmarks/resources: scDrugMap, PerturBench, 2025–2026 perturbation benchmark studies | Multiple papers/resources | DOI/URL TBD | pending | Fast-moving; verify evaluation-regime claims. |
| S020 | Oncology case-study performance claims: Virchow ~0.95 specimen AUC; CHIEF 60k WSIs/19 sites/19.5k validation/24 cohorts | Virchow; CHIEF | DOI/URL TBD | pending | Validate numbers before final teaching materials. |
| S021 | Cancer imaging biomarker foundation model by Pai et al. | Pai et al. 2024, Nature Machine Intelligence | 10.1038/s42256-024-00807-9 | pending | Verify 11,467 lesions and task-transfer claim. |
| S022 | Clinical oncology note/EHR abstraction examples: symptom detection and PD-L1 extraction, zero-shot limitations | Multiple papers | DOI TBD | pending | Identify exact papers and validate claims. |

## Notes

- The original Deep Research output contained internal ChatGPT citation tokens; imported report/intake Markdown has been cleaned, but final materials still need real DOI/URL citations.
- Validation should prioritize fast-moving 2024–2026 model and benchmark claims before lecture-plan generation.
- Keep boundaries explicit: this week is about pretrained representation learning and evaluation, not RAG, agents, prompt engineering, copilots, or general LLM workflow automation.
