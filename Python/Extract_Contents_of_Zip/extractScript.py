#import pyshorteners library
import pyshorteners

# input URL
url = input("Enter the URL:")

# class object
shortener = pyshorteners.Shortener()

# shortened URl
urlShort = shortener.tinyurl.short(url)

# print shortened URL
print("The shortened URL is:" + urlShort)
