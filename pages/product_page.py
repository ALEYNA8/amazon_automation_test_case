from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    # We define the locations of the elements within the page
    SEARCH_RESULT_HEADER = (By.ID, "search")  # Search result title
    SECOND_PAGE_BUTTON = (By.LINK_TEXT, "2")  # 2nd page switch button
    THIRD_PRODUCT = (By.XPATH, "(//div[@data-component-type='s-search-result'])[3]")
    PRODUCT_TITLE = (By.ID, "productTitle")  # Product title
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button") # Add to cart button
    CART_CONFIRMATION = (By.CSS_SELECTOR, ".a-size-medium.a-color-success")  # Cart addition confirmation

    def verify_search_results(self):
        """Verifies that search results are accurate."""
        return self.get_text(self.SEARCH_RESULT_HEADER)

    def go_to_second_page(self):
        """Moves to page 2 of search results."""
        self.close_cookie_popup()  # We close the cookie popup
        self.click_element(self.SECOND_PAGE_BUTTON)  # Click on page 2

    def select_third_product(self):
        """Selects the 3rd product from the top and goes to the product page."""
        self.click_element(self.THIRD_PRODUCT)

    def verify_product_page(self):
        """Verifies if it is on the product page."""
        return self.get_text(self.PRODUCT_TITLE)

    def add_to_cart(self):
        """Adds product to cart."""
        self.click_element(self.ADD_TO_CART_BUTTON)

    def verify_product_added_to_cart(self):
        """Verifies that the product was successfully added to the cart."""
        try:
            success_message = self.driver.find_element(By.CSS_SELECTOR, "#sw-atc-details-single-container")
            return success_message.is_displayed()
        except NoSuchElementException:
            return False