import requests

class MainApi:

    def __init__(self):
        self.base_url = "https://api.kinopoisk.dev/v1.4"
        self.headers = {"accept": "application/json", "X-API-KEY": "V7WNPH3-TM6MBPW-N9QAC4A-NR6Z39V"}

    # Получить список фильмов по названию
    def  get_list_movies_by_title(self, movie_title: str):
        
        path = ("{base_url}/movie/search?query={name}".format(base_url=self.base_url, name=movie_title))
        resp = requests.get(path, headers=self.headers)
        return  resp.json()

    # Получить список стран
    def get_list_countries(self, field_name):

        path = ("{base_url}/movie/possible-values-by-field?field={f_name}".format(base_url=self.base_url, f_name=field_name))
        resp = requests.get(path, headers=self.headers)
        return  resp.json()
    
    # Получить список жанров
    def get_list_genres(self, field_name):

        path = ("{base_url}/movie/possible-values-by-field?field={f_name}".format(base_url=self.base_url, f_name=field_name))
        resp = requests.get(path, headers=self.headers)
        return  resp.json()
    
    # Поиск сезонов
    def get_list_seasons(self):

        path = "https://api.kinopoisk.dev/v1.4/season"
        resp = requests.get(path, headers=self.headers)
        return  resp.json()                

    # Поиск актеров
    def get_list_movies_by_actor_name(self, actor_name):

        path = ("{base_url}/person/search?query={a_name}".format(base_url=self.base_url, a_name=actor_name))
        resp = requests.get(path, headers=self.headers)
        return  resp.json()  

    # Универсальный поиск с фильтрами
    def universal_movie_search_with_filters(self, select_fields):

        path = ("{base_url}/movie?selectFields={s_fields}".format(base_url=self.base_url, s_fields=select_fields))
        resp = requests.get(path, headers=self.headers)
        return  resp.json()  
