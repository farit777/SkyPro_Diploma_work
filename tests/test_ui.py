import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import pytest
import allure
from pages.MainPage import MainPage
from pages.MoviesPage import MoviesPage

@allure.suite("Тестирование сайта Кинопоиск")
class TestKinopoisk:

    @allure.testcase("Тест: Проверка перехода на страницу фильмов")
    def test_navigate_to_movies(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.close_modal_if_open()  # Закрытие модального окна, если открыто
        main_page.go_to_movies()
        assert main_page.browser.current_url == 'https://www.kinopoisk.ru/lists/categories/movies/1/'

    @allure.testcase("Тест: Проверка жанров на странице фильмов")
    def test_check_genres(self, browser):
        movies_page = MoviesPage(browser)
        movies_page.open()
        movies_page.close_modal_if_open()  # Закрытие модального окна, если открыто
        movies_page.open_genres()
        assert movies_page.browser.current_url == 'https://www.kinopoisk.ru/lists/categories/movies/8/'

    @allure.testcase("Тест: Проверка стран на странице фильмов")
    def test_check_countries(self, browser):
        movies_page = MoviesPage(browser)
        movies_page.close_modal_if_open()  # Закрытие модального окна, если открыто
        movies_page.open_countries()
        assert movies_page.browser.current_url == 'https://www.kinopoisk.ru/lists/categories/movies/9/'

    @allure.testcase("Тест: Проверка 'Годы' на странице фильмов")
    def test_check_years(self, browser):
        movies_page = MoviesPage(browser)
        movies_page.close_modal_if_open()  # Закрытие модального окна, если открыто
        movies_page.open_countries()
        assert movies_page.browser.current_url == "a[href='/lists/categories/movies/7/']"

    @allure.testcase("Тест: Проверка критики на странице фильмов")
    def test_check_critics(self, browser):
        movies_page = MoviesPage(browser)
        movies_page.close_modal_if_open()  # Закрытие модального окна, если открыто
        movies_page.open_critics()
        assert movies_page.browser.current_url == "a[href='/lists/categories/movies/18/']"

    @allure.testcase("Тест: Проверка сериалов на странице фильмов")
    def test_check_series(self, browser):
        movies_page = MoviesPage(browser)
        movies_page.close_modal_if_open()  # Закрытие модального окна, если открыто
        movies_page.open_series()
        assert movies_page.browser.current_url == "a[href='/lists/categories/movies/3/']"

    @allure.testcase("Тест: Проверка сборов на странице фильмов")
    def test_check_box_office(self, browser):
        movies_page = MoviesPage(browser)
        movies_page.close_modal_if_open()  # Закрытие модального окна, если открыто
        movies_page.open_incoming()
        assert movies_page.browser.current_url == "a[href='/lists/categories/movies/5/']"
