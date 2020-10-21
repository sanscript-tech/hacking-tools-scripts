# Platform library helps us in getting system information 

#  Importing platform library
import platform 

# Initialize dictionary to store data
information = {} 


# adding platform details  to dictionary 
# platform.platform() will return platform details
information["platform details"] = platform.platform() 


# adding system name to dictionary 
# platform.system()  will return system details
information["system name"] = platform.system() 
 

# adding processor name to dictionary 
# platform.processor()  will return processor that we are using
information["processor name"] = platform.processor() 


# adding architectural detail to dictionary 
# platform.architecture()  will return architecture of PC
information["architectural detail"] = platform.architecture()  

# adding machine detail to dictionary 
# platform.machine() will return type of mechine that we are using
information["machine detail"] = platform.machine()

# adding PC version to dictionary
# platform.version() will return software version
information["PC Version"] = platform.version()


# printing the details in dictionary
for i, j in information.items(): 
	print(i, " - ", j) 
