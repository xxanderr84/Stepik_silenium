from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    input_x = browser.find_element(By.ID, "input_value")
    input_value = browser.find_element(By.ID, "answer")
    res = calc(input_x.text)
    input_value.send_keys(res)
    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click()
finally:
    time.sleep(10)
    browser.quit()