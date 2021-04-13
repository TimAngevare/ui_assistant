from bs4 import BeautifulSoup
from time import sleep
from icalevents.icalevents import events
import requests
#pip3 install icalevents

def weather():
    link = requests.get("https://weather.com/weather/today/l/57fae565d25f68b70131cd8683da28e8b595fb41ae07ae5cd2a827af58233bac")
    soup = BeautifulSoup(link.content, 'html.parser')
    sleep(4)
    temp = soup.find("span", {"class" : "CurrentConditions--tempValue--3KcTQ"}).string
    farenheit = int(temp[0:-1])
    celsuis = int((farenheit - 32)/ (9/5))
    return celsuis

def news():
    global links
    links = []
    news = []
    link = requests.get("https://nos.nl/")
    soup = BeautifulSoup(link.content, 'html.parser')
    stories =  soup.find_all("h2", {'class' : "title_2P9RJtrp"})
    for i in range(2):
        #link = stories[i].get_attribute('href')
        news.append(stories[i].string)
        #links.append(link)
    link = requests.get("https://www.publish0x.com/popular")
    soup = BeautifulSoup(link.content, 'html.parser')
    article = soup.find_all("p", {'class' : "pr-2 pt-2"})
    for i in range(2):
        news.append(article[i].findChild().text)

    print(news)
    return(news)

def btc():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    response_json = response.json()
    rate = float(response_json["bpi"]["EUR"]["rate_float"])
    my_money = 0.01189404 + 0.00298343
    my_money = round(rate * my_money, 2)
    rate = str(round(rate, 2))
    return "BTC rate: €" + rate + "\n \n " + "My holdings: €" + str(my_money) 
 

def icloud():
    sentence = ""
    es = events(url="webcal://p65-caldav.icloud.com/published/2/MTc1NTUwNDcyMzE3NTU1MIlWSz4EvoYPW425i3rzk4W1cefZ14LIwtcNYllAipAB", fix_apple=True)
    for i in range(4):
        sentence = sentence + "\n \n" + str(es[i]).split(":")[-1]
    return sentence
