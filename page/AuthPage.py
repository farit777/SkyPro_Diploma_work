from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class AuthPage:

    def __init__(self, drv: WebDriver):
        self.__url = 'https://passport.yandex.ru/auth/welcome'

#https://passport.yandex.ru/auth/welcome?origin=kinopoisk&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fretpath%3Dhttps%253A%252F%252Fwww.kinopoisk.ru%252F%253Futm_referrer%253Dyandex.by%26uuid%3D69f26db9-01fe-4ecc-ac97-6cfe05c15949

        self.__driver = drv

    def go(self):
        self.__driver.get(self.__url)

    def login_as(self, email: str, passsword: str):
        #self.__driver.find_element(By.CSS_SELECTOR, "#user").send_keys(email)
        #self.__driver.find_element(By.CSS_SELECTOR, "#login").click()

        self.__driver.find_element(By.CSS_SELECTOR, "#passp-field-passwd").send_keys(passsword)
        self.__driver.find_element(By.CSS_SELECTOR, "#passp:sign-in").click()