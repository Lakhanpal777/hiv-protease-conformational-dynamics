# HIV Protease Conformational Dynamics Analysis

## Overview

This project investigates how HIV protease samples and redistributes conformational states across its dynamic landscape, with emphasis on how localized motions regulate functionally relevant structural accessibility.

## Objective

To examine protein behavior as an ensemble of interconverting conformational states rather than a single static structure, and to understand how perturbations reshape conformational sampling, state populations, and gating dynamics.

## Methods

* Multi-replica Molecular Dynamics (MD) simulations
* Principal Component Analysis (PCA) for characterization of collective motions
* Free Energy Landscape (FEL) construction and basin identification
* RMSF-based localization of dynamically active regions
* Conformational state extraction and structural assignment
* State population and flap-distance distribution analysis
* Comparative projection of mutant and wild-type trajectories onto shared conformational spaces

## Key Insights

* Identified distinct metastable conformational ensembles corresponding to open, semi-open, and closed states
* Observed heterogeneous conformational sampling across independent simulation replicas
* Localized dominant conformational variability to the substrate-gating flap region while the catalytic scaffold remained comparatively stable
* Showed that perturbation-associated effects emerged primarily through redistribution of conformational populations rather than generation of entirely new structural states
* Connected collective motions identified through PCA with structurally interpretable thermodynamic basins and functionally relevant gating behavior

## Repository Structure

* `scripts/` → trajectory analysis and visualization workflows (PCA, FEL, RMSF, population analysis, etc.)
* `figures/` → generated structural and dynamical analysis plots
* `data/` → processed trajectory-derived datasets and extracted conformational information

## Relevance

This project focuses on mechanistic interpretation of biomolecular dynamics through ensemble-based analysis and collective-motion characterization. The workflow emphasizes how localized fluctuations, conformational accessibility, and redistribution among metastable states contribute to larger-scale functional behavior in structurally dynamic protein systems.
