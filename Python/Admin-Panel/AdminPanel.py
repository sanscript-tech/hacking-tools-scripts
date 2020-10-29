import urllib.request as ur
from colorama import init, Fore

init(autoreset=True)

url = input(Fore.BLUE + "\nEnter the website URL: ")

print(Fore.CYAN + "\nSearching...\nThis will take some time. Stay patient!")

f = open("links.txt")
count = 0
while True:
	adminLink = f.readline()
	if not adminLink:
		break
	print(adminLink, end="\r")
	completeUrl = url + adminLink
	try:
		search = ur.urlopen(completeUrl)
		print(Fore.GREEN + f"\nAdmin Panel found at {completeUrl}")
		count = count + 1
		break
	except:
		continue

if not count:
	print(Fore.RED + f"\nCouldn't find any Admin Panel!")