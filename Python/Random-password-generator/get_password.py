#Imports and dependencies

import random
import string

random_string = string.digits + string.ascii_letters + "_$#%&*+<>!"

def generate_password():    
    password = ""
    len_of_pswd = int(input("Enter the length of the password : "))
    for i in range(len_of_pswd):
        password += random.choice(random_string) 
    return(password)

if __name__ == "__main__":
    password = generate_password()
    print("The password generated is : " + password)