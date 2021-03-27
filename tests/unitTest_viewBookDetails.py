# Unit test file to determine if the Book List page is displayed when the user
# clicks the 'All books' button in the navigation pane of the local library
# application

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):

        driver = self.driver
        driver.maximize_window()

        driver.get("http://127.0.0.1:8000")
        time.sleep(5)
        # assert "Logged in"
        # find 'All books' and click it – note this is all one Python statement
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul/li[2]/a").click()

        time.sleep(5)

        try:
            # Verify Book List exists on new screen after clicking "All books" button
            # attempt to find the 'Logout' button - if found, logged in
            driver.find_element_by_xpath("/html/body/div/div/div[2]/ul/li[1]/a").click()
            time.sleep(5)
            print("Book Details Are Displayed.")
            assert True

        except NoSuchElementException:
            self.fail("Fail. All authors not working properly")
            assert False
            time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
