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

    print(f"Port {port}: \033[91mCLOSED\033[0m")
    return None

# List to hold open ports.
open_ports = []

# Create a context manager to spawn individual threads for each port.
with concurrent.futures.ThreadPoolExecutor() as executor:

    # Check if the users has provided custom ports or not.
    if len(custom_ports) == 0:
        future_to_port = {
            executor.submit(scan_port, target_IP, port): port for port in range(65535)
        }
    else:
        future_to_port = {
            executor.submit(scan_port, target_IP, int(port)): port for port in custom_ports
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

# Finally print all the open ports.
print(f"Open Ports:{open_ports}")
