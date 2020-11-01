import urllib.request as ur
from colorama import init, Fore

init(autoreset=True)

url = input(Fore.BLUE + "\nEnter the website URL: ")

print(Fore.CYAN + "\nSearching...\nThis will take some time. Stay patient!")

# Opening file containing all the suggested admin links to inject
f = open("links.txt")
count = 0
while True:
	# Reading individual admin links from the links file
	adminLink = f.readline()
	if not adminLink:
		break
	print(adminLink, end="\r")
	completeUrl = url + adminLink
	try:
		# Opening the URL with admin Link
		search = ur.urlopen(completeUrl)
		print(Fore.GREEN + f"\nAdmin Panel found at {completeUrl}")
		count = count + 1
		break
	except:
		continue

# If none of the suggested admin links were correct
if not count:
	print(Fore.RED + f"\nCouldn't find any Admin Panel!")