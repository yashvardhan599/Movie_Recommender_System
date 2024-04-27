import streamlit as st
import pickle
import pandas as pd


def recommend(selected_movie):
    movie_index = movie[movie['title'] == selected_movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movies_list:
        # movie_id = i[0]


        recommended_movies.append(movie.iloc[i[0]].title)
    return recommended_movies


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movie = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Enter your movie name here!',
    movie['title'].values
)

if st.button('Recommend'):
    recommendation = recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)
