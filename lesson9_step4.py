import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(1)

new_window= browser.window_handles[1]
browser.switch_to.window(new_window)

elem = browser.find_element(By.ID, 'input_value').text
answer = browser.find_element(By.ID, 'answer')
btn = browser.find_element(By.TAG_NAME, 'button')

def calc(elem):
  return str(math.log(abs(12*math.sin(int(elem)))))

answer.send_keys(calc(elem))

btn.click()

time.sleep(5)

