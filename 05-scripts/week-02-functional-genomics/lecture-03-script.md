# Week 02 — Functional Genomics in Cancer — Lecture 3 Script

## Lecture metadata

- Module: Week 02 — Functional Genomics in Cancer
- Lecture: Lecture 3 — Application & State of the Field
- Target duration: ~30 minutes
- Target slide count: 20
- Target narration: ~90 seconds per slide
- Slide deck: `04-slides/week-02-functional-genomics/slide-text.md`, Lecture 3 section
- Voice/audio status: production text script ready for Dr. Liu review; after approval, audio synthesis should be handled separately with Dr. Liu's local Qwen3-TTS voice tool
- Validation status: first-pass validated source IDs included; use publication figures only after separate human review of licensing/fair-use context

## Teaching arc

Lecture 3 turns the assay-aware method framework into cancer interpretation. The key message is that functional genomics is most powerful when it is used as graded regulatory evidence: public atlases provide priors, cohort assays reveal regulatory programs, cistrome and enhancer analyses suggest mechanisms, and 3D maps add linkage. None of these layers automatically proves causality by itself.

## Script

### L3-01 — From methods to cancer insight

**Speaker notes**

In Lecture 1, we defined the problem: functional genomics assays are measurement systems, not direct labels. In Lecture 2, we looked at methods that transform those measurements into peaks, domains, footprints, states, and contacts. Now we use that framework to read cancer biology.

The central question for this lecture is: what changes when regulatory evidence is applied at scale? Public resources can turn thousands of assays into reusable priors. Cohort-scale cancer projects can reveal subtype-specific regulatory programs. Focused case studies can show transcription-factor rewiring, enhancer activation, enhancer hijacking, and three-dimensional enhancer connectomes.

But the caution from the first two lectures still applies. A resource annotation is not automatically causal biology. A pan-cancer accessibility peak is not automatically a validated enhancer. A contact is not automatically regulation. Our job is to ask what evidence exists, what claim it supports, and what additional evidence would be needed for a stronger mechanistic statement.

**Transition**

Before the case studies, let’s set up a simple checklist for reading applications.

### L3-02 — The application checklist

**Speaker notes**

For application papers, I want students to use three questions. First, what resource or cohort produced the regulatory evidence? A public atlas, a cancer cohort, a curated database, and a focused experiment each have different strengths and weaknesses.

Second, what assay object and model created the feature? Was the feature a ChIP-seq peak, an ATAC-seq accessible region, a cCRE label, a super-enhancer cluster, or a HiChIP contact? Each one carries different assumptions from the previous lecture.

Third, what cancer claim is justified by the evidence? Some claims are descriptive: this tumor subtype has a distinct accessibility profile. Some are mechanistic hypotheses: this transcription factor may drive a state. Some are stronger causal claims: perturbing this enhancer changes oncogene expression or phenotype. The language should match the evidence level.

This checklist is deliberately repetitive. In cancer genomics, it is easy to get impressed by a colorful browser plot or a large cohort heatmap. The checklist slows us down and asks whether the biological claim is actually supported.

**Transition**

The first application layer is the public regulatory atlas.

### L3-03 — Public atlases are reusable priors

**Speaker notes**

Public regulatory atlases are one of the major achievements of functional genomics. ENCODE and related projects organized many assays across many biosamples so that individual experiments can be interpreted in a broader regulatory context. Instead of treating each new cancer dataset as isolated, we can compare it with known chromatin states, candidate promoters, enhancers, insulators, and other regulatory evidence.

The key phrase is reusable prior. A public atlas can tell us that a genomic region has evidence of regulatory activity in some biosamples. It can suggest whether a region looks promoter-like, enhancer-like, CTCF-associated, or accessible. That is extremely useful for prioritization and interpretation.

But a prior is not a final answer. A candidate cis-regulatory element is candidate evidence. It does not mean the element is active in every tumor, regulates the nearest gene, or is required for a phenotype. Public atlases help us ask better questions, but they do not remove the need to inspect cancer-specific data.

**Transition**

That distinction is especially important when we use SCREEN and cCRE labels.

### L3-04 — SCREEN and cCRE language

**Speaker notes**

SCREEN and the candidate cis-regulatory element registry make regulatory annotations searchable and reusable. For teaching, this is a very good example of evidence aggregation. A cCRE label is built from combinations of signals, such as accessibility, promoter-associated marks, enhancer-associated marks, and CTCF-related evidence.

The benefit is standardization. Instead of every paper inventing a different label for candidate regulatory regions, the registry gives a shared vocabulary. Students can look up a locus and ask what evidence exists in which biosamples.

The danger is over-reading the label. The word candidate should stay visible. Candidate enhancer-like signature is not the same as perturbation-validated enhancer. A cCRE near a cancer gene is not automatically the causal regulatory element for that gene. The label is an evidence summary, not a replacement for biological validation.

This is the same evidence-language discipline from Lecture 1. The stronger the claim, the more layers we need: cancer-specific activity, target-gene evidence, contact or expression support, and ideally perturbation.

**Transition**

A second resource layer is public chromatin-data reuse through Cistrome.

### L3-05 — Cistrome turns public data into hypotheses

**Speaker notes**

Cistrome resources show another kind of application. Instead of only defining regulatory elements, they organize public chromatin datasets — ChIP-seq, ATAC-seq, DNase-seq, and related assays — so researchers can reuse them for regulatory hypotheses. Cistrome Cancer then connects this regulatory-data reuse more directly to cancer questions.

This is powerful because many cancer projects do not have the budget or time to profile every transcription factor, histone mark, or cell state from scratch. Public data can suggest which transcription factors may be active, whether a candidate enhancer has supporting evidence in related samples, or whether a regulatory program appears across datasets.

But reuse is only as good as the metadata and quality control. Was the biosample relevant? Was the antibody specific? Was the assay processed consistently? Does the cancer context match the question? Public data are not magic background knowledge. They are experiments with provenance, bias, and uncertainty.

Used carefully, Cistrome-style resources turn scattered experiments into hypothesis engines. Used carelessly, they can turn mismatched public tracks into misleading stories.

**Transition**

So before we move to cancer cohorts, let’s make the limitation of resource use explicit.

### L3-06 — Resource use is not shortcut biology

**Speaker notes**

Public resources are incredibly useful, but they are not shortcut biology. A common mistake is to find a track that supports a preferred story and treat it as confirmation. That is not enough. We need to ask whether the track is from the right cell type, the right disease context, the right assay quality, and the right processing logic.

For example, an enhancer mark in an unrelated cell line may suggest a region is capable of regulatory activity, but it does not prove activity in a patient tumor. A TF ChIP-seq peak from one model system may suggest a possible binding site, but it does not prove occupancy in another cancer state. A cCRE label may help prioritize a region, but it does not prove target-gene regulation.

The best use of resources is as context. They help nominate candidates, compare evidence, and design follow-up. They are strongest when combined with cancer-specific data from the study itself.

This resource discipline will matter in every case study that follows.

**Transition**

Now let’s look at cohort-scale cancer accessibility, starting with pan-cancer ATAC-seq.

### L3-07 — Pan-cancer ATAC-seq maps regulatory state

**Speaker notes**

The TCGA pan-cancer ATAC-seq study is a good example of moving from assay to cancer state. Instead of profiling a single locus or cell line, it measured chromatin accessibility across hundreds of primary tumors from many cancer types. The output is not just a list of peaks. It is a regulatory matrix across samples.

That matrix lets us ask questions that mutation calls alone cannot answer. Which accessible elements are shared across tumor types? Which are subtype-specific? Which accessibility patterns correspond to lineage programs, immune or stromal signals, or noncoding regulatory activity? Which transcription-factor motifs are associated with particular cancer states?

This is where ATAC-seq becomes a cohort-level biological variable. Accessibility is still a measurement, and peaks are still candidates. But across many tumors, patterns of accessibility can reveal regulatory structure that is hard to see from coding mutations alone.

The study also gives students a template: define candidate regulatory elements, compare them across tumor contexts, connect them to motifs and genes cautiously, and interpret the result as regulatory state evidence.

**Transition**

The important question is what this adds beyond ordinary mutation-centric analysis.

### L3-08 — What pan-cancer accessibility adds

**Speaker notes**

Pan-cancer accessibility adds several things. First, it can highlight active regulatory elements in noncoding regions. Many cancer mechanisms involve enhancers, promoters, insulators, and lineage-defining regulatory programs, not only coding mutations.

Second, accessibility can help interpret risk loci and noncoding associations. If a risk-associated region is accessible in a relevant cancer type or subtype, that gives a plausible regulatory context for follow-up. It still does not prove function, but it makes the hypothesis more concrete.

Third, accessibility can define subtype programs. Tumors with similar mutation profiles may occupy different regulatory states. Conversely, tumors from different tissues may share regulatory programs. This is why cohort-level regulatory maps can change how we think about cancer identity.

The careful wording is that ATAC-seq maps candidate regulatory activity. It tells us where chromatin is accessible and how that accessibility varies. Turning that into enhancer function, target-gene regulation, or therapeutic vulnerability requires additional layers.

**Transition**

A focused transcription-factor example makes this point even sharper.

### L3-09 — AR cistrome rewiring in prostate cancer

**Speaker notes**

The androgen receptor case in prostate cancer teaches that transcription-factor binding is not fixed by the DNA sequence alone. AR recognizes motifs, but the sites it occupies can change dramatically between normal prostate tissue and tumor contexts. Pomerantz and colleagues showed extensive AR cistrome reprogramming during human prostate tumorigenesis.

This is a powerful cancer lesson. If we only looked for AR motifs, we would miss the state-specific binding program. The motif may be present in many places, but occupancy depends on chromatin accessibility, cooperating factors, lineage context, and disease state. FOXA1 and HOXB13 are part of the reported reprogramming context in this case.

So the biological claim is not simply that AR exists or that AR motifs exist. The claim is that the regulatory landscape changes where AR binds, and that this rewiring is connected to prostate tumorigenesis. Functional genomics makes that visible.

This is also a reminder that TF programs in cancer can change without a simple coding mutation in the transcription factor itself.

**Transition**

From that example, we can extract a more general lesson about TF rewiring.

### L3-10 — The lesson from TF rewiring

**Speaker notes**

The general lesson is that transcription-factor activity is contextual. Motif sequence is necessary for many binding events, but it is not sufficient. Chromatin accessibility, histone state, pioneer factors, cooperating transcription factors, and cancer lineage state all shape which motifs become occupied.

This is why cistrome analysis is so useful. A cistrome is the genome-wide binding landscape of a factor. When that landscape changes between normal and cancer states, it can suggest a mechanism for altered gene regulation.

But again, the claim should be graded. A tumor-specific TF peak suggests altered occupancy. Nearby expression changes suggest possible target genes. Perturbation of the factor, enhancer, or target gene is needed for stronger causal statements.

For students, the practical habit is to avoid saying “the motif is enriched, therefore the factor drives the program.” A better statement is: motif enrichment and chromatin evidence nominate a TF program; binding and perturbation evidence determine how strong that nomination is.

**Transition**

Regulatory identity can also be studied through enhancer clusters and super-enhancer states.

### L3-11 — Super-enhancers as regulatory identity markers

**Speaker notes**

Super-enhancer studies ask a different but related question: where are the strongest clusters of enhancer-associated activity, and what genes or transcriptional circuits do they mark? In neuroblastoma, studies of super-enhancer-associated states helped define regulatory identities and heterogeneity.

This matters because tumors are not only collections of mutations. They also occupy cell states. In neuroblastoma, regulatory circuitry and enhancer landscapes can distinguish state-like programs that help explain heterogeneity. Those states may be connected to lineage identity, differentiation, and tumor behavior.

For teaching, the point is not to memorize one super-enhancer definition. The point is that enhancer intensity and clustering can act as a window into regulatory identity. If a cancer cell state depends on a particular transcriptional circuitry, the enhancer landscape can help reveal it.

This is a strong example of functional genomics as state biology rather than just locus annotation.

**Transition**

At the same time, super-enhancer claims need careful interpretation.

### L3-12 — Interpreting super-enhancer claims carefully

**Speaker notes**

Super-enhancer language can become overconfident. These calls often depend on ranking enhancer-associated signals and sometimes stitching nearby enhancers into larger clusters. Choices about ranking, stitching distance, signal type, and cutoff can affect which regions are labeled.

Therefore, a super-enhancer call suggests a strong enhancer-associated regulatory region, but it is not automatically proof of dependency. It is better to treat it as prioritized regulatory evidence. The claim becomes stronger when the region is linked to expression of a relevant gene, conserved across models or tumors, associated with a coherent transcriptional program, or supported by perturbation.

This is another place where graded language helps. We can say super-enhancer-associated state, candidate dependency, or regulatory circuitry hypothesis. We should reserve stronger causal language for experiments that actually test the dependency.

In cancer biology, this caution matters because super-enhancer stories can quickly become therapeutic vulnerability stories. That step requires evidence beyond ranking a signal track.

**Transition**

Next, let’s move from enhancer strength to enhancer position: enhancer hijacking.

### L3-13 — Enhancer hijacking: structural variation meets regulation

**Speaker notes**

Enhancer hijacking is one of the clearest examples of why cancer genomics needs regulatory interpretation. A structural variant can move an enhancer or super-enhancer into a new neighborhood, placing it near an oncogene. The coding sequence of the oncogene may be unchanged, but its regulation changes.

In medulloblastoma, enhancer hijacking was shown to activate GFI1-family oncogenes. The story requires integration. Structural variation shows that the genome has been rearranged. Regulatory evidence shows that strong enhancer activity exists in the new neighborhood. Expression evidence shows that the oncogene is activated.

This is not just a peak-calling result. It is a mechanism assembled from multiple evidence layers. The enhancer is important because of where it is, what activity it carries, and what gene expression pattern follows the rearrangement.

Enhancer hijacking is therefore a bridge between cancer genome structure and functional regulatory state.

**Transition**

A leukemia example shows that the same logic applies beyond solid tumors.

### L3-14 — BCL11B enhancer hijacking in leukemia

**Speaker notes**

The BCL11B enhancer-hijacking example in lineage-ambiguous leukemia extends the same principle. Here, enhancer hijacking drives oncogenic BCL11B expression through aberrant regulatory activation. The key point is that the oncogenic event is regulatory.

This is important for computational oncology because a mutation-centric view can miss the mechanism. If the coding region is not the main altered object, we need to inspect genome structure, chromatin activity, allele-specific regulation, and expression. Functional genomics provides the evidence layers that make the mechanism visible.

This example also reinforces the difference between proximity and regulation. A rearrangement may place elements near each other, but the biological story becomes convincing when regulatory activity and gene expression move together, and stronger still when perturbation or allele-specific evidence supports the model.

So enhancer hijacking is not just a dramatic genome cartoon. It is an evidence-integration problem.

**Transition**

The next layer is three-dimensional genome mapping, which generalizes enhancer-gene linkage across cancers.

### L3-15 — 3D genome maps add enhancer-connectome evidence

**Speaker notes**

Three-dimensional genome maps add another layer to cancer regulatory interpretation. H3K27ac HiChIP and related assays can profile contacts involving active enhancer-associated chromatin. Recent primary-cancer 3D genome maps use this logic to study enhancer connectomes across tumor samples.

The value is that enhancer-promoter linkage becomes more direct than nearest-gene annotation. A distal enhancer may contact a promoter that is not the closest gene. A cancer state may gain or rewire enhancer usage at oncogenes. These patterns can suggest regulatory mechanisms that one-dimensional peak tracks alone might miss.

But the caution from Lecture 1 still applies. A contact is linkage evidence, not automatic causality. The strongest interpretation combines chromatin activity, contact evidence, gene expression, cancer context, and ideally perturbation.

The application lesson is that 3D data help move from “there is a candidate enhancer” to “this enhancer is spatially linked to this promoter in this cancer context.” That is a stronger statement, but still not final proof by itself.

**Transition**

Let’s turn that into a general evidence chain from peaks to enhancer connectomes.

### L3-16 — From peaks to enhancer connectomes

**Speaker notes**

A practical evidence chain looks like this. Accessibility or histone marks identify candidate regulatory elements. Motifs or TF binding suggest possible regulators. Contact maps suggest which promoters those elements may physically interact with. Expression data ask whether the candidate target gene changes in the relevant context. Perturbation asks whether disrupting the element, regulator, or contact changes the outcome.

Each layer answers a different question. Peak or mark: where is candidate activity? Motif or binding: which regulatory proteins may be involved? Contact: which promoter is spatially linked? Expression: which genes are associated? Perturbation: what is causal?

This chain is a useful way to write and critique papers. If a paper claims an enhancer regulates an oncogene, ask which parts of the chain are present and which are inferred. Missing layers do not make the study worthless, but they should weaken the language.

Good computational oncology is often the art of making this evidence chain explicit.

**Transition**

Even with strong evidence chains, bulk functional genomics has important limits.

### L3-17 — Bulk functional genomics still has limits

**Speaker notes**

Bulk functional genomics remains valuable, but it has limits. A tumor sample can contain cancer cells, stromal cells, immune cells, normal tissue contamination, and multiple tumor subclones. A bulk ATAC-seq or ChIP-seq profile averages across that mixture.

Sometimes the average is exactly what we want, especially for cohort-scale signatures. But sometimes it hides the biology. A rare resistant subclone may be diluted. A spatial niche may disappear in the average. An immune-cell signal may be mistaken for tumor-intrinsic regulation. A subtype-associated pattern may reflect sample composition rather than a mechanism inside cancer cells.

This does not invalidate bulk studies. It tells us how to interpret them. Bulk assays are strong for deep coverage, mature QC, and cohort-scale priors. They are weaker when the question requires cell-state resolution, spatial location, or causal networks inside heterogeneous tissue.

Those limitations set up the next modules in the course.

**Transition**

So the natural handoff is to single-cell, spatial, and network approaches.

### L3-18 — Natural handoff to single-cell and spatial modules

**Speaker notes**

The handoff from Week 2 is natural. Single-cell chromatin and transcriptomic assays ask which cell states carry a regulatory program. They help separate tumor cells from immune and stromal cells, and they can reveal rare or transitional states that bulk assays average together.

Spatial methods ask where those states and signals occur in tissue. A regulatory program may matter because it appears at an invasive edge, in a hypoxic niche, near immune cells, or in a treatment-resistant region. Bulk assays usually cannot answer that location question.

Network and causal modeling ask how regulatory elements, transcription factors, pathways, and phenotypes connect into systems. Functional genomics provides many of the features and priors for those models, but the models have to represent uncertainty and causality carefully.

So Week 2 is not isolated. It is the foundation for later modules: understand the assay object, model it carefully, and carry forward evidence with the right strength of language.

**Transition**

Before we finish, here is a checklist students can use when reading cancer functional-genomics papers.

### L3-19 — A reading checklist for cancer papers

**Speaker notes**

When reading a cancer functional-genomics paper, translate every major claim back to the evidence. If the paper says enhancer, ask whether it means accessible region, H3K27ac peak, cCRE, super-enhancer cluster, contact-linked element, or perturbation-validated enhancer.

Separate candidate, linked, active, and validated. Candidate means there is some regulatory evidence. Linked means there is spatial, expression, or annotation evidence connecting it to a gene. Active means the assay supports activity in the relevant context. Validated means an experiment tested function.

Also ask what would change the authors’ conclusion if removed. If the key conclusion depends entirely on nearest-gene assignment, that is weaker than a conclusion supported by contacts and expression. If it depends entirely on motif enrichment, that is weaker than binding or perturbation evidence.

This checklist is not meant to make students cynical. It is meant to make them precise. Precision is what lets functional genomics become real cancer biology rather than decorative genome tracks.

**Transition**

Now we can synthesize Week 2 as a whole.

### L3-20 — Week 2 synthesis

**Speaker notes**

The synthesis for Week 2 is that functional genomics turns molecular readouts into regulatory evidence. ChIP-seq, ATAC-seq, CUT assays, and contact assays each measure different objects. Methods transform those objects into peaks, domains, states, footprints, and contacts. Applications use those outputs to interpret cancer regulatory biology.

The major cancer insights include subtype regulatory programs, transcription-factor cistrome rewiring, super-enhancer-associated identity states, enhancer hijacking, and three-dimensional enhancer linkage. These are mechanisms that mutation lists alone can miss.

But the evidence language must stay disciplined. A peak is not automatically an enhancer. A motif is not binding. A contact is not regulation. A public annotation is not causal proof. Strong interpretation comes from assay-aware methods, reproducibility, calibration, orthogonal evidence, and graded claims.

That is the foundation we will carry into the rest of the course. Later modules will add single-cell resolution, spatial tissue context, network modeling, perturbation screens, imaging, clinical informatics, foundation models, and AI agents. The core habit remains the same: know what was measured, know how it was modeled, and say only what the evidence supports.

## Audio synthesis notes

- Preferred voice: lecturer-style, calm, clear, moderately paced.
- Production target: approximately 90 seconds per slide; synthesize audio only after Dr. Liu reviews and confirms this script, using Dr. Liu's local Qwen3-TTS voice tool rather than OpenAI TTS.
- Autoplay pause: 1 second between slides in HTML delivery.
- Pronunciation notes:
  - ChIP-seq: “chip seek”
  - ATAC-seq: “attack seek”
  - CUT&RUN: “cut and run”
  - CUT&Tag: “cut and tag”
  - Hi-C: “high C”
  - HiChIP: “high chip”
  - H3K27ac: “H three K twenty-seven acetylation”
  - cCRE: “candidate cis-regulatory element” or “C C R E” after first definition
  - Cistrome: “sis-trome”
  - TCGA: “T C G A”
  - ATAC: “attack”
  - AR: “A R”
  - FOXA1: “fox A one”
  - HOXB13: “hox B thirteen”
  - GFI1: “G F I one”
  - BCL11B: “B C L eleven B”
  - HMMRATAC: “Hummer attack”
  - FRiP: “frip,” fraction of reads in peaks
- Sections to synthesize:
  - Do not synthesize audio until Dr. Liu approves this Lecture 3 production script; Dr. Liu will handle voice synthesis separately with local Qwen3-TTS.
