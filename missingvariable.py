import pandas as pd
import numpy as np

data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [20, None, 22, np.nan],
    "Marks": [85, 90, None, 88]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Marks"].fillna(df["Marks"].median(), inplace=True)

print("\nAfter Handling Missing Values:")
print(df)
