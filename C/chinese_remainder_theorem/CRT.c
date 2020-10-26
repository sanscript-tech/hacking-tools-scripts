//CRT Implementation using formula:
//x =  ( sigma(rem[i]*pp[i]*inv[i]) ) % prod  Where 0 <= i <= n-1

#include <stdio.h>
//function to apply  CRT for given arrays
int result( int arr[], int rem[], int s)
{
    int prod = 1, pp[s], inv[s], k, count, x = 0, i;
    //product of coprime numbers in a given array
    for (i = 0; i < s; i++)
    {
        prod = prod * arr[i];
    }
    //pp[i] product of all divided by each array element
    for (i = 0; i < s; i++)
    {
        pp[i] = prod / arr[i];
    }
    //inv[i] is modular multiplicative inverse of pp[i] with respect to arr[i]
    for (i = 0; i < s; i++)
    {   
        count = 1;
        k = 1;
        while(count)
        {
            if(((pp[i] % arr[i]) *  k) % arr[i] == 1)
            {
                inv[i] = k;
                count=0;
            } 
            k++; 
        }
    }
    for (i = 0; i < s; i++)
    {
        x = x + (rem[i] * pp[i] * inv[i]); 
    }
    x = x % prod;
    return x; 
}

int main()
{
    int s, i, arr[100], rem[100];
    printf("Enter size of array:");
    scanf("%d",&s);
    //input array of coprime numbers
    printf("Enter value of coprime numbers:");
    for (i = 0; i < s; i++ )
    {
        scanf("%d", &arr[i]);
    }
    //input array of remainders
    printf("Enter value of remainders:");
    for (i = 0; i < s; i++ )
    {
        scanf("%d", &rem[i]);
    }
    printf("Minimum number found is %d", result( arr, rem, s));
    return 0;
}
