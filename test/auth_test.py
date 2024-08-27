from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from page.AuthPage import AuthPage
from time import sleep


def auth_test(browser):
    auth_page = AuthPage(browser)
#    auth_page.go()

    auth_page.login_as("skyproap@mail.ru", "skypro_ap")

    sleep(5)