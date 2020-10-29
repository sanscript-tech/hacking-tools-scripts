#include<vector>
#include <algorithm>
#include <chrono>
#include <iostream>
using namespace std;
using namespace std::chrono;
int my_function()
{
    //This function contains the code whose execution time you wish to friend
    int num1;
    int num2;
    cout<<"Enter num1"<<endl;
    cin>>num1;
    cout<<"Enter num2"<<endl;
    cin>>num2;
    cout<<"Addition of first and second number is "<<num1+num2<<endl;
    cout<<" "<<endl;

}

int main()
{
    // Starting the clock
    auto start_clock = high_resolution_clock::now();
    my_function();

    // Stopping the clock
    auto stop_clock = high_resolution_clock::now();

    //time in seconds
    auto duration_in_seconds = duration_cast<seconds>(stop_clock - start_clock);

    //converting time to microseconds
    auto duration_in_milliseconds = duration_cast<microseconds>(stop_clock - start_clock);

    cout <<"The amount of time taken to execute your function in milliseconds is "<< duration_in_milliseconds.count() << " microseconds" << endl;
    cout <<"The amount of time taken to execute your function in seconds is "<< duration_in_seconds.count() << " seconds" << endl;

    return 0;
}
