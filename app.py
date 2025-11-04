# import pickle
# import streamlit as st
# import requests
# import pandas as pd
# import certifi


# # # -----------------------------
# # # Fetch poster from TMDB API
# # # -----------------------------
# # def fetch_poster(movie_id):
# #     """Fetches the movie poster URL from TMDB API."""
# #     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=f52e52ebb7825b9dff966c9c1e38696e&language=en-US"
# #     try:
# #         data = requests.get(url)
# #         data.raise_for_status()
# #         data = data.json()
# #         poster_path = data.get('poster_path')
# #         if poster_path:
# #             return f"https://image.tmdb.org/t/p/w500/{poster_path}"
# #     except requests.exceptions.RequestException as e:
# #         st.error(f"Error fetching poster: {e}")
    
# #     # Placeholder poster if not found
# #     return "https://placehold.co/500x750/333/FFFFFF?text=No+Poster"

# # # -----------------------------
# # # Recommendation function
# # # -----------------------------
# # def recommend(movie):
# #     """Recommends 5 similar movies based on cosine similarity."""
# #     try:
# #         index = movies[movies['title'] == movie].index[0]
# #     except IndexError:
# #         st.error("Movie not found in dataset. Please select another.")
# #         return [], [], [], []

# #     distances = sorted(
# #         list(enumerate(similarity[index])),
# #         reverse=True,
# #         key=lambda x: x[1]
# #     )

# #     recommended_movie_names = []
# #     recommended_movie_posters = []
# #     recommended_movie_years = []
# #     recommended_movie_ratings = []

# #     for i in distances[1:6]:
# #         movie_id = movies.iloc[i[0]].movie_id
# #         recommended_movie_names.append(movies.iloc[i[0]].title)
# #         recommended_movie_posters.append(fetch_poster(movie_id))
# #         recommended_movie_years.append(movies.iloc[i[0]].year)
# #         recommended_movie_ratings.append(movies.iloc[i[0]].vote_average)

# #     return recommended_movie_names, recommended_movie_posters, recommended_movie_years, recommended_movie_ratings


# # # -----------------------------
# # # Streamlit UI
# # # -----------------------------
# # st.set_page_config(layout="wide")
# # st.header('🎬 Movie Recommender System using Machine Learning')

# # # Load data
# # try:
# #     movies_dict = pickle.load(open('artifacts/movie_dict.pkl', 'rb'))
# #     movies = pd.DataFrame(movies_dict)
# #     similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))
# # except FileNotFoundError:
# #     st.error("Model files not found. Please run build_similarity.py first.")
# #     st.stop()

# # # Movie dropdown
# # selected_movie = st.selectbox(
# #     "Type or select a movie from the dropdown",
# #     movies['title'].values
# # )

# # # Recommendations display
# # if st.button('Show Recommendation'):
# #     with st.spinner('Finding recommendations...'):
# #         names, posters, years, ratings = recommend(selected_movie)

# #     if names:
# #         cols = st.columns(5)
# #         for i, col in enumerate(cols):
# #             with col:
# #                 st.image(posters[i])
# #                 st.text(names[i])
# #                 year_display = int(years[i]) if pd.notna(years[i]) else "N/A"
# #                 st.caption(f"📅 Year: {year_display}")
# #                 st.caption(f"⭐ Rating: {ratings[i]:.1f}")


# def fetch_poster(movie_id):
#     """Fetches the movie poster URL from TMDB API using SSL verification."""
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=f52e52ebb7825b9dff966c9c1e38696e&language=en-US"
#     try:
#         # Use updated SSL certificates
#         data = requests.get(url, verify=certifi.where(), timeout=10)
#         data.raise_for_status()
#         data = data.json()
#         poster_path = data.get('poster_path')
#         if poster_path:
#             return f"https://image.tmdb.org/t/p/w500/{poster_path}"
#     except requests.exceptions.SSLError as e:
#         st.warning(f"SSL Error: {e}. Retrying without SSL verification...")
#         try:
#             data = requests.get(url, verify=False, timeout=10)
#             data.raise_for_status()
#             data = data.json()
#             poster_path = data.get('poster_path')
#             if poster_path:
#                 return f"https://image.tmdb.org/t/p/w500/{poster_path}"
#         except Exception:
#             pass
#     except Exception as e:
#         st.error(f"Error fetching poster: {e}")
    
#     return "https://placehold.co/500x750/333/FFFFFF?text=No+Poster"


import pickle
import streamlit as st
import requests
import pandas as pd
import certifi

# -----------------------------
# Fetch poster from TMDB API
# -----------------------------
def fetch_poster(movie_id):
    """Fetches the movie poster URL from TMDB API using SSL verification."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=f52e52ebb7825b9dff966c9c1e38696e&language=en-US"
    try:
        # Use updated SSL certificates for HTTPS verification
        #data = requests.get(url, verify=certifi.where(), timeout=10)
        data = requests.get(url, verify=False, timeout=10)
        data.raise_for_status()
        data = data.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    except requests.exceptions.SSLError as e:
        st.warning(f"⚠️ SSL Error: {e}. Retrying without SSL verification...")
        try:
            data = requests.get(url, verify=False, timeout=10)
            data.raise_for_status()
            data = data.json()
            poster_path = data.get('poster_path')
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        except Exception as e2:
            st.error(f"Poster fetch failed: {e2}")
    except Exception as e:
        st.error(f"Error fetching poster: {e}")

    # Placeholder poster if something fails
    return "https://placehold.co/500x750/333/FFFFFF?text=No+Poster"

# -----------------------------
# Recommendation function
# -----------------------------
def recommend(movie):
    """Recommends 5 similar movies based on cosine similarity."""
    try:
        index = movies[movies['title'] == movie].index[0]
    except IndexError:
        st.error("❌ Movie not found in dataset. Please select another.")
        return [], [], [], []

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_years = []
    recommended_movie_ratings = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_years.append(movies.iloc[i[0]].year)
        recommended_movie_ratings.append(movies.iloc[i[0]].vote_average)

    return recommended_movie_names, recommended_movie_posters, recommended_movie_years, recommended_movie_ratings


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")
st.header('🎬 Movie Recommender System using Machine Learning')

# Load data
try:
    movies_dict = pickle.load(open('artifacts/movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))
    st.success("✅ Model and data loaded successfully!")
except FileNotFoundError:
    st.error("❌ Model files not found. Please run build_similarity.py first.")
    st.stop()

# Movie dropdown
selected_movie = st.selectbox(
    "🎥 Type or select a movie from the dropdown:",
    movies['title'].values
)

# Recommendations display
if st.button('🔍 Show Recommendation'):
    with st.spinner('Finding similar movies...'):
        names, posters, years, ratings = recommend(selected_movie)

    if names:
        cols = st.columns(5)
        for i, col in enumerate(cols):
            with col:
                st.image(posters[i])
                st.text(names[i])
                year_display = int(years[i]) if pd.notna(years[i]) else "N/A"
                st.caption(f"📅 Year: {year_display}")
                st.caption(f"⭐ Rating: {ratings[i]:.1f}")
