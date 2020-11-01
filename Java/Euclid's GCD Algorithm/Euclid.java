// Java program to demonstrate working of extended 
import java.util.*; 
import java.io.*; 

class Euclid 
{   
    /*Recursive function to calculate gcd using Euclid's algo*/
	public static int gcd(int a,int b) 
	{ 
		if (a==0) 
			return b; 

		return gcd(b%a, a); 
	} 

    public static void main(String[] args) 
	{ 
        Scanner sc=new Scanner(System.in);

        /*Taking a & b as user input*/
		int a=sc.nextInt();
        int b=sc.nextInt(); 
		
		System.out.println("GCD : " + gcd(a,b)); //Output

	} 
    
} 

