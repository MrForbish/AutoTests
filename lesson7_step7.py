import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

pct = browser.find_element(By.ID, 'treasure')
pct_attr = pct.get_attribute('valuex')
answer = browser.find_element(By.ID, 'answer')
checkbx = browser.find_element(By.ID, 'robotCheckbox')
checkbx.click()
radiobtn = browser.find_element(By.ID, 'robotsRule')
radiobtn.click()
btn = browser.find_element(By.TAG_NAME, 'button')


def calc(pct_attr):
    return str(math.log(abs(12 * math.sin(int(pct_attr)))))


answer.send_keys(calc(pct_attr))

btn.click()

time.sleep(3)
