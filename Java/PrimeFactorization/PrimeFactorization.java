import java.io.*; 
import java.util.*; 

class PrimeFactorization
{ 
    public static void main(String[] args) 
	{   
        Scanner sc=new Scanner(System.in); //Scanner class

        int n=sc.nextInt();   //Raeding user input

		primeFactorization(n); 
	} 
	public static void primeFactorization(int n) 
	{   
        /*If n is a factor of 2,we print 2 and
         then check whether (n/2)%2 is zero or not*/
		while (n%2==0) 
		{ 
			System.out.print(2+" "); 
			n=n/2; 
		} 

        /*Above loop exits only when n becomes odd,so now n is odd,
        so we can skip all the even elements in the for loop i.e i=i+2*/
		for (int i=3;i<=Math.sqrt(n);i+=2) 
		{ 
            /*if i is a factor of n,then print i and then
             divide n by i till i is not a factor of i*/
			while (n%i==0) 
			{ 
				System.out.print(i+" "); 
				n/=i; 
			} 
		} 
        /*condition for the prime numbers 
        greater than 2,we directly print n*/
		if (n>2) 
			System.out.print(n); 
	} 

	
} 
