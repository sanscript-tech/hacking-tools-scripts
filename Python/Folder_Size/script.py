import os

# get the current directory directly 
currentDirectory = os.getcwd()

# or give the required path here
# currentDirectory = r"C:\Users\Sapna\Desktop\hacking-tools-scripts\Python"

# initialize the size as 0
directory_size = 0    

# Size of the current directory in different formats
sizeFormat = {'Bytes': 1,
			  'Kilobytes': float(1)/1024, 
			  'Megabytes': float(1)/(1024*1024), 
			  'Gigabytes': float(1)/(1024*1024*1024)}

for (path, dirs, files) in os.walk(currentDirectory):
    for file in files:
        filename = os.path.join(path, file)
        directory_size += os.path.getsize(filename)

print("Size of current directory:"+ currentDirectory)

# directory size in bytes, kilobytes, megabytes and gigabytes
for key in sizeFormat:       
    print (str(round(sizeFormat[key]*directory_size, 2)) + " " + key)