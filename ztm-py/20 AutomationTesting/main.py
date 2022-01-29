# here we have install sele
# you can install by following command
# pip install selenium

from selenium import webdriver

chrome_browser = webdriver.Chrome(".\chromedriver")

# print(chrome_browser) # it will open the chrome browser

chrome_browser #it will open th echrome browser

chrome_browser.maximize_window() #it will maximize the window

chrome_browser.get("https://reactjs.org/docs/getting-started.html")

print("Getting Started – React" == chrome_browser.title)    #output:- True       #it will check the title of the browser and give it to you

assert chrome_browser.title in "jghvjkvkvjkuhvjkuvbjkhvb"   #assert - if the condition is false then it will give the error and callout of the console











