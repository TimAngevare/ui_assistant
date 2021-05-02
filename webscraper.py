from bs4 import BeautifulSoup
from icalevents.icalevents import events
import requests
import random 
#pip3 install icalevents
api_key = "9a6997a12c32dc59721b12ec5be63131"
url_weather = "https://api.openweathermap.org/data/2.5/weather?q=Amersfoort&units=metric&appid="

def weather():
    link = requests.get(url_weather + api_key)
    response = link.json()
    temp = response['main']['temp']
    return int(temp)

def get_news():
    global links
    global news
    links = []
    news = []
    link = requests.get("https://nos.nl/")
    soup = BeautifulSoup(link.content, 'html.parser')
    stories =  soup.find_all("h2", {'class' : "e48nto-2 jgcOpr"})
    for i in range(2):
        #link = stories[i].get_attribute('href')
        if len(stories[i].string) < 70:
            news.append(stories[i].string)
        else:
            pass
    link = soup.find_all("a", {'class': "sc-1kyc94c-3 NaOUj"})
    for i in range(2):
        links.append(link[i]['href'])
    link = requests.get("https://www.publish0x.com/popular")
    soup = BeautifulSoup(link.content, 'html.parser')
    article = soup.find_all("p", {'class' : "pr-2 pt-2"})
    for i in range(2):
        print(article[i].findChild().text)
        news.append(article[i].findChild().text)
        links.append(article[i].findChild()['href'])

    link = requests.get("https://www.bellingcat.com/")
    soup = BeautifulSoup(link.content, 'html.parser')
    article = soup.find_all('div', {'class' : 'grid_item__content--title'})
    for i in range(2):
        title = article[i].findChild().findChild().text
        news.append(title)
        links.append(article[i].findChild().findChild()['href'])
    random_news = []
    x = 0
    while x <= 2:
        num = random.randint(0,len(news) - 1)
        print(num)
        random_news.append(news[num])
        news.pop(num)
        x += 1
    print(news)
    print(random_news)
    return random_news

def return_links():
    bot_links = {links[i] : news[i] for i in range(len(links))}
    return bot_links

def btc():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        response = requests.get(url)
        response_json = response.json()
        rate = float(response_json["bpi"]["EUR"]["rate_float"])
        my_money = 0.01790922 + 0.00298343
        my_money = round(rate * my_money, 2)
        rate = str(round(rate, 2))
        return "Rate:" + '\n€' + rate + "\n " + "Holdings: \n€" + str(my_money)
    except:
        return "could not \nreturn price"
 

def icloud():
    sentence = ""
    es = events(url="webcal://p65-caldav.icloud.com/published/2/MTc1NTUwNDcyMzE3NTU1MIlWSz4EvoYPW425i3rzk4W1cefZ14LIwtcNYllAipAB", fix_apple=True)
    for i in range(3):
        try:
            event = str(es[i]).replace(')','\n').replace('(','\n')
            sentence = sentence + "\n" + str(event).split(":")[-1]
        except:
            pass
    return sentence
