import os

# Path where we have to count files and directories
HOME_FOLDER = 'C:/Users/Anusha_2/Desktop'

noOfFiles = 0
noOfDir = 0

for base, dirs, files in os.walk(HOME_FOLDER):
    print('Looking in : ',base)
    for directories in dirs:
        noOfDir += 1
    for Files in files:
        noOfFiles += 1

print('Number of files',noOfFiles)
print('Number of Directories',noOfDir)
print('Total:',(noOfDir + noOfFiles))