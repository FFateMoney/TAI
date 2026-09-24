# T6 Region-Level 候选分析结果

日期：2026-03-25

## 输入与来源

- 协议：A2
- checkpoint：`/my_storage/chen/saseg/checkpoints/a2/best.pth`
- 数据集：Synapse val split
- unknown labels：`[12, 13]`
- unknown slots：`M=2`
- slot 二值化阈值：`0.5`
- connected components：`8-connected`

源文件：
- `pictures/t6_region_summary_a2.json`
- `pictures/t6_region_report_a2.md`
- `pictures/t6_region_slices_a2.csv`
- `pictures/t6_region_components_a2.csv`

## 核心统计

- 总 slice 数：`262`
- 含 unknown GT 的 slice 数：`50`
- 提取到的候选 component 总数：`431`
- candidate union 总像素：`253365`
- GT unknown 总像素：`13616`
- candidate-union IoU（unknown slices）：
  - mean：`0.0048`
  - median：`0.0023`

### Unknown-slice hit rate

- 全部 component：
  - overlap > 0：`0.6600`
  - best IoU >= 0.10：`0.0200`
  - best IoU >= 0.25：`0.0000`

- area >= 32 px component：
  - overlap > 0：`0.6200`
  - best IoU >= 0.10：`0.0000`
  - best IoU >= 0.25：`0.0000`

### Component-level precision

- 全部 component：
  - IoU >= 0.10：`0.0023`
  - IoU >= 0.25：`0.0000`

- area >= 32 px component：
  - IoU >= 0.10：`0.0000`
  - IoU >= 0.25：`0.0000`

### 尺度分布

- 原始 component 面积桶：
  - `<16`：`92`
  - `16-63`：`57`
  - `64-255`：`47`
  - `256-1023`：`160`
  - `>=1024`：`75`

- 全部 component：
  - median area：`357 px`

- area >= 32 px component：
  - count：`315`
  - median area：`573 px`
  - mean best IoU：`0.0012`

## 定性结论

1. unknown slot 在 A2 下并非完全没有响应。  
   在 `50` 张含 unknown 的 slice 中，有 `66%` 的 slice 至少有一个 candidate component 与 GT unknown 有像素级接触。

2. 但这些候选区域几乎从未形成可用区域。  
   即使放宽到 `IoU >= 0.10`，unknown-slice 命中率也只有 `0.02`；对 `>=32 px` 的较大 component，这个数直接降为 `0.00`。

3. 候选区域的 purity 极差。  
   candidate union 总像素是 GT unknown 总像素的约 `18.6x`，而 union IoU 的 mean 只有 `0.0048`。这说明 unknown slot 在 A2 下主要表现为大面积误激活，而不是“接近正确区域，只差一个阈值”。

4. 当前 region features 也不足以支持“简单 region-level classifier 就能救回来”的乐观判断。  
   在 `area >= 32 px` 的 component 上，没有任何一个达到 `IoU >= 0.10`，因此根本不存在稳定的正候选可供一个轻量 classifier 学习。

## 对问题定义的解释

这组结果不支持下面这个强说法：

> 模型已经产生了有效候选区域，只差一个 region-level decision。

它只支持一个更弱、更准确的说法：

> unknown slot 在部分 A2 slice 上会粗略靠近 unknown 区域，但 candidate generation / candidate purity 本身仍然很差，瓶颈不只是 pixel-level thresholding。

换句话说，A2 的失败不能简单归因于“逐像素决策不好”；更大的问题是，unknown slot 生成的候选区域本身就不够纯、不够准。

## 对论文的直接意义

### 支持的结论

- `Detection != Structuring` 的分离更清楚了。  
  A2 上 pixel-level ensemble 排序可以很好，但 unknown slot 的 region candidate 仍然几乎不可用。

- A2 的问题不只是 base-rate。  
  base-rate 解释了为什么 F1 很难高，但 T6 进一步表明：即使切到 region level，当前候选本身也没有达到“可决策”的质量。

- 这强化了“unseen unknown structuring 是独立难题”的论点。  
  你可以更有力地说：A2 不只是 detection 后处理问题，而是 candidate generation/purity 问题。

### 不支持的结论

- 不支持把 future work 写成“只要加一个 region-level decision head 就能解决 A2”。
- 不支持把当前 unknown slot 描述成“已经提供了高质量候选区域”。

### 更合适的论文表述

这组结果更适合被写成一个否定式发现：

> Region-level analysis shows that unknown-slot components overlap GT on many A2 slices, but almost never reach even IoU 0.1. Therefore, the A2 bottleneck is not merely region-level decision; candidate purity itself is the dominant failure mode.

## 建议的后续定位

- 如果论文主线是 `A1/A2 protocol + native unknown slots + detection/structuring separation`，那么 T6 是有价值的负结果，应当保留。
- 如果论文主线想转成“我们只差一个 region classifier 就能搞定 A2”，那 T6 反而会削弱这个叙事。
- 更自然的 future work 方向不是直接上 classifier，而是先改善 candidate generation：
  - 调 slot threshold / component filtering
  - 用 ensemble top-r% 生成 seeds 再做区域生长
  - 加器官边界或形态先验约束
  - 重新设计 unseen-unknown 的 region proposal 机制
