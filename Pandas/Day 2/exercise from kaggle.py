import pandas as pd

# Set display options
pd.set_option('display.max_rows', 5)

# Define DataFrame fruits
fruits = pd.DataFrame({'Apples': [30], 'Bananas': [21]})

# Define DataFrame fruit_sales
fruit_sales = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index=['2017 Sales', '2018 Sales'])

# Define Series ingredients
ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'],
                        index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')

# Read CSV dataset into DataFrame reviews
reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv', index_col=0)

# Define DataFrame animals
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])

# Save DataFrame animals to a CSV file
animals.to_csv('cows_and_goats.csv')