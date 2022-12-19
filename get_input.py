import requests
from bs4 import BeautifulSoup

def get_input(url):
    res = requests.get(url, cookies = {"session": "53616c7465645f5f5a1e9e529aa39978812f0acbe7e71654873db2102805c1ba7297f86aa50f3338416af29f4379e0b185ec3c9e67ca0c0b8d636085fe0292b2"})
    html_page = res.content

    soup = BeautifulSoup(html_page, "html.parser")
    text = soup.find_all(text=True)

    return text
