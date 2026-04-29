import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("flap_distance.dat")

distance = data[:,1]

plt.figure()
plt.hist(distance, bins=40)
plt.xlabel("Flap distance (Å)")
plt.ylabel("Population")
plt.title("Flap Distance Distribution")
plt.show()