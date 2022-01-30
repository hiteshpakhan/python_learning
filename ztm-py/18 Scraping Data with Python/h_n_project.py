from os import link
from turtle import title
import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/")
collected_html = BeautifulSoup(res.text, "html.parser")
news_title = collected_html.select(".titlelink")
votes = collected_html.select(".score")

def create_custom_hacker_news(links, votes):
    h_n_list = []
    for index, item in enumerate(links):
        title = links[index].getText()  #it will get the text inside the element
        href = links[index].get("href", None)   #it will catch the link of the news 
        points = int(votes[index].getText().replace(" points", ""))
        print(points)
        h_n_list.append({"title" : title, "href" : href})
    return h_n_list

print(create_custom_hacker_news(news_title, votes))