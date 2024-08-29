import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from pages.MainApi import MainApi

api = MainApi()

def test_get_list_movies_by_title():
    movie_title = "Другие"
    result = api.get_list_movies_by_title(movie_title)
    assert len(result) > 0

def test_get_list_countries():
    field_name = "countries.name"
    result = api.get_list_countries(field_name)
    assert len(result) > 0

def test_get_list_genres():
    field_name = "genres.name"
    result = api.get_list_genres(field_name)
    assert len(result) > 0

def test_get_list_seasons():

    result = api.get_list_seasons()
    assert len(result) > 0

def test_get_list_movies_by_actor_name():

    actor_name = "Абдулов"
    result = api.get_list_movies_by_actor_name(actor_name)
    assert len(result) > 0

def test_universal_movie_search_with_filters():

    select_fields = "name"
    result = api.universal_movie_search_with_filters(select_fields)
    assert len(result) > 0