
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
# opening whatsapp web
driver.get('http://web.whatsapp.com')

#asking user input
name = input('Please input name of user/group you want to send message to')
message = input('Enter the message you wish to send: ')
rep = int(input('Enter number of times message is to be sent : '))

# Manually need to scan the code
input('Press any key after scanning')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
time.sleep(1)
# locating the resp classes and elements
t = driver.find_element_by_class_name("_3uMse")
time.sleep(1)
for j in range(rep):
    k = t.send_keys(message)
    driver.find_element_by_class_name('_1U1xa').click()
