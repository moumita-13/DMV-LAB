import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Basic Line Plot of a Sine Wave")
plt.xlabel("X-axis Value")
plt.ylabel("Y-axis Value")
plt.show()