import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num_1 = browser.find_element(By.ID, 'num1').text
num_2 = browser.find_element(By.ID, 'num2').text
btn = browser.find_element(By.TAG_NAME, 'button')


sumTerms = int(num_1) + int(num_2)
result = str(sumTerms)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(result)

btn.click()

time.sleep(5)
