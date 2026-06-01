# Week 11 — Generative AI, Agents, and Knowledge Systems for Oncology — Deep Research Intake

## Source

- Deep Research doc/link: Private Deep Research attachment (not public)
- Date received: 2026-05-31
- Imported by: Claw

## Raw content

Raw file stored at `deep-research-report.md`.

## Raw content excerpt

# Week 11 Module Research for Generative AI, Agents, and Knowledge Systems for Oncology

## Module overview

This module should tell a very specific story: oncology is no longer a setting where a pretrained model is simply queried for static medical knowledge, but one in which modern systems retrieve current evidence, normalize biomarker and disease entities, call APIs and databases, orchestrate multi-step workflows, attach provenance, and keep humans in the loop for adjudication. The biological and clinical need is obvious: oncology knowledge changes rapidly with new biomarker evidence, trial criteria, and drug approvals, while the key source materials are fragmented across papers, guidelines, trial registries, pathology reports, clinic notes, and structured knowledge bases. Recent oncology reviews show that much early LLM work focused on off-the-shelf question answering, whereas the newer frontier is interactive systems such as RAG over oncology knowledge resources, tool-using agents, and workflow automation for trial matching, tumor board support, and data curation. A strong graduate module should therefore emphasize system design and verification—retrieval pipelines, tool use, knowledge graphs, provenance and citation evaluation, expert-grounded validation, and privacy-aware implementation—rather than generic foundation model pretraining, which belongs to Week 10.

## Must-read papers and resources

**Carl et al., *npj Precision Oncology* (2024), “Large language model use in clinical oncology,” plus Hao et al., *npj Digital Medicine* (2025), “Large language model integrations in cancer decision-making: a systematic review and meta-analysis.”** Read these together as the field-mapping entry point. Carl et al. review 34 peer-reviewed oncology studies through March 2024 and show that most early papers evaluated static oncologic question answering; Hao et al. extend the picture to 56 studies across 15 cancer types and are especially useful for discussing how systems are actually integrated and evaluated in cancer decision workflows. DOI: 10.1038/s41698-024-00733-4; DOI: 10.1038/s41746-025-01824-7.

**Yang et al., *npj Health Systems* (2025), “Retrieval-augmented generation for generative artificial intelligence in health care.”** This is the clean architectural foundation for Lecture 1 or the start of Lecture 2. It formalizes the indexing–retrieval–generation pipeline and frames why RAG matters in medicine: freshness, reliability, personalization, and reduced dependence on stale parametric memory. DOI: 10.1038/s44401-024-00004-1.

**Xiong et al., Findings of ACL (2024), “Benchmarking Retrieval-Augmented Generation for Medicine.”** This is one of the most important methods papers for the module because it introduces the medical MIRAGE benchmark and the MedRAG toolkit, showing how corpus choice, retriever choice, and model choice interact. It is especially valuable pedagogically because it reports concrete implementation lessons, including gains over chain-of-thought prompting and the “lost-in-the-middle” effect in medical RAG. ArXiv:2402.13178.

**Wu et al., *Nature Communications* (2025), “An automated framework for assessing how well LLMs cite relevant medical references.”** This is the core provenance paper to assign. SourceCheckup moves the evaluation target from answer fluency to statement-level evidentiary support, and it shows that citation presence is not enough: many medical LLM outputs still cite papers that fail to support, or even contradict, their claims. DOI: 10.1038/s41467-025-58551-6.

**Jin et al., *Bioinformatics* (2024), “GeneGPT.”** If the module needs one canonical paper on biomedical tool use, this is it. GeneGPT prompts a model to use NCBI web APIs and outperforms previous baselines on GeneTuring; it is ideal for teaching when language models should become API-calling systems rather than pure text generators.

**Matsumoto et al., *Bioinformatics* (2025), “ESCARGOT,” together with Mehandru et al., *Scientific Reports* (2025), “BioAgents.”** Assign these together for the agentic systems lecture. ESCARGOT shows knowledge-graph-guided, graph-of-thought reasoning for biomedical questions; BioAgents shows multi-agent workflow support for bioinformatics using smaller, fine-tuned models plus RAG. Together they illustrate two distinct but complementary design patterns: reasoning over structured knowledge versus orchestrating end-to-end analysis workflows. DOI for ESCARGOT is available through the journal article; BioAgents is in *Scientific Reports* and is useful as a practical workflow automation counterpoint.

**Jin et al., *Nature Communications* (2024), “Matching patients to clinical trials with large language models.”** TrialGPT is the clearest oncology-specific agentic workflow paper in the literature. It decomposes patient-to-trial matching into retrieval, criterion-level matching, and ranking, and it reports large-scale synthetic annotations plus user-study evidence for time savings. DOI: 10.1038/s41467-024-53081-z.

**Sushil et al., *NEJM AI* (2024), “CORAL: Expert-Curated Oncology Reports to Advance Language Model Inference.”** This is a strong paper for teaching oncology text structuring and annotation. Its value is not just the dataset but the schema: oncology notes require more than named entities—they require temporality, treatment history, modifiers, and relations. DOI: 10.1056/AIdbp2300110.

**Lammert et al., *JCO Precision Oncology* (2024), “Expert-Guided Large Language Models for Clinical Decision Support in Precision Oncology.”** MEREDITH is a good case study in domain-tailored evidence integration. It starts from a general-purpose backbone, then improves utility by adding tumor-board-like evidence retrieval over literature, trials, approval status, and guidelines. It is especially useful for classroom discussion of what “expert-guided” really means operationally. DOI: 10.1200/PO-24-00478.

**Jun et al., *Cancer Cell* (2026), “A context-augmented large language model for accurate precision oncology medicine recommendations.”** This is currently one of the strongest oncology RAG case studies. It uses Molecular Oncology Almanac as the retrieval backbone and reports very high accuracy on synthetic and real-world oncologist queries, making it a natural anchor for the application lecture. DOI: 10.1016/j.ccell.2025.12.017.

**Reardon et al., *Nature Cancer* (2021), “Integrating molecular profiles into clinical frameworks through the Molecular Oncology Almanac,” together with the MOAlmanac resource.** Although slightly older than the preferred window, this is a landmark knowledge-system paper for precision oncology. It gives students a concrete example of a curated, updatable clinicogenomic knowledge base that later RAG systems can actually retrieve from. DOI: 10.1038/s43018-021-00243-3.

**Resource bundle for knowledge-grounded oncology systems: OncoKB, CIViC, PrimeKG, and SPOKE.** These are not interchangeable. OncoKB focuses on clinically actionable cancer variants and evidence levels; CIViC is an open, community-curated cancer variant interpretation resource; PrimeKG is a multimodal precision medicine knowledge graph spanning diseases, drugs, and biological scales; and SPOKE is a large, provenance-rich biomedical knowledge graph with an API and weekly rebuilds. Together they define the “knowledge systems” half of this module.


[Truncated here in intake file; see `deep-research-report.md` for full content.]

## Initial triage

- Strongest sections: very clear boundary from Week 10 foundation models into Week 11 interactive oncology systems; strong emphasis on RAG, tool use, knowledge graphs, provenance, claim-level citation support, expert-grounded validation, privacy-aware system design, and human-in-the-loop workflows.
- Weak or missing areas: citation markers are ChatGPT Deep Research internal turn references and must be replaced with real DOI/URL citations; several 2025–2026 oncology RAG/agent papers and benchmark claims are fast-moving and need live verification before lecture-plan generation.
- Claims requiring validation: all must-read papers/resources and DOIs; Carl/Hao oncology LLM review counts; Yang RAG architecture paper; MIRAGE/MedRAG claims; SourceCheckup; GeneGPT/GeneTuring; ESCARGOT/BioAgents; TrialGPT annotation/user-study details; CORAL schema; MEREDITH; Jun 2026 MOAlmanac-based system; MOAlmanac/OncoKB/CIViC/PrimeKG/SPOKE current resource details.
- Suggested source-priority level: very high — this module is current, system-design-oriented, and includes clinical decision-support-adjacent claims that require careful source validation and conservative wording.

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
