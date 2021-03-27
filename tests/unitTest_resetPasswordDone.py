import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class ll_testcase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):

        driver = self.driver
        driver.maximize_window()

        email = "rqueztech@gmail.com"

        # Open up the main website
        driver.get("http://127.0.0.1:8000/")
        time.sleep(5)

        # Click on the Login Link
        driver.find_element_by_xpath("/html/body/div/div/div[1]/ul/li[4]/a").click()
        time.sleep(5)

        # Click Forgot Password
        driver.find_element_by_xpath("/html/body/div/div/div[2]/p[2]/a").click()
        time.sleep(5)

        # Create variable to store get element by id. Send email key to the element's id (TextBox)
        elem = driver.find_element_by_id("id_email")
        elem.send_keys(email)
        time.sleep(5)

        try:
            driver.find_element_by_xpath("/html/body/div/div/div[2]/form/input[2]").click()
            print("Reset Password Page Works")
            assert True

        except NoSuchElementException:
            self.fail("Reset Password Page Error")
            assert False

        time.sleep(5)

def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()