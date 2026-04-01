import matplotlib.pyplot as plt

# Taking number of points
n = int(input("Enter number of data points: "))

x = []
y = []

print("\nEnter the X values:")
for i in range(n):
    value = float(input(f"X[{i+1}]: "))
    x.append(value)

print("\nEnter the Y values:")
for i in range(n):
    value = float(input(f"Y[{i+1}]: "))
    y.append(value)

# Plotting scatter plot
plt.scatter(x, y)

# Labels and Title
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Scatter Plot (User Input)")

# Grid (optional)
plt.grid(True)

# Display
plt.show()
