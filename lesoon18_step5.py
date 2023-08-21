import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

smth_text = ""
id_steps = [
    236895,
    236896,
    236897,
    236898,
    236899,
    236903,
    236904,
    236905
]


@pytest.fixture(scope="session")
def result():
    print(smth_text)


@pytest.mark.parametrize('id_step', id_steps)
def test_lesson18_step6(result, browser, id_step):
    global smth_text
    link = f"https://stepik.org/lesson/{id_step}/step/1"
    browser.get(link)
    browser.find_element(By.ID, "ember33").click()
    browser.find_element(By.NAME, 'login').send_keys('your_login')
    browser.find_element(By.NAME, 'password').send_keys('your_password')
    browser.find_element(By.CLASS_NAME, 'sign-form__btn').click()
    time.sleep(5)
    inp = browser.find_element(By.TAG_NAME, 'textarea')
    inp.send_keys(str(math.log(int(time.time()))))
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    ).click()
    check = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
    if check != 'Correct!':
        smth_text += check
        print(smth_text)
        assert check == 'Correct!'
