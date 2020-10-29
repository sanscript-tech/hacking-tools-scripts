import requests
from bs4 import BeautifulSoup as BS

# We are basically getting the URL of coinmarket camp and scraping it's content
soup = BS(requests.get('https://coinmarketcap.com/currencies/bitcoin/').content, features="lxml")

# Here we are searching for the corresponding div in which span class is present
# then we need to extract the span class
div = soup.find("div", {"class" : "f6l7tu-0 cdygDb cmc-details-panel-price"
}).find("span", {"class" : "cmc-details-panel-price__price"})

# Now we print all elements extracted from div
for i in div:
    print(i)
