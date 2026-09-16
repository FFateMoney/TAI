# Number provenance

This file prevents accidental mixing of result pipelines during the rewrite.

## Diagnostic results: source = `saseg_paper/main_en.tex`
Use only for diagnosis, not as the baseline in the complement full-system table.

- Synapse A1 independent architectures: PerPixel-K+1 F1 0.797 / IoU 0.663; structured query baseline F1 0.721 / IoU 0.564.
- Synapse A2 diagnostic: ensemble AUROC 0.971, AUPR 0.088, structured F1 0.006.
- AMOS22 A2 diagnostic: AUROC 0.990, structured F1 0.010.
- VOC A2 diagnostic: AUROC 0.970, AUPR 0.671, F1 0.002.
- Cityscapes A2 diagnostic: AUROC 0.956, AUPR 0.208, F1 0.022.
- Synapse proposal diagnostics: unknown-slot union IoU 0.005; hit@0.10 0.02; top-0.3% ensemble proposal upper bound union IoU 0.153, hit@0.10 0.70; linear probe AUROC 0.991; centroid distance 8.95.
- Refinement variants: direct redraw 0.039/0.080/0.048; residual refinement 0.071/0.420/0.169; best lightweight variant 0.073/0.440/0.172; proposal upper bound 0.153/0.700/0.188 (union IoU / hit@0.10 / component precision@0.10).

## Complement full-system results: source = `complement_paper/cas-dc-template.tex`
These are the canonical baseline/intervention numbers for VOC and Cityscapes because baseline and variants were evaluated under the same complement-study pipeline.

### VOC
- Baseline: Known mIoU 0.746; Unknown F1 0.008; IoU 0.004; Precision 0.005; Recall 0.012; AUROC 0.980.
- L1: mIoU 0.334; F1 0.175; IoU 0.096; Precision 0.096; Recall 0.994; AUROC 0.731.
- L2: mIoU 0.746; F1 0.372; IoU 0.228; Precision 0.231; Recall 0.954; AUROC 0.981.

### Cityscapes
- Baseline: Known mIoU 0.624; Unknown F1 0.017; IoU 0.008; Precision 0.011; Recall 0.032; AUROC 0.963.
- L1: mIoU 0.279; F1 0.035; IoU 0.018; Precision 0.018; Recall 0.987; AUROC 0.781.
- L2: mIoU 0.583; F1 0.074; IoU 0.038; Precision 0.047; Recall 0.140; AUROC 0.962.

### Road transfer
- RoadAnomaly21 baseline/L2 F1: 0.380 / 0.652.
- RoadObstacle21 baseline/L2 F1: 0.054 / 0.515.

## Controlled intervention: source = `complement_paper/cas-dc-template.tex`
- VOC baseline / stronger score / stronger candidates / both: F1 0.008 / 0.007 / 0.372 / 0.377; mIoU 0.746 / 0.745 / 0.746 / 0.745.
- Cityscapes baseline / stronger score / stronger candidates / both: F1 0.017 / 0.015 / 0.069 / 0.064; mIoU 0.624 / 0.624 / 0.512 / 0.497.

## Candidate-quality diagnostics: source = `complement_paper/cas-dc-template.tex`
- VOC: known-union IoU 0.6956; complement IoU 0.8885; recall 0.9997; precision 0.8887.
- Cityscapes: known-union IoU 0.5324; complement IoU 0.1709; recall 0.9898; precision 0.1711; known leakage 0.8289.
- Synapse CT: known-union IoU 0.6517; complement recall 0.9358; precision 0.0454; known leakage 0.9546.

## Backbone substitution: source = `complement_paper/cas-dc-template.tex`
- Baseline: VOC 0.7459/0.0075; Cityscapes 0.6242/0.0167 (mIoU/F1).
- SAM 3 PCS + L2: VOC 0.7457/0.3719; Cityscapes 0.5833/0.0736.
- SAM 2 + CLIP + L2: VOC 0.7393/0.2224; Cityscapes 0.6222/0.0330.

## Rule
Never present `0.002` and `0.008` as if they are the same VOC baseline measurement, or `0.022` and `0.017` as if they are the same Cityscapes baseline measurement. The first pair belongs to the original diagnostic pipeline; the second pair belongs to the complement full-system pipeline.
