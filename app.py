import streamlit as st
import pandas as pd

# Title
st.title("🎬 Movie Recommender System")

st.write("Select a genre to get movie recommendations.")

# Load dataset
movies = pd.read_csv("movies.csv")

# Get unique genres
genres = movies["genre"].unique()

# Dropdown for genre selection
selected_genre = st.selectbox("Choose a Genre", genres)

# Button to recommend
if st.button("Recommend Movies"):
    
    recommendations = movies[movies["genre"].str.lower() == selected_genre.lower()]
    
    st.subheader("Recommended Movies")
    
    if recommendations.empty:
        st.write("No movies found for this genre.")
    else:
        for movie in recommendations["title"]:
            st.write("🎥 " + movie)