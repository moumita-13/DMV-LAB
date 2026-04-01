import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initial position of circle
x, y = 0, 0

# Circle properties
radius = 0.5

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Labels and grid
ax.set_title("Animated Circle with Keyboard Control")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.grid(True)

# Create circle
circle = plt.Circle((x, y), radius, color='blue')
ax.add_patch(circle)

# Movement step
step = 0.5

# Key press event
def on_key(event):
    global x, y
    if event.key == 'up':
        y += step
    elif event.key == 'down':
        y -= step
    elif event.key == 'left':
        x -= step
    elif event.key == 'right':
        x += step

# Update function for animation
def update(frame):
    circle.center = (x, y)
    return circle,

# Connect keyboard event
fig.canvas.mpl_connect('key_press_event', on_key)

# Animation
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.show()