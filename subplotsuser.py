import matplotlib.pyplot as plt

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

fig, axes = plt.subplots(rows, cols, figsize=(5*cols, 4*rows))

if rows == 1 and cols == 1:
    axes = [[axes]]
elif rows == 1:
    axes = [axes]
elif cols == 1:
    axes = [[ax] for ax in axes]

for i in range(rows):
    for j in range(cols):
        print(f"\nEnter data for subplot ({i+1},{j+1})")
        x = list(map(float, input("Enter x values (space separated): ").split()))
        y = list(map(float, input("Enter y values (space separated): ").split()))
        
        axes[i][j].plot(x, y)
        axes[i][j].set_title(f"Plot {i+1},{j+1}")
        axes[i][j].set_xlabel("X-axis")
        axes[i][j].set_ylabel("Y-axis")

plt.tight_layout()
plt.show()
