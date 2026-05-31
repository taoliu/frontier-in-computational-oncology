# ChatGPT Deep Research Prompts for Frontier in Computational Oncology

Source synced from Google Doc: **Frontier in Computational Oncology** on 2026-05-30.

Purpose: use the prompts below to collect up-to-date background, key methods, landmark papers, current trends, datasets, and teaching ideas for Weeks 2–13 of the proposed course. Each prompt is written to keep the module self-contained while minimizing overlap with neighboring weeks.

---

## General instruction to prepend to every Deep Research query

You are helping design an advanced graduate course titled **Frontier in Computational Oncology**. The course emphasizes **method development**, not simply tool usage. For the module below, collect information that can support three lectures:

1. **Background & Problem Definition** — biological/clinical need, assay/data type, unmet computational challenge.
2. **Method Development & Verification** — statistical models, algorithms, assumptions, implementation choices, simulation/benchmarking/ground-truth validation.
3. **Application & State of the Field** — oncology case studies, biological discoveries, leading tools/resources, current limitations, and near-future directions.

Focus on sources from roughly the last 5–7 years where possible, but include older landmark papers when essential. Prioritize review papers, benchmark papers, influential methods papers, major consortia/resources, and cancer-focused applications. Provide citations with links/DOIs when available. Explicitly separate this module from adjacent modules to avoid overlap.

For the final output, organize the result as:
- One-paragraph module overview
- 8–12 must-read papers/resources with brief annotations
- Key computational problems and assumptions
- Main algorithms/models/tools to teach
- Representative datasets/benchmarks
- Cancer case studies
- Suggested 3-lecture outline
- Open problems and future directions
- Notes on boundaries: what belongs in this module vs. what should be left to other weeks

---

## Week 2 — Functional Genomics in Cancer

**Deep Research prompt**

Using the general instruction above, research a module titled **Functional Genomics in Cancer**.

Module story: from bulk regulatory assays to peak calling and regulatory element discovery.

Scope: ChIP-seq, ATAC-seq, CUT&RUN, CUT&Tag, chromatin interaction assays, assay bias, peak calling, motif analysis, footprinting, ENCODE/Cistrome-style regulatory annotation, and cancer regulatory genomics.

Please collect information to support a self-contained graduate module on computational methods for bulk functional genomics in cancer. Emphasize how experimental assay design creates specific data structures and biases, then how algorithms model signals, backgrounds, uncertainty, enrichment, and reproducibility. Include landmark and current methods such as MACS/MACS3, SPP, SICER-style broad peak callers, HMM-based ATAC-seq approaches such as HMMRATAC, motif/footprinting tools, and selected chromatin interaction methods. Include ENCODE, Cistrome, TCGA-related regulatory analyses, and cancer examples where regulatory element discovery changed biological interpretation.

Boundary guidance: keep this focused on **bulk molecular regulatory assays and regulatory element discovery**. Mention single-cell/spatial extensions only briefly as transition points; detailed single-cell analysis belongs to Week 3, spatial location belongs to Week 4, and network-level causal modeling belongs to Week 6.

---

## Week 3 — Single-Cell and Multimodal Regulatory Genomics

**Deep Research prompt**

Using the general instruction above, research a module titled **Single-Cell and Multimodal Regulatory Genomics**.

Module story: from cell heterogeneity to cell-state-specific regulatory programs.

Scope: scRNA-seq, scATAC-seq, single-cell multiome, data integration, sparsity, clustering, trajectory inference, cell-state identification, transcription factor activity, malignant vs. non-malignant state inference, and resistance programs in cancer.

Please collect information to support a self-contained graduate module on computational methods for single-cell regulatory genomics in cancer. Emphasize why cancer heterogeneity requires single-cell resolution, how sparse/noisy count matrices change statistical modeling, and how scRNA-seq and scATAC-seq are integrated to infer cell states and regulatory programs. Include tools and frameworks such as Seurat, Scanpy, Signac, ArchR, episcanpy, MAESTRO, multiome integration methods, trajectory/pseudotime methods, cell-type annotation, batch correction, and cancer-specific applications in tumor evolution, drug resistance, immune states, and malignant cell programs.

Boundary guidance: keep this focused on **single-cell resolution without explicit spatial coordinates**. Spatial tissue organization belongs to Week 4. Bulk peak calling belongs to Week 2. General foundation models should be saved for Week 10, although single-cell foundation models can be mentioned as an emerging direction.

---

## Week 4 — Spatial Omics of the Tumor Microenvironment

**Deep Research prompt**

Using the general instruction above, research a module titled **Spatial Omics of the Tumor Microenvironment**.

Module story: from dissociated cells to spatially organized tumor ecosystems.

Scope: spatial transcriptomics, spatial proteomics, spatial epigenomics if available, deconvolution, cell segmentation/assignment for molecular assays, niche detection, tumor-immune-stromal neighborhoods, cell-cell interaction inference, spatial gradients, spatial domains, and tumor microenvironment biology.

Please collect information to support a self-contained graduate module on computational methods for spatial molecular profiling in cancer. Emphasize how spatial molecular assays differ from dissociated single-cell assays, what computational problems are introduced by spot resolution, imaging-based molecules, segmentation, alignment, deconvolution, domain detection, spatial statistics, neighborhood analysis, and cell-cell interaction inference. Include major platforms/resources such as Visium, Slide-seq, MERFISH/Xenium/CosMx-style approaches, CODEX/IMC/MIBI for proteomics where relevant, and cancer examples involving immune niches, stromal barriers, tumor invasion fronts, hypoxia gradients, and therapy response.

Boundary guidance: focus on **molecular spatial maps and tumor microenvironment organization**. Avoid broad image morphology/pathology topics, which belong to Week 9. Avoid general single-cell clustering without spatial structure, which belongs to Week 3.

---

## Week 5 — Somatic Mutation, Variant Interpretation, and Cancer Evolution

**Deep Research prompt**

Using the general instruction above, research a module titled **Somatic Mutation, Variant Interpretation, and Cancer Evolution**.

Module story: from tumor genome alteration to driver events and clonal evolution.

Scope: somatic variant calling, driver prediction, mutational signatures, copy-number alteration, structural variation when relevant, tumor purity/ploidy, clonal/subclonal inference, phylogenetic modeling, tumor heterogeneity, evolutionary trajectories, resistance evolution, and AI-assisted variant prioritization.

Please collect information to support a self-contained graduate module on computational methods for interpreting cancer DNA alterations and reconstructing tumor evolution. Emphasize how sequencing data are converted into mutations and copy-number states, how statistical models distinguish signal from artifacts, how driver events are prioritized, and how clonal architecture/evolutionary histories are inferred. Include tools/methods such as Mutect-style callers, Strelka/VarScan-style approaches as appropriate, GATK best practices for somatic calling, dNdScv/MutSig-style driver discovery, COSMIC mutational signatures, copy-number callers, PyClone/PhyloWGS/Treeomics-style clonal inference, and recent machine-learning or knowledgebase approaches for variant interpretation.

Boundary guidance: focus on **DNA-level alterations and evolutionary interpretation**. Regulatory function belongs to Weeks 2–3, systems-level networks to Week 6, treatment response prediction to Week 7, and clinical implementation/decision support to Week 13.

---

## Week 6 — Gene Regulation, Networks, and Systems Oncology

**Deep Research prompt**

Using the general instruction above, research a module titled **Gene Regulation, Networks, and Systems Oncology**.

Module story: from molecular measurements to causal regulatory systems.

Scope: gene regulatory networks, pathway activity, causal inference, Bayesian networks, graphical models, dynamical systems, perturbation-aware network modeling, pathway/signature methods, regulatory circuit inference, and systems-level cancer biology.

Please collect information to support a self-contained graduate module on computational methods that infer regulatory and signaling systems from molecular data. Emphasize the distinction between correlation, association, directionality, causality, dynamics, and perturbation evidence. Include methods such as ARACNe/GENIE3/SCENIC-style regulatory network inference, Bayesian networks, causal discovery methods, pathway enrichment and pathway activity models, ordinary differential equation or dynamical systems models where appropriate, and perturbation-aware network inference. Include oncology case studies in oncogenic signaling, transcriptional addiction, tumor suppressor pathways, immune evasion circuits, and resistance mechanisms.

Boundary guidance: focus on **system-level inference across genes, pathways, and regulatory circuits**. Do not spend much time on the mechanics of generating functional genomics data from Week 2, single-cell preprocessing from Week 3, or screen design and dose-response modeling from Week 7.

---

## Week 7 — Drug Screening, Perturbation Modeling, and Virtual Cell Models

**Deep Research prompt**

Using the general instruction above, research a module titled **Drug Screening, Perturbation Modeling, and Virtual Cell Models**.

Module story: from perturbation experiments to predictive models of drug and genetic response.

Scope: CRISPR screens, RNAi screens where useful historically, pharmacologic screens, Perturb-seq, dose-response modeling, drug synergy, synthetic lethality, resistance prediction, perturbation-response modeling, cell-line/organoid models, and virtual perturbation or virtual cell concepts.

Please collect information to support a self-contained graduate module on computational methods for perturbation experiments in cancer. Emphasize how perturbation design, controls, batch effects, guide efficiency, off-target effects, cell fitness, dose-response curves, and combinatorial treatments shape computational modeling. Include screen-analysis methods such as MAGeCK-style CRISPR screen analysis, drug response resources such as GDSC/CCLE/DepMap/PRISM/CTRP where relevant, perturbational transcriptomics such as LINCS/CMap, Perturb-seq methods, synthetic lethality prediction, drug synergy models, and emerging virtual cell/perturbation-response models.

Boundary guidance: focus on **experimental perturbation and response prediction**. Network inference only belongs here when driven by perturbation data; broader network modeling belongs to Week 6. Digital twins and patient-level simulation belong to Week 12.

---

## Week 8 — Clinical Informatics and Outcome Prediction

**Deep Research prompt**

Using the general instruction above, research a module titled **Clinical Informatics and Outcome Prediction**.

Module story: from real-world clinical data to patient-level risk and outcome models.

Scope: EHR data, cancer registries, structured and semi-structured clinical variables, survival modeling, treatment response, adverse events, multimorbidity, missingness, confounding, clinical endpoints, calibration, fairness, deployment constraints, and real-world evidence.

Please collect information to support a self-contained graduate module on computational methods for clinical oncology informatics and outcome prediction. Emphasize how real-world clinical data differ from curated molecular datasets, including missing-not-at-random data, coding systems, time-varying covariates, treatment selection bias, censoring, competing risks, endpoint definitions, model calibration, and transportability. Include survival models, causal inference for observational data, risk prediction, treatment-response prediction, NLP for extracting clinical variables if appropriate, and examples of oncology EHR/registry-based models. Include clinical validation considerations but reserve full implementation/regulatory translation for Week 13.

Boundary guidance: focus on **structured/semi-structured clinical patient data and outcomes**, not pathology images from Week 9, general LLM agents from Week 11, or final clinical deployment frameworks from Week 13.

---

## Week 9 — Computational Pathology and Cancer Imaging

**Deep Research prompt**

Using the general instruction above, research a module titled **Computational Pathology and Cancer Imaging**.

Module story: from images to morphology-derived cancer phenotypes.

Scope: H&E, IHC, multiplex tissue images when treated as images, radiology if useful, segmentation, weak supervision, multiple-instance learning, morphology representation learning, diagnosis/prognosis models, image-molecular association, image biomarkers, and validation of imaging AI.

Please collect information to support a self-contained graduate module on computational pathology and cancer imaging. Emphasize how image data create different computational challenges than molecular matrices: tiling, resolution, stain normalization, segmentation, annotation scarcity, weak labels, multiple-instance learning, representation learning, domain shift, scanner/site effects, and clinical validation. Include current methods in pathology foundation models and self-supervised learning only as image-specific examples, while reserving the general theory of foundation models for Week 10. Include cancer examples in grading, diagnosis, prognosis, treatment response, tumor microenvironment morphology, and image-genomics association.

Boundary guidance: focus on **visual/morphologic tissue features**. Spatial omics molecular neighborhood analysis belongs to Week 4. Clinical EHR outcome modeling belongs to Week 8. General foundation model concepts belong to Week 10.

---

## Week 10 — Foundation Models for Biomedical and Cancer Data

**Deep Research prompt**

Using the general instruction above, research a module titled **Foundation Models for Biomedical and Cancer Data**.

Module story: from task-specific models to reusable pretrained representations.

Scope: biological sequence foundation models for DNA/RNA/protein, single-cell and perturbation foundation models, pathology/image foundation models, clinical text/EHR foundation models, embeddings, pretraining objectives, transfer learning, fine-tuning, zero-shot/few-shot prediction, benchmarking, and failure modes in cancer datasets.

Please collect information to support a self-contained graduate module on how foundation models are built, adapted, and evaluated for biomedical and cancer data. Emphasize representation learning, pretraining data scale/quality, model architectures, self-supervised objectives, transfer learning, domain adaptation, embedding evaluation, benchmark design, and cancer-specific limitations. Include examples such as protein language models, DNA/RNA models, single-cell foundation models, pathology foundation models, and clinical text/EHR foundation models. Discuss what makes a model “foundation-like” versus a conventional predictive model, and what evidence is needed before using these models in oncology research.

Boundary guidance: focus on **pretrained representations and model adaptation/evaluation**. Do not focus on interactive LLM use, RAG systems, agents, workflow automation, or hallucination control; those belong to Week 11. Do not turn this into a general deep-learning survey.

---

## Week 11 — Generative AI, Agents, and Knowledge Systems for Oncology

**Deep Research prompt**

Using the general instruction above, research a module titled **Generative AI, Agents, and Knowledge Systems for Oncology**.

Module story: from pretrained models to interactive scientific reasoning and workflow automation.

Scope: LLMs for literature, clinical text, protocols, data annotation, RAG systems over papers/grants/guidelines/datasets, AI agents for bioinformatics workflows and metadata curation, generative hypothesis/biomarker/perturbation/treatment-strategy design, tool use, provenance, human-in-the-loop validation, hallucination control, privacy, and safety.

Please collect information to support a self-contained graduate module on generative AI systems in oncology research. Emphasize the shift from static pretrained representations to interactive systems that retrieve knowledge, reason over documents, call tools, produce annotations, automate workflows, and support scientific ideation. Include RAG architectures, evaluation of LLM answers, provenance/citation tracking, biomedical knowledge graphs, agentic workflow systems, clinical guideline/document QA, metadata curation, bioinformatics workflow automation, and safety/validation practices. Include oncology examples where available and broader biomedical examples when cancer-specific work is still emerging.

Boundary guidance: focus on **generative use and AI systems**. General foundation model pretraining and benchmarking belongs to Week 10. Clinical deployment/regulation belongs to Week 13. Digital twin simulation belongs to Week 12.

---

## Week 12 — Digital Twins: Virtual Cell, Virtual Tumor, and Virtual Patient

**Deep Research prompt**

Using the general instruction above, research a module titled **Digital Twins: Virtual Cell, Virtual Tumor, and Virtual Patient**.

Module story: from predictive models to simulation of biological or clinical futures.

Scope: mechanistic models, hybrid AI-mechanistic models, virtual cell/tumor/patient concepts, tumor growth modeling, therapy simulation, counterfactual prediction, individualized treatment modeling, uncertainty quantification, calibration, validation, and limitations of digital twin claims.

Please collect information to support a self-contained graduate module on digital twin concepts in oncology. Emphasize the difference between prediction, simulation, causal counterfactuals, and mechanistic explanation. Include mathematical oncology models, tumor growth and treatment response models, agent-based models, pharmacodynamic/pharmacokinetic modeling when relevant, hybrid machine-learning/mechanistic models, virtual cell ideas, patient-specific calibration, uncertainty quantification, and validation strategies. Include cancer examples in radiation/chemotherapy/immunotherapy response modeling, adaptive therapy, tumor evolution, and virtual clinical trials if appropriate.

Boundary guidance: focus on **simulation and individualized prediction of future biological or clinical states**. Do not duplicate perturbation screen analysis from Week 7, EHR risk prediction from Week 8, or generative AI agents from Week 11.

---

## Week 13 — Clinical Translation of Computational Methods in Oncology

**Deep Research prompt**

Using the general instruction above, research a module titled **Clinical Translation of Computational Methods in Oncology**.

Module story: from promising algorithm to usable clinical or scientific tool.

Scope: benchmarking, validation cohorts, external validation, prospective evaluation, model reporting standards, regulatory/ethical issues, interpretability, reproducibility, clinician adoption, workflow integration, software usability, monitoring, fairness, privacy, and post-deployment performance.

Please collect information to support a self-contained graduate module on how computational oncology methods move from papers to usable tools. Emphasize evaluation design rather than invention of a new algorithm: benchmark construction, data leakage, internal vs external validation, prospective and pragmatic evaluation, clinical utility, decision-curve analysis where appropriate, interpretability, FDA/regulatory frameworks for AI/ML software as medical device, reproducibility, model cards/reporting guidelines, governance, maintenance, monitoring, and user-centered deployment. Include examples of successful and failed translation of oncology computational tools, including diagnostics, pathology AI, genomics decision support, clinical risk models, and workflow tools.

Boundary guidance: focus on **deployment, validation, adoption, and governance**. The technical invention of methods belongs to earlier weeks; this week teaches what evidence is needed before a method can safely influence research or clinical decisions.

---

## Optional meta-prompt after all module searches

After completing the individual module searches, run this synthesis prompt:

Review the collected research notes for Weeks 2–13 of **Frontier in Computational Oncology**. Identify overlaps, gaps, and weak module boundaries. For each week, suggest:
- one sentence sharpening the module story;
- 2–3 topics to keep;
- 2–3 topics to move to another week or remove;
- one best landmark paper and one best recent review/methods paper;
- one capstone-style student project idea.

Then propose a final coherent progression across the 12 modules, making sure the course moves logically from molecular assays, to cellular/spatial systems, to genome/evolution, to networks/perturbation, to clinical/image data, to AI/foundation/generative systems, to digital twins, and finally to translation.
