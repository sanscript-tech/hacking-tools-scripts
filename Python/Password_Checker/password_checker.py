#!/usr/bin/env python3


#python script to check whether the password is strong or not

import re 

password =input("Enter the password:- ")

flag = True

#Length of the password should be atleast 15
if (len(password)<15): 
	flag = False

isUpper=False
isLower=False
isSpecial=False
isDigit=False

for character in range(0,len(password)):
	if password[character].isupper():
		isUpper=True
	if password[character].islower():
		isLower=True
	if password[character].isnumeric():
		isDigit=True
	if password[character]=='@' or password[character] =='$' or password[character] =='#' or password[character]=='_' or character =='*':
		isSpecial=True
    
if isUpper ==True and isLower == True and isDigit==True and isSpecial==True and flag ==True:
	print("Strong Password")   	
else :
	print("Weak Password")
 

