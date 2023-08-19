from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(elem):
    return str(math.log(abs(12*math.sin(int(elem)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    browser.find_element(By.ID, 'book').click()
    browser.execute_script("window.scrollBy(0, 100);")

    elem = browser.find_element(By.ID, 'input_value').text
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(calc(elem))
    browser.find_element(By.ID, 'solve').click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
