from selenium import webdriver
from selenium.webdriver.common.by import By


def test_goog_search():
    chrome = webdriver.Chrome()
    url = 'https://www.google.com/search?'
    chrome.get(url=url)
    search_box = chrome.find_element(By.ID, 'L2AGLb').click()
    search_box = chrome.find_element(By.CLASS_NAME, 'gLFyf')
    search_box.send_keys('python 3.10')
    search_box.submit()
    assert 'python 3.10' in chrome.title
    chrome.close()