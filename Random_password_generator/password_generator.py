#Imports and dependencies
import sys
import random
import string

#The generated password consists of the English alphabet (Capital and small letters), digits from 0-9 and special characters
rand_string = string.ascii_letters + string.digits + "_<>-+*/$%#&^"
start = 0
end = len(rand_string) - 1

def password_generator(length):
    #A random index is chosen from rand_string, this is used to generate the password
    password = ""
    for i in range(length):
        index = random.randint(start, end)
        password += rand_string[index]
    return(password)

if __name__ == "__main__":
    #The length of the password is accepted as a command line argument
    print("Generated password :" + password_generator(int(sys.argv[1])))
