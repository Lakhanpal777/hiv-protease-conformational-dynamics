import numpy as np

data = np.loadtxt("flap_distance.dat")

print(data[:10])
print("Total frames:", len(data))