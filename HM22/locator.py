from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_search_button(browser):
    chrome = browser
    chrome.implicitly_wait(20)
    chrome.get('https://baraholka.onliner.by/')
    submit_button = chrome.find_element(By.XPATH, '//*[@class="b-fleamarket-button"]')
    submit_button.click()

def test_search_button(browser):
    chrome = browser
    chrome.implicitly_wait(20)
    chrome.get('https://baraholka.onliner.by/')
    search_category = chrome.find_element(By.XPATH, '//a[text()="Видеокарты"]//following-sibling::sup')
    search_category.click()

def test_search_button(browser):
    chrome = browser
    chrome.implicitly_wait(20)
    chrome.get('https://baraholka.onliner.by/')
    search_category_dress = chrome.find_element(By.XPATH, '//a[text()="Платья"]//following-sibling::sup')
    search_category_dress.click()

