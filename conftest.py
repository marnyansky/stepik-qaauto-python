import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Функция изменения языка пользовательского интерфейса через CLI
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='es',
                     help='Choose language (default is Hispanic)')


@pytest.fixture(scope="function")
def browser(request):
    # Задание языка пользовательского интерфейса (UI) на основе значения из набора опций
    options_set = Options()
    user_language = request.config.getoption("language")
    options_set.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    # Запуск браузера с набором опций
    print("\nStarting Chrome browser for testing...")
    browser = webdriver.Chrome(options=options_set)
    yield browser

    # Закрытие браузера - завершение теста
    print("\nQuitting browser...")
    browser.quit()
