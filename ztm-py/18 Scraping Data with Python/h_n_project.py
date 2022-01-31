import requests
from bs4 import BeautifulSoup
import pprint   #it just the library that help us to type in the terminal nisely


res = requests.get("https://news.ycombinator.com/")
res2 = requests.get("https://news.ycombinator.com/news?p=2")
collected_html = BeautifulSoup(res.text, "html.parser")
collected_html2 = BeautifulSoup(res.text, "html.parser")

news_title = collected_html.select(".titlelink")
subtext = collected_html.select(".subtext")
news_title2 = collected_html2.select(".titlelink")
subtext2 = collected_html2.select(".subtext")

mega_news_title = news_title + news_title2
mega_subtext = subtext + subtext2


def sort_story_by_votes(h_n_list):
    return sorted(h_n_list, key= lambda k:k["votes"], reverse=True)



def create_custom_hacker_news(links, subtext):
    h_n_list = []
    for index, item in enumerate(links):
        title = links[index].getText()  #it will get the text inside the element
        href = links[index].get("href", None)   #it will catch the link of the news 
        vote = subtext[index].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                h_n_list.append({"title" : title, "href" : href, "votes": points})
    return sort_story_by_votes(h_n_list)

# print(create_custom_hacker_news(news_title, subtext))
# to type nicely inside in the terminal you can print by the following 
pprint.pprint(create_custom_hacker_news(mega_news_title, mega_subtext))


# if you want to learn more about scraping data you can learn on the scrapy, scrapy is the framework that helps you to do scraping 