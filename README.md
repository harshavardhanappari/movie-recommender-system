# 🎬 Movie Recommendation System

A content-based movie recommender system built using Machine Learning and deployed with Streamlit.

---

## 🚀 Live Demo
👉 https://movie-recommender-system-gv7uaq77p9vjbvquggragk.streamlit.app/

---

## 📌 Features
- Content-based movie recommendations
- Cosine similarity for finding similar movies
- TMDB API integration for movie posters
- Clean and interactive Streamlit UI
- Deployed on Streamlit Community Cloud

---

## 🛠️ Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- TMDB API

---

## ⚙️ How It Works
1. Movies are vectorized based on features
2. Cosine similarity matrix is computed
3. For a selected movie, the top similar movies are recommended
4. Movie posters are fetched using TMDB API

---

## 📂 Project Structure
app.py
movies_dict.pkl
similarity.pkl
requirements.txt
README.md



---

## ▶️ Run Locally

pip install -r requirements.txt
streamlit run app.py

---

🔐 API Key
This project uses the TMDB API.

Store your API key securely using Streamlit Secrets:

TMDB_API_KEY = "your_api_key_here"

---

👤 Author

Mani Harsha Vardhan Appari
