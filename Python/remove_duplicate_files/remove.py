# python program to remove duplicate files from directory
import os
import hashlib
import glob
#taking path of directory as user input
PATH_directory = input("Please enter the path of directory in which you wish to remove duplicate files  :  ")
unique_files = []
for file in os.listdir(PATH_directory):
    # checking if path is existing file
    if os.path.isfile(file):
        hash = hashlib.md5(open(file, 'rb').read()).hexdigest()
        # if hash of the file in consideration is unique
        if hash not in unique_files:
            unique_files.append(hash)
        # delete file if it has a matching hash
        else:
            print("Found a duplicate. Now removing duplicate file")
            os.remove(file)
