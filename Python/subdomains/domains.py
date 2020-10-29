import requests
#ask the user for domain whose subdomains are to be found
dmn = input("Please enter the preferred domain ")
# open the file containing subdomains and read it as well as split the lines
subdomains = open("subdomains.txt").read().splitlines()
for subdomain in subdomains:
    # construct the url
    url = f"http://{subdomain}.{dmn}"
    try:
        #if subdomain exists, then it will print it
        requests.get(url)
    except requests.ConnectionError:
        # in this case, if no subdomain is existing, pass it
        pass
    else:
        print("[+] The subdomains found are : ", url)
