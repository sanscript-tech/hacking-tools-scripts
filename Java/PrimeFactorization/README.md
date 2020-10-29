# Sample Input:
36

# Sample Output:
2 2 3 3

# Sample Input:
11

# Sample Output:
11

# Explaination:
<h3>TC 1: 2 * 2 * 3 * 3 =36</h3>
<h3>TC 2: 11 , since 11 itself is a prime number and a prime factor of itself.</h3>

<p>The while loop and for loop take care of composite numbers and last condition takes care of prime numbers. To prove that the complete algorithm works, we need to prove that steps 1 and 2 actually take care of composite numbers. This is clear that step 1 takes care of even numbers. And after step 1, all remaining prime factor must be odd (difference of two prime factors must be at least 2), this explains why i is incremented by 2.</p>


# Time Complexity:
<h3>O(sqrt(n))</h3>

