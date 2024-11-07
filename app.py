import pickle
import streamlit as st
import requests

# Function to recommend movies based on similarity
def recommend(movie):
    # Find the index of the selected movie
    index = movies[movies['title'] == movie].index[0]
    
    # Get the list of movie distances and sort by similarity (highest first)
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    # Prepare the list of recommended movie names
    recommended_movie_names = []
    for i in distances[1:6]:  # Exclude the first item (the selected movie itself)
        recommended_movie_names.append(movies.iloc[i[0]].title)
    
    return recommended_movie_names

# Streamlit header
st.header('Movie Recommender System')

# Load movie list and similarity data (replace with actual path where you have your pickle files)
movies = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

# Create a dropdown for movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

# Show recommendations on button click
if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    
    # Display the names of recommended movies one below the other
    st.subheader("Recommended Movies:")
    for movie in recommended_movie_names:
        st.markdown(f"<h6 style= text-align: center;'>{movie}</h4>", unsafe_allow_html=True)
