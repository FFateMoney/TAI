# SASeg 论文写作方案

**目标期刊**：Knowledge-Based Systems (KBS), Elsevier
**排版格式**：Elsevier 双栏 preprint 模板，XeLaTeX 编译，中文草稿
**日期**：2026-03-30

---

## 1. 论文定位

本文不是"一个全面优于 baseline 的几何 unknown 检测器"论文，而是一篇关于**医学结构化弃权分割**的问题设定 / 协议设计 / 机制验证 / 失败模式分析论文。

核心叙事：**以问题设定为第一贡献，方法为验证问题设定的工具，经验发现为对问题本质的深入刻画。**

---

## 2. 论文标题（候选）

- Structured Abstention Segmentation: Native Unknown Representation for Open-World Medical Image Parsing
- Beyond Detection: Structured Abstention via Native Unknown Slots in Medical Image Segmentation

---

## 3. 三条核心贡献

1. **问题与协议贡献**：提出医学分割中的 structured abstention 视角，将 unknown segmentation 拆分为 seen-unknown structuring (A1) 与 unseen-unknown detection (A2) 两个本质不同的子问题，并设计双协议分别评估。
2. **机制贡献**：提出 native-abstention 区域解析框架，通过 unknown query slots 在与 known queries 同一竞争空间内原生表达 unknown 区域，辅以 prototype-sphere 几何支持度判定；M=0 消融在两个独立数据集上证明原生 unknown 输出空间对结构化弃权的必要性。
3. **经验性发现贡献**：揭示 support-deficit 与 competitive-ambiguity 两类 unknown regime，并通过像素级与区域级分析表明：A2 的瓶颈不只是 detection score，而是 unseen-unknown 的 candidate purity。

---

## 4. 论文结构与章节规划

| 章节 | 标题 | 主要内容 | 预计篇幅 |
|------|------|----------|----------|
| §1 | Introduction | 问题动机 → 现有方法局限 → structured abstention 视角 → 贡献列表 | 2–2.5 页 |
| §2 | Related Work | 医学分割 OOD / open-set recognition / query-based segmentation / prototype learning | 2 页 |
| §3 | Problem Formulation | structured abstention 定义；A1/A2 双协议；detection vs structuring 的区分 | 1 页 |
| §4 | Method | 4.1 整体架构 → 4.2 编码器与像素解码器 → 4.3 区域解析器 → 4.4 支持度模块 → 4.5 损失函数 → 4.6 推理与决策 | 3–4 页 |
| §5 | Experiments | 5.1 实验设置 → 5.2 A1 主结果 → 5.3 A2 主结果 → 5.4 消融实验 → 5.5 跨数据集验证 → 5.6 分析实验 | 5–6 页 |
| §6 | Discussion | detection ≠ structuring 深入讨论；candidate purity 瓶颈；局限性与未来方向 | 1–1.5 页 |
| §7 | Conclusion | 总结贡献与核心发现 | 0.5 页 |

---

## 5. 写作顺序

按以下顺序撰写，每完成一个章节即可交付审阅：

1. **§3 Problem Formulation** — 最核心的贡献，先定义清楚问题
2. **§4 Method** — 方法是支撑问题定义的工具
3. **§5 Experiments** — 实验验证
4. **§6 Discussion** — 深入分析
5. **§1 Introduction** — 基于已写好的内容提炼引言
6. **§2 Related Work** — 最后补充
7. **§7 Conclusion** — 收尾
8. **Abstract** — 全文完成后最后写

---

## 6. 写作红线（不可违反）

以下表述在当前证据下**不成立**，论文中**禁止出现**：

1. ❌ "prototype-sphere 是比 MSP / Energy 更好的 unknown detector"
2. ❌ "A2 的问题主要只差一个 region-level decision"
3. ❌ "unknown slot 已经提供了高质量 unseen-unknown 候选区域"
4. ❌ "我们的方法已经统一解决了 detection 与 structuring"

---

## 7. 写作策略

### 7.1 Prototype-sphere 的定位

不写成"更强的检测器"，而写成：
- 对已知解剖知识的**显式几何编码**（knowledge boundary）
- 原生 unknown 输出空间的**几何基础**
- 在特定操作区间（低 FPR）保留**互补高精度信号**

### 7.2 负结果的转化

- A1 上 support ≈ MSP → 说明 seen-unknown 的结构化能力来自 unknown slot 本身，而非检测信号的选择
- A2 上 F1 ≈ 0 → 揭示 detection ≠ structuring 的核心事实
- T6 candidate purity 极差 → 指出 A2 的瓶颈是 candidate generation，而非 decision

### 7.3 跨数据集验证

AMOS22 的三项结果（A1/A2/M=0）全部跨数据集一致，作为独立小节重点展示。

---

## 8. 数据源映射

论文中每个数字都必须可追溯到具体结果文件：

| 论文内容 | 数据源文件 |
|----------|-----------|
| A1 主表 | `predictions/baselines_a1/baseline_a1_results.json` |
| A2 主表 | `predictions/baselines/baseline_results.json` |
| M=0 消融 | `predictions/m0/eval_m0_results.json` |
| 结构消融 | `predictions/ablation/ablation_results.json` |
| 多 seed | `pictures/t4_multi_seed_results.json` |
| A2 retrieval | `pictures/t5_topr_retrieval_a2.json` |
| A2 region-level | `pictures/t6_region_summary_a2.json` |
| AMOS A1 | `predictions/amos22_ct/eval_results.json` |
| AMOS A2 | `predictions/amos22_ct_a2/eval_results.json` |
| AMOS M=0 | `predictions/amos22_ct_m0_eval/eval_m0_results.json` |

---

## 9. 图表规划

| 编号 | 类型 | 内容 | 来源 |
|------|------|------|------|
| Fig.1 | 概念图 | Structured abstention 动机：后处理 vs 原生输出 | 需新绘 |
| Fig.2 | 架构图 | 四模块流水线 | 需新绘 |
| Fig.3 | 分析图 | T1 score distribution（A1 vs A2 对比） | `pictures/t1_*.png` |
| Fig.4 | 可视化 | M=2 vs M=0 定性对比 | `pictures/t2_*.png` |
| Fig.5 | 曲线图 | A2 PR/ROC 曲线 | `pictures/t3_*.png` |
| Tab.1 | 主表 | A1 方法对比 | §8 数据源 |
| Tab.2 | 主表 | A2 方法对比 | §8 数据源 |
| Tab.3 | 消融 | 结构消融（M/R/Loss） | §8 数据源 |
| Tab.4 | 消融 | M=0 核心消融 | §8 数据源 |
| Tab.5 | 验证 | AMOS22 跨数据集 | §8 数据源 |

---

## 10. 符号约定

在论文全文中统一使用以下符号：

| 符号 | 含义 |
|------|------|
| $\mathcal{K}$ | 已知类标签集合，$|\mathcal{K}|=K$ |
| $\mathcal{U}_{\text{seen}}$ | 训练时可见的 unknown 类别 |
| $\mathcal{U}_{\text{unseen}}$ | 训练时不可见的 unknown 类别 |
| $M$ | Unknown query slot 数量（默认 2） |
| $R$ | 每类 prototype-sphere 数量（默认 2） |
| $\mathbf{F}$ | Pixel decoder 输出特征图 |
| $\mathbf{q}_k$ | 第 $k$ 个 known anatomy query |
| $\mathbf{u}_m$ | 第 $m$ 个 unknown query |
| $\mathbf{z}_r$ | 区域 $r$ 的 region embedding |
| $(\boldsymbol{\mu}_{k,r}, \rho_{k,r})$ | 已知类 $k$ 第 $r$ 个 prototype-sphere |
| $s(\mathbf{z})$ | 支持分数（最小越界量） |
| $U_{\text{union}}$ | Unknown union 响应 |
| $\tau_{\text{obj}}$ | No-object 置信度阈值 |
| $\tau_{\text{abs}}$ | 弃权阈值 |
