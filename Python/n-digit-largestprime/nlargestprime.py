# To find N digit Largest Prime Number

from math import sqrt 
MAX = 100000000
prime = [True] * (MAX + 1) 

def SieveOfEratosthenes() :  
    for p in range(2, int(sqrt(MAX)) + 1) :  
        if (prime[p] == True) : 
            for i in range(p * p, MAX + 1, p) : 
                prime[i] = False

#function to find largest prime number		
def largestPrime(d) :  
    l = 10 ** (d - 1) 
    r = (10 ** d) - 1  
    for i in range(r, l , -1) :   
        if (prime[i]) : 
            return i            
    return -1  

#driver code
if __name__ == "__main__" : 
	N = int(input("Enter N digit")) #input
	SieveOfEratosthenes()  #call to SieveOfEratosthenes() function
	print(largestPrime(N)) #call to function and output
