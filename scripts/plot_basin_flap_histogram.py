import numpy as np
import matplotlib.pyplot as plt

# Load basin data
b1 = np.loadtxt("flap_basin1.dat")
b2 = np.loadtxt("flap_basin2.dat")
b3 = np.loadtxt("flap_basin3.dat")

# Extract distances (second column)
d1 = b1[:,1]
d2 = b2[:,1]
d3 = b3[:,1]

# Plot
plt.figure()

plt.hist(d1, bins=30, alpha=0.6, label="Basin 1")
plt.hist(d2, bins=30, alpha=0.6, label="Basin 2")
plt.hist(d3, bins=30, alpha=0.6, label="Basin 3")

plt.xlabel("Flap distance (Å)")
plt.ylabel("Population")
plt.title("Flap Distance Distribution per Free-Energy Basin")
plt.legend()

plt.show()
print("Mean flap distance:")
print("Basin 1:", np.mean(d1))
print("Basin 2:", np.mean(d2))
print("Basin 3:", np.mean(d3))

