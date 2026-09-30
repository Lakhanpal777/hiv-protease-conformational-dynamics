import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# WT vs I50V Free-Energy Landscape
# I50V is projected into the WT PCA space
# ============================================================

# ------------------------------------------------------------
# Input files
# ------------------------------------------------------------

WT_FILE = "../input/pc1_pc2.dat"
I50V_FILE = "../mutant_I50V/pc1_pc2_I50V.dat"

# ------------------------------------------------------------
# Parameters
# ------------------------------------------------------------

T = 300.0
kB = 0.008314462618

# Same binning as gmx sham:
# 1024 bins = 32 x 32
BINS = 32

# ============================================================
# Load data
# ============================================================

wt = np.loadtxt(WT_FILE)
i50v = np.loadtxt(I50V_FILE)

wt_pc1 = wt[:, 0]
wt_pc2 = wt[:, 1]

i50v_pc1 = i50v[:, 0]
i50v_pc2 = i50v[:, 1]

print("WT frames:", len(wt_pc1))
print("I50V frames:", len(i50v_pc1))

# ============================================================
# Define ONE common WT PCA coordinate range
# ============================================================

all_pc1 = np.concatenate((wt_pc1, i50v_pc1))
all_pc2 = np.concatenate((wt_pc2, i50v_pc2))

pc1_min = all_pc1.min()
pc1_max = all_pc1.max()

pc2_min = all_pc2.min()
pc2_max = all_pc2.max()

# ============================================================
# FEL calculation
# ============================================================

def calculate_fel(pc1, pc2):

    counts, xedges, yedges = np.histogram2d(
        pc1,
        pc2,
        bins=BINS,
        range=[
            [pc1_min, pc1_max],
            [pc2_min, pc2_max]
        ]
    )

    # Convert population counts to probability
    probability = counts / np.sum(counts)

    # Empty bins = no sampled conformations
    probability[probability == 0] = np.nan

    # Relative free energy
    F = -kB * T * np.log(probability)

    # Normalize minimum populated region to zero
    F = F - np.nanmin(F)

    return F


F_wt = calculate_fel(wt_pc1, wt_pc2)
F_i50v = calculate_fel(i50v_pc1, i50v_pc2)

# ============================================================
# Common color scale
# ============================================================

max_F = max(
    np.nanmax(F_wt),
    np.nanmax(F_i50v)
)

levels = np.linspace(0, max_F, 21)

# ============================================================
# Create figure
# ============================================================

fig, axes = plt.subplots(
    1,
    2,
    figsize=(12.5, 5.5),
    sharex=True,
    sharey=True,
    layout="constrained"
)

# ============================================================
# WT FEL
# ============================================================

cf1 = axes[0].contourf(
    F_wt.T,
    levels=levels,
    cmap="viridis",
    extent=[
        pc1_min,
        pc1_max,
        pc2_min,
        pc2_max
    ],
    antialiased=True
)

axes[0].set_title(
    "WT",
    fontsize=15,
    fontweight="bold"
)

axes[0].set_xlabel(
    "PC1",
    fontsize=13
)

axes[0].set_ylabel(
    "PC2",
    fontsize=13
)

# ============================================================
# I50V FEL
# ============================================================

cf2 = axes[1].contourf(
    F_i50v.T,
    levels=levels,
    cmap="viridis",
    extent=[
        pc1_min,
        pc1_max,
        pc2_min,
        pc2_max
    ],
    antialiased=True
)

axes[1].set_title(
    "I50V",
    fontsize=15,
    fontweight="bold"
)

axes[1].set_xlabel(
    "PC1",
    fontsize=13
)

# ============================================================
# Identical axis limits
# ============================================================

for ax in axes:

    ax.set_xlim(pc1_min, pc1_max)
    ax.set_ylim(pc2_min, pc2_max)

    ax.tick_params(
        axis="both",
        labelsize=10
    )

# ============================================================
# Colorbar
# Explicitly attached to BOTH panels.
# It will appear on the FAR RIGHT.
# ============================================================

cbar = fig.colorbar(
    cf2,
    ax=axes,
    location="right",
    shrink=0.90,
    fraction=0.045,
    pad=0.03
)

cbar.set_label(
    "Relative Free Energy (kJ/mol)",
    fontsize=12
)

# ============================================================
# Overall title
# ============================================================

fig.suptitle(
    "Free-Energy Landscapes in WT PCA Space",
    fontsize=17,
    fontweight="bold"
)

# ============================================================
# Save
# ============================================================

plt.savefig(
    "FEL_WT_vs_I50V.png",
    dpi=400,
    bbox_inches="tight"
)

plt.savefig(
    "FEL_WT_vs_I50V.pdf",
    bbox_inches="tight"
)

plt.show()

print("\nSaved:")
print("FEL_WT_vs_I50V.png")
print("FEL_WT_vs_I50V.pdf")