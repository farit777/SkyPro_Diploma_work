import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import allure
from pages.MainApi import MainApi

api = MainApi()

@allure.suite("API: тестирование КИНОПОИСК")
@allure.title("API: Список фильмов по названию")
def test_get_list_movies_by_title():
    with allure.step("Получить список список фильмов по названию"):
        movie_title = "Другие"
        result = api.get_list_movies_by_title(movie_title)
    with allure.step("Проверить, что список не пустой"):
        assert len(result) > 0

@allure.suite("API: тестирование КИНОПОИСК")
@allure.title("API: Список стран")
def test_get_list_countries():
    with allure.step("Получить список стран"):
        field_name = "countries.name"
        result = api.get_list_countries(field_name)
    with allure.step("Проверить, что список не пустой"):    
        assert len(result) > 0

@allure.suite("API: тестирование КИНОПОИСК")
@allure.title("API: Список жанров")
def test_get_list_genres():
    with allure.step("Получить список жанров"):
        field_name = "genres.name"
        result = api.get_list_genres(field_name)
    with allure.step("Проверить, что список не пустой"):
        assert len(result) > 0

@allure.suite("API: тестирование КИНОПОИСК")
@allure.title("API: Список сезонов")
def test_get_list_seasons():
    with allure.step("Получить список жанров"):
        result = api.get_list_seasons()
    with allure.step("Проверить, что список не пустой"):
        assert len(result) > 0

@allure.suite("API: тестирование КИНОПОИСК")
@allure.title("API: Список фильмов по автору")
def test_get_list_movies_by_actor_name():
    with allure.step("Получить список фильмов по автору"):
        actor_name = "Абдулов"
        result = api.get_list_movies_by_actor_name(actor_name)
    with allure.step("Проверить, что список не пустой"):
        assert len(result) > 0

@allure.suite("API: тестирование КИНОПОИСК")
@allure.title("API: Универсальный поиск фильмов с фильтрами")
def test_universal_movie_search_with_filters():
    with allure.step("Получить список фильмов по фильтрам"):
        select_fields = "name"
        result = api.universal_movie_search_with_filters(select_fields)
    with allure.step("Проверить, что список не пустой"):
        assert len(result) > 0