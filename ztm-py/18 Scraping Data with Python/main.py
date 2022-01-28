# scraping data is means we will get the data from the website that is public 
# it can be used when website dont provide us the api

# there is special section of each website where they tail you what are you allow to scraping and what you not
# you can simply add the /robots.txt at the end of any website url and you get the information on the rules of scraping

#  here we are going to scrape the hackernews website
# https://news.ycombinator.com
# https://news.ycombinator.com/robots.txt

# to scrape website we have a library beautifulsoup you can download it by following command
# pip install beautifulsoup4


# also you need to have request library you can download it by following command
# pip install requests



import requests
from bs4 import BeautifulSoup