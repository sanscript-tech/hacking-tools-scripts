#!/usr/bin/env python3


#python script to check whether the password is strong or not
#[Criteria for string password]
"""
Minimum 8 characters.
The alphabets must be between [a-z]
At least one alphabet should be of Upper Case [A-Z]
At least 1 number or digit between [0-9].
At least 1 character from [ _ or @ or $ ].
"""
import re 

password =input("Enter the password:- ")

flag = 0

#Length of the password should be atleast 8
if (len(password)<8): 
	flag = -1

# [a-z] regex to check the presnece for alpabets from a-z
elif not re.search("[a-z]", password): 
	flag = -1

# [A-z] regex to check the presnece for alpabets from A-Z
elif not re.search("[A-Z]", password): 
	flag = -1

# [0-9] regex to check the presnece for alpabets from 0-9
elif not re.search("[0-9]", password): 
	flag = -1

# [-@$] regex to check the presnece for alpabets from '_','@','$'    
elif not re.search("[_@$]", password): 
	flag = -1





if flag ==-1: 
	print("Weak Password")
else :
    print("Strong Password")    

