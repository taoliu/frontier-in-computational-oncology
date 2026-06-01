# Source Validation Log — Module 12 / Week 12 — Digital Twins: Virtual Cell, Virtual Tumor, and Virtual Patient

Raw Deep Research file: `deep-research-report.md`

Note: Dr. Liu labeled this as **Week 12**. In the course outline this corresponds to **Week 12 — Digital Twins: Virtual Cell, Virtual Tumor, and Virtual Patient**.

## Priority validation queue

| ID | Claim / Item | Source | DOI/URL | Status | Notes |
|---|---|---|---|---|---|
| S001 | Digital twin definition: patient/physical-linked, dynamically updated, predictive, decision-informing construct | National Academies 2024 report | URL TBD | pending | Verify official wording and distinction from simulation. |
| S002 | Predictive oncology digital twins as precision cancer care paradigm shift | Hernandez-Boussard et al. 2021, Nature Medicine | 10.1038/s41591-021-01558-5 | pending | Verify manifesto framing and limitations. |
| S003 | NCI/DOE cancer patient digital twin approaches and pilot archetypes | Stahlberg et al. 2022, Frontiers in Digital Health | 10.3389/fdgth.2022.1007784 | pending | Verify community paper and archetypes. |
| S004 | Oncology digital twins review emphasizing continuous updating and barriers | Mollica et al. 2024, ESMO Real World Data and Digital Oncology | 10.1016/j.esmorw.2024.100056 | pending | Verify applications, ethics/practical barriers. |
| S005 | Virtual-cell framing and whole-cell mechanistic landmark | Bunne et al. 2024 Cell; Karr et al. 2012 Cell | DOI TBD; 10.1016/j.cell.2012.05.044 | pending | Validate virtual-cell scope; not oncology twins per se. |
| S006 | Patient-specific mechanistic tumor-growth models with AI/big data | Lorenzo et al. 2024, Annual Review of Biomedical Engineering | 10.1146/annurev-bioeng-081623-025834 | pending | Verify method-development review scope. |
| S007 | Immuno-oncology virtual patients vs digital twins via QSP | Wang et al. 2024, npj Digital Medicine | DOI TBD | pending | Verify virtual patient/twin distinction and treatment-specific framing. |
| S008 | High-grade glioma radiotherapy digital twin under uncertainty | Chaudhuri et al. 2023, Frontiers in Artificial Intelligence | 10.3389/frai.2023.1222612 | pending | Verify calibration, optimization, in silico cohort and reported gains. |
| S009 | MRI-based breast cancer digital twins optimizing neoadjuvant chemotherapy | Wu et al. 2025, npj Digital Medicine | 10.1038/s41746-025-01579-1 | pending | Verify 105 ARTEMIS patients, AUC 0.82, 128 schedule options and claims. |
| S010 | Representation-learning calibration of agent-based tumor models to images | Cess et al. 2023, PLOS Computational Biology | 10.1371/journal.pcbi.1011070 | pending | Verify method role for ABM calibration. |
| S011 | PK/PD tumor growth inhibition landmark | Simeoni et al. 2004, Cancer Research | 10.1158/0008-5472.CAN-03-2524 | pending | Verify historical anchor and TGI/PKPD framing. |
| S012 | Adaptive therapy in mCRPC: eco-evolutionary protocol and abiraterone pilot | Zhang et al. 2017 Nature Communications; Zhang et al. 2022 eLife | 10.1038/s41467-017-01968-5; 10.7554/eLife.76284 | pending | Verify clinical protocol and response/drug-exposure claims. |
| S013 | State construction and observability in virtual cells/tumors/patients | Multiple papers | DOI/URL TBD | pending | Validate concepts with review support. |
| S014 | Mechanistic model families: ODE growth/PKPD, PDE/reaction-diffusion, ABM, QSP, hybrid AI-mechanistic methods | Multiple papers | DOI/URL TBD | pending | Validate method taxonomy and examples. |
| S015 | Simulation ecosystem: PhysiCell, PhysiBoSS 2.0, PhysiPKPD, Chaste, CompuCell3D | Tool papers/docs | DOI/URL TBD | pending | Verify current software roles and citations. |
| S016 | Calibration/UQ methods: Bayesian calibration, ABC, likelihood-free inference, surrogate modeling, representation-learning discrepancies | Multiple papers | DOI/URL TBD | pending | Cite selectively for lecture methods. |
| S017 | Optimization/control: risk-aware optimization, adaptive therapy rules, optimal control, cautious RL framing | Multiple papers | DOI/URL TBD | pending | Validate examples and avoid overclaiming RL. |
| S018 | Longitudinal/multimodal datasets: TCIA, QIN, I-SPY 2, UPenn-GBM, LUMIERE, Yale-Brain-Mets-Longitudinal, RADCURE, TRACERx, PDMR, PDXNet | Resource papers/pages | DOI/URL TBD | pending | Verify current resource names, modality, treatment context, and availability. |
| S019 | Immunotherapy case studies: Butner model; Johns Hopkins NSCLC QSP virtual patients with durvalumab/iAtlas | Multiple papers | DOI TBD | pending | Verify patient/cohort counts and biomarker claims. |
| S020 | Virtual clinical trials / multiscale tumor-immune simulation: NSCLC QSP antibody study; Rocha micrometastasis virtual trajectories | Multiple papers | DOI TBD | pending | Verify virtual-patient and trajectory counts. |
| S021 | Prospective validation and fit-for-purpose validation gaps in oncology digital twins | Reviews/scoping reviews | DOI/URL TBD | pending | Validate limitations and definition policing. |
| S022 | Computational acceleration: differentiable simulators, reduced-order models, surrogates, GPU/TumorTwin frameworks | Multiple papers/tools | DOI/URL TBD | pending | Validate current state and avoid speculative overreach. |

## Notes

- The original Deep Research output contained internal ChatGPT citation tokens; imported report/intake Markdown has been cleaned, but final materials still need real DOI/URL citations.
- Validation should prioritize definition papers, mechanistic-twin reviews, and oncology case studies with numerical claims before lecture-plan generation.
- Keep boundaries explicit: Week 12 is about patient-linked latent dynamical states and treatment-conditioned future trajectories; perturbation screens, EHR-only risk scores, generic survival prediction, and LLM agents belong to adjacent weeks unless embedded in a forward simulator.
