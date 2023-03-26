from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_form(browser):
    chrome= browser
    chrome.implicitly_wait(20)
    chrome.get('https://ultimateqa.com/filling-out-forms/')
    name_field = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_name_0"]')
    name_field.send_keys('kuku')
    message_field = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_message_0"]')
    message_field.send_keys('Hi, from kuku!')
    time.sleep(3)
    submit_button = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_name_0"]/ancestor::form//button')
    submit_button.submit()
    result_message = chrome.find_element(By.XPATH,  '//p[text()="Thanks for contacting us"]').text
    assert result_message  == "Thanks for contacting us"


def test_form_2(browser):
    chrome= browser
    chrome.implicitly_wait(20)
    chrome.get('https://ultimateqa.com/filling-out-forms/')
    name_field_2 = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_name_0"]')
    name_field_2.send_keys('kuku')
    time.sleep(3)
    submit_button_2 = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_name_0"]/ancestor::form//button')
    submit_button_2.click()
    result_message_2 = chrome.find_element(By.XPATH,  '//p[text()="Please, fill in the following fields:"]').text
    assert result_message_2  == "Please, fill in the following fields:"


def test_form_3(browser):
    chrome= browser
    chrome.implicitly_wait(20)
    chrome.get('https://ultimateqa.com/filling-out-forms/')
    message_field = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_message_0"]')
    message_field.send_keys('Hi, are you sure?')
    time.sleep(3)
    submit_button = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_name_0"]/ancestor::form//button')
    submit_button.click()
    result_message = chrome.find_element(By.XPATH,  '//p[text()="Please, fill in the following fields:"]').text
    assert result_message  == "Please, fill in the following fields:"
