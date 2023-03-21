#Python V 3.10.4
import json
import os
import getpass
import subprocess as sp
import sys
from time import sleep

#Tries to import request, if not installed attempts to install via pip
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


#Tries to import art, if not installed attempts to install via pip
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

#Reading Apikey from environment variables
getapikey = os.environ.get("Abuse_APIKEY")



#Function responsible for Main Menu Art
def main():
    tprint("IP Lookup",font="block",chr_ignore=True)
    MainMenu()




def AbuseLookup():
    print("AbuseIPDB Lookup Script")
    url = "https://api.abuseipdb.com/api/v2/check"
    days = '180'
    IPAddr = input("Enter IP Address to check: ")


    querystring = {
    'ipAddress' : IPAddr,
    }

    headers = {
    'Accept': 'application/json',
    'key' : getapikey
    }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)

    if response.status_code == 200:
            decodedResponse = json.loads(response.text)

            print("   IP:          " + str(decodedResponse['data']['ipAddress']))
            print("   Reports:     " + str(decodedResponse['data']['totalReports']))
            print("   Abuse Score: " + str(decodedResponse['data']['abuseConfidenceScore']) + "%")
            print("   Last Report: " + str(decodedResponse['data']['lastReportedAt']))
            print (json.dumps(decodedResponse, sort_keys=True, indent=4))
    MainMenu()

def ClearMenu():
    os.system('cls')
    MainMenu()


def Exit():
    Question = input("Are you sure you want to exit? \n")
    Question = Question.upper()
    if (Question == "Y" ) or (Question == "YES"):
        os.system('cls')
        quit()
    else:
        MainMenu()

def MainMenu():
    print("\nMain Menu     Available Options shown below\n")
    print("OPTION 1: IP Lookup \n")
    print("OPTION 2: Report IP \n")
    print("OPTION 3: Remove Reported IP \n")
    print("OPTION 4: Clear Screen\n")
    print("OPTION 5: Home Menu  \n")
    print("OPTION 0: Quit the program\n")
    userOptions(input())

def ReportIP():
    category = []
    looptimes = int(input("How many categories would you like to add? \n"))
    for x in range(looptimes):
        print("OPTION 1: DNS Compromise      Altering DNS records resulting in improper redirection \n")
        print("OPTION 2: DNS Poisoining      Falsifying domain server cache (cache poisoning) \n")
        print("OPTION 3: Fraud Orders        Fraudulent orders \n")
        print("OPTION 4: DDoS Attack         Participating in distributed denial-of-service (usually part of botnet) \n")
        print("OPTION 5: FTP Brute-Force \n")
        print("OPTION 6: Ping of Death       Oversized IP packet \n")
        print("OPTION 7: Phishing            Phishing websites and/or email  \n")
        print("OPTION 8: Fraud VoIP \n")
        print("OPTION 9: Open Proxy          Open proxy, open relay, or Tor exit node \n")
        print("OPTION 10: Web Spam           Comment/forum spam, HTTP referer spam, or other CMS spam \n")
        print("OPTION 11: Email Spam         Spam email content, infected attachments, and phishing emails. Note: Limit comments to only relevent information (instead of log dumps) and be sure to remove PII if you want to remain anonymous.  \n")
        print("OPTION 12: Blog Spam          CMS blog comment spam  \n")
        print("OPTION 13: VPN IP             Conjunctive category   \n")
        print("OPTION 14: Port Scan          Scanning for open ports and vulnerable services   \n")
        print("OPTION 15: Hacking \n")
        print("OPTION 16: SQL Injection      Attempts at SQL injection   \n")
        print("OPTION 17: Spoofing           Email sender spoofing    \n")
        print("OPTION 18: Brute-Force        Credential brute-force attacks on webpage logins and services like SSH, FTP, SIP, SMTP, RDP, etc. This category is seperate from DDoS attacks.     \n")
        print("OPTION 19: Bad Web Bot        Webpage scraping (for email addresses, content, etc) and crawlers that do not honor robots.txt. Excessive requests and user agent spoofing can also be reported here.    \n")
        print("OPTION 20: Exploited Host     Host is likely infected with malware and being used for other attacks or to host malicious content. The host owner may not be aware of the compromise. This category is often used in combination with other attack categories.     \n")
        print("OPTION 21: Web App Attack     Attempts to probe for or exploit installed web applications such as a CMS like WordPress/Drupal, e-commerce solutions, forum software, phpMyAdmin and various other software plugins/solutions.     \n")
        print("OPTION 22: SSH                Secure Shell (SSH) abuse. Use this category in combination with more specific categories    \n")
        print("OPTION 23: IoT Targeted        Abuse was targeted at an 'Internet of Things' type device. Include information about what type of device was targeted in the comments    \n")
        print("OPTION 0: Main Menu \n")
        option = int(input("category num: \n"))
        if option == 0:
            MainMenu()
        elif option not in category:
            category.append(option)
        else: print("Error Category already present!")
    values = ', '.join(str(v) for v in category)
    url = "https://api.abuseipdb.com/api/v2/report"

    
    IPAddr = input("Enter IP Address to Report: ")
    
    commentquery = input("Would you like to add a comment? (Y/N) \n")
    commentquery = commentquery.upper()
    if (commentquery == "Y" ) or (commentquery == "YES"):
        ReportIpComment = input("Enter Comment: ")
        params = {
            'ip': IPAddr,
            'categories': values,
            'comment': ReportIpComment
                }

        headers = {
            'Accept': 'application/json',
            'Key': getapikey
                }

        response = requests.request(method='POST', url=url, headers=headers, params=params)
    
        decodedResponse = json.loads(response.text)
        print (json.dumps(decodedResponse, sort_keys=True, indent=4))
        MainMenu()
        
    if (commentquery == "N") or (commentquery == "No"):
        print("No comment added, proceeding......")
        params = {
            'ip': IPAddr,
            'categories': values,
                }

        headers = {
            'Accept': 'application/json',
            'Key': getapikey
                }

        response = requests.request(method='POST', url=url, headers=headers, params=params)
    
        decodedResponse = json.loads(response.text)
        print (json.dumps(decodedResponse, sort_keys=True, indent=4))
        MainMenu()

    else:
        print("Invalid Input returning to start.... \n")
        ReportCategories()
        
def ClearAddress():
    
    IPaddressrem = input("Enter IP Address you would like to remove from reported IP: \n")

    url = 'https://api.abuseipdb.com/api/v2/clear-address'
    querystring = {
            'ipAddress': IPaddressrem,
                  }

    headers = {
            'Accept': 'application/json',
            'Key': getapikey
            }

    response = requests.request(method='DELETE', url=url, headers=headers, params=querystring)
    decodedResponse = json.loads(response.text)
    print(json.dumps(decodedResponse, sort_keys=True, indent=4))
    MainMenu()

    
def userOptions(options):

    if (options == "1"):
        AbuseLookup()
    elif (options == "2"):
        ReportIP()
    elif (options == "3"):
        ClearAddress()
    elif (options == "4"):
        ClearMenu()
    elif (options == "5"):
        MainMenu()
    elif (options == "0"):
        Exit()

main()
