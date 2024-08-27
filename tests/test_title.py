import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import pytest
from pages.DashboardPage import DashboardPage

def test_title(setup):
    dashboard_page = DashboardPage(setup)
    assert "КиноПоиск" in dashboard_page.get_title()