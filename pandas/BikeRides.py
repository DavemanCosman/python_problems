import pandas as pd

# Load the CSV file to check its contents
file_name = '6XWX_bike_rides.csv'
df = pd.read_csv(file_name)

# Display the first few rows of the dataframe and the column names
df.head(), df.columns

print(df.info())