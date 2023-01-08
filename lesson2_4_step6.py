import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x = x_element.text
    print(x)
    y = calc(x)
    option1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    option1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()