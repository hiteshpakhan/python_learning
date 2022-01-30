import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/")
collected_html = BeautifulSoup(res.text, "html.parser")
print(collected_html.select(".titlelink")[0])