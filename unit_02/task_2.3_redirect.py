from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    new_window = browser.window_handles[1]
    old_window = browser.window_handles[0]
    browser.switch_to.window(new_window)
    input_x = browser.find_element(By.ID, "input_value")
    input_value = browser.find_element(By.ID, "answer")
    res = calc(input_x.text)
    input_value.send_keys(res)
    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click()
finally:
    time.sleep(20)
    browser.quit()
