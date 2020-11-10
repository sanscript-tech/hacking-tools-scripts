import requests
import json

def get_repo_info():
  name = input("Enter the name of the owner of the repository ")
  repo = input("Enter the name of the repository ")
  size_URL = "https://api.github.com/repos/" + name + "/" + repo
  response_1 = requests.get(size_URL)
  contributors_URL = "https://api.github.com/repos/" + name +"/" + repo + "/contributors" 
  response_2 = requests.get(contributors_URL)
  size_ = json.loads(response_1.text)
  contributors_ = json.loads(response_2.text)
  info = "The size of the repository is " + str(size_["size"]) + " Kilobytes. \n " +  "Number of contributors are " + str(len(contributors_))
  return(info)

if __name__ == "__main__":
  get_repo_info()
