import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

elem_x = browser.find_element(By.ID, 'input_value').text
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("window.scrollBy(0, 100);")
answer = browser.find_element(By.ID, 'answer')


def calc(elem_x):
    return str(math.log(abs(12 * math.sin(int(elem_x)))))


answer.send_keys(calc(elem_x))
browser.find_element(By.ID, 'robotCheckbox').click()
browser.find_element(By.ID, 'robotsRule').click()

button.click()

time.sleep(5)
