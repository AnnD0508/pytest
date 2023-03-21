from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_sitethede(browser):
    chrome = webdriver.Chrome()
    chrome.implicitly_wait(20)
    chrome.get('http://thedemosite.co.uk/savedata.php')
    username = chrome.find_element(By.NAME, 'username')
    username.send_keys('babaжaba')
    password = chrome.find_element(By.NAME, 'password')
    password.send_keys('12345678')
    save_button = chrome.find_element(By.NAME, 'FormsButton2')
    save_button.click()








