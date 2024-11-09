import requests
from bs4 import BeautifulSoup
from lxml import etree

def exct_added(): # TODO: Fix exct added time 
    # sms Received
    try:
        page = requests.get("https://anonymsms.com/")
    except requests.exceptions.ConnectionError:
        print('ConnectionError: check your netowrk connection and try again')
    html = page.text
    soup = BeautifulSoup(html, 'lxml')

    # Convert BeautifulSoup object to lxml etree object
    tree = etree.HTML(str(soup))

    # Use XPath to select elements
    elements = tree.xpath('/html/body/main/section[4]/div/div[1]/div[1]/div[2]/div[3]/p[2]')

    for element in elements:
        hour = str(element.text.replace("\n","").strip())
        return hour

def exct_received():
    # sms Received
    try:
        page = requests.get("https://anonymsms.com/")
        soup = BeautifulSoup(page.content,"html.parser")
        recived = str(soup.find("div",{"class":"sms-card__item"}).text.replace("\n","").strip())
        recived = recived[11:]

        return recived
    except requests.exceptions.ConnectionError:
        print('ConnectionError: check your netowrk connection and try again')

def exct_country():
    # phone number country code
    try:
        page = requests.get("https://anonymsms.com/")
        soup = BeautifulSoup(page.content,"html.parser")
        cunt = str(soup.find("a",{"class":"sms-card__header"}).text.replace("\n","").strip())

        return cunt
    except requests.exceptions.ConnectionError:
        print('ConnectionError: check your netowrk connection and try again')

def exct_phonecart():
    # Phone number
    try:
        page = requests.get("https://anonymsms.com/")
        soup = BeautifulSoup(page.content,"html.parser")
        phone = str(soup.find("div",{"class":"sms-card__number"}).text.replace("\n","").replace('content_copy','').replace(' ', '').strip())
        phone = phone[1:]

        return phone
    except requests.exceptions.ConnectionError:
        print('ConnectionError: check your netowrk connection and try again')

def receive_sms(phone):
    try:
        page = requests.get(f'https://anonymsms.com/number/{phone}/')
        #Fetch webpage
        soup = BeautifulSoup(page.content,"html.parser")

        #Scraping Data
        phone = str(soup.find("td",{"class":"table-panel__message"}).text.replace("\n","").strip())
        phone = phone[1:]
        return phone
    except requests.exceptions.ConnectionError:
        print('ConnectionError: check your netowrk connection and try again')

