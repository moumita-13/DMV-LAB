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
