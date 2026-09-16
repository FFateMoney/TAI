# TAI rewrite: detection-to-structuring

This directory contains the zero-new-experiment rewrite that merges the diagnostic content of `saseg_paper` with the candidate-generation content of `complement_paper`.

## Files
- `main.tex`: rewritten IEEE TAI manuscript.
- `supplementary.tex`: reused implementation details, class splits, prompt ablation, SMIYC public-validation results, and interpretive guardrails.
- `references_additions.bib`: references newly required by the rewritten positioning (RbA, Mask2Anomaly, Mask2Former, SMIYC, SAM 2/3, CLIP).
- `notes/reviewer_map.md`: reviewer concern -> rewrite response mapping.
- `notes/number_provenance.md`: source and evaluator provenance for every load-bearing number.

## Main narrative
1. Unknown detection and structured unknown output are different capabilities.
2. Existing A2 diagnostics localize the dominant missing capability to spatial candidate generation.
3. Complement Candidate Generation explains known concepts first, then uses residual foreground as candidate structure.
4. Controlled interventions show that candidate replacement, not score strengthening, produces the main gain.
5. Existing results define effective (VOC), trade-off (Cityscapes), transfer (RA21/RO21), and failure (medical CT) regimes.

## Claims deliberately removed
- Native unknown queries are **not** claimed to be necessary.
- A1/A2 is **not** presented as a standalone methodological contribution.
- SASeg is **not** claimed to outperform K+1 segmentation in supervised A1.
- Cross-domain observations are **not** stated as universal statistical laws.
- SMIYC results are **not** presented as leaderboard/state-of-the-art claims.

## Build
The manuscript reuses the IEEE TAI class from `saseg_paper` and figures from the two existing project directories.

From `tai_rewrite/`, a typical local build is:

```bash
TEXINPUTS=../saseg_paper: pdflatex main.tex
BIBINPUTS=../saseg_paper:. bibtex main
TEXINPUTS=../saseg_paper: pdflatex main.tex
TEXINPUTS=../saseg_paper: pdflatex main.tex
```

Supplement:

```bash
pdflatex supplementary.tex
BIBINPUTS=../saseg_paper:. bibtex supplementary
pdflatex supplementary.tex
pdflatex supplementary.tex
```

The branch has not executed a LaTeX build in GitHub; compile warnings/errors should be checked locally or in CI before submission.

## Still needed before submission (no new experiments required)
- Add author/affiliation metadata.
- Verify bibliography formatting and identify the specific relevant `Cen et al.` paper requested by Reviewer 2 rather than guessing.
- Run the LaTeX build and fix presentation issues.
- Confirm figure font sizes/resolution.
- Prepare the detailed new-submission response letter referencing old manuscript ID `TAI-2026-Apr-A-00756`.
- Prepare an anonymous code/reproducibility repository if required by the target submission process.
