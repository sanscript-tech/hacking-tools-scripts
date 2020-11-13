#include <iostream>

using namespace std;

void CheckPassword(string& input)   
{
   int n = input.length();      //check length of string
   bool hasLower = false, hasUpper = false;
   bool hasDigit = false, specialChar = false;
    for (int i = 0; i < n; i++)       // from character 1 to end of string
   {
      if (islower(input[i]))          //check if char is lowercase
         hasLower = true;
      else if (isupper(input[i]))     //check if char is uppercase
         hasUpper = true;
      else if (isdigit(input[i]))     //check if char is digit
         hasDigit = true;
      else                             //check if char is special character
         specialChar = true;         
   }
   cout << " Strength of password: ";
   if (hasLower && hasUpper && hasDigit && specialChar && (n >= 8))  
      cout << "Strong" << endl;
   else if ((hasLower || hasUpper) && specialChar && (n >= 6))
      cout << "Moderate" << endl;
   else
      cout << "Weak" << endl;
}
int main() 
{
   string str;
   cout<<"\n Enter Password : ";
   getline(cin,str);       //get a string input
   CheckPassword(str);
   return 0;
}
