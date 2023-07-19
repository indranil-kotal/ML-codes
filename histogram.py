import numpy as np
import matplotlib.pyplot as plt

# Generating some random data for the histogram
data = np.random.normal(loc=0, scale=1, size=1000)

# Plotting the histogram
plt.hist(data, bins=20, edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram')
#plt.grid(True)
plt.show()
