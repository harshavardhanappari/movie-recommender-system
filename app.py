import streamlit as st
import pickle
import pandas as pd
import requests

@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=a9da512d5545e21a8049b537a5cf7748"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data.get('poster_path'):
            return "https://image.tmdb.org/t/p/w500" + data['poster_path']
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"

    except requests.exceptions.RequestException:
        return "https://via.placeholder.com/500x750?text=TMDB+Error"

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_list:
        movies_id=movies.iloc[i[0]].movie_id;
        #fetch poster from api
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movies_id))
    return recommended_movies,recommended_movies_poster

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender system')


selected_movie_name = st.selectbox(
    "Select movie name",
    movies['title'].values
)

if st.button("Recommend"):
    names,posters =recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])