from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input_x = browser.find_element(By.ID, "input_value")
    input_value = browser.find_element(By.ID, "answer")
    res = calc(input_x.text)
    input_value.send_keys(res)
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()
    robot_radio = browser.find_element(By.ID, "robotsRule")
    btn = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    robot_radio.click()
    btn.click()
finally:
    time.sleep(20)
    browser.quit()
