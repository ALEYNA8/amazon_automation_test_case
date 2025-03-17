import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):
    base_url = 'https://www.amazon.com.tr/'

    def setUp(self):
        self.driver = webdriver.Chrome() # Start Chrome driver
        self.driver.get(self.base_url)  # Go to Amazon page
        self.driver.implicitly_wait(10)  # 10 seconds cooldown

    def tearDown(self):
        self.driver.quit() # Close the browser at the end of the test
