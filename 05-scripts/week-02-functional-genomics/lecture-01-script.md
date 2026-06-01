# Week 02 — Functional Genomics in Cancer — Lecture 1 Script

## Lecture metadata

- Module: Week 02 — Functional Genomics in Cancer
- Lecture: Lecture 1 — Background & Problem Definition
- Target duration: ~30 minutes
- Target slide count: 20
- Target narration: ~90 seconds per slide
- Slide deck: `04-slides/week-02-functional-genomics/slide-text.md`, Lecture 1 section
- Voice/audio status: production text script ready; audio synthesis handled separately by Dr. Liu with local Qwen3-TTS voice tool
- Validation status: first-pass validated source IDs included; figures remain placeholders

## Teaching arc

This lecture should make one idea unavoidable: bulk functional genomics assays are not magic enhancer detectors. They are measurement systems. Each assay produces a different statistical object, and every downstream biological claim depends on how we model signal, background, reproducibility, calibration, and evidence integration.

## Script

### L1-01 — Functional Genomics in Cancer

**Speaker notes**

Today we start Week 2, functional genomics in cancer. The most important message for this lecture is that regulatory genomics assays are measurement systems. They do not directly hand us labels like active enhancer, causal transcription factor, or oncogenic loop. They give us molecular observations: sequencing reads, paired fragments, enriched domains, and contact counts. Everything after that is inference.

That matters because the same genome browser picture can be over-interpreted very easily. A tall ChIP-seq peak can look convincing, but it may reflect target binding, local background, antibody behavior, copy number, mappability, or a broad chromatin state. An ATAC-seq peak can suggest accessibility, but accessibility is not automatically function. A chromatin contact can suggest proximity, but proximity is not automatically regulation.

So this lecture is not a software tour. We will mention tools, but the deeper goal is to build habits of interpretation. For every result, ask what was measured, what model transformed the measurement into a call, and what evidence supports the biological claim. Those questions will carry into the method-development lecture and then into the cancer case studies.

**Transition**

Let’s begin with why cancer biology needs these assays at all, even in a world with excellent mutation calls.

### L1-02 — Why mutations are not enough

**Speaker notes**

Cancer genomics often begins with mutation calls: point mutations, copy-number changes, structural variants, and fusions. Those are essential. But they are not the full explanation of cancer behavior. Two tumors can share similar coding alterations and still occupy very different cell states. A tumor can change lineage program, immune visibility, enhancer activity, or transcription-factor dependence without acquiring a clean new coding mutation that explains the shift.

Functional genomics fills that gap by asking when and where the genome is active. Which promoters and enhancers are open? Which transcription factors are bound? Which chromatin domains look active or repressed? Which distal regulatory elements physically contact candidate target genes? These questions connect genotype to regulatory state.

In cancer, this is not abstract. Pan-cancer ATAC-seq reveals subtype-specific accessibility programs. Prostate tumors can rewire the androgen receptor cistrome. Neuroblastoma can occupy super-enhancer-associated regulatory states. Enhancer hijacking can activate an oncogene without changing its coding sequence. So the mutation list is a starting point, but functional genomics helps explain regulatory mechanism.

**Transition**

To use that evidence well, we need a disciplined framework before we choose software.

### L1-03 — Three questions before software

**Speaker notes**

Before choosing a tool, I want you to ask three questions. First, what is the observed statistical object? Is it a pileup of ChIP-seq reads, paired-end ATAC fragments, a broad histone-mark domain, a motif-centered cut-site pattern, or a sparse contact matrix? These objects are not interchangeable, and treating them as interchangeable is the beginning of many bad analyses.

Second, what is signal versus background? A peak is only meaningful relative to an expectation. That expectation may depend on mappability, GC content, open chromatin, local copy number, antibody behavior, transposase bias, enzyme tethering, or genomic distance. A flat background model is often too simple for cancer regulatory data.

Third, how do we know the call is reproducible and biologically interpretable? A tall pileup in one sample is not enough. We need quality control, replicate consistency, calibration, and ideally orthogonal evidence. If you keep these three questions in mind, the rest of this module becomes easier: different methods are different answers to the same interpretive problem.

**Transition**

Now let’s compare the major assay families and the objects they produce.

### L1-04 — Assay chemistry defines the data object

**Speaker notes**

The first discipline is to let assay chemistry define the computational object. ChIP-seq starts with crosslinked or native chromatin, fragments it, enriches DNA associated with a target protein or histone mark, and produces a one-dimensional enrichment profile. We often summarize that profile as peaks or domains.

ATAC-seq is different. Tn5 transposase inserts into accessible DNA, and with paired-end sequencing we observe fragments of different lengths. The short fragments and nucleosome-length fragments carry different information about chromatin structure.

CUT&RUN and CUT&Tag are different again. They tether an enzyme near the target and generate localized cleavage or tagmentation signal, often with lower background and sharper signal geometry than classical ChIP-seq.

Contact assays, including Hi-C and HiChIP-like methods, observe pairs of genomic loci that were close in three-dimensional space. Their object is not a peak track but a contact count or contact matrix. The takeaway is simple: assay chemistry determines what random variable we model.

**Transition**

That shared track-like view is exactly where interpretation can go wrong, so next we will look at why genome-browser tracks can mislead.

### L1-05 — Genome tracks can mislead

**Speaker notes**

Genome browser tracks are powerful, but they are also dangerous. They make different assays look more similar than they really are. A ChIP-seq track, an ATAC-seq track, a CUT&Tag track, and an input-control track can all appear as hills and valleys over the genome. Visually, they invite the same interpretation: high means important, low means unimportant.

But the underlying measurements are different. In ChIP-seq, height reflects enriched fragments associated with an antibody target. In ATAC-seq, height reflects transposase-accessible DNA. In CUT assays, signal depends on tethered enzyme activity and cleavage or tagmentation behavior. Some regions show anomalous signal across many assays because of mappability, repeats, or other artifacts.

So the browser view is not the analysis. It is a useful visualization of data after many assumptions have already entered. When students read a paper, they should ask what assay produced the track, what normalization was applied, what background was expected, and whether the visible pattern survived a formal calling and reproducibility procedure.

**Transition**

Once we stop trusting the picture alone, the next question is what each enrichment signal is being compared against.

### L1-06 — Enrichment assays ask: enriched over what?

**Speaker notes**

ChIP-seq and CUT-based assays are enrichment experiments. In ChIP-seq, we enrich DNA fragments associated with a protein or histone mark. In CUT&RUN and CUT&Tag, we localize cleavage or tagmentation near a target. In both cases, the biological story begins with enrichment: more signal here than expected.

But that phrase, more than expected, is doing most of the work. Expected under what model? A genome-wide background? A local background? An input control? A sparse background appropriate for CUT&RUN? A broad-domain expectation for a histone mark? These choices change which regions are called and how confident we are.

MACS is a classic example because it made local background central for ChIP-seq peak calling. SEACR and GoPeaks illustrate that CUT assays may need different assumptions because their signal and background structure differ. So when we say a peak is significant, we are really saying it is significant under a particular model of enrichment and background.

**Transition**

After defining background, we also have to ask what kind of signal shape the assay and target should produce.

### L1-07 — Peak shape is biological and statistical

**Speaker notes**

Not all peaks have the same shape, and shape is both biological and statistical. A transcription factor often produces focal enrichment around binding sites. A histone modification such as H3K27ac may appear around active enhancers and promoters, while marks such as H3K27me3 or H3K36me3 can occupy broader domains. CUT&Tag histone-mark data can also produce patterns that differ from classical ChIP-seq.

This is why one peak caller is not appropriate for every assay or target. MACS-style reasoning is very effective for many narrow enrichment events. SICER was designed for broader spatial clustering of histone-mark enrichment. GoPeaks was motivated in part by peak calling for CUT&Tag histone modifications.

The biological consequence is important. If we force a broad regulatory domain into a narrow-peak model, we may fragment the biology. If we use a broad-domain model on focal TF binding, we may blur precise binding events. Method choice encodes a hypothesis about signal shape.

**Transition**

With peak shape in mind, ATAC-seq deserves special treatment because its fragments encode more than simple open-versus-closed chromatin.

### L1-08 — ATAC-seq is accessibility plus fragment structure

**Speaker notes**

ATAC-seq is often summarized as open chromatin, but computationally it is richer than a simple accessibility track. Tn5 inserts into accessible DNA. With paired-end sequencing, we observe fragment lengths. Very short fragments tend to come from nucleosome-free DNA, while longer fragments reflect mono-nucleosome or di-nucleosome protected DNA.

That fragment structure matters. HMMRATAC explicitly uses different fragment classes to infer chromatin states from ATAC-seq. It treats the data not as one undifferentiated pileup, but as multiple coverage layers that together describe nucleosome-free and nucleosome-associated regions.

At the same time, we should be careful with interpretation. Accessibility is a measurement, not a final annotation. An accessible locus may be a promoter, enhancer, insulator, poised element, artifact, or cell-mixture signal. It does not automatically tell us which transcription factor is bound or whether the region is functional. ATAC-seq is powerful because it gives an entry point into regulatory state, but it still requires modeling and evidence integration.

**Transition**

Once accessibility is measured, the next temptation is to infer transcription factors, so we need to separate motifs, footprints, and binding.

### L1-09 — Motifs and footprints are not the same as binding

**Speaker notes**

A common temptation in ATAC-seq analysis is to move too quickly from accessibility to transcription-factor binding. We need to separate three ideas. Motif occurrence means the sequence could be recognized by a transcription factor. Footprinting means the cut-site pattern around that motif may show protection or altered accessibility. Actual binding or occupancy is a stronger claim.

The problem is that Tn5 does not cut uniformly. Sequence bias, local chromatin context, and enzyme behavior shape the cut pattern. A footprinting method therefore has to distinguish a true occupancy-related pattern from technical bias and from generic accessibility.

Methods such as TOBIAS are useful teaching examples because they explicitly model bias-aware ATAC footprinting. But the larger lesson is about language. Motif enriched, footprint detected, and transcription factor bound should not be treated as synonyms. In cancer, where cell states and copy-number changes can be complex, careful language matters even more.

**Transition**

The same caution about evidence applies when we leave linear tracks and move to three-dimensional contacts.

### L1-10 — Contact assays measure proximity, not causality

**Speaker notes**

Contact assays move us from one-dimensional genome tracks into three-dimensional genome organization. Hi-C, HiChIP, PLAC-seq, and related methods observe pairs of loci that were close enough in the nucleus to be ligated and sequenced. That is extremely valuable because many regulatory elements act over distance.

But contact data have a dominant background: genomic distance. Loci that are nearby along the linear genome tend to contact more often. Capture design, restriction sites, sequencing depth, mappability, and chromatin state also affect contact counts. So a raw contact count is hard to interpret by itself.

This is why methods such as FitHiC2 and MAPS use distance-aware or assay-aware models to call significant contacts. Even then, the language should be cautious. A contact provides spatial linkage evidence. It does not prove that the enhancer regulates the gene, or that disrupting the contact would change expression. For causal claims, we need additional evidence.

**Transition**

Those background issues become even sharper in cancer genomes, where the genome itself is often rearranged or copy-number altered.

### L1-11 — Cancer genomes make background harder

**Speaker notes**

Cancer data make background modeling harder than many textbook examples. Tumors have copy-number gains and losses. Amplified regions can create more reads even when the underlying regulatory activity is not proportionally higher. Structural rearrangements can move regulatory elements into new neighborhoods. Tumor purity and stromal or immune admixture can make a bulk signal look like a tumor-intrinsic state when it is partly a mixture of cells.

There are also general genomic artifacts. Some regions are difficult to map or repeatedly show anomalous signal in many sequencing assays. The ENCODE blacklist is a practical response to that problem: it identifies regions that can create misleading high signal across experiments.

So in cancer functional genomics, background is not just a technical nuisance. It is part of the biological and statistical model. If we ignore copy number, mappability, cell mixture, or local genomic context, we can convert artifacts into apparently compelling regulatory stories.

**Transition**

Because cancer creates so many structured biases, controls are necessary — but we should treat them as models rather than guarantees.

### L1-12 — Controls help, but they are models

**Speaker notes**

Controls are essential, but they are not magic. An input control in ChIP-seq estimates non-target signal from fragmentation, sequencing, copy number, mappability, and genomic background. It helps distinguish target-associated enrichment from general genomic bias.

But a control also has assumptions. Does the input sample match the ChIP sample well? Does it capture the same copy-number landscape? Does it represent local chromatin accessibility or only generic sequencing background? CUT&RUN and CUT&Tag have different background behavior, so the right control strategy may differ. ATAC-seq often does not have a direct input-control equivalent. Contact assays require distance and capture-aware expectations rather than a simple one-dimensional input track.

Therefore, when reading a paper, do not ask only whether a control exists. Ask what the control is supposed to represent, what biases it captures, what biases it misses, and how the method uses it. Control choice is a modeling decision.

**Transition**

Even with controls in place, we still need to know whether the experiment was good enough to support interpretation.

### L1-13 — QC is evidence, not paperwork

**Speaker notes**

Quality control is often treated as administrative paperwork, but it is actually part of the evidence. If the library has low complexity, then apparent peaks may reflect duplication rather than biology. If ATAC-seq has poor TSS enrichment, then the assay may not be capturing accessible regulatory structure well. If ChIP-seq lacks the expected strand cross-correlation pattern, the protein-binding signal may be weak or noisy.

FRiP, the fraction of reads in peaks, is another useful but context-dependent summary. Blacklist filtering removes regions that repeatedly create artifacts. ENCODE-style pipelines are useful examples not because they are perfect for every context, but because they make QC, provenance, and reproducible processing explicit.

The practical message is that QC is not separate from interpretation. A regulatory claim built on poor-quality data should be weaker. A result that passes thoughtful QC and remains stable through filtering has a stronger evidentiary foundation.

**Transition**

Quality in one library is only the first step; next we ask whether the strongest signals are stable across replicates.

### L1-14 — Replicates test stability of ranked evidence

**Speaker notes**

Replicates are not just a box to check. They test whether the evidence is stable. Two peak lists can overlap, but overlap alone may not capture whether the strongest signals are reproducible. IDR-style thinking, developed for high-throughput experiments and adopted in ENCODE-style workflows, focuses on rank consistency across replicates.

This is especially important because functional genomics produces many candidate regions. Some are strong, stable, and biologically plausible. Others are marginal, sample-specific, or technical. Replicates help us separate robust signal from fragile signal.

For students, the language matters. A peak observed in one sample is a candidate. A peak supported by good QC and reproducible rank behavior is stronger. A regulatory element supported across assays, cohorts, and perturbation evidence is stronger still. Reproducibility is therefore not an afterthought. It is one of the steps that turns a readout into a claim.

Think of this as asking whether the experiment can find the same strongest regions twice. If the answer is no, then downstream motif analysis, enhancer annotation, and target-gene linking are all standing on unstable ground.

**Transition**

If reproducibility tells us which signals are stable, calibration asks whether the reported confidence scores mean what we think they mean.

### L1-15 — Significance is not always calibrated

**Speaker notes**

Even after peak calling, we should be careful with significance. A peak caller reports scores or P values under a model. If the model assumptions are imperfect, those values may not be well calibrated. In other words, a nominal P value may not correspond to the false-positive behavior we think it does.

RECAP is useful here because it directly addresses calibration of ChIP-seq peak-call significance. The broader lesson is not that one recalibration method solves everything. The lesson is that statistical confidence is itself a model output and should be checked when it becomes central to downstream decisions.

This matters when we rank enhancers, compare samples, prioritize transcription factors, or choose regions for validation. If the scores are poorly calibrated, we may overstate differences or chase the wrong candidates. Calibration is part of the bridge from signal detection to defensible biological interpretation.

This is also why calibration is a teaching topic, not a technical footnote. In a cancer study, the top-ranked elements often become the candidates for expensive follow-up experiments, so the ranking system itself needs scrutiny.

**Transition**

With calibrated evidence in hand, the next challenge is combining imperfect layers into regulatory annotations.

### L1-16 — Annotation combines imperfect evidence layers

**Speaker notes**

Regulatory annotation is evidence aggregation. No single assay gives the whole answer. Accessibility suggests that DNA is physically available. H3K27ac can support active enhancer or promoter states. Motifs suggest sequence potential. Contacts suggest spatial proximity. Expression links suggest possible target genes. Perturbation evidence can move the claim closer to function.

Resources such as ENCODE SCREEN and the candidate cis-regulatory element registry formalize this idea by integrating multiple evidence types. Cistrome resources help reuse public chromatin data for regulatory hypotheses, including cancer contexts.

But the language must stay careful. Candidate enhancer is different from validated enhancer. Contacted promoter is different from causal target gene. Motif present is different from transcription factor active. Strong claims require multiple consistent evidence layers, and the strongest claims usually require perturbation or independent validation. This careful vocabulary protects us from turning annotation into overstatement.

For a student reading the literature, this is one of the most important habits: translate confident biological language back into the actual evidence layers that support it, and notice which layer is missing.

**Transition**

This evidence-layer view also explains why bulk assays remain useful even as single-cell and spatial methods become central.

### L1-17 — Bulk assays still matter in the single-cell era

**Speaker notes**

It is fair to ask why we spend time on bulk functional genomics when single-cell and spatial methods are so exciting. The answer is that bulk assays still matter. They often provide deeper coverage, mature quality-control standards, clearer replicate designs, and large cohort-scale resources. Many public regulatory atlases and priors were built from bulk or bulk-like assays.

Bulk data also teach the core concepts that reappear later. Background modeling, fragment interpretation, peak reproducibility, motif support, and contact significance do not disappear in single-cell or spatial assays. They become harder because the data are sparser and the experimental designs more complex.

So this lecture is foundational. We are not treating bulk assays as old technology. We are using them as the cleanest place to learn assay-aware statistical reasoning. In later weeks, single-cell, spatial, and network modules will build on the same logic with additional layers of complexity.

**Transition**

Now we can use the same logic to read cancer case studies more critically.

### L1-18 — Cancer case studies use the same logic

**Speaker notes**

The same interpretive framework explains many cancer case studies. In pan-cancer ATAC-seq, accessibility profiles across hundreds of tumors reveal regulatory elements, subtype programs, risk-locus activity, and noncoding regulatory states. The key is not just that peaks exist, but that accessibility patterns are processed, compared, and interpreted across tumor contexts.

In prostate cancer, androgen receptor binding can be extensively reprogrammed during tumorigenesis. That case teaches that transcription-factor binding is not fixed by the genome sequence alone. It depends on chromatin context, cooperating factors, and cancer state.

Enhancer hijacking provides another example. A structural variant can move an oncogene into a new regulatory neighborhood, activating expression without changing the coding sequence. But proving that story requires integrating structural variation, enhancer evidence, gene expression, and often additional validation. The case studies are different, but the reasoning is the same: assay object, background model, reproducibility, and evidence integration.

These examples also show why this module comes early in the course. Later computational models often start from regulatory features, but those features are only as reliable as the assays and assumptions used to create them.

**Transition**

Those case studies are powerful, but they also show where overclaiming can enter, so let’s make the boundaries explicit.

### L1-19 — What not to overclaim

**Speaker notes**

Let’s make the caution explicit. A peak is not automatically an enhancer. It is an enriched or accessible genomic region under a model. A motif is not automatically binding. It is sequence potential, and binding depends on chromatin, factor expression, cofactors, and context. A contact is not automatically regulation. It is spatial proximity evidence. A correlation between accessibility and expression is not automatically a causal target-gene relationship.

These distinctions can feel pedantic, but they matter. In computational oncology, overclaiming can mislead downstream biology. It can send experimental validation toward the wrong region, identify the wrong target gene, or make a biomarker look stronger than it is.

The solution is not to avoid interpretation. The solution is to use graded language. Candidate enhancer. Putative target. Spatially linked promoter. Motif-supported regulatory element. Perturbation-validated enhancer. Each phrase tells the reader how strong the evidence is. Good computational biology is careful about that scale of evidence.

**Transition**

With those cautions in place, we can summarize the framework that Lecture 2 will turn into concrete method choices.

### L1-20 — Lecture 1 synthesis

**Speaker notes**

The synthesis for Lecture 1 is that functional genomics is assay-aware statistical reasoning. First, define the assay object. Are we modeling enriched fragments, accessible fragments, nucleosome-aware ATAC fragments, broad domains, cut-site patterns, or contact counts?

Second, model signal against structured background. The genome is not a uniform null distribution. Cancer genomes add copy-number changes, rearrangements, tumor purity, and cell mixture. Different assays add different artifacts.

Third, require quality control and reproducibility before interpretation. Library complexity, TSS enrichment, cross-correlation, FRiP, blacklist filtering, replicate consistency, and calibration determine how much trust we should place in calls.

Finally, interpret regulatory biology through evidence integration. Peaks, motifs, histone marks, accessibility, contacts, expression, and perturbations are pieces of a model. They are not proof by themselves.

In the next lecture, we will turn this framework into concrete method choices. We will look at families of tools such as MACS, SICER, HMMRATAC, footprinting approaches, CUT peak callers, contact callers, reproducibility analysis, and calibration. The point will not be to memorize tool names, but to see why different assays require different statistical assumptions.

## Audio synthesis notes

- Preferred voice: lecturer-style, calm, clear, moderately paced.
- Production target: approximately 90 seconds per slide; Dr. Liu will synthesize audio separately with the local Qwen3-TTS voice tool.
- Autoplay pause: 1 second between slides in HTML delivery.
- Pronunciation notes:
  - ChIP-seq: “chip seek”
  - ATAC-seq: “attack seek”
  - CUT&RUN: “cut and run”
  - CUT&Tag: “cut and tag”
  - Hi-C: “high C”
  - HiChIP: “high chip”
  - PLAC-seq: “plack seek”
  - MACS: “max”
  - Tn5: “T N five”
  - H3K27ac: “H three K twenty-seven acetylation”
  - H3K27me3: “H three K twenty-seven tri-methylation”
  - H3K36me3: “H three K thirty-six tri-methylation”
  - CTCF: “C T C F”
  - cCRE: “candidate cis-regulatory element” or “C C R E” after first definition
  - IDR: “I D R”
  - FRiP: “frip,” fraction of reads in peaks
- Sections to synthesize:
  - Synthesize individual slide notes after Dr. Liu approves slide pacing or wording.
