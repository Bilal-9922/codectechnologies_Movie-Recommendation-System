import pandas as pd

# Load dataset
movies = pd.read_csv("movies.csv")

print("Available Genres:")
print(movies["genre"].unique())

# Take user input
genre = input("\nEnter a genre: ")

# Recommend movies
recommendations = movies[movies["genre"].str.lower() == genre.lower()]

print("\nRecommended Movies:")

if len(recommendations) == 0:
    print("No movies found for this genre.")
else:
    for movie in recommendations["title"]:
        print(movie)
