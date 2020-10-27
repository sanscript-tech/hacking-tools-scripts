import java.io.*; 
import java.util.*;

//Assumptions for CRT:divisors are pairwise co-prime, i.e gcd of every pair is 1
class CRT { 
	
	static int solve(int[] div,int[] rem,int n) 
	{ 
		int A = 1;//result initialized 
		while(true) 
		{  int i;
			for ( i=0;i<n;i++) 
			{   //checking for all i up to n whether A%div[i]==rem[i]
            	if (A%div[i]!=rem[i]) 
				break; 
            }	
			if (i==n) //if i==n,i.e,A%div[i] for all i is equal to corresponding rem[i]  and then A is returned
				return A; 
			A++; //if i is not equals to n,that means for some i the condition fails,so next value should be checked for A
		} 
	
	} 
	
	// Driver method 
	public static void main(String args[]) 
	{ /*Given two arrays div and rem,we need to find out the minimum number 'A' */
    /*,for which when the number of div array is divided it gives the corresponding value present in rem array*/
		//Taking input the length of the div array
		int n=sc.nextInt();
		int div[] = new int[n];
		int rem[] =new int[n];
		for(int i=0;i<n;i++){
		div[i]=sc.nextInt();
		}
		for(int i=0;i<n;i++){
		rem[i]=sc.nextInt();
		}
		System.out.println("A : " + solve(div, rem, n)); //Output
	} 
} 

