import concurrent.futures
import socket
import sys
import ipaddress

if len(sys.argv) < 2:
    print("Not enough commandline arguments.")
    sys.exit()

try:
    ipaddress.ip_address(sys.argv[1])
except ValueError:
    try:
        ipaddress.ip_address(socket.gethostbyname(sys.argv[1]))
    except (ValueError, socket.gaierror):
        print("Invalid IP address or domain name.")
        sys.exit()
    else:
        target_IP = socket.gethostbyname(sys.argv[1])
else:
    target_IP = sys.argv[1]

custom_ports = []
if len(sys.argv) > 2:
    custom_ports = sys.argv[2:]

def scan_port(target_IP, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = s.connect_ex((target_IP, port))

    if result == 0:
        print(f"Port {port}: \033[92mOPEN\033[0m")
        return port

    print(f"Port {port}: \033[91mCLOSED\033[0m")
    return None

open_ports = []

with concurrent.futures.ThreadPoolExecutor() as executor:

    if len(custom_ports) == 0:
        future_to_port = {
            executor.submit(scan_port, target_IP, port): port for port in range(65535)
        }
    else:
        future_to_port = {
            executor.submit(scan_port, target_IP, int(port)): port for port in custom_ports
        }

    for future in concurrent.futures.as_completed(future_to_port):
        port = future_to_port[future]
        try:
            open_port = future.result()
        except Exception as e:
            print(f"Exception:{e}")
        else:
            if open_port is not None:
                open_ports.append(open_port)

print(f"Open Ports:{open_ports}")
