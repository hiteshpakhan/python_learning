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
from soupsieve import select

# requests.get("url")
# .text
res = requests.get("https://news.ycombinator.com/")
print(res)  #output:- response 200
print(res.text) #output it will give you all thye page in the form of html

# BeautifulSoup
# .text
# "html.parser"
# beautifulSoupo allows to parse this recived html data
# now you can convert this hole string into the object that can we use by beautifulSoup
soup = BeautifulSoup(res.text, "html.parser")
print(soup) # you can see that it will give all the html data inthe object form
# you can also call now the html elements directly
print(soup.body) # here you can see that it will only give the body in the object
print(soup.a)   #it will give you the first comming a attribute

# .contents()
print(soup.body.contents)   #it will give all the body contents in the list form 

# .find_all()
print(soup.find_all("a")) #we will get all the div in the list form

# .find()
print(soup.find("a"))  #it will give the first a tag

print(soup.find(id="score_30135264"))   #it will give us the 

# .select()
# .     class
# #     id
# *     selects all the element
# ,
# >
# +
# space
# ~
# you can select the class and the id by css selectors
print("\n\n\n\n\n",soup.select(".score"))
print("\n\n\n\n\n",soup.select("#score_30135264"))