# # bar chart python code matplotlib using user input

# import matplotlib.pyplot as plt

# def create_bar_chart_from_user_input():
#     """
#     Prompts the user for data (categories and values) 
#     and generates a bar chart using matplotlib.
#     """
#     data = {}
#     collecting_data = True

#     print("--- Enter Data for Bar Chart ---")
#     print("Type 'done' for the category name when finished.")

#     while collecting_data:
#         category = input("Enter a category name (e.g., 'Apples' or 'done' to finish): ")
#         if category.lower() == 'done':
#             collecting_data = False
#             break
        
#         try:
#             value = float(input(f"Enter the value for '{category}': "))
#             data[category] = value
#         except ValueError:
#             print("Invalid input. Please enter a numerical value.")
#             continue

#     if not data:
#         print("No data entered. Exiting.")
#         return

#     # Extract categories and values from the dictionary
#     categories = list(data.keys())
#     values = list(data.values())

#     # Plotting the bar chart
#     plt.figure(figsize=(10, 6)) # Adjusts the size of the figure
#     plt.bar(categories, values, color='skyblue', edgecolor='black')

#     # Adding labels and title
#     plt.xlabel("Categories")
#     plt.ylabel("Values")
#     plt.title("User Input Bar Chart")

#     # Optional: Rotate x-axis labels if they are long
#     plt.xticks(rotation=45, ha='right')

#     # Ensure layout is clean and display the chart
#     plt.tight_layout()
#     plt.show()

# if __name__ == "__main__":
#     create_bar_chart_from_user_input()

import matplotlib.pyplot as plt

# Get number of bars
n = int(input("Enter number of bars: "))

labels = []
values = []

# Take labels and values as input
for i in range(n):
    label = input(f"Enter label for bar {i+1}: ")
    value = float(input(f"Enter value for bar {i+1}: "))
    
    labels.append(label)
    values.append(value)

# Create bar chart
plt.bar(labels, values)

# Add title and labels
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")

# Show plot
plt.show()
