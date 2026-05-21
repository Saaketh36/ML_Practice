import numpy as np
data = np.array([14, 18, 22, 27, 30, 18, 20])

mean = np.mean(data)
abs_dev = np.abs(data-mean)

amd = np.mean(abs_dev)
print(f"Absolute Mean Deviation: {amd}")
