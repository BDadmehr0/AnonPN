import requests
import platform
from bs4 import BeautifulSoup
from lxml import etree
from colorama import Fore as color
from colorama import Style as font

from lib.banner import *

_ = home()
com_username = platform.node()
def exct_phonecart():
    phone = ''
    try:
        #Request URL
        page = requests.get("https://anonymsms.com/")

        #Fetch webpage
        soup = BeautifulSoup(page.content,"html.parser")

        #Scraping Data
        phone = str(soup.find("div",{"class":"sms-card__number"}).text.replace("\n","").replace('content_copy','').replace(' ', '').strip())
        phone = phone[1:]
        return phone
    except requests.exceptions.ConnectionError:
        print('ConnectionError: Try Again')

def recive_sms(phone):
    URL = f'https://anonymsms.com/number/{phone}/'
    page = requests.get(URL)

    #Fetch webpage
    soup = BeautifulSoup(page.content,"html.parser")

    #Scraping Data
    phone = str(soup.find("td",{"class":"table-panel__message"}).text.replace("\n","").strip())
    phone = phone[1:]
    return phone

if __name__ == "__main__":

    print(_)
    ascii_menu = color.WHITE+'''\t[1] Start\t[0] Exit'''
    
    home_i = int(input(f'— {color.YELLOW}{com_username}{color.WHITE}@{color.GREEN}anonpn{color.YELLOW} ~{color.BLACK} $'))

    # phone = exct_phonecart()
    # lastsms = recive_sms(phone=phone)
    # print(phone, lastsms)