# Limitations & Next Steps

## Sampling and Interpretation of Basin Populations

The WT–I50V results should be interpreted as observations from the sampled simulation ensembles, not as definitive equilibrium populations. Each system was sampled using three independent 10 ns conventional MD replicas; independent trajectories reveal trajectory-to-trajectory heterogeneity, but 10 ns simulations may still undersample slow transitions between metastable states.

This matters specifically because the central result concerns population differences — both in overall occupancy and in how that occupancy is organized (e.g., the three WT basins versus I50V's single dominant basin). A difference observed in finite trajectories may reflect a genuine change in the underlying landscape, incomplete sampling, or both. The relevant question is therefore not whether longer trajectories give more frames, but whether the specific transitions and populations of interest are adequately sampled; further sampling is needed to confirm these differences remain stable as more conformational transitions are accessed.

## V32I Open Investigation

V32I was analysed using the same general framework as WT and I50V, but one replicate produced an anomalous covariance response.

The combined V32I trajectory showed a covariance trace of approximately 676.9 nm², substantially larger than the values obtained from the other trajectories. Examination of individual replicas indicated that the anomaly was dominated by one replicate.

A structural comparison of the complete dimer produced an RMSD of approximately 25 Å, whereas comparisons performed separately for the individual chains produced values around 0.98 Å.

The difference between the whole-dimer and individual-chain comparisons indicates that the apparent large-scale deviation may involve relative protomer orientation, trajectory alignment, periodic-boundary representation, or another issue in the coordinate representation rather than a large deformation of each individual protomer.

The V32I result is therefore not incorporated into the completed WT–I50V mechanistic interpretation until the source of this anomalous covariance behaviour is resolved. The diagnostic workflow includes examination of trajectory alignment, dimer orientation, periodic-boundary treatment, and replicate-specific behaviour before repeating the PCA comparison.

## Enhanced Sampling

Enhanced-sampling approaches provide a natural next step for testing whether the conformational states identified in the conventional MD trajectories remain stable under broader sampling. Methods that increase access to slow conformational transitions could be used to investigate the stability, connectivity, and relative accessibility of the observed states. The purpose would not simply be to generate longer trajectories, but to test whether the state organization and population shifts observed in conventional MD persist when transitions that may be slow on the 10 ns timescale become more accessible.

## Expanding the Descriptor Framework

The inter-flap distance provides a physically interpretable descriptor for the present system, but a single structural coordinate cannot capture every aspect of protease conformational behaviour. Future analysis could examine complementary descriptors such as additional flap-related geometric coordinates, residue–residue or residue–ligand interaction features, active-site accessibility measures, collective-motion coordinates, local structural rearrangements, and ligand-contact descriptors where ligand-bound simulations are considered. The aim would be to determine which simulation-derived features provide complementary information about conformational state while retaining a clear physical interpretation.

## Toward Quantitative Feature Development

A longer-term direction is to evaluate physically interpretable molecular descriptors as quantitative features for predictive modelling. The important constraint is that such modelling should follow, rather than replace, the mechanistic analysis: descriptors should first be connected to identifiable molecular behaviour and evaluated for robustness across independent simulations. This would provide a route from trajectory-level molecular dynamics to compact, interpretable features that can be compared across mutations or incorporated into future predictive models.

## Overall Next Step

The immediate methodological priorities are to: resolve the V32I anomalous replicate and establish whether the covariance response arises from a coordinate/alignment issue or genuine conformational behaviour; assess the robustness of the WT–I50V population differences with additional sampling where appropriate; examine complementary descriptors beyond the inter-flap distance; and evaluate whether a small set of physically interpretable descriptors can generalize across additional resistance-associated mutations.

The broader objective is to move from molecular-dynamics trajectories to validated, physically interpretable molecular features, while maintaining a clear connection between those features and the biological or pharmacological process of interest.
