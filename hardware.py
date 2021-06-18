from time import sleep
import webscraper
import smtplib, ssl

def send_mail():
    port = 465
    password = "Tim1452003"
    context = ssl.create_default_context()
    mail_reciever = "timangevare2003@gmail.com"
    mail = "dutchtim14@gmail.com"
    message = "Subject: Your links \n"
    links = webscraper.return_links()
    for key in links:
        message = message + links[key] + ": " + key + "\n"
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(mail,  password)
        server.sendmail(mail, mail_reciever, message)
    sleep(1)