#  Importing library
import platform 

# Initialize dictionary 
information = {} 


# adding platform details  to dictionary 
information["platform details"] = platform.platform() 


# adding system name to dictionary 
information["system name"] = platform.system() 
 

# adding processor name to dictionary 
information["processor name"] = platform.processor() 


# adding architectural detail to dictionary 
information["architectural detail"] = platform.architecture()  

# adding machine detail to dictionary 
information["machine detail"] = platform.machine()

# adding PC version to dictionary
information["PC Version"] = platform.version()


# printing the details 
for i, j in information.items(): 
	print(i, " - ", j) 
