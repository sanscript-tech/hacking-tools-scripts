#Imports and dependencies
import requests
import json

def get_repo_info():
  name = input("Enter the Github username of the owner of the repository ")
  repo = input("Enter the name of the repository ")
  
  #This is the API endpoint used to obtain information about a repository
  try:
    size_URL = "https://api.github.com/repos/" + name + "/" + repo
    response_1 = requests.get(size_URL)
    contributors_URL = "https://api.github.com/repos/" + name +"/" + repo + "/contributors" 
    response_2 = requests.get(contributors_URL)
    size_ = json.loads(response_1.text)
    contributors_ = json.loads(response_2.text)
    info = "The size of the repository is " + str(size_["size"]) + " Kilobytes. \n " +  "Number of contributors are " + str(len(contributors_))
    return(info)
 except:
    return("Invalid Repository")

if __name__ == "__main__":
  print(get_repo_info())
