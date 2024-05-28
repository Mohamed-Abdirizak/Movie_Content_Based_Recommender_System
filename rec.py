import pickle
import streamlit as st
import requests

# Set the page configuration
st.set_page_config(
    page_title="Recommender System",
    page_icon=":bar_chart:",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Add a title
st.title("Movies Recommendation System Uisng Machine Learning")

# Add a subheader
st.subheader("Content-Based Filtering")

# Add some text
st.write("This recommender system uses a content-based filtering approach to provide personalized recommendations.")

# Add a divider
st.markdown("---")

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=25a52fd1675d98fb10f458012894dac6".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "http://image.tmdb.org/t/p/w500/" + poster_path if poster_path else None
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies_names = []
    recommended_movies_poster = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_names.append(movies.iloc[i[0]].title)
    return recommended_movies_names, recommended_movies_poster

# reading or opening the saved two models
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))

# select box: allows the user to choose or to write the movies
movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Type or select a movie to get recommendation',
    movie_list
)

if st.button("Show recommendation"):
    recommended_movies_names, recommended_movies_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies_names[0])
        try:
            if recommended_movies_poster is not None:
                st.image(recommended_movies_poster[0])
            else:
                st.write("There is no image on this movie....")
        except Exception as e:
            st.write("Error displaying poster:", str(e))
    with col2:
        st.text(recommended_movies_names[1])
        try:
            if recommended_movies_poster is not None:
                st.image(recommended_movies_poster[1])
            else:
                st.write("There is no image on this movie....")
        except Exception as e:
            st.write("Error displaying poster:", str(e))
    with col3:
        st.text(recommended_movies_names[2])
        try:
            if recommended_movies_poster is not None:
                st.image(recommended_movies_poster[2])
            else:
                st.write("There is no image on this movie....")
        except Exception as e:
            st.write("Error displaying poster:", str(e))
    with col4:
        st.text(recommended_movies_names[3])
        try:
            if recommended_movies_poster is not None:
                st.image(recommended_movies_poster[3])
            else:
                st.write("There is no image on this movie....")
        except Exception as e:
            st.write("Error displaying poster:", str(e))
    with col5:
        st.text(recommended_movies_names[4])
        try:
            if recommended_movies_poster is not None:
                st.image(recommended_movies_poster[4])
            else:
                st.write("There is no image on this movie....")
        except Exception as e:
            st.write("Error displaying poster:", str(e))

# Add some more text
st.write("Developer Name:")
st.markdown("**Mohamed Abdrizak Ahmed.**")

# Add a divider
st.markdown("---")

# Add a footer
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 12px;'>© 2024 Recommender System</p>",
    unsafe_allow_html=True
)
