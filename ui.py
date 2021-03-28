import tkinter as tk
from tkinter import Label, font
from tkinter.constants import ANCHOR
from typing import Text
import webscraper
from PIL import Image, ImageTk
from time import sleep
from random import randint

HEIGHT = 700
WIDTH = 1024
yellow = "#595959"
##000000
gray = "#ffffff"

root = tk.Tk()
root.title("GUI Assistant")

def wrap_by_word(s, n):
    a = s.split()
    ret = ''
    for i in range(0, len(a), n):
        ret += ' '.join(a[i:i+n]) + '\n'

    return ret

def quotes():
    file = open("quotes.txt", "r")
    quotes = file.readlines()
    line = quotes[randint(0, len(quotes) - 1)]
    return wrap_by_word(line, 20)
    

def GUI():
    try:
        webscraper.quit()
        sleep(1)
    except:
        pass
    webscraper.start()
    global image
    i = Image.open("./backgrounds/" + str(randint(1,13)) + ".jpeg")
    i.thumbnail((2000, 1000))

    image = ImageTk.PhotoImage( i , master=root)
    my_label = Label(root, image=image )
    my_label.place(x=0, y=0, relheight=1,relwidth=1)    

    #canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    #canvas.pack()

    top = tk.Frame(root, bg=yellow)
    top.place(relheight=0.2, relwidth=0.95, rely=0.025, relx=0.025)

    quote = tk.Label(top,  fg=gray, text=quotes(), bg=yellow, font=("Pacifico", 22))
    quote.place(relheight=0.8, relwidth=0.9, relx=0.05, rely=0.1)

    temp_holder = tk.Frame(root, bg=yellow)
    temp_holder.place(relheight=0.25, relwidth=0.2, rely=0.275, relx=0.025)

    temp = tk.Label(temp_holder, fg=gray, text="Degrees room \n Degrees outside: " + str(webscraper.weather()), font=("Impact", 22), bg=yellow)
    temp.place(relheight=0.8, relwidth=0.9, relx=0.05, rely=0.1)

    btc_holder = tk.Frame(root, bg=yellow)
    btc_holder.place(relheight=0.25, relwidth=0.2, rely=0.55, relx=0.025)
    btc = tk.Label(btc_holder, fg=gray, text=webscraper.btc(), font=("Impact", 22), bg=yellow)
    btc.place(relheight=0.8, relwidth=0.9, relx=0.05, rely=0.1)

    icloud_holder = tk.Frame(root, bg=yellow)
    icloud_holder.place(relheight=0.40, relwidth=0.33, rely=0.275, relx=0.25)
    calender = tk.Label(icloud_holder, text=webscraper.icloud(),fg=gray,  font=("Impact", 22), bg=yellow)
    calender.place(relheight=0.99, relwidth=0.99, relx=0.005, rely=0.005)

    news_holder = tk.Frame(root, bg=yellow)
    news_holder.place(relheight=0.575, relwidth=0.25, relx=0.605 , rely=0.275)
    nieuws = webscraper.news()
    verhalen = []
    for x in range(len(nieuws)):
        verhalen.append(wrap_by_word(nieuws[x], 4))
    nieuws = " \n ".join(verhalen)

    news = tk.Label(news_holder, fg=gray, bg=yellow, font=('impact',18), text=nieuws)
    news.place(relheight=0.95, relwidth=0.9, relx=0.05, rely=0.025)

root.after(70000, GUI())
root.attributes("-fullscreen", True)
root.mainloop()
