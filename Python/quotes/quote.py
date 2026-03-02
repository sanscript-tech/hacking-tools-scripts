import requests
from json import loads
# makijng get request to forismatic API
response = requests.get('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
# printing the response of quote text and quoteAuthor
print("Hey there! This is the quote for the day")
## extracting name and author
print('{quoteText} - {quoteAuthor}'.format(**loads(response.text)))
