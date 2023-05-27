from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

class CookieClickerTest(unittest.TestCase):

    def setUp(self):
        # Create browser session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        # Navigate to the application home page
        self.driver.get("http://www.instagram.com")

    #def test_search_by_text(self):
        # Get the search box
        #self.search_box = self.driver.find_element(By.NAME, "q")
        
        # Enter keyword and send it
        #self.search_box.send_keys("instagram")
        #self.search_box.send_keys(Keys.RETURN)
        #self.search_box.submit()

        # Get the list of search results
        #self.assertEqual(1, len(lists))
        #searchresult = self.driver.find_elements(By.CSS_SELECTOR, "#search > div:nth-child(1)")
        #expectedlink = "https://www.instagram.com/?hl=id"
        #for result in searchresult:
            #thelink = result.find_elements(By.CSS_SELECTOR, "a")
            #for href in thelink:
                #listhref = href.get_attribute("href")
                #if expectedlink in listhref:
                    #self.assertEqual(listhref, expectedlink, "There's no link with expected")
        #print(lists)
        

    def test_login(self):
        self.username = self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(1) > div > label > input")
        self.password = self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(2) > div > label > input")
        self.login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')

        username = "USERNAME"
        password = "PASSWORD"

        self.username.send_keys(username)
        self.password.send_keys(password)
        self.login.click()

        sleep(9)

        # Navigate to the Messages Page
        self.driver.get('https://www.instagram.com/direct/inbox/')

        #Not Now for Notifications
        self.notif = self.driver.find_element(By.XPATH, '//button[contains(text(), "Not Now")]')
        self.notif.click()

        sleep(9)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

