import pytest
from pages.DashboardPage import DashboardPage

def test_genre_filter(setup):
    dashboard_page = DashboardPage(setup)
    # Здесь необходимо реализовать логику фильтрации по жанру "Комедия"
    # Например, нужно нажать на фильтр и проверить результаты
    # Это будет зависеть от структуры сайта и доступных элементов