#Imports and dependencies

import random
import string

#string.digits = 0-9
#string.ascii_letters = a-z and A-Z
random_string = string.digits + string.ascii_letters + "_$#%&*+<>!"

def generate_password():    
    password = ""
    len_of_pswd = int(input("Enter the length of the password : "))
    #A character is picked at random from random_string
    for i in range(len_of_pswd):
        password += random.choice(random_string) 
    return(password)

if __name__ == "__main__":
    password = generate_password()
    print("The password generated is : " + password)
