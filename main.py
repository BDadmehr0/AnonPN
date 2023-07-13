import requests
import platform
from colorama import Fore as color
from colorama import Style as font
from os import system as T

from lib.banner import home , simcart_panel
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
    print(f'{color.WHITE}[{color.CYAN}{font.BRIGHT}1{color.WHITE}{font.NORMAL}]{color.GREEN}{font.BRIGHT} Fake phone number {font.NORMAL}{color.WHITE}[{color.CYAN}{font.BRIGHT}0{color.WHITE}{font.NORMAL}] {font.BRIGHT}{color.RED}Exit\n{font.NORMAL}')
    while True:
        c += 1

        try:
            menu_i = input(f'— {color.YELLOW}{com_username}{color.WHITE}@{color.GREEN}AnonPN{color.YELLOW} ~{color.BLACK} $ {color.WHITE}')
            if menu_i == '1':
                phone = exct_phonecart()
                recive = exct_recvied()
                cuntry = exct_cuntry()

                print(simcart_panel(p=phone, r=recive, c=cuntry))

            elif menu_i == '0':
                exit()
        except KeyboardInterrupt:
            exit()

        if c == 15:
            print("I feel that you don't know how to work with this script or you are trying to enter")
        elif c == 30:
            print('O_O Stop')
        
        
    # lastsms = recive_sms(phone=phone)
    # print(phone, lastsms)
