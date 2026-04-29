import numpy as np
import matplotlib.pyplot as plt

# Load PC1-PC2 data
data = np.loadtxt("pc1_pc2.dat")

pc1 = data[:,0]
pc2 = data[:,1]

# Create scatter plot
plt.figure(figsize=(7,6))
plt.scatter(pc1, pc2, s=10, alpha=0.6)

plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA Conformational Space (PC1 vs PC2)")

plt.tight_layout()
plt.show()

