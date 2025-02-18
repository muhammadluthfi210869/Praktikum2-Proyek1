# main.py
from hacker_news import get_hacker_news
from top_movies import get_top_movies

def main():
    # Mengambil dan menampilkan berita terpopuler dari Hacker News
    hacker_news = get_hacker_news()
    print("Berita terpopuler dari Hacker News:")
    print(f"Judul: {hacker_news['text']}")
    print(f"Link: {hacker_news['link']}")
    print(f"Upvotes: {hacker_news['upvotes']}")
    print("\n")

    # Mengambil dan menampilkan daftar film terbaik
    top_movies = get_top_movies()
    print("Daftar 100 film terbaik menurut Empire Online:")
    for movie in top_movies:
        print(movie)

if __name__ == "__main__":
    main()