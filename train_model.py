import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
data = pd.read_csv("dataset.csv")

# Input and Output
X = data["skills"]
y = data["career"]

# Create ML pipeline
model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])

# Train model
model.fit(X, y)

# Save model
joblib.dump(model, "career_model.pkl")

print("Model trained successfully!")
print("career_model.pkl file created.")