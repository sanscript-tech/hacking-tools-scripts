#include<bits/stdc++.h>
using namespace std;
bool isprime(int num) // use of boolean function to check primality of number 
{
if(num==1) // natural number
return false;
for(int i=2;i*i<=num;i++) 
{
if(num%i==0) //Even number
return false;
}
return true;
}
int main()
{
int num,t;
cin>>t;// no of test cases
while(t--)
{
cin>>num;
if(isprime(num))
cout<<"yes"<<endl;
else
cout<<"no"<<endl;
}
}
