import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset = https://www.kaggle.com/datasets/abcsds/pokemon
df = pd.read_csv("Pokemon.csv")

# Optional: make it small (~30 rows)
df = df.head(30)

print(df.head())

print("Missing Values:\n")
print(df.isnull().sum())

numeric_cols = df.select_dtypes(include=np.number)

for col in numeric_cols.columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower) | (df[col] > upper)]

    print(f"\nOutliers in {col}:")
    print(outliers[[col]])
    
print("\nStatistical Summary:\n")
print(df.describe())

print("\nDataset Info:\n")
print(df.info())

df.groupby("Type 1")["Attack"].mean().plot(kind="bar", color="orange")

plt.title("Average Attack by Type")
plt.xlabel("Type")
plt.ylabel("Attack")
plt.grid(True)
plt.xticks(rotation=45)
plt.show()




