import streamlit as st
import pandas as pd
import pickle

# Load model and encoder
with open("rating_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

# Load dataset
df = pd.read_csv("imdb_movies_sample.csv")

st.set_page_config(page_title="Movie Rating Predictor", layout="centered")
st.title("🎬 Movie Rating Predictor (IMDb Style)")

# Dropdown for movie title
movie_title = st.selectbox("Select Movie Title", df["Title"].unique())

# Get duration and actor based on movie
selected_row = df[df["Title"] == movie_title].iloc[0]
duration = selected_row["Duration"]
actor_name = selected_row["Lead_Actor"]

# Display details
st.write(f"🕒 Duration: {duration} minutes")
st.write(f"👤 Lead Actor: {actor_name}")

# Predict button
if st.button("Predict Rating"):
    try:
        actor_encoded = le.transform([actor_name])[0]
        input_data = [[duration, actor_encoded]]
        rating = model.predict(input_data)[0]
        st.success(f"⭐ Predicted IMDb Rating for '{movie_title}': {rating:.2f}")
    except Exception as e:
        st.error(f"Error: {e}")
