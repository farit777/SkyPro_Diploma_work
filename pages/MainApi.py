import requests
import allure

class MainApi:

    def __init__(self):
        self.base_url = "https://api.kinopoisk.dev/v1.4"
        self.headers = {"accept": "application/json", "X-API-KEY": "V7WNPH3-TM6MBPW-N9QAC4A-NR6Z39V"}

    # Получить список фильмов по названию
    @allure.title("API: получение списка фильмов по названию")
    def  get_list_movies_by_title(self, movie_title: str):
        """
        Функция выполняет запрос к API для получения списка фильмов по заданному названию.
        Аргументы: movie_title (str): Название фильма, по которому будет осуществляться поиск.
        Возвращаемое значение:
        dict: Словарь, содержащий данные о фильмах, полученные в результате запроса.
        Обычно включает информацию о найденных фильмах, такую как их идентификаторы, названия и другие метаданные.
        """
        with allure.step("Запрос на список фильмов по названию"):
            path = ("{base_url}/movie/search?query={name}".format(base_url=self.base_url, name=movie_title))
            resp = requests.get(path, headers=self.headers)
        with allure.step("Возврат списока фильмов по названию"):
            return  resp.json()

    # Получить список стран
    @allure.title("API: получение списка стран")
    def get_list_countries(self, field_name):
        """
        Функция выполняет запрос к API для получения списка стран по заданному полю.
        Параметры
        - `field_name` (str): Название поля, по которому необходимо получить список стран. Это значение будет включено в запрос к API.
        Возвращаемое значение
        - Функция возвращает ответ API в формате JSON, который содержит список стран и другую связанную информацию
        """
        with allure.step("Запрос на список стран"):
            path = ("{base_url}/movie/possible-values-by-field?field={f_name}".format(base_url=self.base_url, f_name=field_name))
            resp = requests.get(path, headers=self.headers)
        with allure.step("Возврат списка стран"):
            return  resp.json()
    
    # Получить список жанров
    @allure.title("API: получение списка жанров")
    def get_list_genres(self, field_name):
        """
        Функция выполняет запрос к API для получения списка жанров по заданному полю.
        Она формирует URL-адрес, отправляет GET-запрос и возвращает результат в формате JSON.
        Параметры
        - `field_name` (str): Название поля, по которому необходимо получить список жанров. Это значение будет включено в запрос к API.
        Возвращаемое значение
        - `dict`: Функция возвращает ответ API в формате JSON, который содержит список жанров и другую связанную информацию.
        """
        with allure.step("Запрос на список жанров"):
            path = ("{base_url}/movie/possible-values-by-field?field={f_name}".format(base_url=self.base_url, f_name=field_name))
            resp = requests.get(path, headers=self.headers)
        with allure.step("Возврат списка жанров"):    
            return  resp.json()
    
    # Поиск сезонов
    @allure.title("API: получение списка сезонов")
    def get_list_seasons(self):
        """
        Функция выполняет запрос к API для получения списка сезонов. Она формирует URL-адрес,
        отправляет GET-запрос и возвращает результат в формате JSON.
        Возвращаемое значение
        - `dict`: Функция возвращает ответ API в формате JSON, который содержит список сезонов.
        """
        with allure.step("Запрос на список сезонов"):
            path = "https://api.kinopoisk.dev/v1.4/season"
            resp = requests.get(path, headers=self.headers)
        with allure.step("Возврат списка сезонов"):
            return  resp.json()                

    # Поиск актеров
    @allure.title("API: получение списка фильмов по актеру")
    def get_list_movies_by_actor_name(self, actor_name):
        """
        Функция `get_list_movies_by_actor_name` выполняет запрос к API для получения списка фильмов,
        в которых принимал участие указанный актер.
        Параметры
        - `actor_name` (str): Имя актера, по которому производится поиск. Должно быть передано в виде строки.
        Возвращаемое значение
        - Возвращает JSON-ответ от API, содержащий список фильмов, в которых указаннй актер принимал участие. 

        """
        with allure.step("Запрос на список фильмов по актеру"):
            path = ("{base_url}/person/search?query={a_name}".format(base_url=self.base_url, a_name=actor_name))
            resp = requests.get(path, headers=self.headers)
        with allure.step("Возврат списка фильмов по актеру"):
            return  resp.json()  

    # Универсальный поиск с фильтрами
    @allure.title("API: получение списка фильмов по универсальным фильрам")
    def universal_movie_search_with_filters(self, select_fields):
        """
        Функция `universal_movie_search_with_filters` выполняет запрос к API для получения списка фильмов с применением универсальных фильтров.
        Функция позволяет выбирать определенные поля (например, название, год выпуска, жанр и т.д.) для фильтрации результатов.
        Параметры
        - `select_fields` (str): Строка, содержащая названия полей, которые необходимо выбрать в результате запроса.
        Поля должны быть разделены запятыми.
        Возвращаемое значение
        - Возвращает JSON-ответ от API, содержащий список фильмов, соответствующих заданным фильтрам.
        """
        with allure.step("Запрос на список фильмов по универсальным фильтрам"):
            path = ("{base_url}/movie?selectFields={s_fields}".format(base_url=self.base_url, s_fields=select_fields))
            resp = requests.get(path, headers=self.headers)
        with allure.step("Возврат списка фильмов по универсальным филльтрам"):
            return  resp.json()  
