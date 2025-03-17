import unittest
from selenium import webdriver
from pages.home_page import HomePage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

class TestCheckAddToCartAmazon(unittest.TestCase):

    def setUp(self):
        """Test öncesi gerekli ayarlamaları yapar."""
        self.driver = webdriver.Chrome()  # Chrome driver'ı başlat
        self.driver.get('https://www.amazon.com.tr/')  # Amazon sayfasına git
        self.driver.implicitly_wait(10)  # 20 saniye bekleme süresi, sayfa ve öğeler yavaş yüklenirse

    def tearDown(self):
        """Test sonrası tarayıcıyı kapatır."""
        self.driver.quit()

    def test_add_product_to_cart(self):
        """Ürün sepete ekleme işlemi."""
        # Ana sayfaya gidiyoruz
        home_page = HomePage(self.driver)
        self.assertTrue(home_page.is_on_home_page())  # Ana sayfada olduğumuzu doğruluyoruz

        # 'Samsung' araması yapıyoruz
        home_page.search_for_item("samsung")
        self.assertTrue(home_page.get_search_results())  # Arama sonuçlarının göründüğünü doğruluyoruz

        # 2. sayfaya geçiyoruz
        category_page = CategoryPage(self.driver)
        category_page.go_to_second_page()
        self.assertTrue(category_page.is_second_page_loaded())  # 2. sayfada olduğumuzu doğruluyoruz

        # Üstten 3. ürüne tıklıyoruz
        product_page = ProductPage(self.driver)
        product_page.select_third_product()
        self.assertTrue(product_page.verify_product_page())  # Ürün sayfasına gittiğimizi doğruluyoruz

        # Ürünü sepete ekliyoruz
        product_page.add_to_cart()
        self.assertTrue(product_page.verify_product_added_to_cart())  # Ürünün sepete eklendiğini doğruluyoruz

        # Sepet sayfasına gidiyoruz
        cart_page = CartPage(self.driver)
        cart_page.open_cart_page()
        self.assertTrue(cart_page.is_cart_header_present())  # Sepet başlığının göründüğünü doğruluyoruz

        # Sepette doğru ürünün olduğundan emin oluyoruz
        self.assertTrue(cart_page.check_product_in_cart("samsung"))

        # Ürünü sepette siliyoruz
        cart_page.remove_product_from_cart()
        self.assertTrue(cart_page.is_cart_empty())  # Sepetin boş olduğunu doğruluyoruz

        # Ana sayfaya dönüyoruz
        cart_page.click_main_logo()
        self.assertTrue(home_page.is_on_home_page())  # Ana sayfada olduğumuzu doğruluyoruz

if __name__ == "__main__":
    unittest.main()