# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load dataset
# df = pd.read_csv("Pokemon.csv")

# # Optional: take first 30 rows
# df = df.head(30)

# # Style
# sns.set(style="whitegrid")

# # Create subplot grid (2 rows, 3 columns)
# fig, axes = plt.subplots(2, 3, figsize=(18, 10))
# fig.suptitle("Pokemon Data Visualization Dashboard", fontsize=16)

# # -------------------------------
# # 1. Bar Chart (Average Attack by Type)
# # -------------------------------
# df.groupby("Type 1")["Attack"].mean().plot(
#     kind="bar", ax=axes[0,0], color="orange"
# )
# axes[0,0].set_title("BAR CHART (Avg Attack by Type)")
# axes[0,0].set_xlabel("Type")
# axes[0,0].set_ylabel("Attack")
# axes[0,0].grid(True)

# # -------------------------------
# # 2. Scatter Plot (Attack vs Defense)
# # -------------------------------
# axes[0,1].scatter(df["Attack"], df["Defense"], color="blue")
# axes[0,1].set_title("SATTER Attack vs Defense")
# axes[0,1].set_xlabel("Attack")
# axes[0,1].set_ylabel("Defense")
# axes[0,1].grid(True)

# # -------------------------------
# # 3. Pie Chart (Type Distribution)
# # -------------------------------
# df["Type 1"].value_counts().plot(
#     kind="pie", autopct="%1.1f%%", ax=axes[0,2]
# )
# axes[0,2].set_title("Pie Chart Type Distribution")
# axes[0,2].set_ylabel("")

# # -------------------------------
# # 4. Stair Chart (Speed)
# # -------------------------------
# axes[1,0].step(df.index, df["Speed"], where="mid")
# axes[1,0].set_title("Speed Stair Chart")
# axes[1,0].set_xlabel("Index")
# axes[1,0].set_ylabel("Speed")
# axes[1,0].grid(True)

# # -------------------------------
# # 5. Line Chart (Total Stats)
# # -------------------------------
# axes[1,1].plot(df["Total"], marker="o", color="green")
# axes[1,1].set_title("Total Stats Trend")
# axes[1,1].set_xlabel("Index")
# axes[1,1].set_ylabel("Total")
# axes[1,1].grid(True)

# # -------------------------------
# # 6. BONUS: Histogram (HP Distribution)
# # -------------------------------
# axes[1,2].hist(df["HP"], bins=10, color="purple")
# axes[1,2].set_title("HP Distribution")
# axes[1,2].set_xlabel("HP")
# axes[1,2].set_ylabel("Frequency")
# axes[1,2].grid(True)

# # Adjust layout
# plt.tight_layout()
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Pokemon.csv")

# Optional: first 30 rows
df = df.head(30)

# Style
sns.set(style="whitegrid")

# Create subplot grid (2 rows, 3 columns)
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle("Pokemon Data Visualization Dashboard", fontsize=16)

# -------------------------------
# 1. Bar Chart
# -------------------------------
df.groupby("Type 1")["Attack"].mean().plot(
    kind="bar", ax=axes[0,0], color="orange"
)
axes[0,0].set_title("Bar Chart (Avg Attack by Type)")
axes[0,0].set_xlabel("Type")
axes[0,0].set_ylabel("Attack")
axes[0,0].grid(True)

# -------------------------------
# 2. Scatter Plot
# -------------------------------
axes[0,1].scatter(df["Attack"], df["Defense"], color="blue")
axes[0,1].set_title("Scatter Plot (Attack vs Defense)")
axes[0,1].set_xlabel("Attack")
axes[0,1].set_ylabel("Defense")
axes[0,1].grid(True)

# -------------------------------
# 3. Pie Chart
# -------------------------------
df["Type 1"].value_counts().plot(
    kind="pie", autopct="%1.1f%%", ax=axes[0,2]
)
axes[0,2].set_title("Pie Chart (Type Distribution)")
axes[0,2].set_ylabel("")

# -------------------------------
# 4. Stair Chart
# -------------------------------
axes[1,0].step(df.index, df["Speed"], where="mid")
axes[1,0].set_title("Stair Chart (Speed)")
axes[1,0].set_xlabel("Index")
axes[1,0].set_ylabel("Speed")
axes[1,0].grid(True)

# -------------------------------
# 5. Line Chart
# -------------------------------
axes[1,1].plot(df["Total"], marker="o", color="green")
axes[1,1].set_title("Line Chart (Total Stats Trend)")
axes[1,1].set_xlabel("Index")
axes[1,1].set_ylabel("Total")
axes[1,1].grid(True)

# -------------------------------
# Remove empty subplot (bottom-right)
# -------------------------------
fig.delaxes(axes[1,2])

# Adjust layout
plt.tight_layout()
plt.show()