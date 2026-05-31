# Week 02 — Functional Genomics in Cancer — Asset Manifest

## Asset status values

- `needed` — identified but not created/found
- `drafted` — rough internal asset exists
- `ready` — ready for slide use
- `licensed` — external asset with license/citation recorded
- `blocked` — cannot use without permission or replacement

## Assets

| Asset ID | File path | Type | Used in | Provenance | License / citation | Status | Notes |
|---|---|---|---|---|---|---|---|
| W02-A001 | `07-assets/images/week-02-functional-genomics/svg/W02-A001_assay_comparison.svg` | schematic | L1-04 | Original assay-comparison graphic | In-house original; cite S001/S004/S006/S010 | drafted | Four-column comparison: ChIP-seq enrichment, ATAC fragments, CUT tethered signal, contact matrix. |
| W02-A002 | `07-assets/images/week-02-functional-genomics/svg/W02-A002_MACS_local_background.svg` | schematic | L2-03 | Recreated conceptual MACS local-background graphic | In-house recreation from S001 | drafted | Avoid copying paper figure directly; show peak, local lambda/background windows, enriched summit. |
| W02-A003 | `07-assets/images/week-02-functional-genomics/svg/W02-A003_HMMRATAC_states.svg` | schematic | L2-06 | HMMRATAC fragment-class/state diagram | In-house recreation from S004 | drafted | Show nucleosome-free, mono/di-nucleosome fragments and HMM states. |
| W02-A004 |  | schematic | L2-10 | Distance-decay null model for chromatin contacts | In-house original; cite S010 | needed | Use generic contact matrix and expected contact decay curve. |
| W02-A005 | `07-assets/images/week-02-functional-genomics/svg/W02-A005_enhancer_hijacking.svg` | schematic | L3-06 | Enhancer hijacking mechanism | In-house original; cite S018/S019 | drafted | SV places oncogene near active enhancer/super-enhancer; use generic labels plus examples. |
| W02-A006 |  | schematic | L1-08 | Structured background and artifact regions | In-house original; cite S001/S014 | needed | Show true signal vs GC/mappability/artifact/blacklist-like regions. |
| W02-A007 |  | schematic | L1-10 | QC gate diagram | In-house original; cite S002/S007/S013/S014 | needed | Gates: library complexity → FRiP/TSS/cross-correlation → blacklist → replicate/IDR. |
| W02-A008 |  | table/diagram | L2-02 | Peak/domain caller model comparison grid | In-house original; cite S001/S003/S004/S006 | needed | Rows: MACS, SICER, HMMRATAC, SEACR/GoPeaks; columns: signal, background, output, best use. |
| W02-A009 |  | schematic | L2-04 | Strand cross-correlation conceptual plot | In-house conceptual recreation from S002 | needed | Show positive/negative strand shift producing correlation peak. |
| W02-A010 |  | schematic | L2-11 | Verification evidence ladder | In-house original; cite S007/S013-S015 | needed | Computational QC → replicate reproducibility → calibrated significance → orthogonal assay → perturbation. |
| W02-A011 |  | schematic | L3-02 | Public resource map | In-house original; cite S008/S009/S011/S012 | needed | ENCODE/SCREEN, Cistrome, TCGA ATAC, primary-cancer 3D genome resources. |
| W02-A012 |  | schematic | L3-03 | TCGA ATAC discovery workflow | In-house original; cite S011 | needed | Tumors → ATAC peaks → regulatory elements/subtypes/risk-locus hypotheses. |
| W02-A013 |  | schematic | L3-10 | Module handoff diagram | In-house original | needed | Week 02 bulk principles → Week 03 single-cell → Week 04 spatial → Week 06 networks. |

## Production notes

- Prefer original simplified schematics over copied paper figures to avoid copyright issues and to keep slides visually consistent.
- Use publication-figure placeholders for case-study result slides where the original paper figure may be pedagogically valuable.
- Each asset should carry source IDs in slide notes, even when the drawing is original.
- For the first pilot, make assets as editable PowerPoint shapes or SVG first; export PNG only for compatibility.

## Publication figure placeholders

These are placeholders only. Do not commit extracted copyrighted figures to the public repository unless license status is explicitly reusable.

| Placeholder ID | File path | Type | Used in | Source | License / citation | Status | Notes |
|---|---|---|---|---|---|---|---|
| W02-P001 |  | publication-figure-placeholder | L3-03 | S011 Corces et al. 2018 Science | Human reviewer to evaluate fair-use/license before insertion | placeholder | Pan-cancer ATAC result figure candidate. |
| W02-P002 |  | publication-figure-placeholder | L3-04 | S016 Pomerantz et al. 2015 Nature Genetics | Human reviewer to evaluate fair-use/license before insertion | placeholder | AR cistrome reprogramming figure candidate. |
| W02-P003 |  | publication-figure-placeholder | L3-05 | S017 van Groningen/Boeva 2017 Nature Genetics | Human reviewer to evaluate fair-use/license before insertion | placeholder | Neuroblastoma enhancer-state figure candidate. |
| W02-P004 |  | publication-figure-placeholder | L3-07 | S012 Yost et al. 2025 Nature Genetics | Human reviewer to evaluate fair-use/license before insertion | placeholder | Primary cancer enhancer-connectome figure candidate. |
