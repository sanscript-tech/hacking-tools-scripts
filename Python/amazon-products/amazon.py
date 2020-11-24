from bs4 import BeautifulSoup
import requests
kw = input("Please enter the keyword to search. For eg: phone, iron, guitar etc ")
url = "https://www.amazon.com/s?k=" + kw + "&ref=nb_sb_noss_2"
headers = {
# the user agent is different for every user. Type user agent in chrome browser and replace the below agent with yours
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip',
'DNT' : '1', # Do Not Track Request Header
'Connection' : 'close'
}


soup = BeautifulSoup(requests.get(url, headers=headers).text, 'lxml')
for count,div in enumerate(soup.select('div[data-asin]')):
    if int(count) <= 5:
        if count!=0:
            if div.select_one('.a-text-normal'):
                print(str(count) + str(div.select_one('.a-text-normal').text).rstrip())
            if div.select_one('.a-price'):
                print(div.select_one('.a-price ').get_text('|',strip=True).split('|')[0])
            print(str(div.find_all('span', {'class':'a-icon-alt'}))[26:29] + " stars")
            print("\n")
    else:
        break
