from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class AuthPage:

    def __init__(self, drv):
        self.__url = 'https://www.kinopoisk.ru'
        self.__driver = drv

    def go(self):
        self.__driver.get(self.__url)
        