import pandas as pd

df = pd.read_csv('National Universities Rankings.csv', encoding='latin1')

# To View the first 5 rows of the DataFrame

print(df.head(10))

# Display basic information about the DataFrame
print(df.info())

# Display descriptive statistics for numerical columns
print(df.describe())

# Select a single column
single_column = df['Rank']

print(single_column)

# Select multiple columns
multiple_columns = df[['Rank', 'Name']]

print(multiple_columns)