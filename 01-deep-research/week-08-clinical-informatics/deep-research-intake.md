# Week 08 — Clinical Informatics and Outcome Prediction — Deep Research Intake

## Source

- Deep Research doc/link: Private Deep Research attachment (not public)
- Date received: 2026-05-31
- Imported by: Claw

## Raw content

Raw file stored at `deep-research-report.md`.

## Raw content excerpt

# Frontier in Computational Oncology Week 8 Clinical Informatics and Outcome Prediction

## Module overview

This module studies how routine oncology data become computational evidence for patient-level risk, prognosis, treatment-effect, and outcome models. The central story is that cancer EHRs, registries, linked claims, and semi-structured clinical notes are not curated “omics-style” research matrices; they are care-generated, code-mediated, irregularly sampled, and often outcome-incomplete records whose missingness can be informative, whose endpoints must be operationalized, and whose treatment choices are confounded by indication. A serious graduate treatment therefore has to connect data representation and phenotype extraction to survival analysis, competing risks, dynamic prediction, causal inference, calibration, fairness, and transportability, while also showing how modern oncology studies validate real-world endpoints such as real-world overall survival and progression-free survival against trials and chart abstraction. The module belongs squarely in computational oncology because much of the difficulty is methodological: defining time zero, handling censoring and competing events, modeling time-varying covariates, coping with coding systems and site differences, and verifying whether a model trained in one care setting remains calibrated and clinically useful in another.

## Must-read papers and resources

1. **Collins et al., 2025, *BMJ Oncology* — “Clinical prediction models using machine learning in oncology: challenges and recommendations.”** DOI: 10.1136/bmjonc-2025-000914. This is the best recent oncology-specific overview of how to build prediction models that are methodologically sound, equitable, and clinically useful; it explicitly covers missing data, censored outcomes, competing risks, fairness, calibration, external validation, and implementation barriers.

2. **Castellanos et al., 2024, *JCO Clinical Cancer Informatics* — “Raising the Bar for Real-World Data in Oncology: Approaches to Quality Across Multiple Dimensions.”** DOI: 10.1200/CCI.23.00046. A foundational paper for explaining why oncology RWD quality is multi-dimensional and “fitness for use” depends on provenance, abstraction, consistency, completeness, and endpoint-specific validation.

3. **Kehl et al., 2024, *Nature Communications* — “Shareable artificial intelligence to extract cancer outcomes from electronic health records for precision oncology research.”** DOI: 10.1038/s41467-024-54071-x. Essential for the semi-structured data portion of the week: it shows how privacy-preserving teacher–student distillation can make note-based outcome extraction models transferable across centers.

4. **Jee et al., 2024, *Nature* — “Automated real-world data integration improves cancer outcome prediction.”** DOI: 10.1038/s41586-024-08167-5. A flagship clinicogenomic informatics paper showing that NLP-derived clinical features from reports materially improve overall-survival prediction beyond stage or genomics alone, while also enabling biological discovery about metastatic tropism.

5. **Lasiter et al., 2021, *Clinical Pharmacology & Therapeutics* — “Real-world Overall Survival Using Oncology Electronic Health Record Data: Friends of Cancer Research Pilot.”** DOI: 10.1002/cpt.2443. A key endpoint-validation paper for teaching why even “simple” outcomes such as overall survival require careful data-source-specific definitions and sensitivity analyses in observational oncology data.

6. **Ton et al., 2022, *Clinical Cancer Research* — “Replication of Overall Survival, Progression-Free Survival, and Overall Response in Chemotherapy Arms of Non–Small Cell Lung Cancer Trials Using Real-World Data.”** DOI: 10.1158/1078-0432.CCR-22-0471. Important because it moves beyond rwOS to rwPFS and response endpoints, showing what real-world endpoint replication can and cannot recover from oncology EHR sources.

7. **van Amsterdam et al., 2025, *Clinical Oncology* — “Causal Inference in Oncology: Why, What, How and When.”** DOI: 10.1016/j.clon.2024.07.002. A concise, oncology-focused introduction to estimands, DAG thinking, confounding, treatment-effect heterogeneity, and when causal questions should not be answered by purely prognostic models.

8. **Hernán and Robins, 2016, *Journal of Clinical Epidemiology* — “Using Big Data to Emulate a Target Trial When a Randomized Trial Is Not Available.”** DOI: 10.1016/j.jclinepi.2016.03.001. This older landmark is still indispensable for the observational-treatment-effect part of the week because it formalizes time zero, eligibility, treatment assignment, follow-up, and causal contrasts in a way that directly prevents immortal-time and selection bias.

9. **Tsegaye et al., 2025, *Journal of Clinical Epidemiology* — “Larger sample sizes are needed when developing a clinical prediction model using machine learning in oncology.”** DOI: 10.1016/j.jclinepi.2025.111675. A valuable corrective to the common assumption that flexible ML automatically solves small-sample oncology prediction problems; it is ideal for discussing events-per-parameter, optimistic performance estimates, and underpowered subgroup analyses.

10. **TRIPOD+AI, 2024, *BMJ* — updated reporting guidance for regression- and AI-based clinical prediction models.** DOI: 10.1136/bmj-2023-078378. This is the practical reporting checklist to pair with methods papers, especially for student critique of oncology CPM manuscripts.

11. **PROBAST+AI, 2025, *BMJ* — updated quality, risk-of-bias, and applicability assessment tool for prediction models.** DOI: 10.1136/bmj-2024-082505. This is the strongest framework for structured appraisal of oncology prediction studies and for teaching why many published models are not implementation-ready.

12. **Hueting et al., 2022, *Journal of Clinical Epidemiology* — “The majority of 922 prediction models supporting breast cancer decision-making are at high risk of bias.”** DOI: 10.1016/j.jclinepi.2022.10.016. This is the sobering oncology-specific field audit: it demonstrates at scale that the literature is crowded with models but shallow in validity, transparency, and transportability.


[Truncated here in intake file; see `deep-research-report.md` for full content.]

## Initial triage

- Strongest sections: strong patient-level clinical-informatics framing; clear distinction between care-generated oncology data and curated research matrices; strong coverage of phenotype extraction, endpoint construction, time zero, censoring, competing risks, dynamic prediction, causal inference, calibration, fairness, and transportability.
- Weak or missing areas: citation markers are ChatGPT Deep Research internal turn references and must be replaced with real DOI/URL citations; several 2024–2025 papers/resources are fast-moving and need current verification before lecture-plan generation, especially TRIPOD+AI/PROBAST+AI, oncology ML prediction recommendations, MSK-CHORD, and clinical NLP endpoint extraction.
- Claims requiring validation: all must-read papers/resources and DOIs; registry/resource counts for SEER, NCDB, CancerLinQ, GENIE, MSK-CHORD; real-world endpoint validation claims; breast-cancer prediction-model risk-of-bias claims; clinical NLP outcome extraction claims; Trial Pathfinder/TrialTranslator generalizability claims; OMOP Oncology representation details.
- Suggested source-priority level: high — this module is clinically consequential and relies on current methodological guidance, real-world endpoint validation studies, and mutable registry/resource counts.

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
