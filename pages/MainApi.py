import requests
import allure

class MainApi:

    def __init__(self):
        self.base_url = "https://api.kinopoisk.dev/v1.4"
        self.headers = {"accept": "application/json", "X-API-KEY": "V7WNPH3-TM6MBPW-N9QAC4A-NR6Z39V"}

    # Получить список фильмов по названию
    @allure.title("API: получение списка фильмов по названию")
    def  get_list_movies_by_title(self, movie_title: str):
        with allure.step("Запрос на список фильмов по названию"):
            path = ("{base_url}/movie/search?query={name}".format(base_url=self.base_url, name=movie_title))
            resp = requests.get(path, headers=self.headers)
        with allure.step("Возврат списока фильмов по названию"):
            return  resp.json()

    # Получить список стран
    @allure.title("API: получение списка стран")
    def get_list_countries(self, field_name):
        with allure.step("Запрос на список стран"):
            path = ("{base_url}/movie/possible-values-by-field?field={f_name}".format(base_url=self.base_url, f_name=field_name))
            resp = requests.get(path, headers=self.headers)
        with allure.step("Возврат списка стран"):
            return  resp.json()
    
    # Получить список жанров
    @allure.title("API: получение списка жанров")
    def get_list_genres(self, field_name):
        with allure.step("Запрос на список жанров"):
            path = ("{base_url}/movie/possible-values-by-field?field={f_name}".format(base_url=self.base_url, f_name=field_name))
            resp = requests.get(path, headers=self.headers)
        with allure.step("Возврат списка жанров"):    
            return  resp.json()
    
    # Поиск сезонов
    @allure.title("API: получение списка сезонов")
    def get_list_seasons(self):
        with allure.step("Запрос на список сезонов"):
            path = "https://api.kinopoisk.dev/v1.4/season"
            resp = requests.get(path, headers=self.headers)
        with allure.step("Возврат списка сезонов"):
            return  resp.json()                

    # Поиск актеров
    @allure.title("API: получение списка фильмов по актеру")
    def get_list_movies_by_actor_name(self, actor_name):
        with allure.step("Запрос на список фильмов по актеру"):
            path = ("{base_url}/person/search?query={a_name}".format(base_url=self.base_url, a_name=actor_name))
            resp = requests.get(path, headers=self.headers)
        with allure.step("Возврат списка фильмов по актеру"):
            return  resp.json()  

    # Универсальный поиск с фильтрами
    @allure.title("API: получение списка фильмов по универсальным фильрам")
    def universal_movie_search_with_filters(self, select_fields):
        with allure.step("Запрос на список фильмов по универсальным фильтрам"):
            path = ("{base_url}/movie?selectFields={s_fields}".format(base_url=self.base_url, s_fields=select_fields))
            resp = requests.get(path, headers=self.headers)
        with allure.step("Возврат списка фильмов по универсальным филльтрам"):
            return  resp.json()  
