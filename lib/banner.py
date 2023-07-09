from colorama import Fore as color
def home():
    ascii_banner = color.CYAN+'''
   ___                  ___  _  __
  / _ | ___  ___  ___  / _ \/ |/ /  | AnonPN 1.0.0
 / __ |/ _ \/ _ \/ _ \/ ___/    /   | get last phone number fake anonymsms.com..
/_/ |_/_//_/\___/_//_/_/  /_/|_/    | https://github.com/BDadmehr0/AnonPN
                                  \n'''
    
    ascii_menu = color.WHITE+'''\t[1] Start\t[0] Exit'''

    return ascii_banner

def start_panel():
    
    ascii_menu = color.WHITE+'''\t[1] Recive last sms\t[0] Exit'''

    return ascii_menu