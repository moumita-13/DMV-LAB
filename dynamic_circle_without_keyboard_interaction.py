import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

speed = float(input("Enter circle speed (example 0.05): "))
frames = int(input("Enter number of frames (example 200): "))

fig, ax = plt.subplots()
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')

x = np.linspace(0, 2 * np.pi, 400)
ax.plot(x, np.sin(x), '--', color='gray', alpha=0.5)

circle = plt.Circle((0, 0), 0.15, color='blue')
ax.add_patch(circle)

def update(frame):
    x_pos = frame * speed
    y_pos = np.sin(x_pos)
    circle.center = (x_pos, y_pos)
    return circle,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=frames,
    interval=30,
    blit=True
)

plt.title("Dynamic Animated Circle")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()

# # give me the link for a downloadable small CSV kaggle dataset of 30x30 that can be used for data visualization and exploration 
# and give the python code to perform the following:-
# 1. To Identify the Outliers and Missing Data (IF ANY - in this dataset)
# 2. To Summarize data and present the results in forms of charts and graphs:-
# Bar chart, Scatter plot, pie chart, stair chart, Line Chart....there should be proper lables and grid in all 