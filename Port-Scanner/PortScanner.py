import sys 
import socket 
from colorama import init, Fore

init(autoreset=True)

def scanAPort():
	hostname = input("Enter the hostname: ")
	port = int(input("Enter the port you want to scan: "))
	target = socket.gethostbyname(hostname)

	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)

		if s.connect_ex((target, port)) == 0:
			print(Fore.BLUE + f"Port {port} is open")
		else:
			print(Fore.BLUE + f"Port {port} is close")
		
		
		s.close()

	except socket.gaierror:
		print(Fore.RED + "Check your hostname!")
		sys.exit()
	except KeyboardInterrupt:
		sys.exit()
	
def scanCommonPorts():
	commonPorts = [20,21,22,23,25,53,80,110,119,123,143,161,194,443,445,464,465,497,500,512,513,514,515,520,521,540,554,563,587,631,636,691,873,993,994,995,1080,1433,1434,1512,1701,1758,1759,1789,1812,1813,1985,2049,2053,2100,2401,2809,3130,3306,4321,4444,5002,5308,5549,6000,9876,10080,11371,11720,13720,13721,31337,33434]

	hostname = input("Enter the hostname: ")
	target = socket.gethostbyname(hostname)

	open_ports = []
	close_ports = []

	for port in commonPorts:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)

			if s.connect_ex((target, port)) == 0:
				print(Fore.CYAN + f"Scanning port {port}...")
				open_ports.append(port)
			else:
				print(Fore.CYAN + f"Scanning port {port}...")
				close_ports.append(port)
			
			s.close()

		except socket.gaierror:
			print(Fore.RED + "Check your hostname!")
			sys.exit()
		except KeyboardInterrupt:
			sys.exit()

	if(open_ports):
		print(Fore.GREEN + "These ports are Open: ")
		print(open_ports)
	if(close_ports):
		print(Fore.GREEN + "These ports are Close: ")
		print(close_ports)

while True:   
	print()
	print("-" * 22, "MENU", "-" * 22)
	print("1. Look for a specific port in a server")
	print("2. Scan for some common ports in a server")
	print("3. Quit")
	print("-" * 50)

	choice = int(input(Fore.GREEN + "Enter the menu option: "))

	if choice == 1:
		scanAPort()
	elif choice == 2:
		scanCommonPorts()
	elif choice == 3:
		break
	else:
		print("\nInvalid Choice. Enter a valid option!")