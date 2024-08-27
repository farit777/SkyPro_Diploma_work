import pytest
from pages.FooterPage import FooterPage

def test_check_footer_links(setup):
    footer_page = FooterPage(setup)
    links = footer_page.get_footer_links()
    assert len(links) > 0  # Проверяем, что есть хотя бы одна ссылка в подвале