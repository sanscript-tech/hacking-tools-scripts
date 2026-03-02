import shutil 
  
# Path 
path = input("Enter the path:")
  
# Get the disk usage statistics 
# about the given path 
stat = shutil.disk_usage(path) 
  
# Print free space in the disk
# shutil.disk_usage(path) returns a tuple with the attributes total, used and free in bytes, therefore the free disk space can be found in the index 2
print("Free disk space present in the given path:"+str(stat[2])+" bytes")

