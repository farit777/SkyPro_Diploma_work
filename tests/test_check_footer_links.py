import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import pytest
from time import sleep
from pages.FooterPage import FooterPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_check_footer_links(browser):
    footer_page = FooterPage(browser)
    footer_page.go()
    sleep(2)
    links = footer_page.get_footer_links()
    assert len(links) > 0  # Проверяем, что есть хотя бы одна ссылка в подвале