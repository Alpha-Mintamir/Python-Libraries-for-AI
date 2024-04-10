import pandas as pd

# Load the dataset
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

# Select the description column
desc = reviews['description']

# Select the first value from the description column
first_description = reviews.description.iloc[0]

# Select the first row of data
first_row = reviews.iloc[0,:]

# Select the first 10 values from the description column
first_descriptions = reviews.description.iloc[:10]

# Select specific records with index labels 1, 2, 3, 5, and 8
indices = [1, 2, 3, 5, 8]
sample_reviews = reviews.loc[indices]

# Create a DataFrame containing specific columns for records with index labels 0, 1, 10, and 100
df = reviews.loc[[0, 1, 10, 100], ['country', 'province', 'region_1', 'region_2']]

# Create a DataFrame containing the country and variety columns of the first 100 records
df = reviews.loc[:99, ['country', 'variety']]

# Create a DataFrame containing reviews of wines made in Italy
italian_wines = reviews[reviews['country'] == 'Italy']

# Create a DataFrame containing reviews with at least 95 points for wines from Australia or New Zealand
top_oceania_wines = reviews.loc[(reviews.country.isin(['Australia', 'New Zealand'])) & (reviews.points >= 95)]