import joblib

# Load trained model
model = joblib.load("career_model.pkl")

# Test skills
skills = input("Enter your skills: ")

# Predict career
prediction = model.predict([skills])

print("\nSuggested Career:")
print(prediction[0])