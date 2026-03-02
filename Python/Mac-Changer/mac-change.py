import sys
import subprocess
import os
import re

# Check if the Operating System is Windows or not.
WINDOWS = os.name != 'posix'
mac_regex = ("^([0-9A-Fa-f]{2}[:-])" +
             "{5}([0-9A-Fa-f]{2})|" +
             "([0-9a-fA-F]{4}\\." +
             "[0-9a-fA-F]{4}\\." +
             "[0-9a-fA-F]{4})$")

# Compile a regular expression to validate MAC addresses.
mac_regex = re.compile(mac_regex)

# Check if MAC address was supplied as a commandline argument.
if len(sys.argv) < 2:
    sys.exit("Enter new MAC address as a commandline argument.")

# Check if the supplied MAC address was valid or not.
new_mac = sys.argv[1]
if not re.search(mac_regex, new_mac):
    sys.exit("Please enter a valid MAC address.")

# Perform different operations based on the operating system.
if not WINDOWS:
    # Get the output containing necessary information.
    output = subprocess.getoutput('ip link show | grep "link/ether"').split()

    # Look for a valid MAC address.
    for entry in output:
        if re.search(mac_regex, entry):
            prev_mac = re.search(mac_regex, entry).group()
            break

    # Extract the nic device associated with the MAC address.
    nic_device = subprocess.getoutput('ip addr show | grep "altname"').split()[1]

    # Perform actions to change MAC address.
    subprocess.call(f'sudo ip link set dev {nic_device} down')
    subprocess.call(f'sudo ip link set dev {nic_device} address {new_mac}')
    subprocess.call(f'sudo ip link set dev {nic_device} up')

else:
    # Get the appropriate output.
    output = subprocess.getoutput('getmac /v | findstr Device').split()

    # Check for a valid MAC address in output.
    for entry in output:
        if re.search(mac_regex, entry):
            prev_mac = re.search(mac_regex, entry).group()
            break

    # Extract the associated nic device.
    nic_device = output[-1][output[-1].find('{'):]

    # Perform actions to change MAC address.
    subprocess.call('reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\%s\0004 /v NetworkAddress /d %s /f'%format(nic_device, new_mac.replace(":", "")))


print(f"Old MAC address: \033[93m{prev_mac}\033[0m")
print(f"New Mac address: \033[92m{new_mac}\033[0m")
