import os
import time
import pyfiglet
from colorama import Fore
import phonenumbers     
from phonenumbers import geocoder 
from phonenumbers import carrier
from phonenumbers import timezone
from datetime import datetime

#def. variables
l = "------------------"
t = time.sleep

result = pyfiglet.figlet_format("PhoneDNS")
print(result)

print(l)
print(f"{Fore.WHITE}[ {Fore.CYAN}\u00A7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX}PhoneDNS {Fore.WHITE}Codex-ops{Fore.LIGHTBLACK_EX} | Licensed under {Fore.WHITE}MIT {Fore.LIGHTBLACK_EX}License")
t(0.3)
print(f"{Fore.WHITE}[ {Fore.CYAN}\u00A7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Original creator: {Fore.WHITE}https://github.com/Codex-ops")
t(0.3)
print(f"{Fore.WHITE}[ {Fore.CYAN}\u00A7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Creator of this version : {Fore.WHITE}https://github.com/Codex-ops")
t(0.3)
t(2)

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
t(2)

number = input("Enter number: ")
t(1)

#See if the numbers valid 
ch_nmber = phonenumbers.parse(number)
print(phonenumbers.is_possible_number(ch_nmber))
print(l)
t(0.5)

#Find their state
ch_nmber = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_nmber, "en"))
print(l)
t(0.5)

#Find their carrier (Still in Development)
ch_nmber = phonenumbers.parse(number, "CH")
carrier.name_for_number(ch_nmber, "en")
print(l)
t(0.5)

#Find their time zone 
ch_nmber = phonenumbers.parse(number)
print(timezone.time_zones_for_number(ch_nmber))
print(l)
t(0.5)
result = pyfiglet.figlet_format("PhoneDNS")
print(result)
print(l)

os.system('python osint.py')

os.system('python Osint2.py')

service_nmber = phonenumbers.parse(number, "CH")
