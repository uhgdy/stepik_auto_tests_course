from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math



try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = x_element.get_attribute("valuex")
    print(x)
    y = calc(x)
    option1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    option1.send_keys(y)

    option2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option2.click()

    option3 = browser.find_element(By.CSS_SELECTOR, "input[value='robots']")
    option3.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла