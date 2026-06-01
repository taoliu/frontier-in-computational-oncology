# Foundation Models for Biomedical and Cancer Data

## Module overview

This module should present foundation models as **reusable pretrained representation learners** for biological and clinical data, not as generic “large models” or end-user copilots. The central story is a shift from training one model per task to pretraining on large unlabeled or weakly labeled corpora so that a single backbone can be adapted across many downstream problems in proteins, DNA/RNA, single-cell data, pathology, radiology, and EHRs. For a computational oncology course, the emphasis should be on **how these models are built, adapted, and verified**: modality-specific tokenization and schemas, self-supervised objectives, scale versus data quality, frozen embeddings versus fine-tuning, zero-shot and few-shot transfer, and benchmark design under external shift. Just as important, the module should teach skepticism: recent studies show that impressive in-distribution or fine-tuned performance can disappear under zero-shot evaluation, external cohorts, cross-center transfer, or comparison to strong simple baselines. That makes this week ideal for teaching students how to decide when a model is truly “foundation-like,” and what evidence is required before relying on it in oncology research.

## Must-read papers and resources

- **Tsang et al., 2025, *Foundation Models for Translational Cancer Biology*.** Best cancer-focused overview for framing the week. It organizes the field around modality, transfer, and translational use, and is especially useful for distinguishing oncology-relevant promise from hype. *Annual Review of Biomedical Data Science.*

- **Wornow et al., 2023, *The shaky foundations of large language models and foundation models for electronic health records*.** Essential methodological reality check. It argues that many clinical foundation-model claims rest on narrow training corpora and weak evaluation tasks, and it proposes clinically meaningful evaluation criteria. DOI: **10.1038/s41746-023-00879-8**.

- **Lin et al., 2023, *Evolutionary-scale prediction of atomic-level protein structure with a language model*.** A canonical scaling paper for protein language models. It is the clearest way to teach how masked sequence modeling can produce general-purpose protein representations and why scaling changed the field. DOI: **10.1126/science.ade2574**.

- **Notin et al., 2023, *ProteinGym: Large-Scale Benchmarks for Protein Design and Fitness Prediction*.** A core benchmarking resource for variant-effect prediction and protein fitness. It is especially useful pedagogically because it shows how to evaluate embeddings against deep mutational scanning and curated clinical annotations rather than anecdotal examples.

- **Dalla-Torre et al., 2025, *Nucleotide Transformer: building and evaluating robust foundation models for human genomics*.** The clearest genomics foundation-model paper to teach in class: models from 50M to 2.5B parameters, pretraining on 3,202 human genomes plus 850 species, and systematic downstream evaluation across genomics tasks. DOI: **10.1038/s41592-024-02523-z**.

- **Theodoris et al., 2023, *Transfer learning enables predictions in network biology*.** The landmark paper behind **Geneformer**. It is excellent for discussing how single-cell transcriptomes can be encoded as contextual gene representations and transferred to data-limited biological tasks. DOI: **10.1038/s41586-023-06139-9**.

- **Cui et al., 2024, *scGPT: toward building a foundation model for single-cell multi-omics using generative AI*.** The most widely discussed single-cell foundation-model paper, and the best entry point for generative pretraining, cell/gene embeddings, and downstream adaptation across annotation, integration, and perturbation tasks. DOI: **10.1038/s41592-024-02201-0**.

- **Kedzierska et al., 2025, *Zero-shot evaluation reveals limitations of single-cell foundation models*.** A required counterweight to the enthusiasm around single-cell FMs. It shows that zero-shot use can underperform simpler baselines, making it ideal for a lecture on verification and benchmarking. DOI: **10.1186/s13059-025-03574-x**.

- **Chen et al., 2024, *Towards a general-purpose foundation model for computational pathology*.** The **UNI** paper. A strong example of self-supervised pathology pretraining with broad downstream reuse from frozen embeddings. DOI: **10.1038/s41591-024-02857-3**.

- **Vorontsov et al., 2024, *A foundation model for clinical-grade computational pathology and rare cancers detection*.** The **Virchow** paper. Particularly useful because it ties representation learning directly to pan-cancer and rare-cancer detection claims and makes the data-scale argument explicit. DOI: **10.1038/s41591-024-03141-0**.

- **Neidlinger et al., 2025, *Benchmarking foundation models as feature extractors for weakly supervised computational pathology*.** One of the most useful verification papers in the area: 19 pathology FMs, 13 patient cohorts, external testing, and the finding that data diversity can matter more than raw volume. DOI: **10.1038/s41551-025-01516-3**.

- **Wornow et al., 2023, *EHRSHOT: An EHR Benchmark for Few-Shot Evaluation of Foundation Models*.** The best public benchmark to teach label efficiency, few-shot evaluation, and structured EHR pretrained backbones such as CLMBR-T-base. DOI: **10.52202/075280-2933**.

## Key computational problems and assumptions

### What makes a model foundation-like

For this module, a model should count as **foundation-like** if it is pretrained on a broad, heterogeneous corpus so that the learned representation can be reused across many downstream tasks with limited additional labels, often through frozen embeddings, lightweight heads, continued pretraining, or parameter-efficient tuning. A model is **not** foundation-like merely because it is deep, transformer-based, or big; a single-endpoint model trained only for one pathology biomarker or one readmission task is still a conventional predictive model. In biomedicine, this distinction matters because claims of generality frequently exceed what the evaluation actually shows.

### Core computational problems

The first problem is **data representation**. Each modality requires a different schema: amino acid tokens for proteins, nucleotide or BPE-style tokens for DNA, sequence-plus-structure priors for RNA, ranked or tokenized gene-expression profiles for cells, tile or patch hierarchies for whole-slide pathology, and longitudinal code or note sequences for EHRs. These are not cosmetic implementation choices; they define what the model can even “see,” and often determine whether transfer works at all. DNABERT and DNABERT-2 illustrate how tokenization design changes genomic model efficiency; ERNIE-RNA shows why RNA structure priors matter; and pathology models demonstrate that slide tiling and hierarchical aggregation are central, not peripheral, design decisions.

The second problem is **self-supervised objective design**. Across modalities, the main families are masked token prediction, autoregressive next-token modeling, denoising or masked reconstruction, contrastive learning, metric learning, and self-distillation. The assumption behind all of them is that predictive structure in the raw corpus overlaps with the information needed downstream. That assumption is partly true but not universal. In proteins and genomics, masked prediction can recover biologically useful sequence regularities; in pathology, DINO-style self-distillation yields reusable visual morphology embeddings; in single-cell, however, zero-shot evaluations suggest that predicting masked genes does not automatically produce embeddings superior to simpler pipelines for discovery-oriented tasks.

The third problem is **scale versus data quality and diversity**. More data often helps, but the strongest recent papers repeatedly show that corpus diversity, curation, and domain match can be as important as parameter count. Nucleotide Transformer benefited from both population-scale human genomes and multispecies data; Virchow and UNI scaled pathology pretraining dramatically; yet an external pathology benchmark found that data diversity outweighed data volume for downstream performance, while the EHR review found that many purported clinical FMs still rely on narrow or poorly matched corpora.

The fourth problem is **adaptation**. In this week, students should explicitly compare frozen embeddings plus a linear head, full fine-tuning, continued pretraining on local data, and parameter-efficient methods such as LoRA or adapter-style tuning. These choices are not interchangeable: in EHRs, continued local pretraining improved cross-hospital transfer; in pathology, many deployments treat the FM as a feature extractor plus multiple instance learning head; and in single-cell drug-response benchmarking, different models won under pooled-data, fine-tuned, and zero-shot settings.

The fifth problem is **evaluation under distribution shift**. Biomedical foundation models are almost always trained and tested under shifting institutions, assay protocols, sequencing platforms, scanners, coding systems, and patient populations. This is where many translational claims weaken. In single-cell biology, zero-shot evaluation exposed failures not visible after fine-tuning; in perturbation prediction, several deep or foundation-style models failed to beat simple linear baselines; in pathology, external multi-cohort benchmarks and robustness studies emphasize center effects; and in EHRs, cross-hospital transfer remains a major barrier.

### Assumptions worth making explicit to students

Students should be taught to interrogate six recurring assumptions. First, that pretraining corpora are representative of the cancer setting they care about. Second, that the pretraining objective captures biology rather than only co-occurrence statistics. Third, that a model that transfers after full fine-tuning will also be useful in zero-shot or few-shot settings. Fourth, that better embeddings imply better mechanistic understanding. Fifth, that gains over weak baselines imply readiness for oncology use. Sixth, that performance on public retrospective data will survive external clinical or assay shift. Recent work in single-cell, perturbation modeling, pathology, and EHRs shows that each of these assumptions can fail.

### Evidence threshold before using a foundation model in oncology research

A sensible evidence bar for oncology should include: transparent pretraining-data disclosure; comparison against strong task-specific and simple baselines; evaluation in zero-shot, few-shot, and fine-tuned regimes; external validation across institutions or assay batches; auditing for confounding variables such as medical-center or coding-system differences; and, when clinical claims are made, validation against orthogonal or clinically meaningful endpoints rather than proxy labels alone. The current literature strongly supports teaching this as a methodological requirement, not a bureaucratic afterthought.

## Main algorithms, models, and tools to teach

For **biological sequence foundation models**, teach the encoder-style masked-language family and its close relatives: **ESM-2** and **ProtTrans** for proteins; **DNABERT**, **DNABERT-2**, and **Nucleotide Transformer** for DNA; and **RNA-FM** plus **ERNIE-RNA** for RNA. The methodological emphasis should be on tokenization, context length, objective choice, and how one converts a pretrained model into downstream predictors through per-token scores, pooled embeddings, or variant-effect heads. DNABERT-2 is a useful example of BPE tokenization and ALiBi-style efficient transformers; HyenaDNA is the canonical non-attention long-context counterexample; and ERNIE-RNA is a good example of injecting biological structure priors directly into the model.

For **single-cell and perturbation foundation models**, teach **Geneformer**, **scGPT**, and **scFoundation** as the main architectural exemplars, then contrast them with **SCimilarity** and **Nicheformer** to show that not all “foundation-like” approaches are language-model clones. Geneformer emphasizes contextual gene embeddings and network biology; scGPT emphasizes generative pretraining and broad downstream adaptation; scFoundation emphasizes scale and an asymmetric transformer-like design; SCimilarity reframes the task as metric learning over atlases; and Nicheformer extends the idea toward spatial context. For practical tooling and reproducible benchmarking, **BioLLM** and the **CZI Virtual Cells Platform** are now important teaching resources.

For **pathology and image foundation models**, teach **UNI**, **Virchow**, **CHIEF**, and **Prov-GigaPath** as four distinct design patterns. UNI is the cleanest self-supervised feature extractor; Virchow demonstrates large-scale DINOv2-based pathology pretraining with strong pan-cancer evaluation; CHIEF combines unsupervised tile-level pretraining with weakly supervised whole-slide learning to produce a general-purpose cancer pathology backbone; and Prov-GigaPath shows why modeling the full whole-slide hierarchy matters for gigapixel pathology. This is also the right place to teach **multiple instance learning**, slide-level aggregation, and the growing role of **vision-language pathology models** such as CONCH, which scored especially well in an external pathology benchmark.

For **clinical text and structured EHR models**, teach the historical progression from **ClinicalBERT** to **GatorTron** for notes and from **BEHRT** and **Med-BERT** to **CLMBR-T-base/EHRSHOT** for structured timelines. These models are useful because they expose several important implementation choices: whether the input is free text or coded events; whether time is encoded explicitly; whether pretraining is masked or causal; and whether cross-institution transfer requires continued local pretraining. The EHR literature is also ideal for teaching that “foundation model” should not be granted automatically when the corpus is tiny, highly local, or only loosely connected to the deployment task.

Across all modalities, the **adaptation methods** worth teaching are frozen linear probes, shallow multilayer heads on embeddings, full fine-tuning, continued domain-adaptive pretraining, and parameter-efficient tuning such as LoRA. The **evaluation tools** worth teaching are also cross-modal: ProteinGym for protein transfer, EHRSHOT for few-shot structured EHRs, BioLLM for integrating single-cell backbones, scDrugMap and PerturBench-like resources for perturbation tasks, and external multi-cohort pathology benchmarks for feature extractors.

## Representative datasets, benchmarks, and cancer case studies

### Representative datasets and benchmarks

For **single-cell**, the most important shared resources are **CZ CELLxGENE Discover**, the **CELLxGENE Census**, and the **Human Cell Atlas**. They matter not just because they are large, but because they provide versioned, queryable, standardized corpora that make pretraining and benchmark design far more reproducible than ad hoc lab-level collections.

For **structured EHR and clinical text**, the workhorse public resources remain **MIMIC-IV**, **EHRSHOT**, and the **eMERGE** ecosystem. MIMIC-IV is the most widely used general public EHR corpus; EHRSHOT is the most directly relevant benchmark for few-shot clinical foundation-model evaluation; and eMERGE is important for thinking about portability across coding/phenotyping conventions and genomics-linked EHR studies.

For **pathology and oncology multi-omics**, core teaching datasets are **TCGA**, **CPTAC**, the **Cancer Digital Slide Archive**, and downstream public slide sets such as **PANDA** that appear repeatedly in pathology FM releases. TCGA and CPTAC remain especially valuable for teaching because they tie tissue images to genomic, transcriptomic, proteomic, and clinical endpoints.

For **protein sequence and variant-effect modeling**, **ProteinGym**, deep mutational scanning datasets, **ClinVar**, and related curated disease-variant resources are the most instructive evaluation assets. They provide much stronger validation for transfer than generic classification benchmarks because they directly test whether embeddings recover biologically meaningful fitness and pathogenicity signals.

For **genomics**, the key benchmarks to teach are **GUE** and the recent independent DNA foundation-model benchmarks that evaluate sequence classification, gene-expression prediction, variant-effect prediction, and chromatin-architecture tasks using both zero-shot embeddings and fine-tuned heads. These are important because they expose how sensitive conclusions are to the choice of sequence length, tokenization, and downstream task family.

For **single-cell perturbation modeling**, the most relevant resources are **scDrugMap**, **PerturBench**, and the 2025–2026 perturbation benchmark studies. They are useful pedagogically because they force students to confront three issues at once: sparse labels, destructive measurement, and generalization to unseen perturbations or cellular contexts.

### Cancer case studies

A strong first oncology case study is **pan-cancer and rare-cancer detection from histopathology**. Virchow achieved about **0.95 specimen-level AUC** across common cancers and also strong performance on rare cancers, which makes it a good example of how broad pathology pretraining can improve label efficiency and support pan-cancer transfer claims.

A second case study is **CHIEF** for generalizable cancer pathology. CHIEF was pretrained on more than **60,000 WSIs** spanning **19 anatomical sites** and validated on nearly **19,500 WSIs** from **24 hospitals/cohorts**, with reported gains over prior deep-learning baselines and explicit emphasis on diagnosis, molecular characterization, and prognosis. This is one of the best examples of a pathology FM designed explicitly around cancer heterogeneity and external validation.

A third case study is **foundation models for cancer imaging biomarkers** in radiology. Pai and colleagues trained a self-supervised lesion encoder on **11,467 radiographic lesions** and showed that a single pretrained representation could support multiple imaging-biomarker tasks. For this module, the main lesson is not radiology per se, but the general point that “foundation-like” value comes from transferable embeddings across endpoints, not from a custom network trained for one biomarker. DOI: **10.1038/s42256-024-00807-9**.

A fourth case study is **single-cell foundation models for cancer drug-response prediction**. In **scDrugMap**, eight single-cell FMs were benchmarked across hundreds of thousands of cells from dozens of datasets spanning tissues, drugs, and cancer conditions. The important teaching point is that the winner changed by evaluation regime: scFoundation did best in pooled-data settings, UCE improved after fine-tuning in cross-data analyses, and scGPT did best in zero-shot conditions. That makes scDrugMap a very good example of why oncology researchers should not ask which model is “best” in the abstract.

A fifth case study is **protein language models for variant interpretation relevant to cancer**. Sequence-only protein LMs have become useful for genome-wide missense variant scoring, and oncology-specific applications such as **D2Deep** are beginning to target driver-mutation prediction directly. But this is also an area where the evidence remains mixed: broad variant-effect benchmarks are strong, whereas prospective cancer-specific validation is still relatively limited. That contrast is pedagogically valuable.

A sixth case study is **clinical oncology abstraction from notes and EHRs**. Fine-tuned language models have been used to detect cancer symptoms in clinical notes and to extract complex biomarker information such as **PD-L1** from unstructured oncology records. The important computational lesson is that domain-specific fine-tuning and expert-labeled ground truth were still crucial; the PD-L1 study explicitly reported that zero-shot extraction was not effective at the model scale examined.

## Suggested three-lecture outline

### Lecture one

**Background and problem definition: from task-specific models to reusable pretrained representations.** Start by defining what “foundation-like” means in biomedical data, then walk modality by modality through the core data structures: protein sequences, genomic sequences, RNA sequences, single-cell count matrices, whole-slide images, and EHR timelines. The computational challenge to foreground is that oncology rarely offers abundant clean labels for every desired task, but it does generate enormous unlabeled corpora. Core readings: Tsang et al., Wornow et al., ESM-2, and Nucleotide Transformer.

A productive class discussion for this lecture is to ask students to classify several models as either truly foundation-like or merely transfer-learned task models, and to justify the distinction using corpus breadth, adaptation range, and evaluation design. That exercise helps avoid a common failure mode of the literature: using “foundation model” as a prestige label rather than a methodological category.

### Lecture two

**Method development and verification: objectives, architectures, and benchmark design.** This lecture should compare masked modeling, autoregressive prediction, contrastive objectives, metric learning, and self-distillation, then show how those choices map onto transformers, state-space or Hyena-style long-context models, vision transformers, hierarchical slide models, and code-based EHR transformers. The second half should be about verification: frozen embeddings versus full fine-tuning, zero-shot versus few-shot transfer, external validation, and the role of strong non-FM baselines. Core readings: ProteinGym, Geneformer, scGPT, EHRSHOT, the zero-shot single-cell benchmark, and the pathology benchmark paper.

The main methodological takeaway should be that **benchmark design is part of the method**, not an afterthought. Students should see concrete examples where the conclusion changes when moving from in-distribution fine-tuning to zero-shot evaluation, from single-center to multicenter data, or from weak internal tasks to external clinically meaningful endpoints.

### Lecture three

**Applications and the state of the field in oncology.** Use this lecture to compare positive and negative case studies. Positive examples include Virchow, CHIEF, and cancer imaging biomarker models that demonstrate meaningful transfer across cancer types and endpoints. Negative or cautionary examples include single-cell zero-shot failures, perturbation models that do not beat linear baselines, and clinical-text extraction tasks that still require supervised adaptation and expert validation. Core readings: Virchow, CHIEF, scDrugMap, the perturbation benchmark papers, and recent oncology clinical-text studies on symptoms and PD-L1 extraction.

This lecture should end with a structured “evidence bar” for oncology researchers: what must be documented, benchmarked, and stress-tested before a pretrained representation is trusted for biological discovery or translational decision support. That framing keeps the week about method development and evaluation rather than about tool enthusiasm.

## Open problems and future directions

The biggest open problem is still **how scaling laws work in biomedical data**, where corpora are smaller, more heterogeneous, and more weakly standardized than internet-scale text. The recent literature suggests that volume alone is not the answer: data diversity, population breadth, assay harmonization, and robust schema design can matter as much as raw token count.

A second major problem is **mechanistic versus statistical representation**. Many current models clearly learn useful correlations, but much less evidence shows that they capture causal regulatory logic or support strong out-of-distribution perturbation reasoning. This is most obvious in single-cell biology, where zero-shot and perturbation benchmarks have repeatedly exposed gaps between strong embedding narratives and actual generalization.

A third challenge is **robustness under real oncology shift**. Cancer data vary by center, preparation protocol, scanner, population, assay platform, and disease prevalence. Pathology and EHR studies already show that external validation and local adaptation are indispensable, and general robustness frameworks for biomedical foundation models argue that robustness testing must be tailored to a predefined deployment specification rather than treated generically.

A fourth challenge is **modality-specific inductive bias**. Pure transformer scaling is not obviously the right answer in every modality. Long genomic context motivates Hyena- or state-space-style models; RNA benefits from structural priors; single-cell data increasingly point toward spatial and atlas-aware pretraining; and pathology is moving toward whole-slide and multimodal report-aligned models rather than tile-only encoders.

A fifth challenge is **access and reproducibility**. Many top biomedical FMs rely on private pathology slides, proprietary EHR corpora, or partially released checkpoints, which makes rigorous academic comparison difficult. Resources such as EHRSHOT, CELLxGENE Census, the Human Cell Atlas, ProteinGym, and public model-integration platforms are therefore strategically important, not merely convenient.

### Open questions and limitations

Two limitations are worth stating explicitly. First, **RNA sequence foundation models** are advancing quickly, but compared with protein, DNA, pathology, and single-cell FMs, the cancer-specific evidence base is still thinner; for teaching, RNA-FM and ERNIE-RNA are presently better treated as emerging exemplars than as settled translational workhorses. Second, **oncology-specific sequence and EHR deployment evidence** remains much less mature than the pathology literature: many of the strongest sequence-model results are still validated on general biological benchmarks, and several oncology EHR applications still depend on task-specific fine-tuning rather than robust zero-shot transfer.

## Notes on boundaries

This module should include **pretrained representation learning, model adaptation, and evaluation** for biomedical and cancer data: corpus construction, tokenization and schemas, self-supervised objectives, frozen versus fine-tuned transfer, benchmark design, external validation, and failure modes across proteins, genomics, single-cell data, pathology, imaging, and EHR text. It should also include strong conventional baselines only when they are needed to test whether a foundation model is actually adding value.

It should **not** become a general deep-learning survey. Detailed coverage of generic CNNs, U-Nets, MIL variants, BERT internals, or standard single-cell preprocessing pipelines belongs elsewhere unless those topics are required to explain how a biomedical foundation model differs from older task-specific methods. Likewise, this week should not center on downstream workflow automation, interactive assistants, RAG, agent systems, prompt engineering, or hallucination control; those belong with the next module on interactive LLM systems rather than with a methods week about pretrained biological representations.

A practical way to keep the boundary sharp is to ask, for every topic: **Is the main learning objective to understand how reusable pretrained representations are constructed, adapted, and stress-tested?** If yes, it belongs here. If the main objective is building a production assistant, orchestrating tools, or deploying conversational systems on top of biomedical knowledge, it belongs in a later week.