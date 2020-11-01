imjort java.util.*; 

class MaxPrime
{ 
static int limit = 100000000; 
static boolean[] sieve = new boolean[limit + 1]; 

/*The Sieve of Eratosthenes marks all the no.s except 
primes to false in the bool arr in most optimal way.*/
static void SieveOfEratosthenes() 
{ 
	for (int i=0;i<limit+1;i++) 
	{ //setting all values to true 
		sieve[i]=true; 
	} 
	for (int j=2;j*j<=limit;j++) 
	{ 
		if(sieve[j]==true) 
		{   //setting all the multiples of j as false
			for (int i=j*j;i<=limit;i+=j) 
				sieve[i]=false; 
		} 
	} 
} 

static int maxPrime(int d) 
{ 
	int l=(int)Math.pow(10,d-1); //lowest d digit number 
	int r=(int)Math.pow(10,d)-1; //highest d digit number
	for (int i=r;i>=l;i--) 
	{   /**The first index with true value in sieve[] will be 
        the answer as we are traversing in decreasing order */
		if(sieve[i]) 
		{ 
			return i; 
		} 
	} 
    
	return -1; 
} 


public static void main(String[] args) 
{ 
	SieveOfEratosthenes(); 

    Scanner sc=new Scanner(System.in);
    int n=sc.nextInt();//Input
    
	System.out.println(maxPrime(n)); //Output
	
} 
} 
 
