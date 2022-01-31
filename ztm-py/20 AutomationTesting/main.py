# here we have install selenium
# you can install by following command
# pip install selenium

from selenium import webdriver


chrome_browser = webdriver.Chrome(".\chromedriver")

# print(chrome_browser) # it will open the chrome browser

chrome_browser #it will open th echrome browser

chrome_browser.maximize_window() #it will maximize the window

chrome_browser.get("http://texttospeechrobot.com/")

assert "Text To Speech Online" in chrome_browser.title   #assert - if the condition is false then it will give the error and callout of the console

# assert "Text To Speech Online" in chrome_browser.body   #error : it has no attribute called body

# there is a probleme here we can not get the body section 
# to get the body section data you have to use the selectors
# you can read about selectors in following link
# http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/

# to select the button from page
button_element = chrome_browser.find_element_by_id("speak_button")
print(button_element, "############################")   #it will grab the button
# to select the element by classname
# chrome_browser.find_element_by_class_name("classname")

print(button_element.get_attribute("innerHTML"), "* well our button dont have any innerHTMl *")

assert "speak_button" in chrome_browser.page_source     #it will check hole page source 

text_area = chrome_browser.find_element_by_id("text_box")
# now we have to check the textarea is empty
text_area.clear()   #it wiull clear the textarea

given_text = input("type the text that you want to convert into the audio : ")

text_area.send_keys(given_text)

button_element.click()

close = input("if you want to close the opened browser type \"y\" and enter : ")

if close == "y":
    chrome_browser.close()  #it will close the browser that we open
else:
    print("you have not type the \"y\" letter so you have to close the browser when you done your task")