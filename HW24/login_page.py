from selenium.webdriver.common.by import By
from selenium import webdriver
from .base_page_my import BasePage


class Login_Locators:
    email_adresse_input = (By.XPATH, "//input[@id='email']")
    password_input_box = (By.XPATH, "//input[@id='passwd']")
    sing_in_button = (By.XPATH, "//button[@id='SubmitLogin']")


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://automationpractice.pl/index.php?controller=authentication&back=my-account"

    def login_page_is_loaded(self):
        assert "Login - My Store" in self.webdriver.title

    def enter_email_create(self):
        self.enter_text(Login_Locators.email_adresse_create, email)

    def submit_sing_in(self):
        self.click(Login_Locators.sing_in_button)

    def login_user_enter(self):
        email = '7777777@gmail.com'
        password = '123456789'
        self.enter_text(Login_Locators.email_adresse_input, email)
        self.enter_text(Login_Locators.password_input_box, password)

    def account_is_loaded(self):
        assert self.get_title() == "My account - My Store"
