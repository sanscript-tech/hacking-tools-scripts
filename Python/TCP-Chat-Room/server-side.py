import socket
import threading
from colorama import Fore, init
init(autoreset=True)
server_host = socket.gethostbyname(socket.gethostname())
server_port = int(input(Fore.CYAN + "Enter the port : "))
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((server_host, server_port))
server_socket.listen()
print(Fore.BLUE + f"Server connected on {server_host}:{server_port}")
# A dictionary of client connections and username
clients = {}
# Broadcast a message to the server
def broadcast(message):
    for client in clients:
        client.send(message.encode())
# 
def handleClient(client, address):
    while 1:
        message = client.recv(1024)       
        if message.decode() != '':
            print(Fore.YELLOW + "Incoming Message : " + str(message.decode()))
            for client_other in clients:
                if client_other != client:
                    client_other.send(message)

while 1:
    # Accepting Client Connections
    client, address = server_socket.accept()
    # Receiving Client's Username
    username = client.recv(1024).decode()
    print(Fore.GREEN + f"{username} connected on {address}")
    clients[client] = username
    server_handler = threading.Thread(target=handleClient, args=(client, address, ))
    server_handler.start()