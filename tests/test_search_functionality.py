import pytest
from pages.SearchPage import SearchPage
from pages.DashboardPage import DashboardPage

def test_search_functionality(setup):
    dashboard_page = DashboardPage(setup)
    dashboard_page.search_for_movie("Титаник")
    search_page = SearchPage(setup)
    assert "Титаник" in search_page.get_result_title()