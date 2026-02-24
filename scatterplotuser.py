# import matplotlib.pyplot as plt
# import sys

# def create_scatterplot_from_user_input():

#     print("Enter the X-axis values separated by commas (e.g., 1, 2, 3):")
#     x_input = sys.stdin.readline().strip()
#     print("Enter the Y-axis values separated by commas (e.g., 4, 5, 6):")
#     y_input = sys.stdin.readline().strip()

#     try:
#         x_values = [float(x.strip()) for x in x_input.split(',')]
#         y_values = [float(y.strip()) for y in y_input.split(',')]

#         if len(x_values) != len(y_values):
#             print("Error: The number of X values must match the number of Y values.")
#             return

#         plt.scatter(x_values, y_values)

#         plt.title("User Input Scatter Plot")
#         plt.xlabel("X values")
#         plt.ylabel("Y values")
#         plt.grid(True)

#         plt.show()

#     except ValueError:
#         print("Error: Please ensure your inputs are valid numbers separated by commas.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# if __name__ == "__main__":
#     create_scatterplot_from_user_input()

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
