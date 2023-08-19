import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

elem = browser.find_element(By.ID, 'input_value')
elemValue = elem.text
answer = browser.find_element(By.ID, 'answer')
checkbx = browser.find_element(By.ID,'robotCheckbox')
checkbx.click()
radiobtn = browser.find_element(By.ID,'robotsRule')
radiobtn.click()
btn = browser.find_element(By.TAG_NAME, 'button')

def calc(elemValue):
  return str(math.log(abs(12*math.sin(int(elemValue)))))

answer.send_keys(calc(elemValue))

btn.click()

time.sleep(3)