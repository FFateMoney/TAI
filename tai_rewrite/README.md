# TAI rewrite: detection-to-structuring

This directory contains the zero-new-experiment rewrite that merges the diagnostic content of `saseg_paper` with the candidate-generation content of `complement_paper`.

## Files
- `main.tex`: rewritten IEEE TAI manuscript.
- `supplementary.tex`: reused implementation details, class splits, prompt ablation, SMIYC public-validation results, and interpretive guardrails.
- `references_additions.bib`: references newly required by the rewritten positioning (RbA, Mask2Anomaly, Mask2Former, Cen et al., SMIYC, SAM 2/3, CLIP).
- `notes/reviewer_map.md`: reviewer concern -> rewrite response mapping.
- `notes/number_provenance.md`: source and evaluator provenance for every load-bearing number.
- `notes/content_audit.md`: content-completeness, consistency, and visual-audit findings, including unresolved non-experimental blockers.

## Main narrative
1. Unknown detection and structured unknown output are different capabilities.
2. Existing A2 diagnostics localize the dominant missing capability to spatial candidate generation.
3. Complement Candidate Generation explains known concepts first, then uses residual foreground as candidate structure.
4. Controlled interventions show that candidate replacement, not score strengthening, produces the main gain.
5. Existing results define effective (VOC), trade-off (Cityscapes), transfer (RA21/RO21), and failure-boundary (Synapse CT) regimes; AMOS22 contributes to the original medical A2 diagnosis rather than to the complement-grounding failure probe.

## Claims deliberately removed
- Native unknown queries are **not** claimed to be necessary.
- A1/A2 is **not** presented as a standalone methodological contribution.
- SASeg is **not** claimed to outperform K+1 segmentation in supervised A1.
- Cross-domain observations are **not** stated as universal statistical laws.
- SMIYC results are **not** presented as leaderboard/state-of-the-art claims.

## Build and PDF QA
The manuscript reuses the IEEE TAI class from `saseg_paper` and figures from the two existing project directories. `.github/workflows/compile-rewrite.yml` performs repeatable GitHub Actions builds of both the main manuscript and supplementary material and uploads PDFs plus LaTeX logs as an artifact.

A local build from `tai_rewrite/` is still possible with:

```bash
TEXINPUTS=../saseg_paper: pdflatex main.tex
BIBINPUTS=../saseg_paper:. bibtex main
TEXINPUTS=../saseg_paper: pdflatex main.tex
TEXINPUTS=../saseg_paper: pdflatex main.tex
```

The CI build has been executed successfully. A PDF visual audit identified and fixed cross-column table overflow, missing spaces after the `CCG` macro, late placement of the qualitative figure after the references, and an empty supplementary references page. See `notes/content_audit.md` for the audit trail.

## Still needed before submission (no new experiments required)
- Recover/document the exact construction of `M_fg` and the class-agnostic candidate-generator configuration from the cloud code/config if possible.
- Add author/affiliation metadata.
- Quantify computational cost only if existing logs allow it; do not invent values.
- Prepare the detailed new-submission response letter referencing old manuscript ID `TAI-2026-Apr-A-00756`.
- Prepare an anonymous code/reproducibility repository if required by the target submission process.
- Keep the CI compile green and perform a final PDF visual check after any substantive manuscript edits.
