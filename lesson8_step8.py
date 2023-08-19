import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.NAME, 'firstname').send_keys('Петя')
browser.find_element(By.NAME, 'lastname').send_keys('Петухов')
browser.find_element(By.NAME, 'email').send_keys('qwe@as.qe')
button = browser.find_element(By.TAG_NAME, "button")
add_file = browser.find_element(By.ID, 'file')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
add_file.send_keys(file_path)

button.click()

time.sleep(5)
