import sys
import random
import string

rand_string = string.ascii_letters + string.digits + "_<>-+*/$%#&^"
start = 0
end = len(rand_string) - 1

def password_generator(length):
    password = ""
    for i in range(length):
        index = random.randint(start, end)
        password += rand_string[index]
    return(password)

if __name__ == "__main__":
    print("Generated password :" + password_generator(int(sys.argv[1])))