import RPi.GPIO as GPIO
from time import sleep
import webscraper
import smtplib, ssl

port = 465
password = "Tim1452003"
context = ssl.create_default_context()
mail_reciever = "timangevare2003@gmail.com"
mail = "dutchtim14@gmail.com"
message = """\
Subject: Your links



"""

GPIO.setwarnings(False)
GPIO.setmode(GPIO.board)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(12) == GPIO.HIGH:
        links = webscraper.return_links()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(mail,  password)
            server.send(mail, mail_reciever, message + links)
        sleep(1)