import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import pytest
from pages.DashboardPage import DashboardPage

def test_navigation_to_top_rated(setup):
    dashboard_page = DashboardPage(setup)
    dashboard_page.navigate_to_top_rated()
    assert "Топ 250" in dashboard_page.get_title()