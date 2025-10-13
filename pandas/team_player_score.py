import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Team": ["Red", "Red", "Blue", "Blue", "Red", "Red", "Blue", "Blue"],
    "Player": [ "Dave", "Rei", "Justin", "Trami", "Mateo", "Soren", "Don", "Lin" ],
    "Score": [ 75, 90, 50, 100, 10, 85, 86, 95 ]
}

df = pd.DataFrame(data)

result = df.groupby("Team")["Score"].apply(lambda x: (x > 85).sum())

print(f"result = {result}")

# colors based on team:
colors = df['Team'].map({'Red':'red', 'Blue': 'blue'})

# Plotting

plt.figure(figsize=(10,6))
plt.scatter(df['Player'], df['Score'],color=colors)

plt.title('Player Scores by Team')
plt.xlabel('Player')
plt.ylabel('Score')
plt.axhline(y=85, linestyle='--')
plt.show()