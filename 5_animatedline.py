import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# 1. Create a figure and axis
fig, ax = plt.subplots()
# Set initial axis limits
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.1, 1.1)

# 2. Initialize an empty line artist
# The comma after 'line' is important to unpack the Line2D object correctly
line, = ax.plot([], [], 'b-') # 'b-' specifies a blue solid line

# 3. Define the initialization function
def init():
    line.set_data([], [])
    return line,

# 4. Define the animation function, called for each frame
def animate(i):
    # Update the data for the line
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x + i * 0.05) # Shift the sine wave based on the frame number 'i'
    line.set_data(x, y)
    return line,

# 5. Create the animation object
# The animation object must be assigned to a variable (e.g., 'ani') that persists,
# or it will be garbage collected and the animation will stop.
ani = FuncAnimation(
    fig,           # The figure to animate
    animate,       # The function to call each frame
    init_func=init, # The function to call once at the beginning
    frames=100,    # Number of frames
    interval=20,   # Delay between frames in milliseconds
    blit=True      # Optimization to only redraw parts that changed
)

# 6. Display the animation
plt.title('Animated Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

# To save the animation as a file (e.g., a GIF or MP4), use the save method:
# ani.save('animation.gif', writer='pillow', fps=50)
# ani.save('animation.mp4', writer='ffmpeg', fps=30)
