from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")
    summ = int(num1.text) + int(num2.text)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(summ))
    btn = browser.find_element(By.TAG_NAME, "button")
    btn.click()
finally:
    time.sleep(30)
    browser.quit()
