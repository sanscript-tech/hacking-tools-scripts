#This script implements Substitution Cipher
#The key for encrypting the message must be passed as a Command line argument in the form of a csv file

#To run the script from terminal, run
#python3 substitution_cipher.py "path_to_csv_file_containing_the_key"

import csv
import sys

def get_key():
    key = dict()
    with open(sys.argv[1] , 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            key[row[0].strip()] = row[1].strip()
    return(key)

def encrypt():
    key = get_key()
    message = input("Enter the message ")
    encrypted_message = ''
    for letter in message:
        try:
            encrypted_message += key[letter]
        except:
            alert = "Your key does not have a suitable match for " + letter +  "\nPlease update your key and try again!" 
            return(-1, alert)
    return(0, encrypted_message)

if __name__ == "__main__":
    exit_code, message = encrypt()
    if (exit_code == 0):
        print("The encrypted message is " , message)
    else:
        print(message)
