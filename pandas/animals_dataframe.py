import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    "A": [5, 6, 8, 9, 7],
    "B": ["Flamingo", "Zebra", "Cart", "Bucket", "Samantha"],
    "C": ["Some", "Alex", "Apple", 5, "Art"]
}

df = pd.DataFrame(data)

max_value_A = df[df["B"].str.len() > 4 & df["C"].str.startswith("A")]["A"].max()
#max_value_B = df[(df["B"].str.len() > 4) & (df["C"].str.startswith("A"))].max()
max_value_C = df[(df["B"].str.len() > 4) & (df["C"].str.startswith("A"))]["A"].max()
#max_value_D = df[(df["B"].len() > 4) & (df["C"].startswith("A"))]["A"].max()

print(f"max_value_A = {max_value_A} | max_value_C = {max_value_C} ")

x = np.arange(len(df))  # [0, 1, 2, 3, 4]
width = 0.4

# Plot
fig, ax = plt.subplots()
ax.bar(x - width/2, df['A'], width, label='A vs B', color='skyblue')
ax.bar(x + width/2, df['A'], width, label='A vs C', color='salmon')

# Custom x-axis labels showing both B and C
labels = [f"{b}\n{c}" for b, c in zip(df['B'], df['C'])]
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45)

# Formatting
ax.set_ylabel('Values of A')
ax.set_title('Multi Bar Chart: Comparing B and C to A')
ax.legend()
plt.tight_layout()
plt.show()



# C is correct (7) because B at A=7 > 4 chars and C at A=7 starts with 'A'. B and D do not work. A gets the wrong value (9); although 9 is the highest and B at A=9 > 4 chars, C at A=9 is 5 which doesn't start with 'A'