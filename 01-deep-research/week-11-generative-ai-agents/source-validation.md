# Source Validation Log — Module 11 / Week 11 — Generative AI, Agents, and Knowledge Systems for Oncology

Raw Deep Research file: `deep-research-report.md`

Note: Dr. Liu labeled this as **Week 11**. In the course outline this corresponds to **Week 11 — Generative AI, Agents, and Knowledge Systems for Oncology**.

## Priority validation queue

| ID | Claim / Item | Source | DOI/URL | Status | Notes |
|---|---|---|---|---|---|
| S001 | Oncology LLM field mapping: 34 peer-reviewed studies through March 2024, mostly static oncology QA | Carl et al. 2024, npj Precision Oncology | 10.1038/s41698-024-00733-4 | pending | Verify counts, scope, and conclusions. |
| S002 | Systematic review/meta-analysis of LLM integrations in cancer decision-making: 56 studies across 15 cancer types | Hao et al. 2025, npj Digital Medicine | 10.1038/s41746-025-01824-7 | pending | Verify counts, integration/evaluation claims. |
| S003 | Healthcare RAG architecture/freshness/reliability framing | Yang et al. 2025, npj Health Systems | 10.1038/s44401-024-00004-1 | pending | Verify title and architectural framework. |
| S004 | MIRAGE/MedRAG benchmark and toolkit; corpus/retriever/model interactions; lost-in-the-middle effect | Xiong et al. 2024, Findings of ACL / arXiv | arXiv:2402.13178 | pending | Verify benchmark/task details and reported lessons. |
| S005 | SourceCheckup statement-level medical citation support evaluation | Wu et al. 2025, Nature Communications | 10.1038/s41467-025-58551-6 | pending | Verify framework, support/contradiction findings. |
| S006 | GeneGPT tool/API calling with NCBI APIs and GeneTuring benchmark | Jin et al. 2024, Bioinformatics | DOI TBD | pending | Verify title, API/tool-use design, and benchmark claims. |
| S007 | ESCARGOT knowledge-graph-guided graph-of-thought biomedical reasoning | Matsumoto et al. 2025, Bioinformatics | DOI TBD | pending | Verify DOI and design pattern. |
| S008 | BioAgents multi-agent workflow support for bioinformatics using smaller/fine-tuned models plus RAG | Mehandru et al. 2025, Scientific Reports | DOI TBD | pending | Verify system scope and workflow claims. |
| S009 | TrialGPT oncology clinical-trial matching: retrieval, criterion-level matching, ranking, synthetic annotations, user-study time savings | Jin et al. 2024, Nature Communications | 10.1038/s41467-024-53081-z | pending | Verify annotation counts and user-study claims. |
| S010 | CORAL oncology report dataset/schema for temporality, treatment history, modifiers, and relations | Sushil et al. 2024, NEJM AI | 10.1056/AIdbp2300110 | pending | Verify schema and dataset claims. |
| S011 | MEREDITH expert-guided precision-oncology decision support with literature/trials/approval/guideline retrieval | Lammert et al. 2024, JCO Precision Oncology | 10.1200/PO-24-00478 | pending | Verify operational definition of expert-guided. |
| S012 | Context-augmented MOAlmanac-based precision-oncology recommendation system | Jun et al. 2026, Cancer Cell | 10.1016/j.ccell.2025.12.017 | pending | Future/current; verify publication details and performance claims. |
| S013 | MOAlmanac as curated clinicogenomic knowledge base | Reardon et al. 2021, Nature Cancer; MOAlmanac resource | 10.1038/s43018-021-00243-3 | pending | Verify resource role and current availability. |
| S014 | Knowledge-resource bundle: OncoKB, CIViC, PrimeKG, SPOKE | Resource docs/papers | DOI/URL TBD | pending | Verify access model, update cadence, API/graph structure, evidence levels. |
| S015 | Medical RAG variants: i-MedRAG, RAG², KG-RAG, MedGraphRAG, KRAGEN | Multiple papers | DOI/URL TBD | pending | Validate method distinctions and evidence. |
| S016 | Tool/agent systems: BioRAGent, ReAct, biomedical agent reviews, multiple-myeloma agentic evaluation | Multiple papers | DOI/URL TBD | pending | Identify exact papers and verify claims/readiness framing. |
| S017 | Validation/evaluation frameworks: TREC BioGen 2024/2025, CREOLA, BioACE, SourceCheckup | Multiple benchmarks/tools | DOI/URL TBD | pending | Verify tasks and claim-level grounding relevance. |
| S018 | Biomedical QA/explanation benchmarks: MultiMedQA, MedQA, PubMedQA, BioASQ, MedExQA | Multiple resources | DOI/URL TBD | pending | Validate role as stress tests, not oncology workflow substitutes. |
| S019 | Oncology-specific corpora: UCSF breast pathology report dataset, PD-L1 extraction study, pathology summarization work | Multiple papers/resources | DOI/URL TBD | pending | Verify counts and extraction/summarization claims. |
| S020 | Workflow/metadata benchmarks: ClinicalTrials.gov, biomarker extraction from trials, metadata harmonization, BioAgent Bench | Multiple resources | DOI/URL TBD | pending | Verify current availability and relevance. |
| S021 | Guideline/patient information QA and radiation-oncology LLM safety evaluations | Multiple papers | DOI TBD | pending | Validate multilingual/reference-quality/harm claims. |
| S022 | Privacy-preserving architecture claims for PHI-heavy oncology corpora | Reviews/studies | DOI/URL TBD | pending | Validate de-identification/on-prem/local-model framing. |

## Notes

- The original Deep Research output contained internal ChatGPT citation tokens; imported report/intake Markdown has been cleaned, but final materials still need real DOI/URL citations.
- Validation should prioritize system papers with oncology decision-support implications and claim-level provenance evaluation before lecture-plan generation.
- Keep boundaries explicit: Week 11 is about oncology-facing generative systems, RAG, agents, knowledge resources, provenance, and workflow validation — not model pretraining/scaling (Week 10), digital twins/perturbation simulation (Week 12), or regulated deployment/enterprise governance (Week 13).
