from pathlib import Path

# One-shot audited text fixes for the rewritten manuscript.
main_path = Path('tai_rewrite/main.tex')
text = main_path.read_text(encoding='utf-8')

replacements = [
    (
        'Under the unified evaluation pipeline, unknown F1 on PASCAL VOC increases from 0.008 to 0.372 while known mIoU remains approximately 0.746; RoadAnomaly21 and RoadObstacle21 improve from 0.380 to 0.652 and from 0.054 to 0.515, respectively. Cityscapes shows a real but non-free gain, while medical CT forms a failure boundary because concept grounding is insufficient.',
        'Under the unified evaluation pipeline, unknown F1 on PASCAL VOC increases from 0.008 to 0.372 while known mIoU remains approximately 0.746. Independent SMIYC public-validation evaluation also shows pixel-level gains on RoadAnomaly21 and RoadObstacle21, while exposing an instance-level aggregation limitation. Cityscapes shows a real but non-free gain, while the Synapse CT probe forms a failure boundary because concept grounding is insufficient.'
    ),
    (
        'anomaly segmentation, open-world segmentation, structured abstention, zero-shot segmentation, foundation models, candidate generation',
        'anomaly segmentation, open-world segmentation, structured abstention, zero-shot candidate generation, foundation models, candidate generation'
    ),
    (
        'Open-set recognition and out-of-distribution (OoD) detection address this failure by estimating whether an input or pixel is outside the known distribution~\\cite{hendrycks2017baselinedetecting,liu2020energyout,yang2024generalizedout}.',
        'Open-set recognition and out-of-distribution (OoD) detection address this failure by estimating whether an input or pixel is outside the known distribution~\\cite{hendrycks2017baselinedetecting,liu2020energyout,yang2024generalizedout}. Open-world semantic segmentation further studies how unknown regions can be detected and subsequently incorporated into an expanding label space~\\cite{cen2021deepmetric}.'
    ),
    (
        'Instead, they show that reserving an explicit unknown output is sufficient to learn structured rejection when the unknown categories are supervised.',
        'Instead, they show that an explicit unknown output can support structured rejection when the unknown categories are supervised.'
    ),
    (
        'The experiments use six datasets with different narrative roles. Synapse and AMOS22 provide medical diagnostic and failure-boundary evidence. PASCAL VOC 2012 is the primary positive natural-image setting.',
        'The experiments use six datasets with different narrative roles. Synapse and AMOS22 both contribute to the original medical A2 diagnosis, while the available complement-grounding failure analysis is specific to Synapse. PASCAL VOC 2012 is the primary positive natural-image setting.'
    ),
    (
        '\\caption{Full-system A2 results from the unified candidate-generation evaluation pipeline. Road-scene rows reuse the Cityscapes checkpoint and report the same unknown-output metrics used in the mechanism study.}',
        '\\caption{Full-system A2 results from the unified candidate-generation evaluation pipeline. Road-scene rows reuse the Cityscapes checkpoint and report the mechanism study\'s unified-protocol unknown-output metrics; these F1 values are distinct from the official SMIYC Pix Best F1 reported separately.}'
    ),
    (
        'The SMIYC public-validation evaluator reveals an additional limitation. L2 improves the pixel-level AP/Best-F1 metrics on both RoadAnomaly21 and RoadObstacle21, but L1 can be substantially stronger on instance-oriented SegEval F1. Mean-score mask filtering improves pixel purity while sometimes discarding or fragmenting large anomalies with spatially non-uniform scores. This divergence is useful because it shows that candidate generation and candidate selection should be evaluated at both pixel and instance levels; the current L2 selector is not instance preserving.',
        'The SMIYC public-validation evaluator reveals an additional limitation and uses metrics that should not be conflated with the unified-protocol F1 above. On RoadAnomaly21, L2 raises pixel AP from 0.5937 to 0.6211 and Pix Best F1 from 0.5186 to 0.5459; on RoadObstacle21, AP rises from 0.4989 to 0.5330 and Pix Best F1 from 0.5117 to 0.5256. At the same time, L1 is substantially stronger than L2 on instance-oriented SegEval F1 mean (0.2990 versus 0.0313 on RoadAnomaly21; 0.2039 versus 0.0740 on RoadObstacle21). Mean-score mask filtering improves pixel purity while sometimes discarding or fragmenting large anomalies with spatially non-uniform scores. This divergence shows that candidate generation and candidate selection should be evaluated at both pixel and instance levels; the current L2 selector is not instance preserving.'
    ),
]

for old, new in replacements:
    if old not in text:
        raise RuntimeError(f'Expected text not found for replacement:\n{old[:160]}')
    text = text.replace(old, new, 1)

main_path.write_text(text, encoding='utf-8')

bib_path = Path('tai_rewrite/references_additions.bib')
bib = bib_path.read_text(encoding='utf-8')
entry = r'''

@inproceedings{cen2021deepmetric,
  author = {Jun Cen and Peng Yun and Junhao Cai and Michael Yu Wang and Ming Liu},
  title = {Deep Metric Learning for Open World Semantic Segmentation},
  booktitle = {Proc. IEEE/CVF Int. Conf. Comput. Vis.},
  year = {2021},
  pages = {15333--15342}
}
'''
if 'cen2021deepmetric' not in bib:
    bib = bib.rstrip() + entry + '\n'
    bib_path.write_text(bib, encoding='utf-8')

print('Applied content-audit fixes.')
