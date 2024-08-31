import pytest
from selenium import webdriver
from pages.MoviesPage import MoviesPage

@pytest.fixture(scope='module')
def browser():
    """
    Функция `browser` - это фикстура для тестирования с использованием Selenium WebDriver.
    Фикстура создаёт экземпляр браузера Chrome с заданными параметрами и обеспечивает его корректное завершение после выполнения тестов.
    Возвращаемое значение:
    WebDriver: Возвращает объект WebDriver для браузера Chrome, который можно использовать в тестах.
    """
    options = webdriver.ChromeOptions()
    options.browser_version = 'stable'
    options.platform_name = 'any'
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(4)
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture(scope='module')
def movies_page(browser):
    """
    Функция `movies_page` - это фикстура для тестирования страницы фильмов, используется вместе с Selenium WebDriver.
    Фикстура создаёт экземпляр страницы фильмов и выполняет начальные действия для её подготовки к тестированию.
    Возвращаемое значение:
    MoviesPage: Возвращает объект страницы фильмов, который можно использовать в тестах.
    """
    movies_page = MoviesPage(browser)
    movies_page.open()
    movies_page.close_modal_if_open()  # Закрытие модального окна, если открыто
    yield movies_page






