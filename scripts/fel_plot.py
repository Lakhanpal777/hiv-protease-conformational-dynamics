import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# Load PCA data
data = np.loadtxt("pc1_pc2.dat")
pc1 = data[:,0]
pc2 = data[:,1]

# Parameters
T = 300.0   # Temperature in Kelvin
kB = 0.008314  # Boltzmann constant in kJ/mol/K

# 2D histogram
bins = 100
H, xedges, yedges = np.histogram2d(pc1, pc2, bins=bins, density=True)

# Avoid log(0)
H[H == 0] = np.min(H[H > 0])

# Free energy calculation
F = -kB * T * np.log(H)

# Normalize
F = F - np.min(F)

# Smooth FEL
F_smooth = gaussian_filter(F, sigma=1.2)

# Grid for plotting
X, Y = np.meshgrid(
    0.5*(xedges[:-1] + xedges[1:]),
    0.5*(yedges[:-1] + yedges[1:])
)

# Plot
plt.figure(figsize=(8,6))

contour = plt.contourf(
    X, Y, F_smooth.T,
    levels=30,
    cmap="viridis"
)

plt.colorbar(contour, label="Free Energy (kJ/mol)")

plt.xlabel("PC1", fontsize=12)
plt.ylabel("PC2", fontsize=12)
plt.title("Free Energy Landscape (PC1 vs PC2)", fontsize=14)

plt.tight_layout()
plt.savefig("FEL_PC1_PC2.png", dpi=300)
plt.show()
