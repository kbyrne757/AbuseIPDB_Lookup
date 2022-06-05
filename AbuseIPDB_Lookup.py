#Python V 3.10.4
import json
import os
import getpass
import subprocess as sp
import sys
from time import sleep
try:
    import requests
except ModuleNotFoundError:
    package_name = "requests"
    print(package_name + " is not installed")
    print("Attempting install of " + package_name)
    sp.check_call([sys.executable, "-m", "pip", "install", package_name])
    sleep(0.5)
    import requests
    print("Import Succesful")

try:
    from art import *
except ModuleNotFoundError:
    package_name = "art"
    print(package_name + " is not installed")
    print("Attempting install of " + package_name)
    sp.check_call([sys.executable, "-m", "pip", "install", package_name])
    sleep(0.5)
    from art import *
    print("Import Succesful")



#function to acquire username for directory listing
def getUser():
    username = getpass.getuser()
    return username


apikeyfile = ("C:\\Users\\" + getUser() + "\\Documents\\abuseipdblookupapikey.txt")
    




def main():
    tprint("IP Lookup",font="block",chr_ignore=True)
    MainMenu()
def ApiKey():
    apikey = input("Enter your AbuseIPDB API Key: ")
    
    with open(apikeyfile, 'w') as f:
        f.writelines(apikey)
    print("API KEY written to " + apikeyfile)
    MainMenu()



def AbuseLookup():
    print("AbuseIPDB Lookup Script")
    url = "https://api.abuseipdb.com/api/v2/check"

    IPAddr = input("Enter IP Address to check: ")

    with open(apikeyfile) as f:
        APIKEY = f.read()

    querystring = {
    'ipAddress' : IPAddr,
    }

    headers = {
    'Accept': 'application/json',
    'key' : APIKEY
    }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)

    decodedResponse = json.loads(response.text)
    print (json.dumps(decodedResponse, sort_keys=True, indent=4))
    MainMenu()

    
def clearScreen():
    os.system('cls')

def ClearMenu():
    clearScreen()
    MainMenu()


def Exit():
    Question = input("Are you sure you want to exit? \n")
    Question = Question.upper()
    if (Question == "Y" ) or (Question == "YES"):
        clearScreen()
        quit()
    else:
        MainMenu()

def MainMenu():
    print("\nMain Menu     Available Options shown below\n")
    print("OPTION 1: Add API Key\n")
    print("OPTION 2: IP Lookup \n")
    print("OPTION 3: Report IP \n")
    print("OPTION 3: Clear Screen\n")
    print("OPTION 4: Home Menu  \n")
    print("OPTION 0: Quit the program\n")
    userOptions(input())

def ReportCategories():
    print("OPTION 1: DNS Compromise      Altering DNS records resulting in improper redirection \n")
    print("OPTION 2: DNS Poisoining      Falsifying domain server cache (cache poisoning) \n")
    print("OPTION 3: Clear Screen\n")
    print("OPTION 4: Home Menu  \n")
    print("OPTION 0: Quit the program\n")
    ReportIP(input())

def ReportIP(option):
    category = 0
    url = "https://api.abuseipdb.com/api/v2/report"

    with open(apikeyfile) as f:
        APIKEY = f.read()
    
    IPAddr = input("Enter IP Address to Report: ")
    
    if (option == "1"):
        category = 1
    elif (option == "2"):
        category = 2

    params = {
    'ip': IPAddr,
    'categories': category,
    }

    headers = {
    'Accept': 'application/json',
    'Key': APIKEY
    }

    response = requests.request(method='POST', url=url, headers=headers, params=params)
    
    decodedResponse = json.loads(response.text)
    print (json.dumps(decodedResponse, sort_keys=True, indent=4))


    
def userOptions(options):

    if (options == "1"):
        ApiKey()
    elif (options == "2"):
        AbuseLookup()
    elif (options == "3"):
        ReportCategories()
    elif (options == "3"):
        clearScreen()
    elif (options == "4"):
        MainMenu()
    elif (options == "0"):
        Exit()

main()
