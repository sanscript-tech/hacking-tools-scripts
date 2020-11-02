# Import statements
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import os

# User input declaration
username = ""
password = ""
solution = ""
driver = None 

def open_codechef():
    # set url to driver
    driver.get("https://www.codechef.com")

def login():
    sleep(2)
    # find username field
    driver.find_element_by_xpath("//*[@id='edit-name']").send_keys(username)
    # find password field
    driver.find_element_by_xpath("//*[@id='edit-pass']").send_keys(password)
    # find Log in button
    driver.find_element_by_xpath("//*[@id='edit-submit']").click()
    sleep(5)

def go_to_problem():
    # Hover over the top bar
    action = ActionChains(driver)
    practice_probelms_dropdown=driver.find_element_by_xpath("//*[@id='menu-302']/a")
    action.move_to_element(practice_probelms_dropdown).perform()
    # Click on Practice problems by difficulty level
    driver.find_element_by_xpath("//*[@id='menu-303']/a").click()
    sleep(2)
    # Click on COVID RUN problem
    driver.find_element_by_xpath("//*[@id='primary-content']/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/div[1]/a").click()
    sleep(5)
    # Click on Submit button
    actions = ActionChains(driver)
    pivot = driver.find_element_by_xpath("//*[@id='ember307']/section/div/h2")
    actions.move_to_element(pivot).perform()
    driver.find_element_by_xpath("//*[@id='problem-statement']/div/a").click()
    sleep(5)

def upload_solution():
    # scroll down to a pivot element
    actions = ActionChains(driver)
    pivot = driver.find_element_by_xpath("//*[@id='edit-submit-1']")
    actions.move_to_element(pivot).perform()
    # click on upload solution button
    solution_path = os.getcwd() + "/"
    driver.find_element_by_xpath("//*[@id='edit-sourcefile']").send_keys(solution_path+solution)
    # Click submit 
    actions.move_to_element(driver.find_element_by_xpath("//*[@id='cc-footer-div']/div[2]")).perform()
    driver.find_element_by_xpath("//*[@id='edit-submit-1']").click()
    sleep(15)


def main():
    global username
    global password
    global solution
    global driver
    # Input from users
    username=input("Enter codechef username: ")
    password=input("Enter codechef password: ")
    solution=input("Enter your solution filename with extension(file must be present in the same directory): ")
    # configuring webdriver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # Automation begins
    open_codechef()
    login()
    go_to_problem()
    upload_solution()
    print("Successfully submitted the solution!")
    driver.close()


if __name__ == "__main__":
    main()
