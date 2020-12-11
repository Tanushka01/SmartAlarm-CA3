import requests
import json
with open('config.json', 'r') as f:
    json_file = json.load(f)
    keys = json_file["API-keys"]
    n_api_key = keys["news"]


def news_info() -> tuple:
    """
    returns a tuple of a list of top 10 news titles from bbc news and the corresponding urls
    """
    base_url = 'http://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey='
    complete_url = base_url + n_api_key
    news = requests.get(complete_url).json()
    articles = news['articles']
    titles = []
    urls = []
    for x in articles:
        titles.append(x['title'])
        urls.append(x['url'])
    return titles, urls


def news_ann() -> str:
    """
    function to return the list of article titles as a string. This is done so that the announcement can be made by
    the titles being recited
    """
    title, url = news_info()
    news_say = ", ".join(title)
    return news_say


def top_news_story() -> list:
    """
    Returns a list containing the article and its corresponding url
    """
    title, url = news_info()
    top_story = [title[0], url[0]]
    return top_story
