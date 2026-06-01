# Week 06 — Gene Regulation, Networks, and Systems Oncology — Deep Research Intake

## Source

- Deep Research doc/link: Private Deep Research attachment (not public)
- Date received: 2026-05-31
- Imported by: Claw

## Raw content

Raw file stored at `deep-research-report.md`.

## Raw content excerpt

# Gene Regulation, Networks, and Systems Oncology

## Module overview

This module should teach students how to move from processed molecular measurements to mechanistic, system-level hypotheses about cancer regulation. The central idea is that tumors are not explained well by single genes alone. They are better described as regulatory circuits and signaling states that link genomic alterations, lineage context, microenvironmental inputs, and therapeutic pressure to transcriptional programs, cell states, and phenotypic plasticity. Methodologically, the module should distinguish undirected association from direct regulation, directionality from genuine causal claims, and static snapshots from dynamic or perturbation-supported models. The core data inputs are processed bulk and single-cell transcriptomes, chromatin accessibility or paired multiome data, phosphoproteomics, and perturbation readouts such as CRISPR or drug-response transcriptomics. The computational focus is method development and verification: network inference, pathway and regulon activity estimation, Bayesian and causal graphical models, dynamical systems, and perturbation-aware modeling, all tied to oncology applications such as oncogenic signaling, transcriptional addiction, tumor suppressor circuitry, immune evasion, and resistance.

## Must-read papers and resources

- **Badia-I-Mompel et al., 2023, *Nature Reviews Genetics*.** The best entry-point review for a graduate module. It organizes GRN inference by data modality and model family, with strong discussion of transcriptome-only versus multiome approaches, priors, and evaluation. It is especially useful for framing what single-cell and multiome data can, and cannot, identify. DOI: **10.1038/s41576-023-00618-5**.

- **Kelly et al., 2022, *Molecular Genetics & Genomic Medicine*, paired with Sachs et al., 2005, *Science*.** Kelly et al. is a concise review of causal discovery for molecular networks, covering assumptions behind Bayesian networks, graphical models, and intervention-based reasoning. Sachs et al. is the landmark signaling paper that made causal structure learning in cell biology concrete with multiparameter single-cell measurements. Together they are ideal for teaching what “causal” really means in this field. DOI: **10.1002/mgg3.2055** and **10.1126/science.1105809**.

- **Margolin et al., 2006, *BMC Bioinformatics*.** The landmark ARACNe paper. It teaches the mutual-information view of network inference and the use of the data processing inequality to prune indirect edges. It remains foundational for cancer master-regulator analysis and for understanding why coexpression is not enough. DOI: **10.1186/1471-2105-7-S1-S7**.

- **Huynh-Thu et al., 2010, *PLoS ONE*.** The GENIE3 paper is still one of the clearest formulations of GRN inference as supervised learning, where each target gene is predicted from candidate regulators using tree ensembles. It is an essential baseline for method comparison and for teaching feature-importance-based network inference. DOI: **10.1371/journal.pone.0012776**.

- **Aibar et al., 2017, *Nature Methods*, with the 2020 pySCENIC protocol.** SCENIC is the canonical regulon-first single-cell method: candidate TF-target links, motif-based pruning, then per-cell regulon activity via AUCell. It is indispensable for teaching why motif or chromatin support matters if one wants to move from correlation toward direct transcriptional regulation. For implementation, the scalable pySCENIC workflow is the practical companion. DOI: **10.1038/nmeth.4463**.

- **Alvarez et al., 2016, *Nature Genetics*.** This paper operationalized VIPER-style thinking at cancer scale by inferring protein activity from regulon targets rather than relying on regulator expression alone. It is central for teaching latent regulator activity, master regulators, and why raw mRNA abundance is often a weak proxy for signaling or TF activity. DOI: **10.1038/ng.3593**.

- **Schubert et al., 2018, *Nature Communications*.** The PROGENy paper is a must-read for pathway activity modeling because it uses perturbation-responsive downstream genes, not merely pathway membership. It is the clearest demonstration that pathway activity should often be treated as a latent variable inferred from footprints. DOI: **10.1038/s41467-017-02391-6**.

- **Liu et al., 2019, *npj Systems Biology and Applications*.** CARNIVAL is an excellent teaching paper for causal reasoning on signed, directed prior networks. It starts from expression footprints and contextualizes large signaling graphs into condition-specific causal subnetworks. DOI: **10.1038/s41540-019-0118-z**.

- **Dugourd et al., 2021, *Molecular Systems Biology*.** COSMOS goes one step beyond transcriptome-centered reasoning by integrating phosphoproteomics, transcriptomics, and metabolomics with prior knowledge to generate mechanistic hypotheses. This is a strong capstone paper for systems oncology because it shows how signaling, regulation, and metabolism can be connected causally. DOI: **10.15252/msb.20209730**.

- **Badia-i-Mompel et al., 2022, *Bioinformatics Advances*, paired with Müller-Dott et al., 2023, *Nucleic Acids Research*.** decoupleR provides a unified software framework for activity inference across many scoring methods, which is ideal for teaching reproducible comparison. CollecTRI expands signed TF-target priors and was benchmarked to improve perturbed-TF recovery, making it a strong modern prior resource for regulon-based inference. DOI: **10.1093/bioadv/vbac016** and **10.1093/nar/gkad841**.

- **Pratapa et al., 2020, *Nature Methods*, paired with Chevalley et al., 2025, *Communications Biology*.** This is the best benchmark pair to teach verification. Pratapa et al. benchmarked GRN inference from single-cell transcriptomic data. Chevalley et al. introduced CausalBench, a real-world perturbational benchmark for network inference from single-cell CRISPR data. Together they show why observational and perturbational benchmarks can yield different conclusions. DOI: **10.1038/s41592-019-0690-6** and **10.1038/s42003-025-07764-y**.

- **Paull et al., 2021, *Cell*, paired with TCGA Oncogenic Signaling Pathways, 2018, *Cell*.** Paull et al. is the best systems-oncology anchor for master-regulator analysis at pan-cancer scale, identifying 407 master regulators arranged into 24 conserved blocks controlling transcriptional identity. The TCGA signaling paper grounds these ideas in a canonical cohort-wide map of altered oncogenic pathways across more than 9,000 tumors. These papers keep the module tied to cancer biology rather than abstract network theory. DOI: **10.1016/j.cell.2020.11.045** and **10.1016/j.cell.2018.03.035**.


[Truncated here in intake file; see `deep-research-report.md` for full content.]

## Initial triage

- Strongest sections: strong conceptual framing from processed molecular measurements to mechanistic systems-level hypotheses; clear distinctions among association, directionality, causality, static versus dynamic models, and perturbation-supported inference; strong method coverage across GRN inference, regulon/pathway activity, Bayesian/causal graphical models, signed-prior causal reasoning, dynamics, and perturbation-aware modeling.
- Weak or missing areas: citation markers are ChatGPT Deep Research internal turn references and are not usable as final citations; several fast-moving benchmark/resource claims need current verification, especially CausalBench 2025, scGRN counts, DepMap/Chronos current details, and recent melanoma/network case studies.
- Claims requiring validation: all must-read papers/resources and DOIs; benchmark claims and dataset counts; TCGA/Paull master-regulator numerical claims; DepMap and LINCS resource descriptions; Perturb-seq/Perturb-CITE-seq counts; current prior-resource claims for OmniPath, CollecTRI, DoRothEA, TRRUST, KnockTF, and scGRN.
- Suggested source-priority level: high — this is a methods-heavy systems module with many claims about causal inference, perturbation benchmarks, and resource counts that should be validated before lecture-plan generation.

## Extraction checklist

- [ ] Landmark papers
- [ ] Recent reviews
- [ ] Current methods/tools
- [ ] Datasets/benchmarks
- [ ] Cancer case studies
- [ ] Figures/assets to recreate or cite
- [ ] Open problems
- [ ] Lecture 1 material
- [ ] Lecture 2 material
- [ ] Lecture 3 material
