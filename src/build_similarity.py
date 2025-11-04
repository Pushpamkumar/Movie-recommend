import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os
import ast

# -----------------------------
# Helper Functions
# -----------------------------
def convert(text):
    """Convert string representation of list to actual list."""
    if isinstance(text, str):
        try:
            return [i['name'] for i in ast.literal_eval(text)]
        except:
            return []
    return []

def convert_cast(text):
    """Extract top 3 cast members from cast list."""
    if isinstance(text, str):
        try:
            L = []
            counter = 0
            for i in ast.literal_eval(text):
                if counter < 3:
                    L.append(i['name'])
                counter += 1
            return L
        except:
            return []
    return []

def fetch_director(text):
    """Extract director name from crew data."""
    if isinstance(text, str):
        try:
            for i in ast.literal_eval(text):
                if i['job'] == 'Director':
                    return [i['name']]
        except:
            return []
    return []

# -----------------------------
# Main Function
# -----------------------------
def main():
    # Create artifacts directory if it doesn't exist
    if not os.path.exists('artifacts'):
        os.makedirs('artifacts')

    # Load datasets
    try:
        movies = pd.read_csv('data/tmdb_5000_movies.csv')
        credits = pd.read_csv('data/tmdb_5000_credits.csv')
    except FileNotFoundError:
        print("❌ Error: Required data files not found!")
        print("Please ensure the following files exist in the 'data/' directory:")
        print("  - tmdb_5000_movies.csv")
        print("  - tmdb_5000_credits.csv")
        return

    # Merge the dataframes
    movies = movies.merge(credits, on='title')

    # Select relevant features
    movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 
                     'cast', 'crew', 'release_date', 'vote_average']]

    # Handle missing data
    movies.dropna(inplace=True)

    # Extract release year
    movies['year'] = pd.to_datetime(movies['release_date'], errors='coerce').dt.year

    # Convert features
    movies['genres'] = movies['genres'].apply(convert)
    movies['keywords'] = movies['keywords'].apply(convert)
    movies['cast'] = movies['cast'].apply(convert_cast)
    movies['crew'] = movies['crew'].apply(fetch_director)

    # Convert overview to list of words
    movies['overview'] = movies['overview'].apply(lambda x: x.split())

    # Merge all tags into a single list
    movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

    # Convert list of words back to a single string
    movies['tags'] = movies['tags'].apply(lambda x: " ".join(x).lower())

    # Create new dataframe for the recommendation system
    new_df = movies[['movie_id', 'title', 'tags', 'year', 'vote_average']]

    # -----------------------------
    # Vectorization and Similarity
    # -----------------------------
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(new_df['tags']).toarray()

    similarity = cosine_similarity(vectors)

    # -----------------------------
    # Save Artifacts
    # -----------------------------
    with open('artifacts/movie_dict.pkl', 'wb') as f:
        pickle.dump(new_df.to_dict(), f)

    with open('artifacts/similarity.pkl', 'wb') as f:
        pickle.dump(similarity, f)

    print("✅ Successfully created model files:")
    print(" - artifacts/movie_dict.pkl")
    print(" - artifacts/similarity.pkl")

# -----------------------------
# Entry Point
# -----------------------------
if __name__ == "__main__":
    main()
