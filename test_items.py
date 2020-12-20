import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_button_add_to_cart_is_displayed(browser):
    # Открытие страницы
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)

    # Ожидание появления на странице кнопки добавления товара в корзину
    WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "btn-add-to-basket"))
    )

    # Ожидание, чтобы убедиться визуально
    time.sleep(5)

    assert browser.find_element_by_class_name("btn-add-to-basket").is_displayed(), \
        "Кнопка добавления товара в корзину отсутствует на странице"
