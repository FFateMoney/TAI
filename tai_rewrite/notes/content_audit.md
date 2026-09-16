# Content completeness and consistency audit

Audit target: `tai_rewrite/main.tex` + `supplementary.tex`, checked against the two source manuscripts and the reviewer comments. No new experimental result is introduced.

## Fixed during audit

1. **Road-scene metric provenance** — The unified-protocol `Unknown F1` values (RA21 0.380 -> 0.652; RO21 0.054 -> 0.515) are now explicitly separated from the official SMIYC `Pix Best F1` values (RA21 0.5186 -> 0.5459; RO21 0.5117 -> 0.5256). The abstract no longer quotes the unified road F1 without provenance, and the main text reports the official SMIYC metrics separately.
2. **Medical dataset role** — AMOS22 is used as evidence for the original medical A2 detection--structuring diagnosis. The available complement-grounding failure analysis is specific to Synapse and is no longer implicitly attributed to AMOS22.
3. **A1 claim strength** — `explicit unknown output is sufficient` was softened to `can support structured rejection`, consistent with the limited supervised-control evidence.
4. **Zero-shot terminology** — Keywords now say `zero-shot candidate generation`; the body already states that zero-shot refers only to held-out unseen categories and that the frozen A2 checkpoint may inherit generic seen-unknown supervision.
5. **Reviewer-requested Cen et al. citation** — Added Jun Cen et al., *Deep Metric Learning for Open World Semantic Segmentation*, ICCV 2021, and cited it in the introduction/related positioning.
6. **Diagnostic-vs-complement numerical provenance** — The rewrite retains separate values for the old diagnostic evaluator and the complement-study evaluator. `0.002` vs `0.008` (VOC) and `0.022` vs `0.017` (Cityscapes) are not treated as identical measurements.

## Internally consistent after audit

- Synapse class partition names in the rewrite match the archived SASeg source manuscript, including its labels 12--13 definition.
- VOC and Cityscapes class counts/names match between main/supplement and the archived split description.
- Intervention numbers match the complement manuscript and are internally consistent with the full-system table.
- Candidate-quality numbers in the main paper are rounded versions of the exact supplementary values.
- Backbone-comparison values match the complement manuscript.
- The claim hierarchy is consistent: A1 is a supervised control; A2 is the main scientific setting; candidate generation is the intervention target; scoring is retained as a selector rather than dismissed as useless.

## Visual/LaTeX audit fixes

- Added `xspace` handling for the `CCG` macro so prose no longer renders as `CCGis` / `CCGassumes`.
- Constrained the single-column diagnostic/candidate tables to `\columnwidth` and the full-system table to `\textwidth`, removing the observed cross-column overflow.
- Added a float barrier before Discussion so the qualitative figure cannot drift behind the References section.
- Removed the empty bibliography from the supplementary material; the first compiled version otherwise produced a mostly empty fourth page containing only `References`.
- A GitHub Actions compile workflow now produces the main and supplementary PDFs plus LaTeX logs for repeatable checking.

## Remaining content-completeness blockers (do not invent)

1. **Exact construction of `M_fg`** — The archived complement manuscript only calls it the image foreground used by the pipeline; it does not specify a reproducible operational construction in the manuscript text available in this repository.
2. **Exact class-agnostic mask-generator configuration** — The archived manuscript describes the capability and backbone comparison but does not provide enough implementation detail in the available text to reconstruct all generator settings. This should be recovered from the cloud code/config before submission if possible; it does not require rerunning experiments.
3. **Computational cost** — Reviewer 1 requested training/inference time, memory, and module overhead. No measured values are present in the archived paper sources, so the rewrite does not fabricate them. This remains an acknowledged unresolved reviewer request.
4. **Held-out leakage guarantee** — Threshold/evaluator provenance is stated conservatively, but the repository does not contain enough raw experiment artifacts in this rewrite folder to independently re-audit every split/threshold selection path. The paper therefore avoids hidden-test or leakage-free benchmark claims.
5. **Author/affiliation and code-release metadata** — Still placeholders / submission logistics.

## Submission-level interpretation

The manuscript is content-complete for its narrowed mechanism narrative except for the implementation details of `M_fg` / the class-agnostic candidate generator. Those two details are the highest-priority non-experimental items to recover before final submission because Reviewer 4 previously criticized incomplete method definitions.
