# Week 02 — Functional Genomics in Cancer — Lecture 2 Script

## Lecture metadata

- Module: Week 02 — Functional Genomics in Cancer
- Lecture: Lecture 2 — Method Development & Verification
- Target duration: ~30 minutes
- Target slide count: 20
- Target narration: ~90 seconds per slide
- Slide deck: `04-slides/week-02-functional-genomics/slide-text.md`, Lecture 2 section
- Voice/audio status: production text script ready; after Dr. Liu review/confirmation, audio synthesis is handled separately with Dr. Liu’s local Qwen3-TTS voice tool
- Validation status: first-pass validated source IDs included; figures remain placeholders

## Teaching arc

This lecture should make method choice feel like evidence design. Students should learn that MACS, SICER, HMMRATAC, SEACR, GoPeaks, footprinting methods, contact callers, IDR, and calibration tools differ because the assays and claims differ.

## Script

### L2-01 — Method development follows the assay

**Speaker notes**

Lecture 1 ended with a framework: functional genomics assays are measurement systems, and every biological claim depends on the model between the measurement and the interpretation. Lecture 2 turns that framework into method development and verification.

The core idea is that tools are not interchangeable labels. A narrow ChIP-seq peak caller, a broad-domain histone-mark caller, an ATAC-seq state model, a CUT&RUN sparse-enrichment method, a footprinting method, and a chromatin-contact caller are built for different statistical objects. They make different assumptions about signal shape, background, replicate behavior, and score interpretation.

So today we will not memorize software names as a shopping list. We will ask why each method exists. What problem was it trying to solve? What signal geometry does it assume? What background does it protect against? What quality-control or reproducibility evidence makes the result credible?

By the end, students should be able to look at a regulatory genomics paper and explain not just what tool was used, but whether the tool’s assumptions match the assay and the biological question.

**Transition**

We start by turning that idea into a reusable checklist.

### L2-02 — Four modeling questions

**Speaker notes**

Before we discuss individual methods, it helps to have a checklist. The first question is signal shape. Are we looking for a focal binding event, a broad histone-modification domain, a nucleosome-free ATAC state, a motif-centered footprint, or a contact between two loci? The wrong shape assumption can either fragment true domains or blur precise binding events.

The second question is background. Background may include local sequencing bias, input signal, mappability, copy number, Tn5 sequence preference, sparse CUT&RUN noise, or genomic-distance decay in contact maps. A method is partly defined by what it treats as background.

The third question is score behavior. A P value, q value, enrichment score, rank, or posterior state is not automatically comparable across assays or tools. Calibration matters.

The fourth question is verification. Replicates, QC metrics, IDR-style rank consistency, blacklist filtering, orthogonal marks, expression links, or perturbation evidence determine how far we can take the claim. This checklist is the spine of Lecture 2.

**Transition**

With the checklist in place, we can begin with the classic narrow-peak case.

### L2-03 — Narrow TF peaks: why MACS mattered

**Speaker notes**

We start with narrow transcription-factor ChIP-seq peaks because they are the cleanest example of signal detection. In a typical TF ChIP-seq experiment, reads accumulate around genomic loci associated with the target factor. The expected signal is focal: a local enrichment over background.

MACS, pronounced max, became influential because it addressed two practical issues. First, reads from the two strands form shifted patterns around the underlying binding event, so the method estimates an empirical fragment shift to improve localization. Second, the genome does not have a flat background. MACS uses local background modeling to protect against regional biases that would otherwise look like enrichment.

The key teaching point is that a MACS peak is a model-based candidate binding event. It is stronger than a visually tall pileup, but it is not automatically a functional enhancer, a causal regulator, or even proof of direct biological effect. It is a well-defined computational object that needs QC, reproducibility, and contextual interpretation.

**Transition**

Now let’s look more closely at why local background matters so much.

### L2-04 — Local background is a biological safeguard

**Speaker notes**

Local background modeling is not just a statistical convenience. It is a safeguard against overinterpretation. If we compare every region only to a genome-wide average, then copy-number gains, mappability problems, open chromatin, or regional sequencing artifacts can look like target-specific binding.

MACS-style local background asks a more cautious question: is this locus enriched relative to its local neighborhood and relevant control signal? That logic matters even more in cancer. Tumors often have amplified or deleted regions, rearranged neighborhoods, and uneven genomic representation. A peak in an amplified region may be visually impressive but not necessarily proportionally enriched for the target.

Blacklist regions are a related practical safeguard. Some loci repeatedly produce anomalous signal across many experiments, and excluding them prevents recurrent artifacts from becoming biological claims.

So when students see a peak caller, they should ask how it handles local expectation. In cancer functional genomics, the null model is not flat. The genome itself has structure, and the tumor genome has even more.

**Transition**

Background modeling is only useful if the underlying experiment has interpretable signal.

### L2-05 — ChIP-seq QC: strand cross-correlation

**Speaker notes**

A peak caller can only work well if the experiment contains usable signal. For protein-binding ChIP-seq, strand cross-correlation is a classic QC idea. If immunoprecipitation enriches real protein-associated fragments, reads on opposite strands show a characteristic shift around binding sites. Cross-correlation measures how well those strand-specific patterns align as one strand is shifted relative to the other.

This gives information about fragment length and signal quality. A strong, well-positioned cross-correlation peak supports the idea that the library contains genuine binding-centered enrichment. A weak or ambiguous pattern raises concern that peak calls may reflect noise, background, or library problems.

The point is not that one QC metric decides everything. The point is that QC is evidence about whether downstream inference is meaningful. ENCODE-style workflows formalized many of these checks because large-scale regulatory resources need consistency, provenance, and defensible thresholds. Method development therefore includes not only the peak caller, but also the evidence that the peak caller is being applied to an interpretable experiment.

**Transition**

QC also needs infrastructure when analyses scale beyond one experiment.

### L2-06 — ENCODE-style pipelines as provenance systems

**Speaker notes**

Large regulatory genomics projects taught the field that reproducibility is partly an infrastructure problem. ENCODE-style uniform pipelines are useful examples because they do more than run one tool. They record processing choices, quality metrics, filters, genome versions, intermediate files, and reports.

For ChIP-seq and ATAC-seq, metrics such as library complexity, fraction of reads in peaks, transcription start site enrichment, alignment quality, duplicate rate, and blacklist overlap help determine whether a result is credible. These metrics do not replace biological judgment, but they prevent invisible processing decisions from becoming hidden sources of variation.

We should be careful not to say that a consortium pipeline is always the best method for every new assay or cancer setting. That would be too strong. The better claim is that standardized pipelines provide provenance and baseline QC. They make the analysis auditable. When a study departs from the pipeline, students should ask whether the departure is justified by the assay or the biological question.

**Transition**

Now we can contrast narrow peaks with broad regulatory domains.

### L2-07 — Broad domains break narrow-peak assumptions

**Speaker notes**

Not all enrichment data look like transcription-factor binding. Some histone modifications occupy broad or diffuse domains. If we force these marks into a narrow-peak model, the caller may split one biologically coherent domain into many small pieces, or miss weaker but spatially consistent enrichment.

SICER was designed around this problem. Instead of focusing only on focal summits, it uses spatial clustering of enriched windows to identify broader histone-modification domains. The important idea is that broad-domain calling changes the unit of interpretation. We are no longer only asking where the tallest point is. We are asking whether neighboring genomic windows collectively support an enriched chromatin domain.

This is a general method-development lesson. Signal shape is a biological hypothesis. If a mark spreads over a domain, the model should allow domain-level evidence. If a factor binds focally, the model should preserve focal resolution. The caller encodes what kind of regulatory feature we think the assay is measuring.

**Transition**

Next we move from ChIP-seq enrichment to ATAC-seq fragment structure.

### L2-08 — ATAC-seq requires fragment-aware modeling

**Speaker notes**

ATAC-seq is often reduced to an accessibility peak track, but paired-end ATAC data contain fragment-length information. Short fragments are enriched for nucleosome-free accessible DNA. Longer fragments correspond to mono-nucleosome or multi-nucleosome protected DNA. If we pool everything into one coverage track, we lose part of the assay’s structure.

HMMRATAC is a useful example because it treats ATAC-seq as a state-modeling problem. It separates fragment classes and uses a hidden Markov model to infer chromatin states, including nucleosome-free and nucleosome-associated regions. The output is not simply a generic peak list; it reflects assumptions about how fragment classes relate to underlying chromatin architecture.

The teaching point is broader than one tool. ATAC-specific methods should respect the chemistry of transposition and the information in fragment lengths. Accessibility is not just a pileup height. It is a structured measurement that can support more nuanced inference when the model matches the data.

**Transition**

Assay-specific modeling becomes even clearer when the chemistry changes to CUT assays.

### L2-09 — CUT assays change the background problem

**Speaker notes**

CUT&RUN and CUT&Tag are not just smaller ChIP-seq experiments. Their chemistry is different. An enzyme is tethered near the target, generating cleavage or tagmentation signal close to binding sites or modified nucleosomes. This can produce lower background and sharper localization, but it also changes the statistical structure of the data.

SEACR was developed for sparse, low-background CUT&RUN chromatin profiling. It reflects the idea that a caller designed for classical ChIP-seq background may not be the right tool for a low-background tethered-enzyme assay. GoPeaks provides another example, emphasizing histone-modification peak calling for CUT&Tag data.

The main lesson is that assay innovation often forces method innovation. When the experimental chemistry changes, the old background model may no longer be appropriate. Students should be suspicious of automatic tool reuse across assay families. The first question should be whether the method’s assumptions match the signal and background produced by the assay.

**Transition**

After peak or domain calling, many analyses move into sequence motifs.

### L2-10 — Motif enrichment is sequence evidence

**Speaker notes**

Motif analysis is one of the most common downstream steps after peak calling. It asks whether particular sequence patterns are enriched in a set of regions compared with a background. If a motif is enriched, we may hypothesize that a transcription factor family contributes to the regulatory program.

But motif enrichment is sequence evidence, not binding evidence. Many transcription factors share similar motifs. A motif may be present but inaccessible. A factor may not be expressed in the sample. A motif may be enriched because of GC content or because the background set was poorly chosen. Therefore, motif analysis is best treated as a hypothesis generator.

The background matters. Comparing enhancer-like regions to random genomic sequence can inflate results because regulatory regions differ in composition and mappability. A better background should match relevant properties of the tested regions. Good motif analysis is therefore not just running a database scan. It is designing a fair sequence comparison and using cautious language afterward.

**Transition**

Footprinting asks a related but stronger question than motif enrichment.

### L2-11 — Footprinting asks a stronger question

**Speaker notes**

Footprinting asks a stronger question than motif enrichment. Instead of asking whether a motif sequence is present, it asks whether the pattern of cuts around that motif is consistent with protein occupancy or protection. In ATAC-seq, that means looking at Tn5 insertion patterns around motif sites.

However, Tn5 has sequence bias. Some cut patterns can arise from enzyme preference rather than transcription-factor occupancy. Chromatin context, local accessibility, and sample composition also shape the signal. That is why bias-aware methods such as TOBIAS are important teaching examples. They explicitly attempt to correct for Tn5 bias before interpreting footprint-like patterns.

The language still needs restraint. A footprint is not the same as a ChIP-seq binding peak, and neither is automatically a causal regulatory effect. Footprinting provides occupancy-like evidence that can strengthen a TF hypothesis when combined with motif enrichment, factor expression, accessibility changes, and ideally perturbation or ChIP/CUT validation.

**Transition**

Contact maps require an entirely different null model.

### L2-12 — Contact calling needs a distance-aware null

**Speaker notes**

Chromatin-contact data require a different kind of background model. In Hi-C and related assays, loci close together on the linear genome contact more often than loci far apart. That distance decay dominates the raw data. Therefore, a high contact count is not meaningful until we ask whether it is high relative to the expected contact frequency at that distance and under that assay design.

FitHiC2 is a useful example for statistically significant Hi-C contact detection because it explicitly models confidence relative to contact-distance behavior. MAPS is useful for PLAC-seq and HiChIP because those assays enrich for protein-associated or mark-associated interactions and need model-based analysis of long-range contacts.

The biological interpretation remains cautious. A significant contact suggests spatial linkage. It does not prove that an enhancer controls a gene. The method gives a statistically supported interaction candidate, and the biological claim depends on integration with regulatory marks, expression, and perturbation evidence.

**Transition**

Across all of these methods, reproducibility remains central.

### L2-13 — Replicates are about ranked stability

**Speaker notes**

Replicates are sometimes summarized as overlap, but overlap alone is not enough. If two experiments share many weak regions but disagree on the strongest signals, the analysis may not be stable. IDR-style thinking focuses on rank consistency: do the strongest calls in one replicate tend to be strong in the other replicate?

This is important because downstream interpretation usually starts from ranked candidates. We choose top peaks for motif analysis, top enhancers for target-gene linking, or top interactions for validation. If those ranks are not reproducible, the downstream biology becomes fragile.

IDR is not a substitute for good experimental design, and it does not solve every assay type equally. But as a concept, it teaches students to think of reproducibility as stability of evidence, not just presence or absence. A peak that is high-scoring, quality-controlled, and reproducible across replicates deserves more confidence than a peak that appears only once or ranks inconsistently.

**Transition**

Even reproducible scores still need calibration.

### L2-14 — Calibration affects prioritization

**Speaker notes**

After calling peaks, we often treat scores as if they are calibrated measures of confidence. That is risky. A P value or q value is only as good as the null model and assumptions behind it. If those assumptions are imperfect, nominal significance may not match empirical false-positive behavior.

RECAP is useful because it directly addresses this issue for ChIP-seq peak calls. It shows that peak-caller significance can be miscalibrated and that resampling-based recalibration can improve null calibration. For teaching, the important point is not that every analysis must use one specific recalibration tool. The important point is that reported significance should not be accepted uncritically.

Calibration affects prioritization. If the top-ranked candidates are selected for expensive perturbation experiments, validation assays, or mechanistic storytelling, then score behavior matters. A poorly calibrated ranking can waste effort and create overconfident claims. Method verification therefore includes asking whether the scores mean what we think they mean.

**Transition**

Calibration and reproducibility lead naturally into benchmark design.

### L2-15 — Benchmark design must match the claim

**Speaker notes**

Method papers often include benchmarks, but students should ask what the benchmark actually tests. A gold-standard set of regulatory elements may be incomplete, biased toward well-studied loci, or defined using related assays that share assumptions with the method being evaluated. Simulations are useful because they provide known truth, but they only test the assumptions built into the simulation.

The best benchmark depends on the claim. If a caller claims better narrow TF peak detection, replicate consistency and orthogonal binding evidence may be relevant. If a method claims enhancer-target linking, expression and perturbation support become more important. If a contact caller claims significant loops, distance-aware null behavior and replicate stability are central.

So benchmark design is not a generic leaderboard. It should match the biological decision the method is supposed to support. A method can perform well on one benchmark and still be poorly suited for a different assay, cancer context, or downstream interpretation task.

**Transition**

Benchmarks are useful, but biological interpretation still needs orthogonal evidence.

### L2-16 — Orthogonal evidence strengthens weak labels

**Speaker notes**

Regulatory labels are usually assembled from imperfect evidence layers. A ChIP-seq or ATAC-seq peak gives one type of evidence. A histone mark gives another. A motif suggests sequence potential. Expression links suggest a possible target gene. Contact data suggest spatial proximity. Perturbation can test function more directly.

Orthogonal evidence is powerful because each assay has different biases. If an accessible region also has H3K27ac, a relevant motif, reproducible signal, and expression association with a nearby gene, the candidate enhancer interpretation becomes stronger. If the evidence layers disagree, that does not mean the region is uninteresting, but it should reduce confidence or sharpen the hypothesis.

This is why public resources and integrated annotations are useful, but also why their labels should be read carefully. Candidate regulatory elements are not all equally validated. For causal claims, especially in cancer mechanism studies, perturbation evidence carries special weight. The method pipeline should support that evidence ladder rather than pretending one assay proves everything.

**Transition**

In cancer, verification also has tumor-specific complications.

### L2-17 — Cancer-specific verification adds extra checks

**Speaker notes**

Cancer functional genomics adds verification problems that are less prominent in simple cell-line examples. Copy-number changes can alter read depth. Tumor purity and immune or stromal admixture can change apparent regulatory states. Subtype composition can create signals that are real at the cohort level but not tumor-intrinsic in the way a mechanistic claim implies.

Therefore, method verification in cancer should include tumor context. Does the signal remain after considering copy number? Is the regulatory state associated with a subtype, lineage, or sample-composition variable? Are problematic regions filtered? Are contact or enhancer calls interpreted in the context of structural variation and local genome organization?

This does not mean cancer data are unusable. It means the verification standard is higher. A technically valid peak call may still be biologically ambiguous if sample mixture or genomic alteration explains the pattern. Good computational oncology keeps assay QC and cancer biology in the same frame.

**Transition**

Now we can summarize method choice as a choice about what claim is justified.

### L2-18 — Choosing a method is choosing a claim

**Speaker notes**

At this point, we can summarize method choice as claim choice. A narrow peak caller supports a statement about focal enrichment. A broad-domain caller supports a statement about spatially extended enrichment. An ATAC state model supports a statement about fragment-informed chromatin state. A footprinting method supports occupancy-like evidence around motifs. A contact caller supports spatial proximity evidence under a distance-aware model.

Those statements are related to regulatory biology, but they are not identical to final biological claims. The tool output should be described in language that matches the evidence. If the result is a MACS peak, call it a candidate binding region or enriched locus, not automatically an enhancer. If the result is a FitHiC2 contact, call it a significant contact, not automatically a causal enhancer-gene interaction.

This careful mapping from method to claim is one of the most valuable professional habits students can build. It makes papers clearer, presentations more honest, and validation plans more rational.

**Transition**

Let’s turn that into a practical checklist.

### L2-19 — A practical verification checklist

**Speaker notes**

Here is the practical checklist I want students to carry into paper reading and project design. First, assay-object match: does the method fit the data object? A broad histone mark, an ATAC fragment-state problem, and a chromatin contact map should not be treated as the same analysis problem.

Second, QC and filtering: is the experiment interpretable? Look for library complexity, enrichment metrics, TSS enrichment where relevant, cross-correlation where relevant, blacklist filtering, and clear processing provenance.

Third, replicates and calibration: are the rankings stable and the scores meaningful? Replicate consistency, IDR-style reasoning, and calibration checks all determine whether top candidates deserve trust.

Fourth, biological integration: what evidence supports the claim? A peak, motif, footprint, domain, or contact should be translated into a graded biological statement, not inflated into a causal conclusion.

This checklist is intentionally simple. It is meant to slow down overconfident interpretation and make method sections readable as chains of evidence.

**Transition**

Finally, we can synthesize the lecture and bridge to applications.

### L2-20 — Lecture 2 synthesis

**Speaker notes**

The synthesis for Lecture 2 is that method development in functional genomics is the design of evidence. We choose methods because assays produce different objects: focal ChIP-seq enrichment, broad histone domains, ATAC fragment states, CUT sparse signal, motif-centered cut patterns, and distance-dependent contact counts.

We verify those methods through QC, filtering, replicate stability, calibration, benchmarks, and orthogonal evidence. These steps are not paperwork. They determine whether a computational call can support a biological statement.

The cancer setting raises the stakes because regulatory calls can become claims about oncogene activation, subtype identity, therapeutic vulnerability, or enhancer dependence. If the method and verification are weak, the biological story becomes fragile. If the evidence chain is strong, functional genomics can reveal mechanisms that mutation lists alone miss.

In the next lecture, we will move from methods to applications. We will use public regulatory resources and cancer case studies, including ENCODE and Cistrome resources, pan-cancer ATAC-seq, AR cistrome rewiring, super-enhancer states, enhancer hijacking, and primary-cancer 3D genome maps, to see how these methods become biological insight.

## Audio synthesis notes

- Preferred voice: lecturer-style, calm, clear, moderately paced.
- Production target: approximately 90 seconds per slide; synthesize audio only after Dr. Liu reviews and confirms this script, using Dr. Liu’s local Qwen3-TTS voice tool rather than OpenAI TTS.
- Autoplay pause: 1 second between slides in HTML delivery.
- Pronunciation notes:
  - MACS: “max”
  - ChIP-seq: “chip seek”
  - ATAC-seq: “attack seek”
  - CUT&RUN: “cut and run”
  - CUT&Tag: “cut and tag”
  - Hi-C: “high C”
  - HiChIP: “high chip”
  - PLAC-seq: “plack seek”
  - Tn5: “T N five”
  - HMMRATAC: “Hummer attack”
  - SICER: “sigh-ser”
  - SEACR: “seeker”
  - GoPeaks: “go peaks”
  - TOBIAS: “toe-BYE-us”
  - H3K27ac: “H three K twenty-seven A C”
  - IDR: “I D R”
  - FRiP: “frip,” fraction of reads in peaks
- Sections to regenerate:
  - Do not synthesize audio until Dr. Liu approves this Lecture 2 production script; Dr. Liu will handle voice synthesis separately with local Qwen3-TTS.
