from typing import Any
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

def test_checkbox(browser):
    chrome = browser
    chrome.get('http://the-internet.herokuapp.com/dynamic_controls')
    WebDriverWait(chrome, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                   '[type=checkbox][label=blah]'))).click()

    WebDriverWait(chrome, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                '[type=button][onclick="swapCheckbox()"]'))).click()

    WebDriverWait(chrome, 20).until(EC.presence_of_element_located([By.XPATH,
                                                                    '//p[text()="It\'s gone!"]']))

    assert WebDriverWait(chrome, 20).until_not(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                      '[type=checkbox][label=blah]')))

    assert WebDriverWait(chrome, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                    'input[type="text"]'))).is_displayed()

    WebDriverWait(chrome, 10).until(EC.presence_of_element_located([By.XPATH,
                                                                     '//button[text()="Enable"]'])).click()

    WebDriverWait(chrome, 10).until(EC.presence_of_element_located([By.XPATH,
                                                                   '//p[text()="It\'s enabled!"]']))

    assert WebDriverWait(chrome, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                           'input[type="text"]'))).is_enabled()

