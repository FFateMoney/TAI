# Cityscapes 接入与处理方案

## 1. 文档目的

本文档用于说明如何将已经下载好的 `Cityscapes` 数据接入当前 `SASeg` 项目，并与项目现有的 `A1 / A2 / M=0` 实验框架保持一致。

本文档只解决四件事：

- 当前 Cityscapes 原始数据中哪些文件真正需要使用
- 在本项目中应如何组织与预处理 Cityscapes 数据
- 如何把 Cityscapes 映射为 `known / seen unknown / unseen unknown`
- 后续代码接入时最少需要改哪些模块

---

## 2. 当前应使用的数据包

对于当前论文扩展实验，只使用以下两个官方包：

- `leftImg8bit_trainvaltest.zip`
- `gtFine_trainvaltest.zip`

不使用：

- `gtCoarse.zip`
- `leftImg8bit_trainextra.zip`
- 其他 stereo / disparity / camera / vehicle / timestamp 数据

原因很简单：

- 当前任务是语义分割，不需要额外模态
- 当前目标是补充 `A1 / A2 / M=0` 的跨域验证，不是做 Cityscapes 完整 benchmark
- `gtCoarse` 和 `train_extra` 会增加协议复杂度，不利于和主线对齐

---

## 3. 推荐的本地目录结构

推荐将 Cityscapes 解压到：

- `/my_storage/chen/saseg/dataset/cityscapes`

解压后目标结构应为：

- `/my_storage/chen/saseg/dataset/cityscapes/leftImg8bit/train`
- `/my_storage/chen/saseg/dataset/cityscapes/leftImg8bit/val`
- `/my_storage/chen/saseg/dataset/cityscapes/leftImg8bit/test`
- `/my_storage/chen/saseg/dataset/cityscapes/gtFine/train`
- `/my_storage/chen/saseg/dataset/cityscapes/gtFine/val`
- `/my_storage/chen/saseg/dataset/cityscapes/gtFine/test`

推荐解压命令：

```bash
mkdir -p /my_storage/chen/saseg/dataset/cityscapes
unzip -q /my_storage/chen/saseg/dataset/leftImg8bit_trainvaltest.zip -d /my_storage/chen/saseg/dataset/cityscapes
unzip -q /my_storage/chen/saseg/dataset/gtFine_trainvaltest.zip -d /my_storage/chen/saseg/dataset/cityscapes
```

---

## 4. Cityscapes 中真正要用哪些文件

对于当前项目的语义分割任务，推荐只使用：

### 4.1 图像

- `leftImg8bit/<split>/<city>/*_leftImg8bit.png`

例如：

- `leftImg8bit/train/jena/jena_000001_000019_leftImg8bit.png`

### 4.2 语义分割标签

- `gtFine/<split>/<city>/*_gtFine_labelIds.png`

例如：

- `gtFine/train/jena/jena_000001_000019_gtFine_labelIds.png`

### 4.3 当前阶段不需要的文件

- `*_gtFine_polygons.json`
- `*_gtFine_instanceIds.png`
- `*_gtFine_color.png`

这些都不是当前主线必须输入。  
当前项目只需要：

- 原始 RGB 图像
- 按像素编码的语义标签图

---

## 5. 当前项目中对 Cityscapes 的固定使用范围

当前阶段只使用：

- `train`
- `val`

不使用：

- `test`

原因是：

- 当前论文扩展实验只需要本地可评估的结果
- 官方 `test` 不适合作为当前本地主评估集
- 当前工程虽然保留 `train / val / test` 三个 split 接口，但 Cityscapes 的第一版实现应与 `VOC` 一样，优先保证 `train / val` 跑通

推荐约定：

- `train` = 官方 `train`
- `val` = 官方 `val`
- `test` = 暂时复用官方 `val`

这只是为了兼容现有工程接口，不代表论文要报告单独 test 结果。

---

## 6. Cityscapes 的标签处理原则

### 6.1 不直接使用原始 `labelIds`

Cityscapes 的 `*_gtFine_labelIds.png` 使用的是官方原始标签编码。  
在本项目中，不应直接把这些原始编码作为训练标签，而应先统一映射到标准 `trainIds`。

固定规则如下：

- 先读取 `*_gtFine_labelIds.png`
- 再将其映射为 `trainIds`
- 所有非 19 个主类的像素统一映射为 `255`

### 6.2 固定采用 19 类 `trainIds`

本项目中，Cityscapes 统一采用以下 `trainIds`：

- `0` road
- `1` sidewalk
- `2` building
- `3` wall
- `4` fence
- `5` pole
- `6` traffic light
- `7` traffic sign
- `8` vegetation
- `9` terrain
- `10` sky
- `11` person
- `12` rider
- `13` car
- `14` truck
- `15` bus
- `16` train
- `17` motorcycle
- `18` bicycle
- `255` ignore

### 6.3 固定的 `labelIds -> trainIds` 映射

原始 `labelIds` 应按下列规则转换：

- `7 -> 0`
- `8 -> 1`
- `11 -> 2`
- `12 -> 3`
- `13 -> 4`
- `17 -> 5`
- `19 -> 6`
- `20 -> 7`
- `21 -> 8`
- `22 -> 9`
- `23 -> 10`
- `24 -> 11`
- `25 -> 12`
- `26 -> 13`
- `27 -> 14`
- `28 -> 15`
- `31 -> 16`
- `32 -> 17`
- `33 -> 18`

除此之外，全部映射为：

- `255`

这一步非常关键，因为当前项目的下游逻辑需要一个稳定、连续、可控的多类标签空间。

### 6.4 `255` 的含义

`255` 在本项目中固定解释为：

- ignore / void

因此：

- `255` 不能当 background
- `255` 不能当 unknown
- `255` 必须在训练损失、边界图构造和评估中排除

---

## 7. 推荐的 Cityscapes 协议划分

当前建议严格沿用 `doc/拓展意见.md` 中已经确定的划分。

### 7.1 Known（14 类）

- road
- sidewalk
- building
- wall
- fence
- pole
- traffic light
- traffic sign
- vegetation
- terrain
- sky
- person
- rider
- car

对应 `trainIds`：

- `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]`

### 7.2 Seen Unknown（3 类）

- truck
- bus
- train

对应 `trainIds`：

- `[14, 15, 16]`

### 7.3 Unseen Unknown（2 类）

- motorcycle
- bicycle

对应 `trainIds`：

- `[17, 18]`

---

## 8. 在 SASeg 中如何定义 A1 / A2

### 8.1 A1

训练和验证都把：

- `[14, 15, 16]`

作为 unknown 联合区域。

也就是说：

- train unknown labels = seen unknown
- val unknown labels = seen unknown

核心验证点：

- `M=2` 能否形成 coherent unknown mask
- `M=0` 后 unknown F1 是否显著崩塌

### 8.2 A2

训练时把：

- `[14, 15, 16]`

作为 unknown 监督；

验证时把：

- `[17, 18]`

作为 unseen unknown。

也就是说：

- train unknown labels = seen unknown
- val unknown labels = unseen unknown

核心验证点：

- detection 排序是否仍保持较强
- 最终 structured abstention mask 是否明显失效

---

## 9. 推荐的预处理输出格式

建议完全仿照当前已经跑通的 `VOC2012` 实现。

输出目录固定为：

```text
dataset/preprocessed/
  cityscapes/
    train/
    val/
    test/
```

对每张图固定保存四个文件：

### 9.1 图像

- `<stem>_img.npy`

格式：

- `float32`
- 形状 `(3, 512, 512)`
- 值域 `[0, 1]`

### 9.2 标签图

- `<stem>_lbl.npy`

格式：

- `uint8`
- 形状 `(512, 512)`
- 取值为 `0..18, 255`

这里保存的是已经完成 `labelIds -> trainIds` 转换后的标签图。

### 9.3 ignore mask

- `<stem>_ign.npy`

格式：

- `float32`
- 形状 `(512, 512)`
- `1 = ignore`
- `0 = valid`

固定规则：

- `ign = (lbl == 255).astype(np.float32)`

### 9.4 boundary map

- `<stem>_bnd.npy`

格式：

- `float32`
- 形状 `(512, 512)`
- 值域 `[0, 1]`

固定构造方式：

1. 先复制标签图
2. 将 `255` 临时替换为 `0`
3. 对替换后的标签图调用当前项目已有的 `make_boundary_map()`
4. 再把 ignore 区域置零

---

## 10. 推荐的预处理行为

`process_cityscapes()` 的固定行为应为：

1. 遍历 `leftImg8bit/train` 与 `gtFine/train`
2. 遍历 `leftImg8bit/val` 与 `gtFine/val`
3. 逐一匹配文件名 stem
4. 图像用双线性插值 resize 到 `512 x 512`
5. 标签图用最近邻插值 resize 到 `512 x 512`
6. 将原始 `labelIds` 映射为 `trainIds`
7. 生成 `ignore_mask`
8. 生成 `boundary_map`
9. 写入 `dataset/preprocessed/cityscapes/{train,val,test}`

其中：

- `test` 先固定复用 `val`

这一点与当前 `VOC` 的工程处理方式保持一致。

---

## 11. 与 VOC 的关系

当前 Cityscapes 最合理的接入方式，不是重新发明一套数据逻辑，而是：

- 复用 VOC 的 RGB 输入接口
- 复用 VOC 的 `ignore_mask` 接口
- 复用 VOC 的 `img/lbl/ign/bnd` 四文件输出格式

Cityscapes 相对于 VOC 的唯一关键新增步骤是：

- 必须先做 `labelIds -> trainIds`

因此，Cityscapes 应被视为：

> VOC 接入模式在更复杂 scene parsing 数据上的直接扩展。

---

## 12. 后续代码接入时最少需要改哪些模块

### 12.1 `code/data/preprocess.py`

新增：

- `CITYSCAPES_ROOT = DATASET_ROOT / "cityscapes"`
- `process_cityscapes()`

并在 CLI 中增加：

- `--dataset cityscapes`

### 12.2 `code/data/dataset.py`

新增：

- `CITYSCAPES_CLASS_NAMES`
- `CITYSCAPES_KNOWN_LABELS`
- `CITYSCAPES_SEEN_UNKNOWN_LABELS`
- `CITYSCAPES_UNSEEN_UNKNOWN_LABELS`
- `CityscapesDataset`

同时在 `build_datasets()` 中加入：

- `dataset_name == "cityscapes"` 的分支

### 12.3 配置文件

新增：

- `code/configs/cityscapes_a1.yaml`
- `code/configs/cityscapes_a2.yaml`
- `code/configs/cityscapes_m0.yaml`

其中：

- `data.dataset: cityscapes`
- `data.image_size: 512`
- `data.known_labels: [0..13]`
- `data.seen_unknown_labels: [14, 15, 16]`
- `data.unseen_unknown_labels: [17, 18]`

---

## 13. 当前阶段不建议做的事

当前阶段不建议：

- 引入 `gtCoarse`
- 引入 `train_extra`
- 使用官方 `test` 作为主实验集
- 把 Cityscapes 做成新的完整 benchmark

当前最重要的是：

- 先复现 `A1`
- 再复现 `A2`
- 再做 `M=0`

也就是只验证两条核心现象：

1. `native unknown slots` 的必要性
2. `detection-structuring gap`

---

## 14. 一句话总结

对于当前项目，Cityscapes 的最合理接入方式是：

> 使用 `leftImg8bit train/val + gtFine labelIds train/val` 作为原始输入，在预处理阶段统一将 `labelIds` 映射到 `trainIds (0..18, 255)`，再按与 `VOC2012` 相同的 `img / lbl / ign / bnd` 四文件格式落到 `dataset/preprocessed/cityscapes`，并在数据集层通过固定的 `known / seen unknown / unseen unknown` 划分实现 `A1 / A2 / M=0`。
