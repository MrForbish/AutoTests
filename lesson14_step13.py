from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestForLess0n6Step11(unittest.TestCase):
    def test_1(self):

        global browser
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(By.XPATH, "//html/body/div/form/div[1]/div[1]/input")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.XPATH, "//html/body/div/form/div[1]/div[2]/input")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.XPATH, "//html/body/div/form/div[1]/div[3]/input")
            input3.send_keys("123@asd.qwe")
            input4 = browser.find_element(By.XPATH, "//html/body/div/form/div[2]/div[1]/input")
            input4.send_keys("70000000000")
            input5 = browser.find_element(By.XPATH, "//html/body/div/form/div[2]/div[2]/input")
            input5.send_keys("блабла")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

            welcome_text = welcome_text_elt.text

            assert "Congratulations! You have successfully registered!" == welcome_text

        finally:
            time.sleep(3)
            browser.quit()

    def test_2(self):

        global browser
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(By.XPATH, "//html/body/div/form/div[1]/div[1]/input")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.XPATH, "//html/body/div/form/div[1]/div[2]/input")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.XPATH, "//html/body/div/form/div[1]/div[3]/input")
            input3.send_keys("123@asd.qwe")
            input4 = browser.find_element(By.XPATH, "//html/body/div/form/div[2]/div[1]/input")
            input4.send_keys("70000000000")
            input5 = browser.find_element(By.XPATH, "//html/body/div/form/div[2]/div[2]/input")
            input5.send_keys("блабла")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

            welcome_text = welcome_text_elt.text

            assert "Congratulations! You have successfully registered!" == welcome_text

        finally:
            time.sleep(3)
            browser.quit()
