# QG-SASeg server handoff

## Purpose

This directory contains an internal reference manuscript showing the proposed revision direction. The original manuscript remains unchanged in `main_en.tex`; the reference version is `main_simulated.tex`.

## Proposed model

QG-SASeg combines:

1. Swin-T + FPN pixel decoder;
2. a dense unknown auxiliary head with class-balanced Dice--Focal supervision;
3. native unknown query slots with union supervision and connected-component assignment;
4. a query-guided convolutional refinement head;
5. candidate-level prototype-sphere support reweighting.

The intended reason for this design is to retain the strong dense supervision of PerPixel-K+1 while preserving the region-level candidate and support representation that distinguishes SASeg from a plain K+1 classifier.

## Required server experiments

Run the following in order.

### Stage 1: baseline reproduction

- Original SASeg, seeds 42/43/44;
- PerPixel-K+1, seeds 42/43/44;
- QG-SASeg, seeds 42/43/44.

Use the same split, preprocessing, backbone initialization, and validation-only threshold selection. Save checkpoints, logs, predictions, and the exact YAML configuration for every run.

### Stage 2: ablations

On Synapse A1, run:

- QG-SASeg without refinement head;
- QG-SASeg without dense unknown branch;
- QG-SASeg without support reweighting;
- QG-SASeg without unknown queries;
- optional query-only and pixel-only variants.

### Stage 3: cross-dataset check

Run QG-SASeg and PerPixel-K+1 on AMOS22, VOC, and Cityscapes with seeds 42/43/44 if resources permit. If resources are limited, prioritize AMOS22 first, then VOC and Cityscapes.

### Stage 4: A2

Report foreground AUROC, foreground AUPR, FPR@TPR95, auxiliary F1/IoU, candidate purity, candidate hit rate, and class/component-level results. Do not tune any threshold on the final evaluation labels.

## Acceptance criteria

The model can replace the simulated reference numbers only if:

- Synapse A1 unknown F1 exceeds the reproduced PerPixel-K+1 mean;
- the improvement is present across seeds rather than one run;
- known mIoU does not materially regress;
- at least one region-level measure improves, such as class-level F1, candidate purity, or candidate-level IoU;
- the gain can be attributed to the hybrid design through ablations.

If these criteria fail, do not preserve the QG-SASeg superiority claims in the manuscript. Replace the tables with the actual results and revise the claims to match the evidence.

## Files

- `main_simulated.tex`: internal reference manuscript;
- `simulated_results.csv`: seed-level table used to construct the manuscript values;
- `simulated_class_results.csv`: class-level A1 table;
- `fig_sim_a1_comparison.png`: Synapse A1 comparison;
- `fig_sim_cross_dataset.png`: cross-dataset A1 comparison;
- `fig_sim_class_f1.png`: class-level F1 comparison;
- `fig_sim_ablation.png`: ablation plot;
- `simulated_data_manifest.json`: provenance and replacement instructions.

## Important replacement rule

The CSV files and plots are planning artifacts. Before external submission, overwrite them with server-generated results, preserve raw predictions and logs, rerun the plotting script, and regenerate the PDF. The internal note at the end of the reference PDF must be removed from any genuine submission copy.
