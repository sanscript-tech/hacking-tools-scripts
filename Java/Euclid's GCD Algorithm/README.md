
# Sample Input:

10 15

  

# Sample Output:

5

  

# Sample Input:

20 48

  

# Sample Output:

4

  

# Explaination:
TC 1:         
 10 = 2 * 5

15 = 3 * 5

The Greatest common divisor is 5

  

TC 2: 
20 = 2 * 2 * 5

48 = 2 * 2 * 2 * 2 * 3

The Greatest common divisor is 2 * 2 = 4

  

The algorithm is based on below facts:

  

--If we subtract smaller number from larger (we reduce larger number), GCD doesn’t change. So if we keep subtracting repeatedly the larger of two, we end up with GCD.

--Now instead of subtraction, if we divide smaller number, the algorithm stops when we find remainder 0.

  

# Time Complexity:

<h3>O(log min(a,b))</h3>