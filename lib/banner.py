from colorama import Fore as color
from colorama import Style as font
from requests import get as g

''''Regular Colors
Value	Color
\e[0;30m	Black
\e[0;31m	Red
\e[0;32m	Green
\e[0;33m	Yellow
\e[0;34m	Blue
\e[0;35m	Purple
\e[0;36m	Cyan
\e[0;37m	White
Bold
Value	Color
\e[1;30m	Black
\e[1;31m	Red
\e[1;32m	Green
\e[1;33m	Yellow
\e[1;34m	Blue
\e[1;35m	Purple
\e[1;36m	Cyan
\e[1;37m	White''''

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
