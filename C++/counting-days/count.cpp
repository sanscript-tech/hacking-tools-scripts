#include <iostream>
#include <ctime>
using namespace std;
int main()
 {
   // asking user input for next birthday
   time_t now = time(0);
   tm *ltm = localtime(&now);
   int m,d,y;
   cout<<"Enter month of birthday ";
   cin>>m;
   cout<<"Enter day of birthday ";
   cin>>d;
   cout<<"Enter the year of your next birthday";
   cin>>y;

   //current day and date

   int current_day = ltm->tm_mday;
   int current_month = 1+(ltm->tm_mon);
   int current_year = 1900 +(ltm->tm_year);
   int monthDays[12]= { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
   int middle_days;
   middle_days= 0;


   //if birthday falls the same year
   if(current_year == y)

   {
    //fallling same month
    if(current_month==m)
    {
    	cout<<d-current_day;
	}
    else
    //different month
	{
	for(int i = current_month; i<m-1;i++)
	middle_days+=monthDays[i];
    cout<<d+(monthDays[current_month-1]-current_day)+middle_days;
	}

    cout<<" days are left for your birthday";
   }

   middle_days = 0;
   //if birthday falls the next year
   if(current_year != y)
    {
      for(int i = current_month;i<12;i++)
     {
      middle_days+=monthDays[i];
     }
     for(int i = 0;i<m-1;i++)
     {
      middle_days+=monthDays[i];
     }
     cout<<d+(monthDays[current_month-1]-current_day)+middle_days;
     cout<<" days are left for your birthday"<<endl;
  }

}
