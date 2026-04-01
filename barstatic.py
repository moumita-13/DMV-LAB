import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
categories = ['Apples', 'Bananas', 'Oranges', 'Grapes']
values = [23, 45, 56, 12]

# Create the bar chart
plt.bar(categories, values, color='skyblue')

# Add labels and a title
plt.xlabel('Fruit Type')
plt.ylabel('Sales (Units)')
plt.title('Fruit Sales Bar Chart')

# Display the plot
plt.show()
