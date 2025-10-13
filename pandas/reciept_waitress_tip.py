import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Receipt ID": ["124DC", "4442A", "222BZ", None, "5421T"],
    "Waiter/Waitress Name": ["Todd", None, "Lenny", "Jennifer", "Yazmin"],
    "Tip Amount": [12, 4, 3, 44, 29]
}

df = pd.DataFrame(data)

#df.fillna("Unknown",inplace=True) #this modifies other cols
df["Receipt ID"] = df["Receipt ID"].fillna("Unknown") #seems to work
#df.fillna({"Receipt ID": "Unknown"}) #error
#df = df.fillna("Receipt ID": "Unknown") #error

plt.figure(figsize=(10,6))
plt.bar(df["Receipt ID"], df["Tip Amount"])

plt.title('Tips by amount')
plt.xlabel('Receipt ID')
plt.ylabel('Tip Amount')
plt.show()

#plt.figure(figsize=(10,6))
#plt.bar(df["Waiter/Waitress Name"], df["Tip Amount"])
#
#plt.title('Waiter/Waitress Name Tips by amount')
#plt.xlabel('Waiter/Waitress Name')
#plt.ylabel('Tip Amount')
#plt.show()