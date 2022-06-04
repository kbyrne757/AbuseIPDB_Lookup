#Python V 3.10.0
import json
import os
import getpass
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


def main():
    tprint("IP Lookup",font="block",chr_ignore=True)
    MainMenu()
apikeyfile = ("C:\\Users\\" + getUser() + "\\Documents\\abuseipdblookupapikey.txt")
def ApiKey():
    apikey = input("Enter your AbuseIPDB API Key: ")
    
    with open(apikeyfile, 'w') as f:
        f.writelines(apikey)
    print("API KEY written to " + apikeyfile)



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

    


def MainMenu():
    print("\nMain Menu     Available Options shown below\n")
    print("OPTION 1: Add API Key\n")
    print("OPTION 2: IP Lookup \n")
    print("OPTION 3: Clear Screen\n")
    print("OPTION 4: Home Menu  \n")
    print("OPTION 0: Quit the program\n")
    userOptions(input())


def userOptions(options):

    if (options == "1"):
        ApiKey()
    elif (options == "2"):
        AbuseLookup()
    elif (options == "3"):
        print(test)
    elif (options == "4"):
        print(test)
    elif (options == "0"):
        print(test) 

main()
