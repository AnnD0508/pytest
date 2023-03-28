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


def test_iframes(browser):
    chrome = browser
    chrome.get('http://the-internet.herokuapp.com/iframe')
    frame_locator = (By.XPATH, '//iframe[@id="mce_0_ifr"]')
    WebDriverWait(chrome, 10).until(EC.frame_to_be_available_and_switch_to_it(frame_locator))
    WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                    '//p[text()="Your content goes here."]')))
    assert chrome.find_element(By.XPATH, '//p[text()="Your content goes here."]').text == "Your content goes here."
    chrome.switch_to.default_content()

