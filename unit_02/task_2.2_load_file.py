from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    first_name.send_keys('Иван')
    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name.send_keys('Иванов')
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys('ivanov@gmail.com')
    file_loader = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file_loader.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(20)
    browser.quit()
