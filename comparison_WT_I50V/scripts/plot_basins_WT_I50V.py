import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Load flap-distance data for each FEL basin
# Columns: frame, flap_distance_Angstrom
# ---------------------------------------------------------

wt_b1 = np.loadtxt("../input/flap_basin1.dat")
wt_b2 = np.loadtxt("../input/flap_basin2.dat")
wt_b3 = np.loadtxt("../input/flap_basin3.dat")
i50v_b1 = np.loadtxt("flap_basin1_I50V.dat")

# Extract flap-distance column
wt_b1_dist = wt_b1[:, 1]
wt_b2_dist = wt_b2[:, 1]
wt_b3_dist = wt_b3[:, 1]
i50v_b1_dist = i50v_b1[:, 1]

# ---------------------------------------------------------
# Common bins
# Keep the same range/binning for direct comparison
# ---------------------------------------------------------

bins = np.arange(5, 17.25, 0.25)

# ---------------------------------------------------------
# Plot
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.hist(
    wt_b1_dist,
    bins=bins,
    density=True,
    histtype="step",
    linewidth=2.5,
    linestyle="-",
    label="WT Basin 1"
)

plt.hist(
    wt_b2_dist,
    bins=bins,
    density=True,
    histtype="step",
    linewidth=2.5,
    linestyle="--",
    label="WT Basin 2"
)

plt.hist(
    wt_b3_dist,
    bins=bins,
    density=True,
    histtype="step",
    linewidth=2.5,
    linestyle="-.",
    label="WT Basin 3"
)

plt.hist(
    i50v_b1_dist,
    bins=bins,
    density=True,
    histtype="step",
    linewidth=2.5,
    linestyle=":",
    label="I50V Basin 1"
)

# ---------------------------------------------------------
# Formatting
# ---------------------------------------------------------

plt.xlabel("Ile50–Ile50′ Cα distance (Å)", fontsize=12)
plt.ylabel("Probability density", fontsize=12)

plt.xlim(5, 17)
plt.ylim(bottom=0)

plt.legend(frameon=False, fontsize=10)

plt.tight_layout()

# Save
plt.savefig(
    "WT_I50V_individual_basin_flap_distribution_density_outline.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()