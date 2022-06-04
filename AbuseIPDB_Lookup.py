#Python V 3.10.0
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

MainMenu()
