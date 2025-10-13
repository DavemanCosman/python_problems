import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Steps': [8000, 9500, 7000, 12000, 10000]
})

plt.plot(df['Day'], df['Steps'], marker='o')
plt.title('Steps per Day')
plt.xlabel('Day')
plt.ylabel('Steps')
plt.grid(True)
plt.show()