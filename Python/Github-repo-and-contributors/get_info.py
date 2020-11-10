import requests
import json

name = input("Enter the name of the owner of the repository ")
repo = input("Enter the name of the repository ")
size_URL = "https://api.github.com/repos/" + name + "/" + repo
response = requests.get(size_URL)
co = requests.get("https://api.github.com/repos/" + name +"/" + repo + "/contributors")
co = json.loads(co.text)
r = response.text
r = json.loads(r)
print("The size of the repository is" ,r["size"], "Kilobytes.")
print("Number of contributors are", len(co))
