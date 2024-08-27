import pytest
from pages.SearchPage import SearchPage
from pages.MoviePage import MoviePage
from pages.DashboardPage import DashboardPage

def test_movie_details(setup):
    dashboard_page = DashboardPage(setup)
    dashboard_page.search_for_movie("Титаник")
    search_page = SearchPage(setup)
    search_page.search_for_movie("Титаник")

    movie_page = MoviePage(setup)
    assert movie_page.is_page_loaded()