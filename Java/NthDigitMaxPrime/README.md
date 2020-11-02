# Sample Input:

2

  

# Sample Output:

97

  

# Sample Input:

6

  

# Sample Output:

999983

  

# Explaination:
TC 1:         
l=10^(2-1)=10
r=10^2-1=99

After checking in the sieve[] in decreasing order,the first time comes out to be 97


# Time Complexity:

<h3>O(limit log(log limit))</h3>,where limit is the size of the sieve[].This is the most optimal way to find out the  required solution.