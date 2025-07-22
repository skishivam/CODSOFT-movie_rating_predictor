:

🎬 Movie Rating Predictor App
This is a Streamlit-based web application that predicts the IMDb rating of a movie based on its title, duration, and actors' names using machine learning.

<!-- Optional: Replace with your own screenshot or remove -->

🚀 Features
🎥 Select movie title from a dropdown

⏱️ Enter movie duration

👨‍🎤 Enter actor(s) name

🧠 Predicts IMDb rating using a trained Random Forest model

✅ Easy to run and extend

📁 Project Structure
graphql
Copy
Edit
movie_rating_app/
│
├── app.py                # Streamlit frontend
├── train_model.py        # Model training script
├── rating_model.pkl      # Saved ML model
├── label_encoder.pkl     # Encoder for actor names
├── imdb_movies_sample.csv # Sample IMDb movie dataset
└── README.md             # Project documentation
🛠️ How to Run
Step 1: Clone or Download the Project
bash
Copy
Edit
git clone https://github.com/yourusername/movie-rating-predictor.git
cd movie-rating-predictor
Or just unzip the movie_rating_app.zip file provided.

Step 2: Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is not present, manually run:

bash
Copy
Edit
pip install streamlit pandas scikit-learn
Step 3: Start the Streamlit App
bash
Copy
Edit
streamlit run app.py
🧠 Model Information
Model Used: Random Forest Regressor

Features:

Movie Title (categorical)

Duration (numerical)

Actor Name (categorical)

Target: IMDb Rating (float)

🗂️ Dataset
A sample dataset imdb_movies_sample.csv is included. You can replace it with your own dataset but ensure it contains at least the following columns:

title

duration

actors

imdb_rating

📌 To-Do / Future Enhancements
Add support for multiple actors

Add sentiment analysis from movie description

Deploy on Streamlit Cloud or Render

Add input by typing movie name (autocomplete)

🧑‍💻 Author
Shivam Kumar Jha

LinkedIn

GitHub

📄 License
This project is licensed under the MIT License. See LICENSE for more information.

