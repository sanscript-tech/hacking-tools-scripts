# Automate code submission in codechef through selenium script
The aim of the program is to submit a simple code solution for the problem [COVID RUN](https://www.codechef.com/problems/CVDRUN) to [CodeChef website](https://www.codechef.com/) website using automated script.

### Libraries used:
* [Selenium](https://selenium-python.readthedocs.io/index.html) : A popular automation tool.
* [webdriver-manager](https://pypi.org/project/webdriver-manager/) : Supporting package.

### Pre-requisites:
* **Chromedriver has to be installed before executing the program**
* **An existing account in CodeChef.com**

`>> pip3 install selenium`

`>> pip3 install webdriver-manager`

### Usage:
`>> python codechef_selenium_script.py`

### I/O:
```
Enter codechef username: $(username)

Enter codechef password: $(password)

Enter your solution filename with extension(file must be present in the same directory): $(solution)

Successfully submitted the solution! 
```


