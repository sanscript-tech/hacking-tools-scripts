# Importing library
import speedtest   

# Creating instance for class
st = speedtest.Speedtest() 

print("Speed test has been stared and it can take upto 30 seconds ")

# Upload method will return data in bits dividing by 8000 will return in kbs
print("Upload speed {:0.3f} kb/s ".format(st.upload()/8000))

# Download method will return data in bits dividing by 8000 will return in kbs
print("Download speed {:0.3f} kb/s ".format(st.download()/8000))

# Initilising list
servernames =[]   

# Getting ping of servers
st.get_servers(servernames)   

# Printing ping from list of dictionaries  
print("Ping {:0.2f}".format(st.results.ping))