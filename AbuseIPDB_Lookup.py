#Python V 3.10.0
import json
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


apikey = input("Enter your AbuseIPDB API Key: ")



def MainMenu():
    print("AbuseIPDB Lookup Script")
    url = "https://api.abuseipdb.com/api/v2/check"

    IPAddr = input("Enter IP Address to check: ")

    querystring = {
    'ipAddress' : IPAddr,
    }

    headers = {
    'Accept': 'application/json',
    'key' : apikey
    }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)

    decodedResponse = json.loads(response.text)
    print (json.dumps(decodedResponse, sort_keys=True, indent=4))

MainMenu()
