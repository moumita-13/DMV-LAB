# subplots python code matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5, 0.25)
y1, y2, y3, y4 = x, x**2, x**3, np.sin(x)

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

ax[0, 0].plot(x, y1, 'r-')
ax[0, 0].set_title('Linear')

ax[0, 1].plot(x, y2, 'g--')
ax[0, 1].set_title('Quadratic')

ax[1, 0].plot(x, y3, 'b-.')
ax[1, 0].set_title('Cubic')

ax[1, 1].plot(x, y4, 'k:')
ax[1, 1].set_title('Sine')

fig.suptitle('Mathematical Functions Comparison', fontsize=16)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()
