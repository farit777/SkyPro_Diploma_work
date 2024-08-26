from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.AuthPage import AuthPage
from time import sleep


def test_first():
    browser = WebDriver.Chrome() #service=Service(ChromeDriverManager().Install()))
    browser.implicity_wait(4)
    browser.maximize_window()

    auth_page = AuthPage(browser)
    auth_page.go()

    sleep(5)