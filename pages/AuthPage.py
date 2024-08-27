from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep

class AuthPage:

    def __init__(self, drv: WebDriver):
        self.__url = 'https://passport.yandex.ru/auth/welcome?origin=kinopoisk&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fretpath%3Dhttps%253A%252F%252Fwww.kinopoisk.ru%252F%26uuid%3D5f689d74-fc18-4b3b-92b6-c6897a45aec9'

#https://passport.yandex.ru/auth/welcome?origin=kinopoisk&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fretpath%3Dhttps%253A%252F%252Fwww.kinopoisk.ru%252F%253Futm_referrer%253Dyandex.by%26uuid%3D69f26db9-01fe-4ecc-ac97-6cfe05c15949
#https://passport.yandex.ru/auth/welcome?origin=kinopoisk&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fretpath%3Dhttps%253A%252F%252Fwww.kinopoisk.ru%252F%26uuid%3D5f689d74-fc18-4b3b-92b6-c6897a45aec9
        self.__driver = drv

    def go(self):
        self.__driver.get(self.__url)

    def login_as(self, email: str, passsword: str):
        sleep(5)
        self.__driver.find_element(By.CSS_SELECTOR, "#user").send_keys(email)
        self.__driver.find_element(By.CSS_SELECTOR, "#login").click()
        sleep(10)

        self.__driver.find_element(By.CSS_SELECTOR, "#passp-field-passwd").send_keys(passsword)
        self.__driver.find_element(By.CSS_SELECTOR, "#passp:sign-in").click()