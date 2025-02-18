# hacker_news.py
from bs4 import BeautifulSoup
import requests

def get_hacker_news():
    response = requests.get("https://news.ycombinator.com/news")
    contents = response.text
    soup = BeautifulSoup(contents, "html.parser")

    articles = soup.find_all(name="span", class_="titleline")
    article_texts = []
    article_links = []
    for article in articles:
        article_tag = article.select("span a")[0]
        article_text = article_tag.getText()
        article_link = article_tag.get("href")

        article_texts.append(article_text)
        article_links.append(article_link)

    article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

    highest_upvote = 0
    highest_upvote_article = 0
    for i in range(len(article_upvotes)):
        if article_upvotes[i] > highest_upvote:
            highest_upvote = article_upvotes[i]
            highest_upvote_article = i

    return {
        "text": article_texts[highest_upvote_article],
        "link": article_links[highest_upvote_article],
        "upvotes": article_upvotes[highest_upvote_article]
    }