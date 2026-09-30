import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Load WT deep-basin flap-distance data
# ============================================================

wt_b1 = np.loadtxt("../input/flap_basin1.dat")[:, 1]
wt_b2 = np.loadtxt("../input/flap_basin2.dat")[:, 1]
wt_b3 = np.loadtxt("../input/flap_basin3.dat")[:, 1]

# Combine all WT deep-basin frames
wt_combined = np.concatenate([wt_b1, wt_b2, wt_b3])

# I50V deep basin
i50v_b1 = np.loadtxt("flap_basin1_I50V.dat")[:, 1]

print("Frame counts")
print("WT Basin 1:", len(wt_b1))
print("WT Basin 2:", len(wt_b2))
print("WT Basin 3:", len(wt_b3))
print("WT combined:", len(wt_combined))
print("I50V Basin 1:", len(i50v_b1))

# ============================================================
# Common histogram bins
# ============================================================

bins = np.arange(5, 17.5, 0.5)

# ============================================================
# FIGURE 1
# WT deep-basin population vs I50V deep-basin population
# ============================================================

plt.figure(figsize=(9, 6))

plt.hist(
    wt_combined,
    bins=bins,
    density=True,
    alpha=0.60,
    color="steelblue",
    label="WT deep-basin population"
)

plt.hist(
    i50v_b1,
    bins=bins,
    density=True,
    alpha=0.60,
    color="darkorange",
    label="I50V deep-basin population"
)

plt.xlabel("Ile50–Ile50′ flap distance (Å)")
plt.ylabel("Probability density")
plt.title("Flap-Distance Distribution of Deep FEL Populations")
plt.legend()
plt.xlim(5, 17)
plt.tight_layout()

plt.savefig(
    "WT_vs_I50V_deep_basin_flap_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ============================================================
# FIGURE 2
# Individual WT basins + I50V basin
# ============================================================

plt.figure(figsize=(9, 6))

plt.hist(
    wt_b1,
    bins=bins,
    density=True,
    alpha=0.55,
    color="royalblue",
    label="WT Basin 1"
)

plt.hist(
    wt_b2,
    bins=bins,
    density=True,
    alpha=0.55,
    color="seagreen",
    label="WT Basin 2"
)

plt.hist(
    wt_b3,
    bins=bins,
    density=True,
    alpha=0.55,
    color="mediumpurple",
    label="WT Basin 3"
)

plt.hist(
    i50v_b1,
    bins=bins,
    density=True,
    alpha=0.55,
    color="darkorange",
    label="I50V Basin 1"
)

plt.xlabel("Ile50–Ile50′ flap distance (Å)")
plt.ylabel("Probability density")
plt.title("Flap-Distance Distribution of Individual FEL Basins")
plt.legend()
plt.xlim(5, 17)
plt.tight_layout()

plt.savefig(
    "WT_I50V_individual_basin_flap_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()