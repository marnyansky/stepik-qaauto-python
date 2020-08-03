from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Страница
    link = "http://suninjuly.github.io/explicit_wait2.html"

    # Открытие страницы
    browser = webdriver.Chrome()
    browser.get(link)

    # Ожидание, пока цена не снизится до $100
    house_price = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    # Клик по кнопке 'Book'
    book_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.ID, "book"))
        )
    book_button.click()

    # Прокрутка вниз, до значения 'x'
    x_value_element = browser.find_element_by_id("input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_value_element)

    # Получение значения 'x'
    x_value = browser.find_element_by_id("input_value").text

    # Вычисление результата
    res = calc(x_value)

    # Прокрутка до поля ввода результата и ввод результата
    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(str(res))

    # Клик по кнопке 'Submit' 
    submit_button = browser.find_element_by_id("solve")
    submit_button.click()



finally:
    # Ожидание для оценки результатов (10 с)
    time.sleep(10)
    # Закрытие браузера
    browser.quit()
