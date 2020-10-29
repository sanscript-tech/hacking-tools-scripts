# Finding subdomains of a domain
- - - - - - - - - - - - - - - - - 
## Aim
Aim of the script is to find subdomains corresponding to a particular domain. First, we build up the URL to be suitable for sending a request. Then we get the HTTP response from the server, this will raise a ConnectionError exception whenever a server does not respond, that's why we wrapped it in a try/except block.
Finally, when the exception isn't raised, then the subdomain exists.

## Requirements
```pip install requests```

## To run
Enter the domains whose subdomains are to be found. </br>
```python domains.py```

## Example Output
For ```google.com```

![alt-text](https://github.com/TaniaMalhotra/hacking-tools-scripts/blob/subdomains/Python/subdomains/Screenshot%20(499).png)
