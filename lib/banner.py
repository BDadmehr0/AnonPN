from colorama import Fore as color
def home():
    ascii_banner = color.CYAN+'''
                                  ______  ______  
           /\                    (_____ \|  ___ \ 
          /  \  ____   ___  ____  _____) ) |   | |
         / /\ \|  _ \ / _ \|  _ \|  ____/| |   | |
        | |__| | | | | |_| | | | | |     | |   | |
        |______|_| |_|\___/|_| |_|_|     |_|   |_|\n'''
    
    ascii_menu = color.WHITE+'''\t[1] Start\t[0] Exit'''

def start_panel():
    
    ascii_menu = color.WHITE+'''\t[1] Recive last sms\t[0] Exit'''