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
def send_mail():
    links = webscraper.return_links()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(mail,  password)
        server.send(mail, mail_reciever, message + links)
    sleep(1)