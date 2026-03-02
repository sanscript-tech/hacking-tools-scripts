#import requried Libraries
from PyDictionary import PyDictionary

#creating an object
dictionary=PyDictionary()

#input
print("Enter the word")
word=input()

#creating an empty dictionary
search=dict()

#search
search=dictionary.meaning(word)
result=list(search.values())[0]

#print the output
print('Meaning of ',word,'is:')
for meaning in result:
    print("*" ,meaning)