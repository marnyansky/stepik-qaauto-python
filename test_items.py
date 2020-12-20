import time


def test_button_add_to_cart_is_displayed(browser):
    # Открытие страницы
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)

    # Ожидание полной загрузки страницы
    time.sleep(30)

    assert browser.find_element_by_class_name("btn-add-to-basket").is_displayed(), \
        "Кнопка добавления товара в корзину отсутствует на странице"
