from selenium.webdriver.common.by import By
from selenium import webdriver
from .base_page_my import BasePage


class Home_Locators(BasePage):
    button_sing_in = (By.CSS_SELECTOR, '[class="header_user_info"]')
    button_shopping_cart = (By.CSS_SELECTOR, '[class= "shopping_cart"]>a')
    box_search = (By.CSS_SELECTOR,'[id="search_query_top"]')
    submit_search = (By.CSS_SELECTOR,'[class="btn btn-default button-search"]')
    button_dresses = (By.XPATH,'//div/ul[@class]/li/a[text()="Dresses"]')
    button_Tshirt = (By.XPATH, '//ul[@class]/li/a[text()="T-shirts"]')


class Home_Page(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = "http://automationpractice.pl/index.php"

    def page_is_loaded(self):
        assert 'My Store' in self.webdriver.title

    def click_to_sing_in(self):
        self.click(Home_Locators.button_sing_in)

    def click_to_shopping_cart(self):
        self.click(Home_Locators.button_shopping_cart)

    def click_submit_search(self):
        self.click(Home_Locators.submit_search)

    def click_button_dresses(self):
        self.click(Home_Locators.button_dresses)

    def page_dresses(self):
        assert 'Dresses - My Store' in self.get_title()

    def click_button_Tshirt (self):
        self.click(Home_Locators.button_Tshirt)

    def page_Tshirt(self):
        assert 'T-shirts - My Store' in self.get_title()
