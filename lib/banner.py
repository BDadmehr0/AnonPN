from colorama import Fore as color
from colorama import Style as font
from requests import get as g

ss

def home():
    v = g('https://raw.githubusercontent.com/BDadmehr0/AnonPN/main/lib/version').text
    ascii_banner = color.WHITE+f'''
   ___                  ___  _  __
  / _ | ___  ___  ___  / _ \/ |/ /  |{color.GREEN} AnonPN{font.BRIGHT} {v}{font.NORMAL}{color.WHITE}
 / __ |/ _ \/ _ \/ _ \/ ___/    /   |{color.WHITE} get last phone number fake anonymsms.com{color.WHITE}
/_/ |_/_//_/\___/_//_/_/  /_/|_/    |{color.CYAN} https://github.com/BDadmehr0/AnonPN\n'''
    
    return ascii_banner

def simcart_panel(p, r, c):
    ascii_simcart = f'\n[{color.CYAN}{font.BRIGHT}Number{font.NORMAL}{color.WHITE}]{color.GREEN} {p}\n[{color.CYAN}{font.BRIGHT}Used{font.NORMAL}{color.WHITE}]{color.GREEN} {r}\n[{color.CYAN}{font.BRIGHT}Cuntry{font.NORMAL}{color.WHITE}]{color.GREEN} {c}\n'
    return ascii_simcart
