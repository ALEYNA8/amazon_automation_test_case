from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HomePage(BasePage):
    # Locator of the search section
    search_box_locator = (By.ID, "twotabsearchtextbox")

    def __init__(self, driver):
        super().__init__(driver)

    def search_for_item(self, item):
        search_box = self.find_element(self.search_box_locator)
        search_box.send_keys(item)  # Writes the text to be searched
        search_box.submit()  # Presses the search button

    def is_on_home_page(self):
        """If the word "Amazon" is in the url, you are on the home page."""
        current_url = self.get_current_url()
        return "amazon" in current_url

    def get_search_results(self):
        """Returns search results."""
        results_locator = (By.CSS_SELECTOR, "div.s-main-slot div.s-result-item")

        # Let's wait until the search results appear
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located(results_locator)
            )
            results = self.driver.find_elements(*results_locator)  # We get search results
            return len(results) > 0  # If there is a result we return True
        except:
            return False
