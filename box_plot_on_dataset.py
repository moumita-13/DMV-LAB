import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Pokemon.csv")

plt.figure(figsize=(12,6))
sns.boxplot(x='Type 1', y='Attack', data=df)

plt.xticks(rotation=90)
plt.title("Boxplot of Attack by Pokémon Type")
plt.show()

