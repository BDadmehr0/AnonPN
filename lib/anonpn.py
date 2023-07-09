import requests
from bs4 import BeautifulSoup
from lxml import etree

def exct_added():
    # sms Received
    response = requests.get('https://anonymsms.com/')
    html = response.text
    soup = BeautifulSoup(html, 'lxml')

    # Convert BeautifulSoup object to lxml etree object
    tree = etree.HTML(str(soup))

    # Use XPath to select elements
    elements = tree.xpath('/html/body/main/section[4]/div/div[1]/div[1]/div[2]/div[3]/p[2]')

    for element in elements:
        return element.text

def exct_recvied():
    # sms Received
    page = requests.get("https://anonymsms.com/")
    soup = BeautifulSoup(page.content,"html.parser")
    recived = str(soup.find("div",{"class":"sms-card__item"}).text.replace("\n","").strip())
    recived = recived[11:]

    return recived

def exct_cuntry():
    # phone number cuntry
    page = requests.get("https://anonymsms.com/")
    soup = BeautifulSoup(page.content,"html.parser")
    cunt = str(soup.find("a",{"class":"sms-card__header"}).text.replace("\n","").strip())

    return cunt

def exct_phonecart():
    # Phone number
    page = requests.get("https://anonymsms.com/")
    soup = BeautifulSoup(page.content,"html.parser")
    phone = str(soup.find("div",{"class":"sms-card__number"}).text.replace("\n","").replace('content_copy','').replace(' ', '').strip())
    phone = phone[1:]

    return phone

def recive_sms(phone):
    URL = f'https://anonymsms.com/number/{phone}/'
    page = requests.get(URL)

    #Fetch webpage
    soup = BeautifulSoup(page.content,"html.parser")

    #Scraping Data
    phone = str(soup.find("td",{"class":"table-panel__message"}).text.replace("\n","").strip())
    phone = phone[1:]
    return phone

s = exct_added()
print(s)