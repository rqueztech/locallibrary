import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class ll_ATS(unittest.TestCase):
    # setUp function which sets up the webdriver
    def setUp(self):
        # Initiate the selenium Chrome webdriver
        self.driver = webdriver.Chrome()

    # Main test case which tests add groups
    def test_AddGroups(self):
        # Create a variable named "driver"
        driver = self.driver

        # Maximize the browser window
        driver.maximize_window()

        # Use driver to open chrome to the admin login page
        driver.get("http://127.0.0.1:8000/admin")
        time.sleep(5)

        # The username and password (which is an admin account) that will
        # be used for this test case to login to the admin page
        user = "rqueztech"
        pwd = "isqa3900"

        # Create a variable that gets the element id_username by the id, following
        # That we will send the key (user) into the username field
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(5)

        # Create a variable that gets the element id_password by the id, following
        # That we will send the key (pwd) into the username field
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)

        # The following is the equivalent of hitting the enter button after entering
        # The password in the password field. This will log in to the admin page
        elem.send_keys(Keys.RETURN)
        time.sleep(5)

        try:
            # Click on add Users
            driver.find_element_by_xpath("//*[@id=\"content-main\"]/div[1]/table/tbody/tr[2]/td[1]/a").click()
            print("Add+ Users Page Is Running")

        except NoSuchElementException:
            self.fail("Add+ Users Not Working Properly")

        time.sleep(7)

def tearDown(self):
    self.driver.Close()

if __name__ == "__main__":
    unittest.main()