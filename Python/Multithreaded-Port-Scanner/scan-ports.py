import concurrent.futures
import socket
import sys
import ipaddress

# Check if the user has provided commandline arguments.
if len(sys.argv) < 2:
    print("Not enough commandline arguments.")
    sys.exit()

# Check if the IP address or website is valid or not.
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

# create a list to store custom ports.
custom_ports = []
if len(sys.argv) > 2:
    custom_ports = sys.argv[2:]

# Method to scan a single port
def scan_port(target_IP, port):
    # Create a socket object.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set default timeout to 1 second.
    socket.setdefaulttimeout(1)

    # Try to connect the target
    result = s.connect_ex((target_IP, port))

    # Check if connection was successful
    if result == 0:
        print(f"Port {port}: \033[92mOPEN\033[0m")
        return port

    return None


def scan_ports(port_range):

    if not port_range:
        port_range = map(int, input("Enter ports(space separated):").split())

    # List to hold open ports.
    open_ports = []

    # Create a context manager to spawn individual threads for each port.
    with concurrent.futures.ThreadPoolExecutor() as executor:

        future_to_port = {
            executor.submit(scan_port, target_IP, port): port for port in port_range
        }

        # Run a loop to collect open ports.
        for future in concurrent.futures.as_completed(future_to_port):
            # Get the selected port
            port = future_to_port[future]
            try:
                # Check if it a valid port.
                open_port = future.result()
            except Exception as e:
                # Print any errors.
                print(f"Exception:{e}")
            else:
                # Add to the list if it's a valid port.
                if open_port is not None:
                    open_ports.append(open_port)

    return open_ports


if __name__ == "__main__":

    MENU_PROMPT =\
"""[1] Reserved Ports.
[2] All Ports.
[3] Critical Ports.
[4] Manual Ports.
Enter your choice:"""

    # Get user choice
    choice = int(input(MENU_PROMPT))

    # Define switcher
    switcher = {
        1: range(1024),
        2: range(65536),
        3: [15, 20, 21, 22, 23, 25, 49, 50, 51, 53, 67, 68, 69, 79, 80, 88,
            110, 111, 119, 123, 135, 137, 138, 139, 143, 161, 389, 443, 445,
            500, 520, 546, 547, 636, 993, 995, 1512, 1701, 1720, 1723, 1812,
            1813, 3306, 3389, 5004, 5005, 5060, 5061, 5900, 8080],
        4: []
    }

    # Call method to scan ports.
    open_ports = scan_ports(switcher[choice])

    # Finally print all the open ports.
    print(f"Open Ports:{open_ports}")
