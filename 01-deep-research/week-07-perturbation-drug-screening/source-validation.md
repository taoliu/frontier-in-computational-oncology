# Source Validation Log — Module 7 / Week 07 — Drug Screening, Perturbation Modeling, and Virtual Cell Models

Raw Deep Research file: `deep-research-report.md`

Note: Dr. Liu labeled this as **Week 7**. In the course outline this corresponds to a perturbation-driven module covering drug screening, CRISPR/RNAi screens, Perturb-seq, and virtual-cell/virtual-perturbation modeling.

## Priority validation queue

| ID | Claim / Item | Source | DOI/URL | Status | Notes |
|---|---|---|---|---|---|
| S001 | High-content CRISPR screening primer; pooled vs high-content phenotypes and computational design implications | Bock et al. 2022, Nature Reviews Methods Primers | 10.1038/s43586-021-00093-4 | pending | Verify title, year, DOI, and scope. |
| S002 | Benchmark of pooled CRISPR screen analysis algorithms | Bodapati et al. 2020, Genome Biology | 10.1186/s13059-020-01972-x | pending | Verify algorithm families and benchmark conclusions. |
| S003 | CRISPR-Cas9 bias-correction benchmark covering copy-number and proximity biases | Vinceti et al. 2024, Genome Biology | 10.1186/s13059-024-03336-1 | pending | Verify bias types and current conclusions. |
| S004 | Cancer Dependency Map current/future perspective | Arafeh et al. 2025, Nature Reviews Cancer | 10.1038/s41568-024-00763-x | pending | Fast-moving; verify exact Phase/next-generation claims. |
| S005 | Clinically informed pan-cancer dependency map across 930 cancer cell lines | Pacini et al. 2024, Cancer Cell | DOI TBD | pending | Verify title, counts, and target-prioritization framing. |
| S006 | PRISM pooled-cell-line pharmacologic screening and non-oncology drug repurposing resource | Corsello et al. 2020 | DOI TBD | pending | Verify compound and cell-line counts. |
| S007 | LINCS/CMap L1000 landmark perturbational-transcriptomics resource | Subramanian et al. 2017, Cell | 10.1016/j.cell.2017.10.049 | pending | Verify profile count and teaching framing. |
| S008 | Genome-scale Perturb-seq genotype–phenotype landscape | Replogle et al. 2022, Cell | DOI TBD | pending | Verify >2.5M cells and genome-scale claims. |
| S009 | Benchmarking generalizable single-cell perturbation response prediction | Wei et al. 2025, Nature Methods | 10.1038/s41592-025-02980-0 | pending | Current benchmark; verify conclusions and baselines. |
| S010 | MuSyC synergy framework distinguishing potency and efficacy synergy | Wooten et al. 2021, Nature Communications | 10.1038/s41467-021-24789-z | pending | Verify synergy-metric framing. |
| S011 | Virtual-cell AI review / conceptual framework | Bunne et al. 2024, Cell | 10.1016/j.cell.2024.11.015 | pending | Verify scope and avoid overclaiming solved capabilities. |
| S012 | Base-editing screens for cancer drug-resistance mechanisms | Coelho et al. 2024, Nature Genetics | 10.1038/s41588-024-01948-8 | pending | Verify targeted-agent count and cancer models. |
| S013 | CRISPR/RNAi analysis methods: MAGeCK, MAGeCK-VISPR, MAGeCKFlute, BAGEL/BAGEL2, CERES, Chronos, DEMETER2 | Multiple method papers | DOI/URL TBD | pending | Validate exact assumptions and tool roles. |
| S014 | Drug-gene interaction and synthetic-lethality modeling: DrugZ, Project DRIVE, SCHEMATIC, SL benchmarks | Multiple papers/resources | DOI/URL TBD | pending | Verify method/case-study claims and counts such as 1,805 interactions. |
| S015 | Dose–response metrics and models: Hill/4PL, IC50/AUC/AAC, GR, NDR, hierarchical Bayes, multi-output GP | Multiple papers | DOI/URL TBD | pending | Validate definitions and teaching distinctions. |
| S016 | Synergy metrics/tools: Bliss, Loewe, HSA, ZIP, MuSyC, SynergyFinder 3.0 | Multiple papers/tools | DOI/URL TBD | pending | Verify tool versions and consensus scoring claims. |
| S017 | Single-cell perturbation models/tools: scGen, CPA, GEARS, CellOT, pertpy, scPerturBench | Multiple papers/tools | DOI/URL TBD | pending | Current/fast-moving; verify generalization benchmark conclusions. |
| S018 | Public data stack: DepMap, CCLE, GDSC, CTRPv2, PRISM, PharmacoDB 2.0 | Multiple resources | DOI/URL TBD | pending | Verify current counts: cell lines, compounds, screens, integrated studies. |
| S019 | Perturbation databases/benchmarks: scPerturb, PerturbDB, scPerturBench | Multiple resources | DOI/URL TBD | pending | Verify dataset counts and current availability. |
| S020 | Melanoma Perturb-CITE-seq immune-evasion case and CD58 finding | Frangieh et al. and resources | DOI TBD | pending | Verify co-culture model, multimodal readouts, and B2M/HLA contrast. |
| S021 | CRISPR–drug combination maps and targeted-therapy combination studies | Lee et al.; Tiedt et al. | DOI TBD | pending | Identify exact papers and validate claims. |
| S022 | Patient-derived organoid pharmacotyping in pancreatic cancer and outcome association | PDO pharmacotyping papers | DOI TBD | pending | Verify clinical outcome claims and limitations. |

## Notes

- The original Deep Research output contained internal ChatGPT citation tokens; imported report/intake Markdown has been cleaned, but final materials still need real DOI/URL citations.
- Validation should prioritize fast-moving 2024–2025 papers/resources before generating slide text or scripts.
- Keep the module boundary explicit: this week is about learning causal response structure from experimental perturbations, not general network inference or patient-level digital twins.
