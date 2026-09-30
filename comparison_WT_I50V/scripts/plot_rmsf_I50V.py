import numpy as np
import matplotlib.pyplot as plt

# Load RMSF data
data = np.loadtxt("rmsf_ca_I50V.xvg", comments=['@','#'])

residue = data[:,0]
rmsf = data[:,1]

# Split chains (assuming 99 residues each)
n = int(len(residue)/2)

resA = residue[:n]
rmsfA = rmsf[:n]

resB = residue[n:] - residue[n] + 1
rmsfB = rmsf[n:]

plt.figure(figsize=(8,5))

plt.plot(resA, rmsfA, label="Chain A")
plt.plot(resB, rmsfB, label="Chain B")

plt.xlabel("Residue Number")
plt.ylabel("RMSF (nm)")
plt.title("I50V Backbone Flexibility (Cα RMSF)")
plt.legend()
plt.tight_layout()

plt.savefig("RMSF_I50V.png", dpi=300)
plt.show()