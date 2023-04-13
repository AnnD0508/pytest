from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from .home_page import Home_Page
from .login_page import LoginPage
from .cart_shopping import Shopping_Cart_Page


class Test_Web_Page:
    def test_from_home_go_to_shopping_cart(self, browser):
        home_page = Home_Page(browser)
        cart_shopping = Shopping_Cart_Page(browser)
        home_page.open()
        home_page.page_is_loaded()
        home_page.click_to_shopping_cart()
        cart_shopping.open()
        cart_shopping.shopping_cart_page_is_loaded()

    def test_from_home_go_to_login(self, browser):
        home_page = Home_Page(browser)
        login_page = LoginPage(browser)
        home_page.open()
        home_page.page_is_loaded()
        home_page.click_to_sing_in()
        login_page.open()
        login_page.login_page_is_loaded()

    def test_shopping_cart_is_empty(self, browser):
        home_page = Home_Page(browser)
        cart_shopping = Shopping_Cart_Page(browser)
        home_page.open()
        home_page.page_is_loaded()
        home_page.click_to_shopping_cart()
        cart_shopping.open()
        cart_shopping.shopping_cart_page_is_loaded()
        cart_shopping.is_cart_empty()

    def test_return_to_home_from_sgopping_cart(self, browser):
        home_page = Home_Page(browser)
        cart_shopping = Shopping_Cart_Page(browser)
        home_page.open()
        home_page.page_is_loaded()
        home_page.click_to_shopping_cart()
        cart_shopping.open()
        cart_shopping.shopping_cart_page_is_loaded()
        cart_shopping.is_cart_empty()
        cart_shopping.go_to_home()
        home_page.page_is_loaded()

    def test_clickable_button_tshirts(self, browser):
        home_page = Home_Page(browser)
        home_page.open()
        home_page.page_is_loaded()
        home_page.click_button_Tshirt()
        home_page.page_Tshirt()

    def test_clickable_button_dresess(self, browser):
        home_page = Home_Page(browser)
        home_page.open()
        home_page.page_is_loaded()
        home_page.click_button_dresses()
        home_page.page_dresses()

    def test_user_authorization(self, browser):
        home_page = Home_Page(browser)
        login_page = LoginPage(browser)
        home_page.open()
        home_page.page_is_loaded()
        home_page.click_to_sing_in()
        login_page.open()
        login_page.login_page_is_loaded()
        login_page.login_user_enter()
        login_page.submit_sing_in()
        login_page.account_is_loaded()
