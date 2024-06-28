from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split


# Load the Boston House Prices dataset
boston = load_boston()

# Separate features (X) and target (y)
X = boston.data
y = boston.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


