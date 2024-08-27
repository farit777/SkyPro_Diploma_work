from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from page.AuthPage import AuthPage
from time import sleep


def test_first(browser):
    auth_page = AuthPage(browser)
    auth_page.go()

    sleep(5)