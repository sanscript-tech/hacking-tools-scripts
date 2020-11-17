import socket
from socket import AF_INET, SOCK_STREAM, SOCK_DGRAM
def scan_ports(name, port):
    sock = socket.socket(AF_INET, SOCK_STREAM)
    try:
        #connect to the port
        sock.connect((name,port))
        sock.send(b'200 OK\r\n')
        # accepting banner as ascii string
        banner = str(sock.recv(256), 'ascii')
        # printing status portwise
        print("[+] {port}/tcp is open".format_map(vars()))
        # printing banner
        print("- Banner")
        print(banner)
    except:
        # if port is filtered or closed
        print("{port} is filtered/closed/timedout".format_map(vars()))

def main():
    target_host = input("Please enter the target host. For eg. www.example.com ")
    # listing common ports for convenience
    target_ports = [22, 25, 53, 80, 443]
    socket.setdefaulttimeout(5)
    # selecting one port a time
    for port in target_ports:
        scan_ports(target_host, port)


if __name__ == "__main__":
    main()
