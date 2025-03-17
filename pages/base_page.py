from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def close_cookie_popup(self):
        """Closes the cookie acceptance popup."""
        cookie_accept_button = (By.ID, "sp-cc-accept")  # ID of the cookie acceptance button
        try:
            self.click_element(cookie_accept_button)
            print("Cookies accepted.")
        except NoSuchElementException:
            print("Cookie acceptance popup not found or already closed.")

    def find_element(self, locator):
        """Finds the item with the given locator."""
        try:
            element = self.driver.find_element(*locator)
            return element
        except NoSuchElementException:
            print(f"Item {locator} not found!")
            return None

    def click_element(self, locator, timeout=10):
        """Clicks the specified item, but waits for the item to appear first."""
        element = self.wait_for_element_visible(locator, timeout)
        if element:
            element.click()
        else:
            print(f"No item found to click on: {locator}")

    def send_keys_to_element(self, locator, text):
        """Sends text to the element with the given locator."""
        element = self.find_element(locator)
        if element:
            element.clear()  # Clear previously entered text
            element.send_keys(text)

    def wait_for_element_visible(self, locator, timeout=10):
        """Checks whether the element is visible."""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)  # Waits for the item to appear
            )
            return element
        except TimeoutException:
            print(f"The element {locator} was not visible within {timeout} seconds.")
            return None

    def get_text(self, locator):
        """Returns the text at the given locator."""
        element = self.find_element(locator)
        return element.text if element else None

    def get_current_url(self):
        """Returns the current URL."""
        return self.driver.current_url

    def is_element_present(self, locator):
        """Checks if the element with the given locator is on the page."""
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False