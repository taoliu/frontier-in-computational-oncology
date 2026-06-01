# Source Validation Log — Module 8 / Week 08 — Clinical Informatics and Outcome Prediction

Raw Deep Research file: `deep-research-report.md`

Note: Dr. Liu labeled this as **Week 8**. In the course outline this corresponds to **Week 08 — Clinical Informatics and Outcome Prediction**.

## Priority validation queue

| ID | Claim / Item | Source | DOI/URL | Status | Notes |
|---|---|---|---|---|---|
| S001 | Oncology ML clinical prediction challenges/recommendations covering missingness, censoring, competing risks, fairness, calibration, validation, implementation | Collins et al. 2025, BMJ Oncology | 10.1136/bmjonc-2025-000914 | pending | Verify title, scope, and recommendations. |
| S002 | Real-world oncology data quality and fitness-for-use framework | Castellanos et al. 2024, JCO Clinical Cancer Informatics | 10.1200/CCI.23.00046 | pending | Verify quality dimensions and endpoint-specific validation framing. |
| S003 | Shareable AI for extracting cancer outcomes from EHRs via privacy-preserving teacher–student distillation | Kehl et al. 2024, Nature Communications | 10.1038/s41467-024-54071-x | pending | Verify transferable outcome-extraction claims. |
| S004 | Automated real-world data integration / MSK-CHORD improves cancer outcome prediction and metastatic-tropism discovery | Jee et al. 2024, Nature | 10.1038/s41586-024-08167-5 | pending | Verify title, dataset size, features, and survival-prediction claim. |
| S005 | Friends of Cancer Research real-world overall survival pilot | Lasiter et al. 2021, Clinical Pharmacology & Therapeutics | 10.1002/cpt.2443 | pending | Verify endpoint validation and sensitivity-analysis claims. |
| S006 | Real-world replication of OS, PFS, and response in NSCLC trial chemotherapy arms | Ton et al. 2022, Clinical Cancer Research | 10.1158/1078-0432.CCR-22-0471 | pending | Verify what endpoints replicate and limitations. |
| S007 | Oncology-focused causal inference overview | van Amsterdam et al. 2025, Clinical Oncology | 10.1016/j.clon.2024.07.002 | pending | Verify estimands/DAG/confounding/treatment-effect framing. |
| S008 | Target trial emulation landmark for observational treatment-effect studies | Hernán and Robins 2016, Journal of Clinical Epidemiology | 10.1016/j.jclinepi.2016.03.001 | pending | Verify time-zero/eligibility/treatment/follow-up framing. |
| S009 | Larger sample sizes needed for ML clinical prediction models in oncology | Tsegaye et al. 2025, Journal of Clinical Epidemiology | 10.1016/j.jclinepi.2025.111675 | pending | Verify sample-size and events-per-parameter conclusions. |
| S010 | TRIPOD+AI reporting guidance for regression- and AI-based prediction models | TRIPOD+AI 2024, BMJ | 10.1136/bmj-2023-078378 | pending | Verify checklist scope and final citation details. |
| S011 | PROBAST+AI risk-of-bias/applicability assessment tool | PROBAST+AI 2025, BMJ | 10.1136/bmj-2024-082505 | pending | Verify scope and use for oncology CPM critique. |
| S012 | Audit of 922 breast-cancer decision-support prediction models at high risk of bias | Hueting et al. 2022, Journal of Clinical Epidemiology | 10.1016/j.jclinepi.2022.10.016 | pending | Verify number and conclusions. |
| S013 | Oncology clinical data representation: ICD-10-CM, SNOMED CT, RxNorm, OMOP Oncology extension | Multiple docs/papers | DOI/URL TBD | pending | Verify ontology/CDM details and oncology episodes. |
| S014 | Missingness, censoring, competing-risk, and endpoint-construction issues in oncology EHR/RWD | Multiple methods papers | DOI/URL TBD | pending | Validate claims and teaching examples. |
| S015 | Survival/dynamic prediction methods: Cox, flexible parametric, cause-specific/Fine–Gray, landmarking, joint models | Multiple papers/resources | DOI/URL TBD | pending | Validate method descriptions and oncology examples. |
| S016 | ML survival models: random survival forests, boosting survival learners, DeepSurv, DeepHit, Dynamic-DeepHit | Multiple papers | DOI/URL TBD | pending | Verify model roles and cautionary framing. |
| S017 | Observational causal methods: propensity scores, IPW, overlap weighting, g-computation, marginal structural models, doubly robust estimation, causal ML | Multiple papers | DOI/URL TBD | pending | Validate design-stage assumptions and target-trial alignment. |
| S018 | Clinical NLP/phenotype extraction from radiology/oncology notes/pathology reports | Multiple papers | DOI/URL TBD | pending | Keep NLP scoped to endpoint/phenotype extraction, not general LLMs. |
| S019 | Resource counts: SEER coverage, NCDB facilities, CancerLinQ patients, GENIE centers, MSK-CHORD patients | Resource pages/papers | DOI/URL TBD | pending | Mutable counts; verify live before final materials. |
| S020 | Trial generalizability and RWD emulation examples: Trial Pathfinder and TrialTranslator | Multiple papers/tools | DOI/URL TBD | pending | Verify claims and teaching scope. |
| S021 | Supportive-care/short-term mortality prediction and PRO/EHR integration | Parikh and related papers | DOI TBD | pending | Verify outcome/actionability/calibration claims. |
| S022 | Symptoms/adverse events/supportive outcomes from oncology EHR and notes | Multiple papers | DOI TBD | pending | Identify exact papers and validate endpoint definitions. |

## Notes

- The original Deep Research output contained internal ChatGPT citation tokens; imported report/intake Markdown has been cleaned, but final materials still need real DOI/URL citations.
- Validation should prioritize methodological guidance and endpoint-validation studies before lecture-plan generation.
- Keep module boundaries explicit: NLP belongs here only when it supports phenotype extraction or endpoint construction; image-based pathology/radiology, general LLM agents, and clinical deployment/regulatory operations belong elsewhere.
