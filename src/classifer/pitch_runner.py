import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os

from src.classifer.pitch_models import PitchClassifier

# Load pitch data from a CSV file
data = pd.read_csv('/Users/danielpatterson/PitchData.csv')

# 'TaggedPitchType' is the column you want to predict, and the rest are features
X = data.drop('TaggedPitchType', axis=1)
y = data['TaggedPitchType']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert the data to dictionaries
X_train = [row.to_dict() for _, row in X_train.iterrows()]
X_test = [row.to_dict() for _, row in X_test.iterrows()]


# Create and train the classifier
classifier = PitchClassifier()
classifier.fit(X_train, y_train)

# Make predictions
predictions = classifier.predict(X_test)

# Evaluate the accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")