import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(170, 10, 1000)

plt.hist(data, bins=30, color='skyblue', edgecolor='black') 

plt.title("Basic Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()