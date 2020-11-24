# importing requests package
from newsapi import NewsApiClient
import requests
import pyttsx3
# initializing the text to speech engine
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

#asking for news API key from https://newsapi.org/register
apiKey = input("Please input your news API key by registering at https://newsapi.org/register : ")
newsapi = NewsApiClient(api_key=apiKey)
engine.say('Please enter the category of news from the following')
engine.runAndWait()
engine.say('business, entertainment, general, health, science, sports and technology')
engine.runAndWait()
category = input("Please enter the category of news from the following: business, entertainment, general, health, science, sports and technology: ")

# fetching top headlines
top_headlines = newsapi.get_top_headlines(category=category,language='en',country='us')
engine.say("Here are the top 5 news headlines from your chosen category")
engine.runAndWait()
for i in range(5):
    print(top_headlines["articles"][i]['title'])
    engine.say(top_headlines["articles"][i]['title'])
    engine.runAndWait()
