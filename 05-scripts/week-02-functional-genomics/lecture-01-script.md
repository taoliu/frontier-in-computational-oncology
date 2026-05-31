# Week 02 — Functional Genomics in Cancer — Lecture 1 Script

## Lecture metadata

- Module: Week 02 — Functional Genomics in Cancer
- Lecture: Lecture 1 — Background & Problem Definition
- Target duration: 50–60 minutes
- Slide deck: `04-slides/week-02-functional-genomics/slide-text.md`, Lecture 1 section
- Voice/audio status: text script ready; audio not generated
- Validation status: first-pass validated source IDs included; figures remain placeholders

## Teaching arc

This lecture should make one idea unavoidable: bulk functional genomics assays are not magic enhancer detectors. They are measurement systems. Each assay produces a different statistical object, and every downstream biological claim depends on how we model signal, background, reproducibility, and evidence integration.

## Script

### L1-01 — Functional Genomics in Cancer

**Speaker notes**

Today we start the functional genomics module. The theme is simple but important: these assays do not directly tell us “this is an enhancer,” “this transcription factor is active,” or “this loop is causal.” They give us molecular readouts — reads, fragments, domains, or contact counts — and we have to turn those readouts into regulatory claims.

So this is not mainly a tour of software names. We will talk about tools, but the deeper goal is to understand what problem each tool is trying to solve. A peak caller, a domain caller, a footprinting method, and a loop caller all encode assumptions about the assay and about the background signal.

By the end of the week, I want you to be able to look at a regulatory genomics result in a cancer paper and ask: what exactly was measured, what model converted that measurement into a call, and how strong is the evidence for the biological interpretation?

**Transition**

Let’s begin with why cancer biology needs these assays at all, even in a world with excellent mutation calls.

### L1-02 — Why mutations are not enough

**Speaker notes**

Cancer genomics often starts with mutations: point mutations, copy number changes, structural variants. Those are essential, but they do not explain everything. Two tumors can have similar coding alterations and very different cell states. A tumor can change lineage program, immune visibility, enhancer activity, or transcription factor dependence without a simple new coding mutation.

That is where functional genomics enters. These assays ask when and where the genome is active. Which promoters are open? Which enhancers are active? Which transcription factors are bound? Which regulatory regions physically contact candidate target genes?

In cancer, this matters for several recurring mechanisms. In pan-cancer ATAC-seq, accessibility maps reveal regulatory programs and subtype structure. In prostate cancer, the androgen receptor can be redistributed across a new cistrome during tumorigenesis. In neuroblastoma, super-enhancer landscapes help define regulatory cell states. In enhancer hijacking, the coding sequence of an oncogene may be unchanged, but a structural rearrangement moves it into a new regulatory neighborhood.

So the mutation list is not the whole mechanism. Functional genomics gives us evidence about regulatory state.

**Transition**

But to use that evidence well, we need a disciplined framework.

### L1-03 — Three questions before software

**Speaker notes**

Before choosing a tool, I want you to ask three questions.

First: what is the observed statistical object? Is it a pileup of ChIP-seq reads? Paired-end ATAC fragments? A sparse contact matrix? These are not interchangeable.

Second: what is signal versus background? A peak only means something relative to an expected background. That background may depend on mappability, GC content, chromatin accessibility, local copy number, enzyme bias, or genomic distance.

Third: how do we know the call is reproducible and biologically interpretable? A tall pileup in one sample is not enough. We need quality control, replicate consistency, calibration, and ideally some orthogonal evidence.

If you keep these three questions in mind, the rest of the week becomes much easier. Different tools are different answers to these questions.

**Transition**

Now let’s compare the major assay families and the objects they produce.

### L1-04 — Assay families produce different objects

**Speaker notes**

Here are four major families we will use throughout the module.

ChIP-seq enriches DNA fragments associated with a target protein or histone mark. The output is usually a genomic enrichment track, and we often summarize it as peaks or domains.

ATAC-seq uses Tn5 transposase to insert into accessible chromatin. The output is a collection of paired-end fragments. Those fragments tell us about accessibility, but their lengths also carry information about nucleosome structure.

CUT&RUN and CUT&Tag use tethered enzymes to cut or tag DNA near a target. These assays often have lower background and different signal geometry from classical ChIP-seq.

Finally, Hi-C, HiChIP, PLAC-seq, and related assays measure pairs of genomic loci that are close in 3D space. Their output is a contact map or a list of contact counts, not a simple one-dimensional peak track.

The key point is that assay chemistry defines the statistical object. You cannot responsibly analyze all of these as if they were the same kind of signal.

**Transition**

Let’s look first at enrichment assays like ChIP-seq and CUT-based methods.

### L1-05 — ChIP-seq and CUT assays are enrichment experiments

**Speaker notes**

ChIP-seq and CUT assays both produce enrichment signals along the genome, but they get there differently.

In ChIP-seq, we fragment chromatin, use an antibody to enrich DNA associated with a protein or histone mark, and then sequence the enriched fragments. In CUT&RUN or CUT&Tag, an enzyme is targeted near a protein of interest and cuts or tags nearby DNA.

In both cases, the visual output can look deceptively simple: a genome browser track with hills and valleys. But those hills are not self-interpreting. A tall region may reflect true binding, broad chromatin state, local background, antibody behavior, mappability artifacts, or other biases.

That is why peak calling is a statistical problem. We are not just looking for tall piles of reads; we are asking which regions are enriched beyond what we expect under an appropriate background model.

**Transition**

ATAC-seq looks similar in a genome browser, but the measurement is different.

### L1-06 — ATAC-seq measures accessibility and structure

**Speaker notes**

ATAC-seq is often described as measuring open chromatin, and that is a useful shorthand. But computationally, ATAC-seq gives us more than a one-dimensional accessibility track.

Tn5 inserts into accessible DNA. With paired-end sequencing, we observe fragments of different lengths. Very short fragments tend to represent nucleosome-free DNA. Longer fragments can represent mono-nucleosome or di-nucleosome protected DNA.

That means the fragment length distribution itself carries biological structure. Later, when we discuss HMMRATAC, we will see a method that explicitly uses these fragment classes to model chromatin states.

But we should also be careful. Accessibility is a measurement. It does not automatically mean a region is an active enhancer, and it does not automatically tell us which transcription factor is bound.

**Transition**

Now let’s move from one-dimensional genome tracks to three-dimensional contact assays.

### L1-07 — Contact assays are sparse and distance-biased

**Speaker notes**

Contact assays measure pairs of genomic loci. In Hi-C, HiChIP, PLAC-seq, and related methods, the basic observation is that two loci were close enough in the nucleus to be ligated and sequenced as a pair.

This is powerful, because enhancer activity often depends on long-range regulatory relationships. But contact data are strongly biased by genomic distance. Loci that are close along the linear genome contact each other more often by default. So a contact count is not meaningful without an expectation model.

This is why methods like FitHiC2 and MAPS focus on distance-aware significance. The question is not simply whether two loci contact. The question is whether they contact more often than expected, given distance, capture design, and assay context.

And even then, a contact is not proof of regulation. It is physical proximity evidence.

**Transition**

That brings us to a broader lesson: background is not flat.

### L1-08 — Background is structured

**Speaker notes**

One of the most important ideas in this module is that background varies across the genome.

Some regions are easier to map. Some regions have unusual GC content. Some regions are open or repetitive in ways that create signal in many assays. Some regions repeatedly show anomalous enrichment and are captured in resources like the ENCODE blacklist.

So if we say “this is a peak,” we should ask: a peak relative to what? Relative to a genome-wide constant? Relative to nearby local background? Relative to an input control? Relative to a replicate? Relative to a distance-matched contact expectation?

MACS is a classic example because it made local background modeling central to ChIP-seq peak calling. The deeper lesson is not just MACS itself; the lesson is that background estimation is part of the biological claim.

**Transition**

Controls help, but controls are also models.

### L1-09 — Controls are models, not magic

**Speaker notes**

It is tempting to think that a control track solves the background problem. It helps, but it does not eliminate modeling.

An input control in ChIP-seq estimates non-target signal from fragmentation, sequencing, copy number, and genomic biases. But it may not perfectly match the immunoprecipitated sample. CUT assays may have different background properties. ATAC-seq often does not have the same kind of input control. Contact assays require their own distance and capture-aware expectations.

So controls reduce artifacts, but they also encode assumptions. What is the control supposed to represent? What biases does it capture? What biases does it miss?

When you read a paper, do not just ask whether there was a control. Ask whether the control matches the statistical problem.

**Transition**

The same principle applies to reproducibility and quality control.

### L1-10 — Reproducibility is part of the model

**Speaker notes**

Quality control is often presented as a checklist, but it is more than that. It determines how much confidence we should place in the calls.

For these assays, common QC concepts include library complexity, fraction of reads in peaks, TSS enrichment for ATAC-seq, strand cross-correlation for ChIP-seq, blacklist filtering, and replicate consistency.

Replicate consistency is especially important. IDR-style thinking asks whether highly ranked calls are reproducible across replicates. That is different from simply asking whether two peak lists overlap by eye.

The practical lesson is this: a peak without reproducibility evidence is still only a candidate. It may be interesting, but it is not yet a strong regulatory claim.

**Transition**

Even after we have reproducible calls, we still have to interpret them carefully.

### L1-11 — Regulatory annotation is evidence aggregation

**Speaker notes**

Regulatory annotation is not a single measurement. It is evidence aggregation.

A region may be accessible. It may have H3K27ac. It may contain a transcription factor motif. It may contact a promoter. Its accessibility may correlate with gene expression. Each of these is an evidence layer.

Resources like ENCODE SCREEN and the cCRE registry formalize this idea by integrating accessibility, histone marks, CTCF, and other evidence. Cistrome resources do something related for public chromatin profiles and cancer regulatory hypotheses.

But even when multiple layers agree, we should keep language careful. “Candidate enhancer” is different from “validated enhancer.” “Contacted gene” is different from “causal target gene.” Stronger claims require stronger evidence, especially perturbation evidence.

**Transition**

Let’s end Lecture 1 by summarizing the habits we will use for the rest of the week.

### L1-12 — Lecture 1 synthesis

**Speaker notes**

The main message today is that functional genomics is assay-aware statistical reasoning.

First, define the assay object. Are we modeling enriched fragments, accessible fragments, broad domains, footprints, or contact counts?

Second, model signal against structured background. The genome is not a uniform null distribution, and different assays create different artifacts.

Third, require reproducibility before interpretation. QC, replicate consistency, blacklist filtering, calibration, and orthogonal evidence all determine how strong the claim can be.

And finally, interpret regulatory biology as evidence integration. Peaks, motifs, histone marks, accessibility, contacts, and expression are pieces of a model. They are not automatically proof by themselves.

In Lecture 2, we will apply this framework to specific method families: MACS, SICER, HMMRATAC, footprinting, CUT peak callers, contact callers, and verification strategies.

## Audio generation notes

- Preferred voice: lecturer-style, calm, clear, moderately paced.
- Pronunciation notes:
  - ChIP-seq: “chip seek”
  - ATAC-seq: “attack seek”
  - CUT&RUN: “cut and run”
  - CUT&Tag: “cut and tag”
  - Hi-C: “high C”
  - HiChIP: “high chip”
  - PLAC-seq: “plack seek”
  - Tn5: “T N five”
  - H3K27ac: “H three K twenty-seven A C”
  - CTCF: “C T C F”
  - cCRE: “candidate cis-regulatory element” or “C C R E” after first definition
  - IDR: “I D R”
  - FRiP: “frip,” fraction of reads in peaks
- Sections to regenerate:
  - Regenerate individual slide notes after Dr. Liu adjusts slide pacing or removes case-study references.
