import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from colorama import Fore, init, Style
from progress.bar import ChargingBar
init(autoreset=True)
# Get all forms of the mentioned URL
def getAllForms(url):
    page = requests.get(url)
    parser = BeautifulSoup(page.content, 'html.parser')
    return parser.find_all('form')
f = open("payloads.txt", "r").readlines()
successful_payloads = []
def xss():
    forms = getAllForms(url)
    for form in forms:
        # Getting Payload Scripts for Payloads file
        bar = ChargingBar(Fore.GREEN + 'Injecting Scripts and finding XSS Vulnerability', max=36)
        for payload in f:
            bar.next()
            # Getting the URL where the form data will be sent
            action = form.attrs.get('action').lower()
            finalURL = urljoin(url, action)
            # Getting the Method through which form data will be sent (GET/POST)
            # By default, the method is GET
            method = form.attrs.get('method', 'get').lower()
            # Filling the Form with Random Data basically the script from Payloads
            randomData = {}
            for input in form.find_all('input'):
                if input['type'] == 'text' or input['type'] == 'search':
                    input['value'] = payload
                inputName = input.get('name')
                inputValue = input.get('value') 
                if inputName and inputValue:
                    randomData[inputName] = inputValue
            if method=='post':
                content = requests.post(finalURL, data=randomData)
            else:
                content = requests.get(finalURL, params=randomData)
            # Return True if Payload was successfully Injected
            if payload in content.text:
                successful_payloads.append(payload)
        bar.finish()
url = input(Fore.BLUE + "\nEnter the URL: ")
vulnerable = xss()
if len(successful_payloads):
    print(Fore.GREEN + "\nSite is vulnerable to XSS Attack!\n")
    for i in successful_payloads:
        print(Fore.CYAN + "Payload Injected Successfully --> " + Fore.YELLOW + i)
else:
	print(Fore.RED + Style.BRIGHT + "\nXSS Vulnerability not Present!")