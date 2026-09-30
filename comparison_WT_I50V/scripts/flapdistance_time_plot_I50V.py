import numpy as np
import matplotlib.pyplot as plt

# Load WT and I50V flap-distance data
wt = np.loadtxt("../input/flap_distance.dat")
i50v = np.loadtxt("flap_distance_I50V.dat")

# Separate columns
wt_frame = wt[:, 0]
wt_distance = wt[:, 1]

i50v_frame = i50v[:, 0]
i50v_distance = i50v[:, 1]

# Plot
plt.figure(figsize=(10, 5))

plt.plot(wt_frame, wt_distance, alpha=0.7, label="WT")
plt.plot(i50v_frame, i50v_distance, alpha=0.7, label="I50V")

plt.xlabel("Frame")
plt.ylabel("Flap distance (Å)")
plt.title("WT vs I50V Flap Dynamics")
plt.legend()

plt.tight_layout()
plt.show()