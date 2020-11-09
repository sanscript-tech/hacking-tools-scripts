#Imports and dependencies
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import requests

#The task of obtaining the instagram profile picture, given username is achieved by using the framework Selenium.
time_wait_ten = 10

def get_profile_picture():
    u_name = input("Enter the instagram username ")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    URL = "https://www.instagram.com/" + u_name
    driver.get(URL)
    time.sleep(time_wait_ten)
    path = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/div/div/div/button/img")
    image_url = (path.get_attribute("src"))
    img_data = requests.get(image_url).content
    with open('instagram_profile.jpg', 'wb') as handler:
            handler.write(img_data)

if __name__ == "__main__":
    get_profile_picture()
