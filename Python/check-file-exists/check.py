import os

# Taking the input path from the user
PATH = input('Enter the path where you would wish to search the file or directory')

# Asking user to input file name
file_name = input('Enter the name of file or directory')

# making the complete PATH by concatenating filename to path
Full_path = PATH + "/" + file_name

# Using os.path as it checks for both file and directory
print(os.path.exists(Full_path))

# If path exists, then file also exitss
if(os.path.exists(Full_path)):
    print("The file or directory you are searching for exists in the given path")

# if path os incorrect, that means no such file exits
else:
    print("The file or directory you are searching for does not exist in the given path")
