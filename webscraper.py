from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from icalevents.icalevents import events
import requests
#pip3 install icalevents

ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
def start():
    global driver
    driver = webdriver.Chrome(executable_path="/Users/timangevare/Documents/Code/chromedriver")
    global wait
    wait = WebDriverWait(driver, 60, ignored_exceptions=ignored_exceptions)

def weather():
    driver.get("https://weather.com/weather/today/l/57fae565d25f68b70131cd8683da28e8b595fb41ae07ae5cd2a827af58233bac")
    sleep(4)
    temp = driver.find_element_by_class_name("CurrentConditions--tempValue--3KcTQ")
    farenheit = int(temp.text[0:-1])
    celsuis = int((farenheit - 32)/ (9/5))
    return celsuis

def news():
    global links
    links = []
    news = []
    driver.get("https://www.forbes.com/?sh=43e5cbfe2254")
    agree = wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "trustarc-agree-btn")))
    agree.click()
    stories = wait.until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME,"body--dense-merriweather")))
    for i in range(3):
        #link = stories[i].get_attribute('href')
        news.append(stories[i].text)
        #links.append(link)
    return(news)
def btc():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    response_json = response.json()
    rate = float(response_json["bpi"]["EUR"]["rate_float"])
    my_money = 0.01189404 + 0.00298343
    my_money = round(rate * my_money, 2)
    rate = str(round(rate, 2))
    return "€" + rate + "\n \n " + "€" + str(my_money) 

    

def icloud():
    sentence = ""
    es = events(url="webcal://p65-caldav.icloud.com/published/2/MTc1NTUwNDcyMzE3NTU1MIlWSz4EvoYPW425i3rzk4W1cefZ14LIwtcNYllAipAB", fix_apple=True)
    for i in range(4):
        sentence = sentence + "\n \n" + str(es[i]).split(":")[-1]
    return sentence



def quit():
    driver.quit()
