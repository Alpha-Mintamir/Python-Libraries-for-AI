from sklearn.datasets import load_boston


# Load the Boston House Prices dataset
boston = load_boston()

# Separate features (X) and target (y)
X = boston.data
y = boston.target

