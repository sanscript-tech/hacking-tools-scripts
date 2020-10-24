import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

username = ""
password = ""
driver = None 

def open_instagram():
    # set url to driver
    driver.get("https://instagram.com")

def login():
    sleep(2)
    # find username field
    driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
    # find password field
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    # find Log in button
    driver.find_element_by_xpath("//button[@type='submit']").click()
    sleep(5)
    # click on not now for saving password
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    sleep(2)
    # click on not now for turning on notifications
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    sleep(2)

def get_unfollowers():
    # go to profile page
    driver.find_element_by_xpath("//a[contains(@href,'{}')]".format(username)).click()
    sleep(5)
    # click on following 
    driver.find_element_by_xpath("//a[contains(@href,'{}/following')]".format(username)).click()
    sleep(2)
    # Get the list of following accounts
    following = get_names(driver)
    # click on followers
    driver.find_element_by_xpath("//a[contains(@href,'{}/followers')]".format(username)).click()
    sleep(2)
    # Get the list of followers accounts
    followers = get_names(driver)
    # compare both lists to find the difference accounts 
    not_following_back = [user for user in following if user not in followers]
    return not_following_back

def get_names():
    # keep scrolling till the end of scroll view
    scroll_box = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
    last_ht, ht = 0, 1
    while last_ht != ht:
        last_ht = ht
        sleep(1)
        ht = driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight); 
            return arguments[0].scrollHeight;
            """, scroll_box)
    links = scroll_box.find_elements_by_tag_name('a')
    names = [name.text for name in links if name.text != '']
    # close button
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
    return names

def main():
    global username
    global password
    global driver
    # Input from users
    username=input("Enter username:")
    password=input("Enter password:")
    # configuring webdriver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # operations
    open_instagram()
    login()
    unfollowers = get_unfollowers()
    # output
    print("Total unFollowers : {}\n".format(len(unfollowers)))
    for i in unfollowers:
        print(i)
        print("\n")
    driver.close()
    

if __name__ == "__main__":
    main()
