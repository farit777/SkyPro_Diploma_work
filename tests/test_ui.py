import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import allure
from pages.MoviesPage import MoviesPage

@allure.suite("UI: тестирование КИНОПОИСК")
@allure.title("UI: Проверка жанров на странице фильмов")
def test_check_genres(movies_page: MoviesPage):
    """
    Функция предназначена для проверки корректности работы страницы жанров на сайте кинообзоров.
    Она выполняет переход на страницу жанров и проверяет, что URL загруженной страницы соответствует ожидаемому значению.
    """
    with allure.step("Перейти на страницу 'Жанры'"):
        movies_page.open_genres()
    with allure.step("Проверить загрузку страницы"):
        assert movies_page.browser.current_url == 'https://www.kinopoisk.ru/lists/categories/movies/8/'

@allure.suite("UI: тестирование КИНОПОИСК")
@allure.title("UI: Проверка 'страны' на странице фильмов")
def test_check_countries(movies_page: MoviesPage):
    """
    Функция предназначена для проверки корректности работы страницы "Страны" на сайте фильмов.
    Она выполняет переход на страницу стран и проверяет, что URL загруженной страницы соответствует ожидаемому значению.
    """
    with allure.step("Перейти на страницу 'Страны'"):
        movies_page.open_countries()
    with allure.step("Проверить загрузку страницы"):
        assert movies_page.browser.current_url == 'https://www.kinopoisk.ru/lists/categories/movies/9/'

@allure.suite("UI: тестирование КИНОПОИСК")
@allure.title("UI: Проверка 'Годы' на странице фильмов")
def test_check_years(movies_page: MoviesPage):
    """
    Функция предназначена для проверки корректности работы страницы "Годы" на сайте фильмов.
    Она выполняет переход на страницу годов и проверяет, что URL загруженной страницы соответствует ожидаемому значению.
    """
    with allure.step("Перейти на страницу 'Годы'"):
        movies_page.open_years()
    with allure.step("Проверить загрузку страницы"):
        assert movies_page.browser.current_url == "https://www.kinopoisk.ru/lists/categories/movies/7/"

@allure.suite("UI: тестирование КИНОПОИСК")
@allure.title("UI: Проверка 'критика' на странице фильмов")
def test_check_critics(movies_page: MoviesPage):
    """
    Функция предназначена для проверки корректности работы страницы "Критика" на сайте фильмов.
    Она выполняет переход на страницу критиков и проверяет, что URL загруженной страницы соответствует ожидаемому значению.
    """
    with allure.step("Перейти на страницу 'Критика'"):
        movies_page.open_critics()
    with allure.step("Проверить загрузку страницы"):
        assert movies_page.browser.current_url == "https://www.kinopoisk.ru/lists/categories/movies/18/"

@allure.suite("UI; тестирование КИНОПОИСК")
@allure.title("UI: Проверка 'сборы' на странице фильмов")
def test_check_box_office(movies_page: MoviesPage):
    """
    Функция `test_check_box_office` предназначена для автоматической проверки корректности работы страницы "Поступления"
    на сайте фильмов. Она выполняет переход на страницу, отображающую сборы фильмов, и проверяет, что URL загруженной
    страницы соответствует ожидаемому значению.
    """
    with allure.step("Перейти на страницу 'Поступления'"):
        movies_page.open_incoming()
    with allure.step("Проверить загрузку страницы"):
        assert movies_page.browser.current_url == "https://www.kinopoisk.ru/lists/categories/movies/5/"
