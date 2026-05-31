# Source Validation Log — Module 5 / Week 05 — Somatic Mutation, Variant Interpretation, and Cancer Evolution

Raw Deep Research file: `deep-research-report.md`

Note: This module appears to correspond to **Week 05** in the prepared course repository: somatic mutation, variant interpretation, and cancer evolution.

## Priority validation queue

| ID | Claim / Item | Source | DOI/URL | Status | Notes |
|---|---|---|---|---|---|
| S001 | GATK Mutect2-era somatic short variant workflow: local assembly, contamination, orientation-bias learning/filtering | Broad GATK Somatic Short Variant Discovery docs; Cibulskis et al. 2013 | Docs URL TBD; 10.1038/nbt.2514 | pending | Verify current workflow date and exact steps before teaching as “current best practice.” |
| S002 | Strelka2 as high-performance somatic/germline SNV/indel caller | Kim et al. 2018, Nature Methods | 10.1038/s41592-018-0051-x | pending | Verify somatic design and benchmark context. |
| S003 | SEQC2 HCC1395/HCC1395BL truth sets and pipeline/purity/assay benchmarking | Fang et al. 2021; Xiao et al. 2021, Nature Biotechnology | 10.1038/s41587-021-00993-6; 10.1038/s41587-021-00994-5 | pending | Confirm reference materials, call-set scope, and teaching claims. |
| S004 | dNdScv / dN-dS positive-selection framework for somatic driver discovery | Martincorena et al. 2017, Cell | 10.1016/j.cell.2017.09.042 | pending | Verify method framing and background-rate corrections. |
| S005 | COSMIC mutational signatures v3.6 and Alexandrov SBS/DBS/ID catalog paper | Alexandrov et al. 2020, Nature; COSMIC signatures site | 10.1038/s41586-020-1943-3; URL TBD | pending | Verify current COSMIC version/classes at time of slide generation. |
| S006 | MuSiCal as newer signature discovery/assignment method and benchmark claim | Jin et al. 2024, Nature Genetics | 10.1038/s41588-024-01659-0 | pending | Verify claims comparing signature fitting tools. |
| S007 | HATCHet allele- and clone-specific copy-number inference with multi-sample deconvolution | Zaccaria & Raphael 2020, Nature Communications | 10.1038/s41467-020-17967-y | pending | Confirm purity/ploidy/WGD and MASCoTE validation framing. |
| S008 | PyClone-VI bulk clonal clustering from corrected cancer cell fractions | Gillis & Roth 2020, BMC Bioinformatics | 10.1186/s12859-020-03919-2 | pending | Verify input assumptions and practical teaching scope. |
| S009 | MEDICC2 copy-number phylogenies and WGD-aware modeling | Kaufmann et al. 2022, Genome Biology | 10.1186/s13059-022-02794-9 | pending | Verify haplotype-specific copy-number and WGD claims. |
| S010 | PCAWG ITH scale and findings: 2,658 WGS, 38 cancer types, branching subclones, driver timing/signature dynamics | Dentro et al. 2021, Cell | 10.1016/j.cell.2021.03.009 | pending | Verify numerical claims and exactly what was shown. |
| S011 | TRACERx lung evolution scale and WGD/outcome claims | Frankell et al. 2023, Nature | 10.1038/s41586-023-05783-5 | pending | Verify 1,644 regions/421 patients and WGD percentages. |
| S012 | ClinGen/CGC/VICC oncogenicity standards for somatic variant interpretation | Horak et al. 2022, Genetics in Medicine | 10.1016/j.gim.2022.01.001 | pending | Confirm terminology: oncogenicity vs actionability. |
| S013 | CancerVar AI/rule-based prioritization framework | Li et al. 2022, Science Advances | 10.1126/sciadv.abj1624 | pending | Verify method positioning and avoid overstating clinical utility. |
| S014 | GDC publishes multiple somatic mutation pipelines rather than one consensus | GDC documentation | URL TBD | pending | Verify currently active pipelines and wording. |
| S015 | TCGA MC3: ~10,000 samples, seven callers, ~3.5M variants | Ellrott et al. / MC3 PanCanAtlas resource | DOI/URL TBD | pending | Validate exact counts and caller list. |
| S016 | Hartwig Medical Database: metastatic WGS + clinical data, >8,000 patients | Hartwig docs; metastatic pan-cancer papers | URLs/DOIs TBD | pending | Verify current sample count and access details. |
| S017 | COLO829/COLO829BL SV benchmark: curated 68 somatic SVs and purity/depth evaluation | 2022 COLO829 SV truth-set paper | DOI TBD | pending | Need exact paper identity and DOI. |
| S018 | DREAM SMC-Het / subclonal reconstruction benchmarks including 2025 crowd-sourced benchmark | DREAM/SMC-Het papers | DOI TBD | pending | Validate 31 algorithms / 51 simulated tumors claim. |
| S019 | Metastatic colorectal cancer evolution/signature case studies | Mendelaar et al.; Dang et al. | DOI TBD | pending | Need exact paper identities and claims. |
| S020 | Multiple myeloma timing/mutational process case studies | Maura et al.; Rustad et al. | DOI TBD | pending | Validate serial WGS/exome counts and melphalan signature claim. |
| S021 | Therapy-driven metastatic breast cancer/APOBEC 2025 claim | 2025 metastatic breast cancer study | DOI TBD | pending | Fast-moving claim: verify carefully before use. |

## Notes

- The Deep Research output contains internal ChatGPT citation tokens such as `turn39view0`; these are not usable in final course materials.
- Validation should replace those tokens with real DOI/URL citations and mark unsupported claims for revision.
- Because the module is very broad, validation should also flag items that are accurate but too detailed for a three-lecture week.
