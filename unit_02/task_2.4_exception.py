from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/cats.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_id("button")
finally:
    browser.quit()