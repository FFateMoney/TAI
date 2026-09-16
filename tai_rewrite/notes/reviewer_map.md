# Reviewer-to-rewrite map

This note tracks how the new manuscript changes the load-bearing claims without adding new experiments.

## Associate Editor
- **Concern:** key claims lacked supporting evidence; experiments and clarifications were insufficient.
- **Rewrite response:** the paper no longer centers architectural superiority. The main claims are restricted to (i) detection/structuring separation, (ii) candidate-generation diagnosis in the studied A2 runs, (iii) the existing complement-candidate intervention, and (iv) empirically observed applicability boundaries.

## Reviewer 1 / attached report
- **Seen-unknown supervision must be explicit.** Addressed in Sec. III-A and Supplement: A1 is described as supervised K+1 control; A2 checkpoints may inherit generic seen-unknown supervision; zero-shot refers only to held-out unseen categories.
- **A2 previously did not solve unseen structured output.** Addressed by making Complement Candidate Generation the main method and by promoting the existing controlled intervention to the central experiment.
- **Thresholding criticism was inconsistent with threshold-heavy inference.** Reframed: the paper no longer argues that thresholding is intrinsically invalid. It argues that score thresholding cannot compensate for missing spatial candidates. Candidate generation supplies structure; score aggregation supplies selectivity.
- **PerPixel-K+1 beats SASeg on A1.** Explicitly acknowledged in the main paper. The old native-query-necessity claim is removed.
- **Need exact class splits.** Added to Supplement.
- **Need qualitative A2 evidence.** Existing qualitative triptych promoted into the main paper.
- **Computational cost.** Not newly measured. Because the rewrite is not claiming efficiency or deployment readiness, runtime superiority is not a load-bearing claim. This remains a limitation to quantify in a future benchmark-oriented version.

## Reviewer 2
- **Method has no clear A1 advantage; test all four datasets at >=3 seeds or down-scope.** Chose the explicit down-scope option. A1 is a supervised control and not a headline contribution. Cross-domain claims are qualitative boundary characterization rather than universal statistical claims.
- **Flagship gap may be threshold/rare-class artifact; report component-level F1/AUPRC.** Existing AUPR and structured-F1 diagnostics are retained where available; more importantly, the controlled score-vs-candidate intervention is now the load-bearing evidence. The rewrite avoids claiming that every part of the gap is caused only by candidate generation.
- **Cite RbA, Mask2Anomaly, Cen et al.** RbA and Mask2Anomaly have been added. A verified, directly relevant Cen et al. citation still needs to be identified before submission rather than guessed.
- **Leakage-free load-bearing tables.** The manuscript now explicitly separates diagnostic runs from the complement-study evaluator and does not merge incompatible baselines. Public-validation/validation-selected results are described as mechanism evidence rather than hidden-test estimates. A fully held-out benchmark claim is not made.

## Reviewer 3
- **Code/reproducibility.** The rewrite documents exact class partitions, checkpoint roles, score equation, thresholds, prompt forms, and evaluator provenance. Repository/code release logistics still need to be prepared for submission.
- **A1/A2 is not itself a contribution.** Removed from contribution list. A1/A2 appears only as a useful experimental regime distinction.
- **Detection-structuring gap is an observation, not a contribution.** Reframed as diagnosis whose support comes from region-level analysis and controlled intervention; it is not listed as a standalone protocol novelty.
- **Why spatial consistency matters.** Introduction now motivates region-level review, measurement, handoff, and connected-region downstream logic.
- **Architecture figure/novelty unclear; MaskFormer/Mask2Anomaly missing.** The old SASeg architecture is no longer the core method. Related work now explicitly cites MaskFormer/Mask2Former/Mask DINO/RbA/Mask2Anomaly and states that mask classification is not claimed as new.
- **Experiments looked like ablations rather than external comparisons.** The new experimental narrative is diagnosis -> intervention -> boundary, not an architecture leaderboard. Existing SMIYC evaluation is retained as external mechanism validation.
- **Qualitative outputs missing.** Existing qualitative triptych is in the main paper.

## Reviewer 4
- **A1 is supervised K+1.** Explicitly accepted and stated.
- **M=0 cannot prove native unknown queries indispensable.** The indispensability claim is removed; M=0 is no longer load-bearing and is omitted from the new main paper.
- **Need parameter-matched generic queries / binary branch / class-agnostic query baselines.** These were requested to support the old architecture-necessity claim. Since that claim has been removed, the new paper does not depend on these missing controls.
- **Method definitions incomplete.** The new paper focuses on the candidate-generation mechanism, whose equations and roles are stated directly; old SASeg implementation detail is delegated to the frozen-backbone description and supplementary provenance.

## Remaining pre-submission checks that do not require new experiments
1. Verify all bibliography entries and add the specific Cen et al. paper requested by Reviewer 2 if it is genuinely relevant.
2. Replace placeholder author information.
3. Run LaTeX compile and fix formatting/citation warnings.
4. Check that all reused figures meet IEEE resolution/font requirements.
5. Prepare anonymous repository/code instructions if the target venue requires them.
6. Draft the resubmission response letter referencing old paper ID TAI-2026-Apr-A-00756.
