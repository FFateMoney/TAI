# T6 Region-Level Candidate Analysis

## Input
- Protocol: `A2`
- Checkpoint: `/my_storage/chen/saseg/checkpoints/a2/best.pth`
- Dataset: `synapse`
- Unknown labels (A2 eval): `[12, 13]`
- Unknown slots: `2`
- Slot binarization threshold: `0.5`
- Connectivity: `8`-connected
- Slices analyzed: `262` (`unknown_slices=50`)

## Global Summary
- Raw candidate components: `431`
- Mean candidate-union IoU on unknown slices: `0.0048`
- Median candidate-union IoU on unknown slices: `0.0023`
- Area buckets: `{'<16': 92, '16-63': 57, '64-255': 47, '256-1023': 160, '>=1024': 75}`

## Candidate Summary (all components)
- Components per slice: mean `1.65`, median `1.00`
- Components per unknown slice: mean `3.80`
- Unknown-slice hit rate (overlap > 0): `0.6600`
- Unknown-slice hit rate (best IoU >= 0.10): `0.0200`
- Unknown-slice hit rate (best IoU >= 0.25): `0.0000`
- Component match rate (IoU >= 0.10): `0.0023`
- Component match rate (IoU >= 0.25): `0.0000`
- Size median: `357.0` px

## Candidate Summary (components >= 32 px)
- Components: `315`
- Unknown-slice hit rate (overlap > 0): `0.6200`
- Unknown-slice hit rate (best IoU >= 0.10): `0.0000`
- Unknown-slice hit rate (best IoU >= 0.25): `0.0000`
- Component match rate (IoU >= 0.10): `0.0000`
- Mean best IoU: `0.0012`
- Median size: `573.0` px

## Feature Comparison (components >= 32 px)
- Matched (`IoU>=0.10`) mean features: `{'mean_neg_maxprob': nan, 'mean_u_union': nan, 'mean_ensemble': nan, 'mean_area_px': nan}`
- Clear unmatched (`IoU==0`) mean features: `{'mean_neg_maxprob': 0.8853289558878301, 'mean_u_union': 0.9206121820572009, 'mean_ensemble': 0.8923856119138066, 'mean_area_px': 652.0427046263345}`

## Discussion
- Large candidates reach GT on a non-trivial fraction of unknown slices (overlap hit `0.620`), but IoU-qualified hits remain modest (`0.000`). This suggests rough candidate localization exists, while purity / selection is still the bottleneck.
- Candidate precision at IoU>=0.10 is low (`0.000`), so any future region-level decision head will need strong filtering rather than simple thresholding.

## Top Components by IoU (area >= 32 px)
| case | slice | slot | comp | area | best IoU | overlap frac | mean neg_maxprob | mean u_union |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| img0040 | 108 | 0 | 2 | 1136 | 0.039 | 0.043 | 0.904 | 0.975 |
| img0040 | 104 | 0 | 2 | 2679 | 0.027 | 0.029 | 0.977 | 0.933 |
| img0037 | 71 | 0 | 2 | 2597 | 0.022 | 0.023 | 0.981 | 0.930 |
| img0040 | 105 | 0 | 4 | 2048 | 0.022 | 0.024 | 0.987 | 0.922 |
| img0040 | 106 | 0 | 3 | 1216 | 0.019 | 0.024 | 0.965 | 0.944 |
| img0038 | 70 | 0 | 1 | 1212 | 0.019 | 0.021 | 0.992 | 0.967 |
| img0037 | 78 | 0 | 3 | 782 | 0.018 | 0.029 | 0.943 | 0.968 |
| img0037 | 73 | 0 | 3 | 4086 | 0.017 | 0.018 | 0.940 | 0.936 |
| img0039 | 69 | 0 | 2 | 589 | 0.017 | 0.019 | 0.975 | 0.980 |
| img0040 | 109 | 0 | 2 | 942 | 0.015 | 0.018 | 0.945 | 0.972 |

## Hard False Positives by mean_u_union (IoU == 0, area >= 32 px)
| case | slice | slot | comp | area | best IoU | overlap frac | mean neg_maxprob | mean u_union |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| img0037 | 90 | 1 | 1 | 55 | 0.000 | 0.000 | 0.991 | 1.000 |
| img0037 | 90 | 1 | 2 | 53 | 0.000 | 0.000 | 0.993 | 1.000 |
| img0037 | 92 | 1 | 1 | 34 | 0.000 | 0.000 | 0.994 | 1.000 |
| img0037 | 90 | 0 | 1 | 1083 | 0.000 | 0.000 | 0.768 | 0.994 |
| img0037 | 91 | 0 | 1 | 938 | 0.000 | 0.000 | 0.992 | 0.993 |
| img0039 | 85 | 0 | 1 | 491 | 0.000 | 0.000 | 0.999 | 0.991 |
| img0037 | 89 | 0 | 1 | 1177 | 0.000 | 0.000 | 0.820 | 0.991 |
| img0040 | 126 | 0 | 1 | 841 | 0.000 | 0.000 | 0.999 | 0.990 |
| img0037 | 88 | 0 | 1 | 1328 | 0.000 | 0.000 | 0.999 | 0.989 |
| img0040 | 127 | 0 | 1 | 856 | 0.000 | 0.000 | 0.999 | 0.988 |
