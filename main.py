import requests
import platform
from colorama import Fore as color
from colorama import Style as font
from os import system as T

from lib.banner import home
from lib.anonpn import *

c = 0
_ = home()
com_username = platform.node()

def clear():
    try:
        T('clear')
    except:
        T('cls')

if __name__ == "__main__":

    print(_)
    print(f'{color.WHITE}[{color.CYAN}{font.BRIGHT}1{color.WHITE}{font.NORMAL}]{color.GREEN}{font.BRIGHT} Start {font.NORMAL}{color.WHITE}[{color.CYAN}{font.BRIGHT}0{color.WHITE}{font.NORMAL}] {font.BRIGHT}{color.RED}Exit\n{font.NORMAL}')
    while True:
        c += 1
        home_i = input(f'— {color.YELLOW}{com_username}{color.WHITE}@{color.GREEN}anonpn{color.YELLOW} ~{color.BLACK} $ {color.WHITE}')
        if c == 15:
            print("\nI feel that you don't know how to work with this script or you are trying to enter")
            c = 0
        
        if home_i == '1':
            clear()
            #Recive last sms
            print(_)
            print(f'{color.WHITE}[{color.CYAN}{font.BRIGHT}1{color.WHITE}{font.NORMAL}]{color.GREEN}{font.BRIGHT} Get Phone Number {font.NORMAL}{color.WHITE}[{color.CYAN}{font.BRIGHT}0{color.WHITE}{font.NORMAL}] {font.BRIGHT}{color.RED}Exit\n{font.NORMAL}')
            
            try:
                menu_i = input(f'— {color.YELLOW}{com_username}{color.WHITE}@{color.GREEN}menu{color.YELLOW} ~{color.BLACK} $ {color.WHITE}')
                if menu_i == '1':
                    phone = exct_phonecart()
                elif home_i == '0':
                    print('Bye Bye')
                    exit()
            except KeyError:

    # lastsms = recive_sms(phone=phone)
    # print(phone, lastsms)
