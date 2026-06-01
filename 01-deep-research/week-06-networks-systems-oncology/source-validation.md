# Source Validation Log — Module 6 / Week 06 — Gene Regulation, Networks, and Systems Oncology

Raw Deep Research file: `deep-research-report.md`

Note: Dr. Liu labeled this as **Week 6**. In the course outline this corresponds directly to **Week 06 — Gene Regulation, Networks, and Systems Oncology**.

## Priority validation queue

| ID | Claim / Item | Source | DOI/URL | Status | Notes |
|---|---|---|---|---|---|
| S001 | GRN inference review across data modalities, model families, priors, and evaluation | Badia-I-Mompel et al. 2023, Nature Reviews Genetics | 10.1038/s41576-023-00618-5 | pending | Verify scope and use as module entry review. |
| S002 | Causal discovery review plus landmark Sachs signaling causal-structure study | Kelly et al. 2022; Sachs et al. 2005 Science | 10.1002/mgg3.2055; 10.1126/science.1105809 | pending | Verify causal assumptions and teaching framing. |
| S003 | ARACNe mutual-information network inference and data-processing-inequality pruning | Margolin et al. 2006, BMC Bioinformatics | 10.1186/1471-2105-7-S1-S7 | pending | Verify landmark status and cancer master-regulator link. |
| S004 | GENIE3 tree-ensemble GRN inference | Huynh-Thu et al. 2010, PLoS ONE | 10.1371/journal.pone.0012776 | pending | Verify target-wise supervised-learning framing. |
| S005 | SCENIC regulon workflow and pySCENIC scalable protocol | Aibar et al. 2017; pySCENIC protocol | 10.1038/nmeth.4463; DOI TBD | pending | Verify motif pruning, AUCell activity scoring, and implementation citation. |
| S006 | VIPER / protein activity inference from regulon targets at cancer scale | Alvarez et al. 2016, Nature Genetics | 10.1038/ng.3593 | pending | Verify latent regulator activity and master-regulator claims. |
| S007 | PROGENy pathway activity from perturbation-responsive downstream genes | Schubert et al. 2018, Nature Communications | 10.1038/s41467-017-02391-6 | pending | Verify footprint-based pathway activity framing. |
| S008 | CARNIVAL causal reasoning on signed directed prior networks | Liu et al. 2019, npj Systems Biology and Applications | 10.1038/s41540-019-0118-z | pending | Verify expression-footprint-to-causal-subnetwork framing. |
| S009 | COSMOS multi-omics causal reasoning integrating phosphoproteomics/transcriptomics/metabolomics | Dugourd et al. 2021, Molecular Systems Biology | 10.15252/msb.20209730 | pending | Verify mechanistic systems-oncology capstone use. |
| S010 | decoupleR and CollecTRI for activity inference and signed TF-target priors | Badia-i-Mompel et al. 2022; Müller-Dott et al. 2023 | 10.1093/bioadv/vbac016; 10.1093/nar/gkad841 | pending | Verify prior-resource and benchmarking claims. |
| S011 | GRN benchmark pair: Pratapa single-cell benchmark and CausalBench perturbational benchmark | Pratapa et al. 2020; Chevalley et al. 2025 | 10.1038/s41592-019-0690-6; 10.1038/s42003-025-07764-y | pending | Fast-moving benchmark claim; verify exact conclusions carefully. |
| S012 | Pan-cancer master regulators and TCGA oncogenic signaling pathways | Paull et al. 2021 Cell; Sanchez-Vega et al. 2018 Cell | 10.1016/j.cell.2020.11.045; 10.1016/j.cell.2018.03.035 | pending | Verify 407 regulators/24 blocks and >9,000 tumor pathway claims. |
| S013 | DepMap/CCLE and Chronos as dependency resources for network-state validation | DepMap/CCLE/Chronos docs and papers | DOI/URL TBD | pending | Current resource details should be verified live before final materials. |
| S014 | LINCS L1000 perturbation signatures and LINCS portal | LINCS resources | DOI/URL TBD | pending | Validate resource scope and current URLs. |
| S015 | Perturb-seq benchmark datasets: Replogle genome-scale CRISPRi and Norman combinatorial perturbations | Replogle et al.; Norman et al. | DOI TBD | pending | Verify cell counts and dataset descriptions. |
| S016 | Frangieh Perturb-CITE-seq melanoma immune-evasion dataset counts and CD58 finding | Frangieh et al. | DOI TBD | pending | Verify 218,331 cells / 23,712 genes and immune-evasion claims. |
| S017 | Prior-knowledge stack: OmniPath, DoRothEA, TRRUST v2, KnockTF 2.0, scGRN counts | Multiple resources | DOI/URL TBD | pending | Verify current counts for scGRN and resource status. |
| S018 | Melanoma plasticity/resistance case-study arc: Wouters, Pillai, Pozniak | Multiple papers | DOI TBD | pending | Need exact paper identities and claims. |
| S019 | scGeneRAI NSCLC patient-specific GRN application | scGeneRAI paper | DOI TBD | pending | Verify >15,000 cells / 10 NSCLC patients and claims. |
| S020 | Dynamic/perturbation-aware methods: SINGE, CellOracle, perturbation biology, transition landscapes | Multiple papers | DOI TBD | pending | Verify method scope and module boundaries. |

## Notes

- The original Deep Research output contained internal ChatGPT citation tokens; imported report/intake Markdown has been cleaned, and final materials still need real DOI/URL citations.
- Validation should replace those tokens with real DOI/URL citations and mark unsupported claims for revision.
- Keep module boundaries explicit: this week starts from processed matrices/states and focuses on system-level inference, not assay generation, single-cell preprocessing, or CRISPR screen execution.
