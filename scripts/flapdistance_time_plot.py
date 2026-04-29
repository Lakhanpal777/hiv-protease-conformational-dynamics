import numpy as np
import matplotlib.pyplot as plt

# Load distance data
data = np.loadtxt("flap_distance.dat")

# Separate columns
frame = data[:,0]
distance = data[:,1]

# Plot
plt.figure()
plt.plot(frame, distance)
plt.xlabel("Frame")
plt.ylabel("Flap distance (Å)")
plt.title("Flap Dynamics Across Trajectory")
plt.show()