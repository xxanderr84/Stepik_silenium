from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "book")
    text_wait = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()
    input_x = browser.find_element(By.ID, "input_value")
    input_value = browser.find_element(By.ID, "answer")
    res = calc(input_x.text)
    input_value.send_keys(res)
    btn = browser.find_element(By.ID, 'solve')
    btn.click()
finally:
    time.sleep(10)
    browser.quit()
