import os
try:
    import colorama
except:
    os.system("pip install colorama")

colorama.init(autoreset=True)
from colorama import init, Fore
init()
n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [lg, r, w, cy, ye]

try:
    import telethon
    os.system("pip install -U telethon")
except:
    os.system("pip install telethon")

os.system("pip install requests")
os.system("pip install python-cfonts")

os.system("cls" if os.name=='nt' else 'clear')

print ('All Packages Installed Sucessfully')

script_made_by_Legend_dev = input()