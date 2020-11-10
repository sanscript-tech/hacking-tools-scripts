import os

#path where we have to count files and directories
path = input("Enter path: ")

noOfFiles = 0
noOfDir = 0

for base, dirs, files in os.walk(path):
    print('Looking in : ',base)
    for directories in dirs:
        noOfDir += 1
    for Files in files:
        noOfFiles += 1
#print number of files,directories,total
print('Number of files',noOfFiles)
print('Number of Directories',noOfDir)
print('Total:',(noOfDir + noOfFiles))
