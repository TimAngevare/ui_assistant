from bs4 import BeautifulSoup
from time import sleep
from icalevents.icalevents import events
import requests
#pip3 install icalevents
api_key = "9a6997a12c32dc59721b12ec5be63131"
url_weather = "https://api.openweathermap.org/data/2.5/weather?q=Amersfoort&units=metric&appid="

def weather():
    link = requests.get(url_weather + api_key)
    response = link.json()
    temp = response['main']['temp']
    return int(temp)

def news():
    global links
    links = []
    news = []
    link = requests.get("https://nos.nl/")
    soup = BeautifulSoup(link.content, 'html.parser')
    stories =  soup.find_all("h2", {'class' : "title_2P9RJtrp"})
    for i in range(2):
        #link = stories[i].get_attribute('href')
        if len(stories[i].string) < 57:
            news.append(stories[i].string)
        else:
            pass
        #links.append(link)
    link = requests.get("https://www.publish0x.com/popular")
    soup = BeautifulSoup(link.content, 'html.parser')
    article = soup.find_all("p", {'class' : "pr-2 pt-2"})
    for i in range(2):
        news.append(article[i].findChild().text)
    return(news)

def btc():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    response_json = response.json()
    rate = float(response_json["bpi"]["EUR"]["rate_float"])
    my_money = 0.01189404 + 0.00298343
    my_money = round(rate * my_money, 2)
    rate = str(round(rate, 2))
    return "Rate:" + '\n€' + rate + "\n " + "Holdings: \n€" + str(my_money) 
 

def icloud():
    sentence = ""
    es = events(url="webcal://p65-caldav.icloud.com/published/2/MTc1NTUwNDcyMzE3NTU1MIlWSz4EvoYPW425i3rzk4W1cefZ14LIwtcNYllAipAB", fix_apple=True)
    for i in range(3):
        event = str(es[i]).replace(')','\n').replace('(','\n')
        sentence = sentence + "\n" + str(event).split(":")[-1]
    return sentence
