## Script to scan multi-threaded ports
##  Libraries imported
# socket 
Socket will be used for our connection attempts to the host at a specific port.
# queue
Queue is a data structure that will help us to manage the access of multiple threads on a single resource, which in our case will be the port numbers.
# threading
Threading will allow us to run multiple scanning functions simultaneously.

## How to use it 
Run the following command
# python port.py
Enter the Ip Address , then enter the mode and then no of threads.

