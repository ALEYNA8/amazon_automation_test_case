import unittest
from selenium import webdriver
from pages.home_page import HomePage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


class TestCheckAddToCartAmazon(unittest.TestCase):

    def setUp(self):
        """Makes the necessary adjustments before the test."""
        self.driver = webdriver.Chrome()  # Start Chrome driver
        self.driver.maximize_window() # Maximizes the browser window to ensure all elements are visible
        self.driver.get('https://www.amazon.com.tr/')  # Go to Amazon page
        self.driver.implicitly_wait(20)  # 20 seconds wait time if page and elements load slowly

    def test_add_product_to_cart(self):
        """Product adding to cart."""
        home_page = HomePage(self.driver) # We go to the home page
        self.assertTrue(home_page.is_on_home_page())  # We verify that we are on the home page

        # We search for 'Samsung'
        home_page.search_for_item("samsung")
        self.assertTrue(home_page.get_search_results())  # Verify that search results appear

        # We are moving to page 2
        category_page = CategoryPage(self.driver)
        category_page.go_to_second_page()
        self.assertTrue(category_page.is_second_page_loaded())  # We verify that we are on page 2

        # Click on the 3rd product from the top
        product_page = ProductPage(self.driver)
        product_page.select_third_product()
        self.assertTrue(product_page.verify_product_page())  # We verify that we went to the product page

        # We add the product to the cart
        product_page.add_to_cart()
        self.assertTrue(product_page.verify_product_added_to_cart()) # We verify that the product has been added to the cart

        # We go to the cart page
        cart_page = CartPage(self.driver)
        cart_page.open_cart_page()
        self.assertTrue(cart_page.is_cart_header_present())  # Verify that the cart title is visible

        # We make sure that the right product is in the cart
        self.assertTrue(cart_page.check_product_in_cart("samsung"))

        # We delete the product from the cart
        cart_page.remove_product_from_cart()
        self.assertTrue(cart_page.is_cart_empty())  # Verify that the cart is empty

        # Returning to the home page
        cart_page.click_main_logo()
        self.assertTrue(home_page.is_on_home_page())  # We verify that we are on the home page

    def tearDown(self):
        """Closes the browser after the test."""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()