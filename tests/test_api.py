import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import allure
from pages.MainApi import MainApi

api = MainApi()

@allure.suite("API: тестирование КИНОПОИСК")
@allure.title("API: Список фильмов по названию")
def test_get_list_movies_by_title():
    """
    Функция предназначена для тестирования API, который возвращает список фильмов
    на основе заданного названия. Тест проверяет, что возвращаемый список фильмов не пустой.
    """
    with allure.step("Получить список список фильмов по названию"):
        movie_title = "Другие"
        result = api.get_list_movies_by_title(movie_title)
    with allure.step("Проверить, что список не пустой"):
        assert len(result) > 0

@allure.suite("API: тестирование КИНОПОИСК")
@allure.title("API: Список стран")
def test_get_list_countries():
    """
    Функция предназначена для проверки API, предоставляющего список стран.
    Она выполняет запрос к API для получения списка стран и проверяет, что полученный список не пуст.
    """
    with allure.step("Получить список стран"):
        field_name = "countries.name"
        result = api.get_list_countries(field_name)
    with allure.step("Проверить, что список не пустой"):    
        assert len(result) > 0

@allure.suite("API: тестирование КИНОПОИСК")
@allure.title("API: Список жанров")
def test_get_list_genres():
    """
    Функция предназначена для проверки API, предоставляющего список жанров.
    Она выполняет запрос к API для получения списка жанров и проверяет, что полученный список не пуст.
    """
    with allure.step("Получить список жанров"):
        field_name = "genres.name"
        result = api.get_list_genres(field_name)
    with allure.step("Проверить, что список не пустой"):
        assert len(result) > 0

@allure.suite("API: тестирование КИНОПОИСК")
@allure.title("API: Список сезонов")
def test_get_list_seasons():
    """
    Функция `test_get_list_seasons` предназначена для проверки корректности работы API, предоставляющего список сезонов.
    Она выполняет запрос к API для получения списка сезонов и проверяет, что полученный список не пустой.
    """
    with allure.step("Получить список жанров"):
        result = api.get_list_seasons()
    with allure.step("Проверить, что список не пустой"):
        assert len(result) > 0

@allure.suite("API: тестирование КИНОПОИСК")
@allure.title("API: Список фильмов по автору")
def test_get_list_movies_by_actor_name():
    """
    Функция `test_get_list_movies_by_actor_name` предназначена для проверки корректности работы API,
    предоставляющего список фильмов по имени актера. Она выполняет запрос к API для получения списка фильмов,
    связанных с указанным актером, и проверяет, что полученный список не пустой.
    """
    with allure.step("Получить список фильмов по автору"):
        actor_name = "Абдулов"
        result = api.get_list_movies_by_actor_name(actor_name)
    with allure.step("Проверить, что список не пустой"):
        assert len(result) > 0

@allure.suite("API: тестирование КИНОПОИСК")
@allure.title("API: Универсальный поиск фильмов с фильтрами")
def test_universal_movie_search_with_filters():
    """
    Функция `test_universal_movie_search_with_filters` предназначена для проверки корректности работы API,
    предоставляющего универсальный поиск фильмов с возможностью применения фильтров. Она выполняет запрос к API
    для получения списка фильмов в соответствии с заданными параметрами и проверяет, что полученный список не пустой.
    """
    with allure.step("Получить список фильмов по фильтрам"):
        select_fields = "name"
        result = api.universal_movie_search_with_filters(select_fields)
    with allure.step("Проверить, что список не пустой"):
        assert len(result) > 0