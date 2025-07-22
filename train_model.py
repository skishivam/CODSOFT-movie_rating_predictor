import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import pickle

# Load the dataset
df = pd.read_csv("imdb_movies_sample.csv")

# Encode categorical column
le = LabelEncoder()
df["Lead_Actor"] = le.fit_transform(df["Lead_Actor"])

# Features and target
X = df[["Duration", "Lead_Actor"]]
y = df["Rating"]

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model and encoder
with open("rating_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("label_encoder.pkl", "wb") as f:
    pickle.dump(le, f)
