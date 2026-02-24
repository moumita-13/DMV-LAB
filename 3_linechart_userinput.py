import matplotlib.pyplot as plt
import numpy as np

def draw_user_line_chart():
    """
    Prompts the user for data points and draws a line chart.
    """
    y_values = []

    # 1. Get the number of data points from the user
    while True:
        try:
            num_data = int(input("Enter the number of data points: "))
            if num_data <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # 2. Get the y-values from the user using a loop
    for i in range(num_data):
        while True:
            try:
                value = float(input(f"Enter value for point {i+1}: "))
                y_values.append(value)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    # 3. Create corresponding x-values (0, 1, 2, ...) if not provided
    x_values = np.arange(len(y_values))

    # 4. Plot the data
    plt.figure(figsize=(8, 5)) # Optional: set the figure size
    plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')

    # 5. Add labels and title for clarity
    plt.xlabel("X-axis (Data Point Index)")
    plt.ylabel("Y-axis (User Value)")
    plt.title("Line Chart from User Input")
    plt.grid(True) # Optional: adds a grid for better readability

    # 6. Display the chart
    plt.show()

if __name__ == "__main__":
    draw_user_line_chart()
