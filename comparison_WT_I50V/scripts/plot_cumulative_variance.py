import numpy as np
import matplotlib.pyplot as plt

# Load cumulative variance data
wt = np.loadtxt("../input/cumvar.dat")
i50v = np.loadtxt("cumvar_I50V.dat")

# Create figure
plt.figure(figsize=(7,5))

# Plot WT
plt.plot(
    wt[:,0],
    wt[:,1],
    label="WT",
    linewidth=2
)

# Plot I50V
plt.plot(
    i50v[:,0],
    i50v[:,1],
    label="I50V",
    linewidth=2
)

# Labels
plt.xlabel("Principal Component")
plt.ylabel("Cumulative Explained Variance")

# Limits
plt.xlim(1,50)
plt.ylim(0,1.02)

# Legend
plt.legend()

plt.tight_layout()

plt.savefig("cumulative_variance_WT_I50V.png", dpi=300)

plt.show()