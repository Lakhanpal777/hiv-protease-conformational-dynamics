import numpy as np
import matplotlib.pyplot as plt

# Load WT and I50V flap-distance data
wt = np.loadtxt("../input/flap_distance.dat")[:, 1]
i50v = np.loadtxt("flap_distance_I50V.dat")[:, 1]

# Same bins for both systems
bins = np.linspace(5, 17, 49)

plt.figure(figsize=(8, 5))

plt.hist(
    wt,
    bins=bins,
    density=True,
    alpha=0.6,
    label="WT"
)

plt.hist(
    i50v,
    bins=bins,
    density=True,
    alpha=0.6,
    label="I50V"
)

plt.xlabel("Flap distance (Å)")
plt.ylabel("Probability density")
plt.title("WT vs I50V Flap Distance Distribution")
plt.legend()

plt.tight_layout()
plt.show()