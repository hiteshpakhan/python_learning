# here we have install selenium
# you can install by following command
# pip install selenium

from selenium import webdriver

chrome_browser = webdriver.Chrome(".\chromedriver")

# print(chrome_browser) # it will open the chrome browser

chrome_browser #it will open th echrome browser

chrome_browser.maximize_window() #it will maximize the window

chrome_browser.get("https://reactjs.org/docs/getting-started.html")

print("Getting Started – React" == chrome_browser.title)    #output:- True       #it will check the title of the browser and give it to you

# assert chrome_browser.title in "jghvjkvkvjkuhvjkuvbjkhvb"   #assert - if the condition is false then it will give the error and callout of the console

# there is a probleme here we can not get the body section 
# to get the body section data you have to use the selectors
# you can read about selectors in following link
# http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/


# we can grab items inside the page by using the selectrs
element = chrome_browser.find_element_by_class_name("css-19nz7r4")  #ti will grabe the element by the class name as we said
print(element)  #you can see the button that we grab  # but if you want to grab the info about that button you can do following
print(element.get_attribute("innerHtml")) 
#we will do the automation after some time
