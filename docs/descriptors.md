# Biophysical Descriptors

## Inter-Flap Distance

The PCA/FEL analysis identifies where the system occupies conformational space, but a projected coordinate does not by itself provide a direct physical interpretation of the corresponding molecular motion. The inter-flap Cα–Cα distance between the two residue-50 flap tips was therefore used as a physically interpretable descriptor of flap opening — a specific structural motion, rather than an aggregate measure of overall protein fluctuation.

The descriptor was validated by mapping frames from individual FEL basins back onto the flap-distance distribution, directly relating statistically defined regions of conformational space to a measurable structural feature (see [Key Findings](../README.md#key-findings)).

## Why This Matters

PCA identifies dominant directions of variation in a trajectory; the flap distance is what turns that abstract coordinate into an interpretable molecular quantity. This distinction matters beyond this one project: a useful simulation-derived feature should not only distinguish systems statistically, but should have a clear physical relationship to the biological process under study — the same property that would be needed of any descriptor evaluated as a feature for predictive modelling (see [Limitations & Next Steps](limitations_and_next_steps.md) for how this project would extend in that direction).
