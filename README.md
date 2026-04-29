## HIV Protease Conformational Dynamics Analysis
This project explores how HIV protease samples its conformational landscape and how these states influence access to binding-competent configurations.

## Objective
To move beyond static structural representations and examine protein behavior as a dynamic ensemble, focusing on how conformational states regulate ligand accessibility.

## Methods
- Molecular Dynamics simulations (multiple replicas)
- Principal Component Analysis (PCA) for dominant motions
- Free Energy Landscape (FEL) construction
- Conformational state identification and population analysis

## Key Insights
- Identified distinct conformational states (open, semi-open, closed)
- Observed heterogeneous sampling across simulation replicas
- Found that conformational variability is localized in the flap region, governing access to the binding site
- Demonstrated that protein function is influenced by state populations, not just structural existence

## Repository Structure
- `scripts/` → analysis scripts (PCA, FEL, RMSF, etc.)
- `figures/` → generated plots and visualizations
- `data/` → processed trajectory-derived data

## Relevance
This work reflects a mechanistic approach to understanding protein behavior through dynamics, which is essential for identifying binding-relevant conformations and informing structure-based ligand design.
Provides a basis for identifying binding-relevant conformations by linking state populations to accessibility of the active site.
