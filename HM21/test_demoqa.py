from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_sitedemo(browser):
    chrome = browser
    chrome.implicitly_wait(20)
    chrome.get('https://demoqa.com/text-box')
    fullname = chrome.find_element(By.ID, 'userName')
    fullname.send_keys('babaжaba')
    mail_box = chrome.find_element(By.ID, 'userEmail')
    mail_box.send_keys('tesddemo@gmail.com')
    current_address_box = chrome.find_element(By.ID, 'currentAddress')
    current_address_box.send_keys('planetVenera')
    permanent_address_box = chrome.find_element(By.ID, 'permanentAddress')
    permanent_address_box.send_keys('planetMars')
    submit_button = chrome.find_element(By.ID, 'submit')
    submit_button.click()