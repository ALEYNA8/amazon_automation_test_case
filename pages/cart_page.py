from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    # General Locators
    CART_HEADER = (By.CLASS_NAME, "sc-cart-header")  # Cart header
    CART_ITEM = (By.CLASS_NAME, "sc-list-item-content")  # Item in cart
    REMOVE_ITEM = (By.CLASS_NAME, "sc-action-delete")  # Delete product button
    EMPTY_CART_MESSAGE = (By.CLASS_NAME, "sc-your-amazon-cart-is-empty")  # Cart empty message
    MAIN_LOGO = (By.ID, "nav-logo") # Amazon homepage logo

    def is_cart_header_present(self):
        """Validates Cart Title."""
        return self.get_text(self.CART_HEADER)

    def is_product_in_cart(self):
        """Checks if there are any products in the cart."""
        return self.is_element_present(self.CART_ITEM)

    def remove_product_from_cart(self):
        """Deletes the product from the cart."""
        self.click_element(self.REMOVE_ITEM)

    def is_cart_empty(self):
        """Checks if the cart is empty."""
        return not self.is_element_present(self.EMPTY_CART_MESSAGE)

    def click_main_logo(self):
        """Returns to the home page."""
        self.click_element(self.MAIN_LOGO)

    def open_cart_page(self):
        """Opens the cart page."""
        self.click_element((By.ID, "nav-cart"))

    def check_product_in_cart(self, expected_name):
        """Verifies whether the correct product is in the cart."""
        product_text = self.get_text(self.CART_ITEM)
        return expected_name.lower() in product_text.lower()
