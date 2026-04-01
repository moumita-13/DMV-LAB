# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load dataset
# df = pd.read_csv("pokemon.csv")

# # Basic cleaning (optional)
# df = df.dropna()

# # Create scatter plot
# plt.figure(figsize=(10,6))

# sns.scatterplot(
#     x='Attack',
#     y='Defense',
#     hue='Legendary',   # creates clusters (legendary vs non-legendary)
#     size='Speed',      # adds another dimension
#     data=df,
#     sizes=(20, 200),
#     alpha=0.7
# )

# # Title and labels
# plt.title("Scatter Plot of Attack vs Defense (Pokemon Dataset)")
# plt.xlabel("Attack")
# plt.ylabel("Defense")

# # Define outliers (example: very high attack)
# outliers = df[df['Attack'] > 150]

# plt.figure(figsize=(10,6))
# sns.scatterplot(x='Attack', y='Defense', data=df, alpha=0.5)

# # Highlight outliers in red
# plt.scatter(outliers['Attack'], outliers['Defense'], color='red', label='Outliers')

# plt.legend()
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("pokemon.csv")
df = df.dropna()

# Identify outliers
outliers = df[df['Attack'] > 150]

# Plot
plt.figure(figsize=(10,6))

sns.scatterplot(
    x='Attack',
    y='Defense',
    hue='Legendary',   # creates clusters automatically
    data=df,
    alpha=0.6
)

# Highlight outliers separately
plt.scatter(
    outliers['Attack'],
    outliers['Defense'],
    color='red',
    s=80,
    label="Outliers (Attack > 150)"
)

# Title and axis labels (mention all required concepts here)
plt.title("Scatter Plot: Clusters (Legendary vs Non-Legendary), Outliers, Positive Correlation")
plt.xlabel("Attack (shows positive correlation with Defense)")
plt.ylabel("Defense")

# Show legend
plt.legend()

plt.show()