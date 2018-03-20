import numpy as np
import scipy
import pandas as pd
import _pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

vectorizer = None
forest = None

with open ('vectorizer.txt', 'rb') as f:
	vectorizer = _pickle.load(f)

with open('forest.txt', 'rb') as f:
	forest = _pickle.load(f)

review = input('enter a review > ')
# Get a bag of words for the test set, and convert to a numpy array
test_data_features = vectorizer.transform([review])
test_data_features = test_data_features.toarray()
# Use the random forest to make sentiment label predictions
result = forest.predict(test_data_features)

# Copy the results to a pandas dataframe with an "id" column and
# a "sentiment" column
print(result[0])
