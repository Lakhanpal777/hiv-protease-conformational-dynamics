import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Load PC data
data = np.loadtxt("pc1_pc2.dat")
pc1 = data[:,0]
pc2 = data[:,1]

# KDE for probability density
values = np.vstack([pc1, pc2])
kde = gaussian_kde(values)

# Create grid
xmin, xmax = pc1.min(), pc1.max()
ymin, ymax = pc2.min(), pc2.max()

X, Y = np.mgrid[xmin:xmax:200j, ymin:ymax:200j]
positions = np.vstack([X.ravel(), Y.ravel()])
Z = np.reshape(kde(positions).T, X.shape)

# Convert to Free Energy
kB = 0.008314  # kJ/mol/K
T = 300        # Kelvin

F = -kB * T * np.log(Z)
F = F - np.min(F)   # shift minimum to zero

# ===== Plot =====
plt.figure(figsize=(8,6))

# FEL contour (background)
contour = plt.contourf(X, Y, F, levels=20, cmap="viridis")

# Overlay PCA scatter
plt.scatter(pc1, pc2, s=5, c="white", alpha=0.4)

# Labels
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Free Energy Landscape with PCA Projection")

# Colorbar
cbar = plt.colorbar(contour)
cbar.set_label("Free Energy (kJ/mol)")

# White background
plt.gca().set_facecolor("white")

plt.tight_layout()
plt.savefig("FEL_overlay.png", dpi=300)
plt.show()
