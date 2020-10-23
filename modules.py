import requests
from bs4 import BeautifulSoup
import smtplib
import time
from __main__ import *

urlhepsiburada = "https://www.hepsiburada.com/product-url"
urltrendyol = "https://www.trendyol.com/apple/product-url"  
headers = {"User-Agent" : 'paste your user agent'}
sendermail = "sender email"
password = "app password"
gettermail = "getter email"

class Hepsiburada():
   
    def __init__(self, urlhepsiburada, headers, sendermail, password, gettermail):
        self.urlhepsiburada = urlhepsiburada
        self.header = headers
        self.sendermail = sendermail
        self.password = password
        self.gettermail = gettermail
        
        


    def kontrol(self):
        page = requests.get(urlhepsiburada, headers=headers)

        soup = BeautifulSoup(page.content, "html.parser")
        #print(soup.prettify())
        title = soup.find(id="detail-container").get_text()
        #print(title)
        price = soup.find(id="offering-price").get_text()
        #print(price)
        c_price = price = float(price[0:4])
        #set your price
        if float(c_price) > 1.000:
            self.send_mail()
        
    def send_mail(self):
        server = smtplib.SMTP('smtp.gmail.com', 587) 
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(sendermail, password)

        sub = "Price dropped\n"
        body = "Check your item \n {}".format(urlhepsiburada)
        msg = f"Subject: {sub}\n\n{body}"
        server.sendmail(
            sendermail,
            gettermail,
            msg.encode("utf-8")
        )
        print("Sent")
        server.quit()    
                    

class TrendYol():
    def __init__(self, urltrendyol, headers, sendermail, password, gettermail):
        self.urltrendyol = urltrendyol
        self.headers = headers
        self.sendermail = sendermail
        self.password = password
        self.gettermail = gettermail
    def kontrol(self):
        page = requests.get(urltrendyol, headers=headers)

        soup = BeautifulSoup(page.content, "html.parser")
        #print(soup.prettify())
        title = soup.find("div", attrs={"class": "pr-in-cn"}).get_text()
        c_title = title[0:25]
        #print(c_title)
        price = soup.find("span", attrs={"class": "prc-dsc"}).get_text()
        c_price = price[0:5]
        
        #set your price
        if float(c_price) > 1.000:
            
            self.send_mail()
            
            
               
    
    def send_mail(self):
        server = smtplib.SMTP('smtp.gmail.com', 587) 
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(sendermail, password)

        sub = "Price dropped\n"
        body = "Check your item \n {}".format(urltrendyol)
        msg = f"Subject: {sub}\n\n{body}"
        server.sendmail(
            sendermail,
            gettermail,
            msg.encode("utf-8")
        )
        print("sent")
        server.quit()    
                

