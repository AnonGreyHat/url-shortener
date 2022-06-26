import pyshorteners
import pyfiglet
import colorama
from colorama import Fore
res = pyfiglet.figlet_format("shortener")
print(Fore.GREEN,res)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(Fore.RED+"                        URL SHORTENER         "+Fore.GREEN)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("""
[+]Author: AnonGreyHat Pro Cracker
[+]Team: Dark Exploit Hacker
[+]Github: https://github.com/anongreyhat
[+]Whatsapp: +2349042794223
""")
print(Fore.YELLOW+"                   Turn on Mobile data on"+Fore.GREEN)
url = input("Enter your url: ")
s = pyshorteners.Shortener().tinyurl.short(url)
print("short link -->", s)
