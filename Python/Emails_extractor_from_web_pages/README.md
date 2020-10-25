## Introduction
Emails_extractor is a python script wihih eill extract all email in a web page using regular expressions
This script will crawl through web page and retrive all emails in a web page and store them in a excel sheet

## Libraries Used
* Beauty soup - To retrive and process html data
* urllib - To send request to web server
* XLWT - To save retrived data to excel sheet
* Date time - To get current date and time
* re - To use regular expressions

## Setup
Initially we have to install all required libraries
Install all require libraries using command
```bash 
pip install -r"requirements.txt"
```

## Usage
Run script using python command in your command prompt/terminal
```bash 
python emails_extractor.py
```
## Sample output 
#### Input
![inp](https://user-images.githubusercontent.com/48166328/97102451-a8237400-16cb-11eb-8c70-a3352d23dcb9.png)
#### Output
![opt](https://user-images.githubusercontent.com/48166328/97102454-a9ed3780-16cb-11eb-89f3-5b8a58fdca9e.png)


