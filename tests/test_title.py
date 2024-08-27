import pytest
from pages.DashboardPage import DashboardPage

def test_title(setup):
    dashboard_page = DashboardPage(setup)
    assert "КиноПоиск" in dashboard_page.get_title()