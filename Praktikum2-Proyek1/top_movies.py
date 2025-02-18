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

    return movies

def add_movie():
    file = open("movies.txt", "r")
    lines = len(file.readlines())
    file.close()
    
    movie = input("Ketik judul film yang ingin anda masukkan: ").title().strip()
    file = open("movies.txt", "a")
    file.write(f"{lines + 1}) {movie}\n")
    file.close()
    
    print(f"Film {movie} telah ditambahkan ke daftar film")

def remove_movie():
    movie = input("Ketik judul film yang ingin anda hapus: ").title().strip()
    file = open("movies.txt", "r")
    lines = file.readlines()
    file.close()
    movie_found = False
    for line in lines:
        if movie in line:
            movie_found = True
            break
    if not movie_found:
            print(f"Film '{movie}' tidak ditemukan dalam daftar.")
            return
        
    file = open("movies.txt", "w")
    num = 1
    for line in lines:
        if movie not in line:
            movie_title = line.split(') ', 1)[1] if ') ' in line else line
            file.write(f"{num}) {movie_title}")
            num += 1
    file.close()
    
    print(f"Film {movie} telah dihapus dari daftar film")

def edit_movie():
    movie = input("Ketik judul film yang ingin anda ubah: ").title()
    file = open("movies.txt", "r")
    lines = file.readlines()
    file.close()
    
    movie_found = False
    new_movie = ""
    
    file = open("movies.txt", "w")
    for line in lines:
        if movie in line and not movie_found:
            new_movie = input("Ketik judul film baru: ").strip().title()
            if not new_movie:
                print("Judul film baru tidak boleh kosong!")
                file.writelines(lines)
                return
            updated_line = line.replace(movie, new_movie)
            file.write(updated_line)
            movie_found = True
        else:
            file.write(line)
    if movie_found:
        print(f"Film '{movie}' telah diubah menjadi '{new_movie}'")
    else:
        print(f"Film '{movie}' tidak ditemukan dalam daftar!")
    file.close()

get_top_movies()
remove_movie()