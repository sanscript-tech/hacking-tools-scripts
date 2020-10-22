'''
Aim : To demonstate working of bcrypt hash algorithm , which generates salt 
and hash value and compares it with password entered to check whether it is 
valid or invalid.

Scenario : User enters username , password at time of registration , upon which 
hashed password is created by hashpw() function. Upon login , the entered password
is checked against the hashed password and if matched , login is successful else 
not.

Note 1 : Each time a unique hash value , salt is generated.

Note 2 : This is one such scenario implemented using bcrypt module for understanding of hash functions.
Many other applications / variations can be implemented. 



'''


# import the bcrypt module.
import bcrypt
import time
# input username ,password
user=input("Enter username : ")
inputstr=input("Enter password : ")
strs=bytes(inputstr, 'utf-8')

# get start time
start = time.time()

#A salt is generated with the gensalt() function.
salt = bcrypt.gensalt()

#A hashed value is created with hashpw() function, which takes the cleartext value and a salt as parameters.
 
# each time a unique salt and hashed values are generated.
hashed = bcrypt.hashpw(strs, salt)

end = time.time()
 
print("Salt : " ,salt)
print("\nHash value generated : ",hashed)

print("\nRegistration Successful!")
 
# check the password against generated  hashed value.

print("\n---- Login ----")

users=input("\nEnter username : ")
if(user==users):

    checkstr=input("Enter password to verify: ")
    checkstrs=bytes(checkstr, 'utf-8')
    
    if bcrypt.checkpw(checkstrs, hashed):
        print("Password Valid")
        print("\nLogin Successful!")
    else:
        print("Invaid Password")
       
    time_taken=end - start
        
    print("\nTime taken :",time_taken)
    
else:
    print("\nUser does not exists")

