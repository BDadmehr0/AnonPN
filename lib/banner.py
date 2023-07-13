from colorama import Fore as color
from colorama import Style as font
from requests import get as g
class colors:


'''Colors class:reset all colors with colors.reset; two
sub classes fg for foreground
and bg for background; use as colors.subclass.colorname.
i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
underline, reverse, strike through,
and invisible work with the main class i.e. colors.bold'''
reset = '\033[0m'
bold = '\033[01m'
disable = '\033[02m'
underline = '\033[04m'
reverse = '\033[07m'
strikethrough = '\033[09m'
invisible = '\033[08m'

class fg:
		black = '\033[30m'
		red = '\033[31m'
		green = '\033[32m'
		orange = '\033[33m'
		blue = '\033[34m'
		purple = '\033[35m'
		cyan = '\033[36m'
		lightgrey = '\033[37m'
		darkgrey = '\033[90m'
		lightred = '\033[91m'
		lightgreen = '\033[92m'
		yellow = '\033[93m'
		lightblue = '\033[94m'
		pink = '\033[95m'
		lightcyan = '\033[96m'

	class bg:
		black = '\033[40m'
		red = '\033[41m'
		green = '\033[42m'
		orange = '\033[43m'
		blue = '\033[44m'
		purple = '\033[45m'
		cyan = '\033[46m'
		lightgrey = '\033[47m'

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
