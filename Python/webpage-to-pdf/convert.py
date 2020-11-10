import pdfcrowd
import sys

## ask input URL from user
URL = input("Please enter the URL of webpage you'd like to convert : ")
User = input("Please enter your pdfcrowd API username ")
KEY = input("Please enter your API key ")
try:
    # Authenticate API and write result to pdf file in current directory
    pdfcrowd.HtmlToPdfClient(User, KEY).convertUrlToFile(URL, 'new.pdf')

except pdfcrowd.Error as why:
    # report the error
    sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))
    # rethrow or handle the exception
    raise
