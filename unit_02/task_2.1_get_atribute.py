import math
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    img_treasure = browser.find_element(By.ID, "treasure")
    input_value = browser.find_element(By.ID, "answer")
    res = calc(img_treasure.get_attribute("valuex"))
    input_value.send_keys(res)
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()
    robot_radio = browser.find_element(By.ID, "robotsRule")
    robot_radio.click()
    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
