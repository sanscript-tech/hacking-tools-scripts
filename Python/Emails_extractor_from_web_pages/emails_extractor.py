# Importing required libraries
import urllib.request,urllib.error,urllib.parse
from xlwt import Workbook
from bs4 import BeautifulSoup
from datetime import datetime
import re  

#Tacking URL input from user
url=input("Enter site to get emails\n")
links=[]
while(len(url)==0):
    url=input("Enter site to get emails\n")
try:
    # Sending request to server using BeautifulSoup
    html_data=urllib.request.urlopen(url).read()
    
    #Beautyfying all data to html form 
    soup=BeautifulSoup(html_data,'html.parser')

    #Retriving all anchor tags in html data
    text=soup.get_text()
    emails = re.findall('\S+@\S+', text)

except:
    #Check if any errors
    print("Please check the URL properly")


if(len(emails)==0):
    print("No links to fetch")
else:
    # Tackning workbook
    wb=Workbook()

    #Creaing sheet in workbook
    sheet1 = wb.add_sheet('Links')

    #adding all data in list to excel sheet
    for i in range(0,len(emails)):
        sheet1.write(i,0,emails[i])
    
    #Getting date and time to create file
    data_time=datetime.now()
    current_time = str(data_time.strftime("%H-%M-%S"))
    
    #Adding time to file name and saving file locally
    wb.save('links for '+current_time+'.xls')
    print("Done writing data to excel sheet")