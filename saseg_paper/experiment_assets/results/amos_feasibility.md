# AMOS22 Feasibility Check (T7-2)

## Setup

- Data domain: `AMOS22 CT-only`
- CT cases: train=`200`, val=`100`
- Known labels: `[1, 2, 3, 4, 6, 7, 8, 10]`
- Seen unknown labels: `[5, 9, 13, 14]`
- Unseen unknown labels: `[11, 12, 15]`

## Protocol-Level Summary

- A1 train seen-unknown prevalence (known ∪ seen): `10.05%`
- A1 val seen-unknown prevalence (known ∪ seen): `10.19%`
- A2 val unseen-unknown prevalence (known ∪ unseen): `2.49%`
- Train CT cases with seen unknown: `200/200` (100.00%)
- Val CT cases with seen unknown: `100/100` (100.00%)
- Val CT cases with unseen unknown: `100/100` (100.00%)
- Val CT cases with label 15: `97/100` (97.00%)

## Foreground Composition

- Train fg pixels: `311583601`
- Train known / seen / unseen pixels: `274060740` / `30612167` / `6910694`
- Val fg pixels: `190196571`
- Val known / seen / unseen pixels: `166982757` / `18944183` / `4269631`

## Largest Classes by Pixel Share (CT-only train)
- ` 6` liver: cases=200, slices=8263, pixels=152351977 (48.90% of fg)
- ` 7` stomach: cases=198, slices=5617, pixels=39714480 (12.75% of fg)
- ` 1` spleen: cases=198, slices=4798, pixels=22573422 (7.24% of fg)
- ` 3` left kidney: cases=199, slices=5425, pixels=17596993 (5.65% of fg)
- ` 2` right kidney: cases=200, slices=5310, pixels=17002272 (5.46% of fg)
- `14` bladder: cases=195, slices=2523, pixels=14473529 (4.65% of fg)
- ` 8` aorta: cases=200, slices=13939, pixels=13229591 (4.25% of fg)
- `10` pancreas: cases=200, slices=4303, pixels=8254228 (2.65% of fg)

## Largest Classes by Pixel Share (CT-only val)
- ` 6` liver: cases=100, slices=4867, pixels=89374776 (46.99% of fg)
- ` 7` stomach: cases=99, slices=3404, pixels=26760156 (14.07% of fg)
- ` 1` spleen: cases=100, slices=3036, pixels=15405959 (8.10% of fg)
- ` 3` left kidney: cases=100, slices=3271, pixels=10177775 (5.35% of fg)
- ` 2` right kidney: cases=98, slices=3025, pixels=9474661 (4.98% of fg)
- `14` bladder: cases=99, slices=1591, pixels=9056744 (4.76% of fg)
- ` 8` aorta: cases=100, slices=8222, pixels=8522207 (4.48% of fg)
- `10` pancreas: cases=100, slices=2509, pixels=5146468 (2.71% of fg)

## Feasibility Conclusion
- Verdict: `feasible`
- Current CT-only split is statistically feasible for a first AMOS round.
- A1 has non-empty seen-unknown signal in both train and val.
- A2 has non-empty unseen-unknown signal with enough positive pixels to make AUROC/AUPR interpretable.
- The remaining risk is not emptiness but difficulty: A2 may still be dominated by small-structure detection.

## Interpretation for T7

- If this split is feasible, the next step should be `T7-3` code/config integration rather than more protocol debate.
- If later training fails, that failure should be interpreted as a modeling or protocol-transfer issue, not as a missing-positive-sample artifact.
- If AMOS eventually needs a split revision, the first labels to revisit are `14` and `15`, exactly because they can dominate A1 or destabilize A2.
