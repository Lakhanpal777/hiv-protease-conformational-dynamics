import numpy as np
import matplotlib.pyplot as plt

# Load data again (required in every script)
data = np.loadtxt("flap_distance.dat")

distance = data[:,1]

# Split replicas (based on your concatenation)
rep1 = distance[:1000]
rep2 = distance[1000:2000]
rep3 = distance[2000:3001]

# Plot replica-wise histograms
plt.figure()

plt.hist(rep1, bins=40, alpha=0.5, label="Replica 1")
plt.hist(rep2, bins=40, alpha=0.5, label="Replica 2")
plt.hist(rep3, bins=40, alpha=0.5, label="Replica 3")

plt.xlabel("Flap distance (Å)")
plt.ylabel("Population")
plt.title("Replica-wise Flap Distance Distribution")
plt.legend()

plt.show()