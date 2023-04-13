import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.webdriver = driver
        self.url: str = ''

    def open_url(self, url):
        self.webdriver.get(self.url)

    def open(self):
        self.open_url(url=self.url)

    def wait_for_element(self, locator, timer=10):
        return WebDriverWait(self.webdriver, timer).until(EC.visibility_of_element_located(locator))

    def wait_for_elements(self, locator, timer=10):
        return WebDriverWait(self.webdriver, timer).until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator):
        self.wait_for_element(locator).click()

    def get_title(self):
        return self.webdriver.title

    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)
