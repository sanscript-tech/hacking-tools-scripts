import socket
import threading
from colorama import init, Fore
init(autoreset=True)
# Connecting Client to server address
host = input(Fore.CYAN + "Enter Server Host: ")
port = int(input(Fore.CYAN + "Enter Server Port: "))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
# Getting Client Username
username = input(Fore.CYAN + "Enter username : ")
print()
client_socket.send(username.encode())
def handle_messages():
    while 1:
        print(client_socket.recv(1024).decode())
def handle_input():
    while 1:
        client_socket.send((Fore.MAGENTA + username + ' - ' + Fore.YELLOW + input()).encode())
message_handler = threading.Thread(target=handle_messages, args=())
message_handler.start()
input_handler = threading.Thread(target=handle_input, args=())
input_handler.start()