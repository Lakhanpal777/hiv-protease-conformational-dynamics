# HIV-1 Protease Conformational Dynamics: From Genetic Variation to Biophysical Descriptors

An end-to-end molecular simulation study investigating how resistance-associated mutations reshape conformational ensembles, state populations, and functionally relevant dynamic descriptors of HIV-1 protease.

---

## Project Status

**WT — complete · I50V — complete · V32I — diagnostic investigation**

The completed WT–I50V analysis combines molecular-dynamics trajectories, principal component analysis (PCA), cross-system projection, free-energy landscape (FEL) analysis, conformational-state characterization, and mapping to a physically interpretable descriptor of protease flap opening.

V32I was analysed using the same general framework, but one replicate produced an anomalous covariance response. That trajectory is therefore being treated separately until the source of the anomaly is resolved.

---

## Research Question

HIV-1 protease is a dynamic drug target in which resistance-associated mutations can alter inhibitor response without necessarily producing large changes in average protein structure.

This project asks:

> Does a resistance-associated mutation primarily reorganize the structure of the protein, or does it redistribute the population and accessibility of functionally relevant conformational states?

Rather than comparing only representative structures, the analysis treats each trajectory as a sampled conformational ensemble and asks how the distribution of states changes between WT and mutant systems.

---

## Approach

Three independent 10 ns atomistic molecular-dynamics replicas were analysed for each system. The dominant collective motions were defined from the WT ensemble using PCA, and mutant trajectories were projected onto the same WT eigenvectors to enable comparison within a common conformational coordinate system.

The resulting PC1–PC2 spaces were analysed using free-energy landscapes to identify populated conformational basins. These basin populations were then connected to the inter-flap Cα–Cα distance between the two residue-50 tips, providing a direct structural descriptor of flap opening.

---

## Key Findings

### 1. WT samples multiple conformational basins

The WT free-energy landscape contained three clearly resolved deep basins, together comprising 813 of 3001 analysed frames (27.1%). These basins occupied distinct regions of the inter-flap distance distribution, corresponding to closed, intermediate, and more open-like conformational regimes.

### 2. I50V shifts the flap-distance ensemble toward larger openings

The full-trajectory inter-flap distance distributions differed substantially between WT and I50V:

| Inter-flap distance | WT    | I50V  |
| ------------------- | ----- | ----- |
| 6–8 Å               | 49.6% | 0.07% |
| 8–10 Å              | 40.8% | 7.5%  |
| 10–12 Å             | 9.4%  | 73.5% |
| >12 Å               | —     | 18.9% |

WT sampled approximately 5.6–12.0 Å with a mean of 7.98 Å, whereas I50V sampled approximately 7.7–16.4 Å with a mean of 11.3 Å — a redistribution of the sampled I50V ensemble toward larger inter-flap distances.

### 3. Similar deep-basin occupancy does not imply the same conformational organization

The dominant I50V basin contained 773 of 3003 frames (25.7%), comparable in overall fraction to the 27.1% represented by the three WT deep basins. However, the populations were organized differently: WT deep-basin frames were distributed across three resolved minima, whereas the I50V deep-basin population was concentrated in one. Within this I50V basin, 96.5% of frames had an inter-flap distance ≥10 Å.

Total occupancy alone does not describe how the conformational ensemble is organized.

### 4. The I50V change is localized rather than a global increase in flexibility

The maximum Cα RMSF was similar between WT and I50V (approximately 3.03 Å and 3.08 Å, respectively). The principal differences were localized around the flap region, including altered fluctuations around residues 50–55 — a redistribution of flap-associated dynamics, not a uniform increase in protein-wide flexibility.

---

## Overall Interpretation

Together, the PCA, free-energy landscape, basin-population, flap-distance, and RMSF analyses indicate that I50V is associated with a redistribution of sampled conformational populations toward larger inter-flap distances, without requiring a large global structural rearrangement — connecting a resistance-associated sequence change to a specific, physically interpretable change in a functionally relevant dynamic motion.

---

## Repository Structure

```text
hiv-protease-conformational-dynamics/
│
├── README.md
├── LICENSE
│
├── docs/
│   ├── background.md
│   ├── methods.md
│   ├── descriptors.md
│   └── limitations_and_next_steps.md
│
├── data/
│   ├── wt/
│   ├── i50v/
│   └── v32i/
│
├── scripts/
│   ├── simulation_setup/
│   ├── trajectory_processing/
│   ├── pca_projection/
│   ├── fel_basin_analysis/
│   └── descriptor_analysis/
│
└── results/
    ├── figures/
    │   ├── wt_vs_i50v/
    │   └── v32i_diagnostics/
    └── tables/
