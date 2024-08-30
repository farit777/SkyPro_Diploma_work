import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import pytest
import allure
from pages.MainPage import MainPage
from pages.MoviesPage import MoviesPage


@allure.suite("UI тестирование КИНОПОИСК")
@allure.title("Ui: Проверка перехода на страницу фильмов")
def test_navigate_to_movies(self, main_page: MainPage):
    with allure.step("Перейти на страницу 'Фильмы'"):
        main_page.go_to_movies()
    with allure.step("Проверить загрузку страницы"):        
        assert main_page.browser.current_url == 'https://www.kinopoisk.ru/lists/categories/movies/1/'

@allure.suite("UI: тестирование КИНОПОИСК")
@allure.title("UI: Проверка жанров на странице фильмов")
def test_check_genres(self, movies_page: MoviesPage):
    with allure.step("Перейти на страницу 'Жанры'"):
        movies_page.open_genres()
    with allure.step("Проверить загрузку страницы"):
        assert movies_page.browser.current_url == 'https://www.kinopoisk.ru/lists/categories/movies/8/'

@allure.suite("UI: тестирование КИНОПОИСК")
@allure.title("UI: Проверка 'страны' на странице фильмов")
def test_check_countries(self, movies_page: MoviesPage):
    with allure.step("Перейти на страницу 'Страны'"):
        movies_page.open_countries()
    with allure.step("Проверить загрузку страницы"):
        assert movies_page.browser.current_url == 'https://www.kinopoisk.ru/lists/categories/movies/9/'

@allure.suite("UI: тестирование КИНОПОИСК")
@allure.title("UI: Проверка 'Годы' на странице фильмов")
def test_check_years(self, movies_page: MoviesPage):
    with allure.step("Перейти на страницу 'Годы'"):
        movies_page.open_years()
    with allure.step("Проверить загрузку страницы"):
        assert movies_page.browser.current_url == "a[href='/lists/categories/movies/7/']"

@allure.suite("UI: тестирование КИНОПОИСК")
@allure.title("UI: Проверка 'критика' на странице фильмов")
def test_check_critics(self, movies_page: MoviesPage):
    with allure.step("Перейти на страницу 'Критика'"):
        movies_page.open_critics()
    with allure.step("Проверить загрузку страницы"):
        assert movies_page.browser.current_url == "a[href='/lists/categories/movies/18/']"

@allure.suite("UI: тестирование КИНОПОИСК")
@allure.title("UI: Проверка 'сериалы' на странице фильмов")
def test_check_series(self, movies_page: MoviesPage):
    with allure.step("Перейти на страницу 'Сериалы'"):
        movies_page.open_series()
    with allure.step("Проверить загрузку страницы"):
        assert movies_page.browser.current_url == "a[href='/lists/categories/movies/3/']"

@allure.suite("UI; тестирование КИНОПОИСК")
@allure.title("UI: Проверка 'сборы' на странице фильмов")
def test_check_box_office(self, movies_page: MoviesPage):
    with allure.step("Перейти на страницу 'Поступления'"):
        movies_page.open_incoming()
    with allure.step("Проверить загрузку страницы"):
        assert movies_page.browser.current_url == "a[href='/lists/categories/movies/5/']"
