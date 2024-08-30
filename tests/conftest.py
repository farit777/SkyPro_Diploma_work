import pytest
from selenium import webdriver
from pages.MainPage import MainPage
from pages.MoviesPage import MoviesPage

@pytest.fixture(scope='module')
def browser():
    options = webdriver.ChromeOptions()
    options.browser_version = 'stable'
    options.platform_name = 'any'
    #options.accept_insecure_certs = True
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(4)
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture(scope='module')
def movies_page(browser):
    movies_page = MoviesPage(browser)
    movies_page.open()
    movies_page.close_modal_if_open()  # Закрытие модального окна, если открыто
    yield movies_page

@pytest.fixture(scope='function')
def main_page(browser):
    main_page = MoviesPage(browser)
    main_page.open()
    main_page.close_modal_if_open()  # Закрытие модального окна, если открыто
    yield main_page




# def FireFox_options():
#     options = webdriver.FirefoxOptions()
#     options.browser_version = 'stable'
#     driver = webdriver.Firefox(options=options)
