# top_movies.py
import requests
from bs4 import BeautifulSoup

def get_top_movies():
    URL = "https://www.empireonline.com/movies/features/best-movies-2/"
    response = requests.get(URL)
    website_html = response.text
    soup = BeautifulSoup(website_html, "html.parser")
    all_movies = soup.find_all("h2")
    movies_titles = [h2.getText() for h2 in all_movies if h2.find("strong")]
    movies = movies_titles[::-1]  # Membalikkan list dari 100 ke 1 menjadi 1 ke 100

    with open("movies.txt", "w") as file:
        for movie in movies:
            file.write(f"{movie[:-6]}\n")  # Menghilangkan tahun

    with open("movies.txt", "a") as file:
        file.write("101) Timun Mas")

    return movies