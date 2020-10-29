from tqdm import tqdm
import zipfile
import sys

# input from user
wordlist = input("Enter Words list filename: ")
zip_file = input("Enter zip filename: ")

# initialize the Zip File object
zip_file = zipfile.ZipFile(zip_file)
# count the number of words in this wordlist
n_words = len(list(open(wordlist, "rb")))
# print the total number of passwords
print("Total passwords to test:", n_words)
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            # Check if the current selected password unzips the zip file
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            # if password found from the word list,
            # exit from program
            print("Password found:", word.decode().strip())
            exit(0)
print("Password not found, try other wordlist.")
