import numpy as np
import matplotlib.pyplot as plt

# ---------- Load data ----------
wt = np.loadtxt("../input/pc1_pc2.dat")
i50v = np.loadtxt("../mutant_I50V/pc1_pc2_I50V.dat")

# ---------- Plot ----------
plt.figure(figsize=(7,6))

plt.scatter(
    wt[:,0],
    wt[:,1],
    s=8,
    alpha=0.37,
    label="WT"
)

plt.scatter(
    i50v[:,0],
    i50v[:,1],
    s=10,
    alpha=0.5,
    label="I50V"
)
plt.axis("equal")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("WT vs I50V in WT PCA Space")

plt.legend()

plt.tight_layout()

plt.savefig("WT_I50V_PC1_PC2.png", dpi=300)

plt.show()