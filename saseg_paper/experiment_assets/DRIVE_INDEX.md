# Google Drive asset index

Experiment backup root:

https://drive.google.com/drive/folders/1ZuB3jnd_RwPLpovVbWMvPxHxasgby46j?usp=drive_link

## Assets kept in Drive

| Drive directory | Purpose | Why not copied wholesale to GitHub |
|---|---|---|
| `code/` | complete training, model, data, loss, inference and evaluation source | full source snapshot remains in the server backup for now; GitHub contains configs and evidence needed for paper handoff |
| `dataset/` | Synapse, AMOS22, VOC2012, Cityscapes, MOOD and preprocessed data | large files, dataset licensing, local data organization |
| `checkpoints/` | trained model weights | individual `.pth` files are roughly hundreds of MB |
| `predictions/` | per-image/per-slice prediction arrays | many `.npy` files; large aggregate size |
| `logs/` | full raw training/evaluation history | complete logs remain available on Drive |
| `pictures/` | figures plus intermediate CSV/JSON/NPZ analysis assets | selected load-bearing numeric outputs are copied to `results/` |
| `result/` | complete result/diagnostic working directory | selected load-bearing summaries are copied to `results/` |
| `doc/` | experiment and writing notes | selected useful handoff documents are copied to `docs/` |

## Important exclusions

- `dataset/synapse_token`: credential/token-like file; never commit it to a source repository.
- Cityscapes `leftImg8bit_trainvaltest.zip` is multi-GB and remains in Drive.
- checkpoint files such as `best.pth` / `latest.pth` remain in Drive.
- bulk `.npy` predictions remain in Drive.

## Recommended handoff workflow

1. Read the first-paper manuscript under `saseg_paper/` and the reviewer materials under `审稿意见/`.
2. Use `experiment_assets/docs/` to understand experiment history and dataset-integration decisions.
3. Use `experiment_assets/configs/` to trace splits, protocols, supervision and output paths.
4. Use `experiment_assets/results/` to check load-bearing numeric claims.
5. Open the Drive backup only when raw source, a complete log, checkpoint, prediction array, or dataset is needed.
