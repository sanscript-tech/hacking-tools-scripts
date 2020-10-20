import sys 
import socket 
from colorama import init, Fore

init(autoreset=True)

def getTarget():
	hostname = input("Enter the hostname: ")
	target = socket.gethostbyname(hostname)
	return target	

def scan(target, port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		print(Fore.CYAN + f"Scanning port {port}...")
		if s.connect_ex((target, port)) == 0:
			print(Fore.BLUE + f"Port {port} is Open")
		else:
			print(Fore.BLUE + f"Port {port} is Close")
		s.close()
	except socket.gaierror:
		print(Fore.RED + "Check your hostname!")
		sys.exit()
	except KeyboardInterrupt:
		sys.exit()

def reservedPorts():
	target = getTarget()
	for port in range(1024):
		scan(target, port)

def scanAllPorts():
	target = getTarget()
	for port in range(65536):
		scan(target, port)

def scanAPort():
	target = getTarget()
	port = int(input("Enter the port you want to scan: "))
	scan(target, port)
	
def criticalPorts():
	criticalPorts = [15, 20, 21, 22, 23, 25, 49, 50, 51, 53, 67, 68, 69, 79, 80, 88, 110, 111, 119, 123, 135, 137, 138, 139, 143, 161, 389, 443, 445, 500, 520, 546, 547, 636, 993, 995, 1512, 1701, 1720, 1723, 1812, 1813, 3306, 3389, 5004, 5005, 5060, 5061, 5900, 8080]
	target = getTarget()
	for port in criticalPorts:
		scan(target, port)

while True:   
	print()
	print("-" * 22, "MENU", "-" * 22)
	print("Press 1 for Reserved Ports")
	print("Press 2 to scan all the ports")
	print("Press 3 for Critical Ports")
	print("Press 4 to scan a particular port")
	print("-" * 50)

	choice = int(input(Fore.GREEN + "Enter the menu option: "))

	if choice == 1:
		reservedPorts()
	elif choice == 2:
		scanAllPorts()
	elif choice == 3:
		criticalPorts()
	elif choice == 4:
		scanAPort()
	else:
		print("\nInvalid Choice. Enter a valid option!")