import socket
import threading
from queue import Queue

target = input("Enter the  IP-Address or domain of the host you are trying to scan\n ")
print_lock = threading.Lock()
queue = Queue()
open_ports = []

# Function to check whether port is open or closed
def port_scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #To connect target to specific port
        sock.connect((target,port))
        return True
    except:
        return False

 # Function to get ports       
def get_ports(mode):
    if mode == 1:
        for port in range(1, 1024):
            queue.put(port)
    elif mode == 2:
        for port in range(1, 49152):
            queue.put(port)
    # some important ports
    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            queue.put(port)
    # Taking port from user
    elif mode == 4:
        ports = input("Enter your ports (seperate by blank):")
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)

#Function to get port, scan them and print the reults
def worker():
    while not queue.empty():
        port = queue.get()
        if port_scan(port):
            print("Port {} is open.".format(port))
            open_ports.append(port)
        else:
            continue

# Function to create, start and manage threads.      
def run_scanner(threads, mode):

    get_ports(mode)

    thread_list = []

    for _ in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print("Open ports are:", open_ports)

print("Enter the mode :\n 1. standardized ports\n 2. reserved ports\n 3. important ports\n 4. input the port")
mode = int(input())
thread = int(input("Enter the thread\n"))
run_scanner(thread,mode)


        