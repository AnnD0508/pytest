from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_clicker1(browser):
    chrome = browser
    chrome.implicitly_wait(20)
    chrome.get('https://ultimateqa.com/complicated-page/')
    submit_button = chrome.find_element(By.XPATH, '//*[@class="et_pb_row et_pb_row_2 et_pb_row_4col"]')
    submit_button.click()


def test_clicker2(browser):
    chrome = browser
    chrome.implicitly_wait(20)
    chrome.get('https://ultimateqa.com/complicated-page/')
    submit_button2 = chrome.find_element(By.CSS_SELECTOR, ".et_pb_button.et_pb_button_4")
    submit_button2.click()


def test_clicker3(browser):
    chrome = browser
    chrome.implicitly_wait(20)
    chrome.get('https://ultimateqa.com/complicated-page/')
    submit_button2 = chrome.find_element(By.CLASS_NAME, 'et_pb_button_module_wrapper.et_pb_button_4_wrapper')
    submit_button2.click()
