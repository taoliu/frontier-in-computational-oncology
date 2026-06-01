# Week 10 — Foundation Models for Biomedical and Cancer Data — Deep Research Intake

## Source

- Deep Research doc/link: Private Deep Research attachment (not public)
- Date received: 2026-05-31
- Imported by: Claw

## Raw content

Raw file stored at `deep-research-report.md`.

## Raw content excerpt

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


[Truncated here in intake file; see `deep-research-report.md` for full content.]

## Initial triage

- Strongest sections: strong definition of foundation models as reusable pretrained representation learners rather than generic large models or copilots; good cross-modality coverage across protein, DNA/RNA, single-cell, pathology, imaging, and EHR; strong emphasis on adaptation regimes, external shift, benchmark design, and skepticism toward overbroad claims.
- Weak or missing areas: citation markers are ChatGPT Deep Research internal turn references and must be replaced with real DOI/URL citations; many 2024–2026 foundation-model and benchmark claims are fast-moving and need current verification before lecture-plan generation.
- Claims requiring validation: all must-read papers/resources and DOIs; current status of Tsang 2025 Annual Review; ProteinGym citation details; Nucleotide Transformer claims; Geneformer/scGPT/scFoundation/SCimilarity/Nicheformer; single-cell zero-shot benchmark; pathology foundation-model claims for UNI/Virchow/CHIEF/Prov-GigaPath/Neidlinger; EHRSHOT citation; scDrugMap/PerturBench and virtual-cell resources; oncology case-study performance numbers.
- Suggested source-priority level: very high — this is a fast-moving methods module where benchmark claims and model names can become stale quickly.

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
