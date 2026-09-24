# T4 多 Seed 稳定性结果

日期：2026-03-25

## 输入与来源

- 协议：A1
- seeds：42 / 43 / 44
- source files:
  - `predictions/baselines_a1/baseline_a1_results.json`
  - `predictions/baselines_a1_seed43/baseline_a1_results.json`
  - `predictions/baselines_a1_seed44/baseline_a1_results.json`
- 聚合 JSON：`pictures/t4_multi_seed_results.json`

## 每个 seed 的 unknown F1

| Seed | SASeg | MSP | Energy | U_union | Ensemble |
|---|---:|---:|---:|---:|---:|
| 42 | 0.7210 | 0.7219 | 0.7218 | 0.7280 | 0.7248 |
| 43 | 0.7096 | 0.7096 | 0.7096 | 0.7119 | 0.7110 |
| 44 | 0.7028 | 0.7028 | 0.7028 | 0.7117 | 0.7078 |

## mean±std 汇总

| 方法 | known mIoU | unknown F1 | unknown IoU | Precision | Recall |
|---|---:|---:|---:|---:|---:|
| SASeg | 0.8071±0.0029 | 0.7111±0.0075 | 0.5518±0.0091 | 0.7679±0.0214 | 0.6632±0.0216 |
| MSP | 0.8067±0.0025 | 0.7114±0.0079 | 0.5521±0.0095 | 0.7685±0.0216 | 0.6632±0.0216 |
| Energy | 0.8067±0.0025 | 0.7114±0.0079 | 0.5521±0.0095 | 0.7685±0.0216 | 0.6632±0.0216 |
| U_union | 0.8067±0.0025 | 0.7172±0.0076 | 0.5591±0.0093 | 0.7580±0.0167 | 0.6810±0.0146 |
| Ensemble | 0.8068±0.0025 | 0.7146±0.0074 | 0.5559±0.0089 | 0.7631±0.0208 | 0.6727±0.0187 |

## 关键结论

1. `SASeg / MSP / Energy` 仍然几乎不可区分。  
   `unknown F1` 分别为 `0.7111±0.0075`、`0.7114±0.0079`、`0.7114±0.0079`，差距只有 `0.0003` 量级。

2. `U_union` 在三个 seed 中都排第一。  
   它的 `unknown F1 = 0.7172±0.0076`，相对 `SASeg` 的平均增益为 `+0.0061±0.0028`。

3. `Ensemble` 稳定排第二，但提升仍然不大。  
   它相对 `SASeg` 的平均增益为 `+0.0034±0.0015`。

4. `known mIoU` 在所有方法间都非常接近。  
   结果集中在 `0.8067~0.8071`，说明差异主要来自 unknown 决策信号，而不是 backbone 波动。

5. 这组多 seed 结果支持当前的否定式结论：  
   `prototype-sphere support` 不是比简单 uncertainty baseline 更强的主导信号；论文主线更应放在 `unknown slot / structured abstention / A1-A2 protocol`。

## 额外观察

- 在 seed43 和 seed44 上，`SASeg`、`MSP`、`Energy` 的 A1 指标数值完全一致，进一步说明这三种决策信号在当前设置下难以区分。
- `U_union` 的方向性优势是稳定的，但量级仍然偏小，不适合写成“显著领先”。

## 备注

- 当前 T4 的 seed42 结果来自 `checkpoints/ablation/baseline/best.pth`，不是 `checkpoints/best.pth`。
- 因此 `code/eval/t4_multi_seed.py` 已同步对齐到这个 seed42 路径，确保脚本与本结果文档口径一致。
