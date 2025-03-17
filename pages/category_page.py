from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class CategoryPage(BasePage):
    # Locators
    second_page_locator = (By.XPATH, "//a[@aria-label='2 rating']")
    cookie_accept_button_locator = (By.ID, "sp-cc-accept")

    def go_to_second_page(self):
        """Scrolls down to the 'Page 2' button and clicks it."""
        # Click the cookie acceptance button (if any)
        try:
            cookie_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.cookie_accept_button_locator)
            )
            cookie_button.click()  # Accept cookies
            print("Cookies accepted.")
        except TimeoutException:
            print("No cookie popup found.")

        # Scroll down to the 'Page 2' button
        try:
            second_page_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.second_page_locator)
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", second_page_button)
            print("Scrolled to the 'Page 2' button.")

            # Click on the button
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.second_page_locator)
            ).click()
            print("Clicked on the 'Page 2' button.")
        except TimeoutException:
            print("ERROR: 'Page 2' button not found or not clickable.")

    def verify_second_page(self):
        """Confirms that we are on page 2."""
        return "page=2" in self.driver.current_url

    def is_second_page_loaded(self):
        """Checks whether page 2 has loaded successfully."""
        try:
            element = self.driver.find_element(By.XPATH, "//span[contains(text(), '2')]")
            return element.is_displayed()
        except:
            return False