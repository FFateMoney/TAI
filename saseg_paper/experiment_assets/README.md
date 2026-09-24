# SASeg experiment assets (handoff copy)

This directory contains a lightweight handoff copy of the experiment assets around the first SASeg manuscript. It is meant for manuscript revision, result tracing, and protocol auditing without mirroring the full server backup into GitHub.

## Included in GitHub

- `docs/`: experiment/design/dataset-integration notes from the server backup.
- `configs/`: representative Synapse, AMOS22, VOC2012, Cityscapes, A1/A2/M0, PerPixel-K/K+1, and alternative-split YAML configurations.
- `results/`: lightweight JSON/CSV/Markdown outputs for multi-seed stability, operating points, region-level diagnostics, and AMOS feasibility.
- `requirements.txt`: environment dependency list from the experiment backup.

The documents in `docs/` are historical working materials. Some contain interpretations or claims that were later challenged by reviewers. Preserve them as provenance; do not treat every sentence as a current paper claim. For evidence, prioritize the submitted manuscript, raw result files, configs, and reviewer comments.

## Kept in Google Drive

The full source tree, complete logs, datasets, checkpoints, prediction arrays, and bulk intermediate outputs remain in Google Drive because of size, licensing, or repository hygiene:

https://drive.google.com/drive/folders/1ZuB3jnd_RwPLpovVbWMvPxHxasgby46j?usp=drive_link

See `DRIVE_INDEX.md` for the mapping.

## Security

Credential-like files are intentionally excluded. In particular, `dataset/synapse_token` from the server backup is **not** copied into this repository.

## Provenance

The files here are copied from the existing experiment Drive backup; they are not newly generated experiments. Directory placement is reorganized only for handoff clarity.
