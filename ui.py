import tkinter as tk
from tkinter import Label, font
from tkinter.constants import ANCHOR
from typing import Text
import webscraper
import hardware
from PIL import Image, ImageTk
from time import sleep
from random import randint
from datetime import datetime
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

HEIGHT = 600
WIDTH = 1024
yellow = "#595959"
##000000
gray = "#ffffff"

root = tk.Tk()
root.title("GUI Assistant")

def button_pressed(channel):
    hardware.send_mail()

def wrap_by_word(s, n):
    a = s.split()
    ret = ''
    for i in range(0, len(a), n):
        ret += ' '.join(a[i:i+n]) + '\n'

    return ret

def quotes():
    file = open("/home/pi/Desktop/ui_assistant/quotes.txt", "r")
    quotes = file.readlines()
    line = quotes[randint(0, len(quotes) - 1)]
    return wrap_by_word(line, 12)
    

global image
webscraper.get_pic()
i = Image.open("backgroundpic.jpg")
i.thumbnail((2000, 1000))

image = ImageTk.PhotoImage( i , master=root)
my_label = Label(root, image=image )
my_label.place(x=0, y=0, relheight=1,relwidth=1)    

#canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
#canvas.pack()

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(10, GPIO.RISING, callback=button_pressed)

top = tk.Frame(root, bg=yellow)
top.place(relheight=0.2, relwidth=0.95, rely=0.025, relx=0.025)

quote = tk.Label(top,  fg=gray, text=quotes(), bg=yellow, font=("Pacifico", 20))
quote.place(relheight=0.8, relwidth=0.9, relx=0.05, rely=0.1)

temp_holder = tk.Frame(root, bg=yellow)
temp_holder.place(relheight=0.25, relwidth=0.2, rely=0.275, relx=0.025)

temp = tk.Label(temp_holder, fg=gray, text="temp", font=("Impact", 18), bg=yellow)
temp.place(relheight=0.8, relwidth=0.9, relx=0.05, rely=0.1)

btc_holder = tk.Frame(root, bg=yellow)
btc_holder.place(relheight=0.325, relwidth=0.2, rely=0.55, relx=0.025)
btc = tk.Label(btc_holder, fg=gray, text="btc", font=("Impact", 18), bg=yellow)
btc.place(relheight=0.8, relwidth=0.9, relx=0.05, rely=0.1)

icloud_holder = tk.Frame(root, bg=yellow)
icloud_holder.place(relheight=0.40, relwidth=0.33, rely=0.275, relx=0.25)
calender = tk.Label(icloud_holder, text= 'calender' ,fg=gray,  font=("Impact", 18), bg=yellow)
calender.place(relheight=0.99, relwidth=0.99, relx=0.005, rely=0.005)

time_holder = tk.Frame(root, bg=yellow)
time_holder.place(relheight=0.275, relwidth=0.33, rely=0.7, relx=0.25)
time = tk.Label(time_holder, text="time", fg=gray, font=("Impact", 70), bg=yellow)
time.place(relheight=0.99, relwidth=0.99, relx=0.005, rely=0.005)

news_holder = tk.Frame(root, bg=yellow)
news_holder.place(relheight=0.7, relwidth=0.375, relx=0.605 , rely=0.275)

news = tk.Label(news_holder, fg=gray, bg=yellow, font=('impact',18), text='news')
news.place(relheight=0.95, relwidth=0.9, relx=0.05, rely=0.025)

def update_news():
    nieuws = webscraper.get_news()
    verhalen = []
    for x in range(len(nieuws)):
        verhalen.append(wrap_by_word(nieuws[x], 3))
    nieuws_string = " \n ".join(verhalen)
    news.config(text=nieuws_string)

update_news()

def update():
    temp.config(text = "Room \n Outside: " + str(webscraper.weather()) + "??")
    btc.config(text = webscraper.btc())
    date = datetime.now()
    try:
        calender.config(text = webscraper.icloud())
    except:
        calender.config(text = "Couldn't reach your calender")
    if int(date.strftime("%M")) % 29 == 0:
        try:
            update_news()
        except:
            sleep(120)
            print('news update failed')
            update_news()
    time.config(text=date.strftime("%H:%M"))
    root.after(30000, update)

root.after(30000, update)
root.attributes("-fullscreen", True)
root.mainloop()
