from selenium.webdriver.common.by import By
from selenium import webdriver
from .base_page_my import BasePage


class Shopping_Cart_Locators:
    button_shopping_cart = (By.CSS_SELECTOR, '[class="shopping_cart"]')
    cart_shopping_is_empty = (By.XPATH, "//p[text()='Your shopping cart is empty.']")
    button_return_to_home = (By.XPATH, '//i[@class="icon-home"]')


class Shopping_Cart_Page(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = "http://automationpractice.pl/index.php?controller=order"

    def shopping_cart_page_is_loaded(self):
        assert "Order - My Store" in self.webdriver.title

    def shopping_cart_is_empty(self):
        return self.wait_for_element(Shopping_Cart_Locators.cart_shopping_is_empty)

    def is_cart_empty(self) -> bool:
        return self.shopping_cart_is_empty().text == 'Your shopping cart is empty.'

    def go_to_home(self):
        self.click(Shopping_Cart_Locators.button_return_to_home)
