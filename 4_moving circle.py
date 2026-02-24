# import turtle

# # Set up the screen
# screen = turtle.Screen()
# screen.title("Moving Circle Animation")
# screen.bgcolor("black")
# screen.setup(width=600, height=400)

# # Create the circle object
# circle = turtle.Turtle()
# circle.shape("circle")
# circle.color("cyan")
# circle.shapesize(2) # Size of the circle
# circle.penup()
# circle.speed(0) # Fastest animation speed

# # Animation loop
# while True:
#     circle.forward(5) # Move forward
    
#     # Check boundaries for wrapping
#     if circle.xcor() > 300:
#         circle.setx(-300)
#     elif circle.xcor() < -300:
#         circle.setx(300)
    
#     # Add a slight turn to make it look spiral/dynamic
#     circle.right(2)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# --- Setup the figure and axes ---
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
# Ensure the aspect ratio is equal so the circle isn't an ellipse
ax.set_aspect("equal")
ax.set_title("Moving Circle Animation")

# --- Create the initial circle object (artist) ---
# Start the circle at an initial position (e.g., center at (0, 0)) and radius
circle_radius = 1.0
circle = Circle((0, 0), circle_radius, color='b', fill=True)
ax.add_patch(circle)

# --- Define the animation update function ---
def animate(frame):
    """
    Updates the position of the circle for each frame.
    The 'frame' argument is automatically passed by FuncAnimation.
    Here, we use it to calculate a new position based on a sine wave pattern.
    """
    # Example movement: a simple oscillation using sine and cosine
    x = 5 * np.cos(frame * 0.1) # X position oscillates between -5 and 5
    y = 5 * np.sin(frame * 0.1) # Y position oscillates between -5 and 5
    circle.center = (x, y) # Update the circle's center coordinates
    return [circle] # Return a list/tuple of artists that have been modified

# --- Create the animation ---
ani = animation.FuncAnimation(
    fig,
    animate,
    frames=100,          # Number of frames in the animation
    interval=50,         # Delay between frames in milliseconds
    blit=True,           # Optimizes drawing by only updating changed parts
    repeat=True          # Animation repeats indefinitely
)

# --- Show the animation ---
plt.show()

