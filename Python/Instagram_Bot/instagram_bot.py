import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from secrets import username, password 

def open_instagram(driver):
    driver.get("https://instagram.com")

def login(driver):
    sleep(2)
    driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    sleep(5)
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    sleep(2)
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    sleep(2)

def get_unfollowers(driver):
    driver.find_element_by_xpath("//a[contains(@href,'{}')]".format(username)).click()
    sleep(5)
    driver.find_element_by_xpath("//a[contains(@href,'{}/following')]".format(username)).click()
    sleep(2)
    following = get_names(driver)
    driver.find_element_by_xpath("//a[contains(@href,'{}/followers')]".format(username)).click()
    sleep(2)
    followers = get_names(driver)
    not_following_back = [user for user in following if user not in followers]
    return not_following_back

def get_names(driver):
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
    driver = webdriver.Chrome(ChromeDriverManager().install())
    open_instagram(driver)
    login(driver)
    unfollowers = get_unfollowers(driver)
    print("Total unFollowers : {}\n".format(len(unfollowers)))
    for i in unfollowers:
        print(i)
        print("\n")
    driver.close()
    

if __name__ == "__main__":
    main()