import pandas as pd

from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load Dataset
data = pd.read_csv("dataset.csv")

X = data["skills"]
y = data["career"]

# Pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

# Cross Validation
scores = cross_val_score(
    model,
    X,
    y,
    cv=4
)

print("Cross Validation Scores:")
print(scores)

print("\nAverage Accuracy:")
print(f"{scores.mean()*100:.2f}%")