import sys
import socket
import ipaddress

if len(sys.argv) < 2:
    sys.exit("Please provide an IP address or a domain name.")

query = sys.argv[1]

try:
    ipaddress.ip_address(query)
except:
    ipv4, ipv6 = map(lambda x: x[4][0], socket.getaddrinfo(query,22,type=socket.SOCK_STREAM))
    print("Domain Name:", query)
    print("IPV4:", ipv4)
    print("IPV6:", ipv6)
    print("Server Domain:", socket.gethostbyaddr(ipv4)[0])
else:
    ip_info = socket.gethostbyaddr(query)
    print("Domain Name:", ip_info[0])
    print("IP:", query)
