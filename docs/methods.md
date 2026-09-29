# Methods

## Molecular-Dynamics Design

- Three independent 10 ns atomistic MD replicas were used for each protein variant (WT, I50V, V32I), to examine trajectory-to-trajectory conformational heterogeneity rather than relying on a single dynamical realization.
- WT and mutant systems were simulated under the same overall protocol, with the sequence mutation representing the intended physical difference between systems.

## Trajectory Processing

- Trajectories were processed using consistent structural selections and alignment procedures, so equivalent protein coordinates could be compared across replicas and systems.
- Cα atoms, with matching residue indices, were used as the common structural representation for WT and mutant trajectories, avoiding differences introduced by inconsistent atom selections.

## RMSD and Cα-RMSF

- RMSD and Cα-RMSF were used to assess global structural deviation and residue-level fluctuation, respectively, as complementary diagnostics alongside the PCA/FEL analysis below.

## Principal Component Analysis (PCA)

- Collective motions were defined from the WT ensemble; mutant trajectories were projected onto the same WT eigenvectors rather than analysed via independent PCA, enabling direct comparison within one conformational coordinate system.

## Free-Energy Landscape (FEL) & Basin Extraction

- The leading PC1–PC2 coordinates were converted into a free-energy landscape to identify populated, low-free-energy conformational basins.
- For WT, three clearly resolved deep basins were identified; representative frames from each were extracted for descriptor analysis. The same framework was applied to I50V; V32I was treated separately once an anomalous replicate was identified (see [Limitations & Next Steps](limitations_and_next_steps.md)).

## Mapping Conformational Basins to a Physical Descriptor

To connect the statistical organization of PCA/FEL space to a specific structural motion, basin-associated frames were mapped back to an inter-flap Cα–Cα distance — the distance between the Cα atoms of the two residue-50 flap tips (Ile50–Ile50′ in the WT structure). This descriptor was chosen because it corresponds to a specific, physically interpretable structural motion — the relative opening and closing of the two protease flaps that gate access to the active site — rather than an aggregate or abstract statistical quantity. By mapping each basin's representative frames onto this distance, a populated region of PCA/FEL space could be directly related to a measurable, functionally relevant motion, rather than remaining an abstract coordinate. This mapping is therefore a structural interpretation of the conformational states identified by PCA and FEL, not an independent classification scheme.

## Cross-System Comparison

WT and I50V were compared using the same WT-defined PCA coordinate system and the same flap-distance definition, across: the distribution of projected conformations in PC space; the location and population of low-free-energy basins; full-trajectory and basin-specific inter-flap distance distributions; and residue-level fluctuation profiles. This combination distinguishes genuine differences in conformational organization from differences that could simply reflect independently defined coordinate systems.

See [Key Findings](../README.md#key-findings) for results, and [Biophysical Descriptors](descriptors.md) for the rationale behind the flap-distance descriptor specifically.
