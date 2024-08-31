from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure

class MoviesPage:
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.url = "https://www.kinopoisk.ru/lists/categories/movies/1/"

    @allure.step("Открываем страницу фильмов Кинопоиска")
    def open(self):
        """Открывает страницу фильмов"""
        self.browser.get(self.url)

    @allure.step("Закрыть модальное окно, если оно открыто")
    def close_modal_if_open(self):
        """Функция закрывает модальное окно, если оно присутствует"""
        try:
            modal_close_button = self.browser.find_element(By.CSS_SELECTOR, "body > div.ReactModalPortal > div > div > div > div:nth-child(1) > div.styles_buttonContainer__R98ro > button.style_button__PNtXT.style_buttonSize48__7RF4w.style_secondaryTransparent__ehaDu.style_buttonDark__beFpy.style_fullWidth__Kw7rX")
            modal_close_button.click()
        except Exception as e:
            allure.attach(self.browser.get_screenshot_as_png(), name="Modal Close Error", attachment_type=allure.attachment_type.PNG)
            print("Модальное окно не найдено или не открыто.")

    @allure.step("Проверка доступности жанров")
    def open_genres(self):
        """Открывает страницу жанров по ссылке"""
        genres_link = self.browser.find_element(By.CSS_SELECTOR, "a[href='/lists/categories/movies/8/']")
        genres_link.click()

    @allure.step("Проверка доступности стран по ссылке")
    def open_countries(self):
        """Открывает страницу стран"""
        countries_link = self.browser.find_element(By.CSS_SELECTOR, "a[href='/lists/categories/movies/9/']")
        countries_link.click()

    @allure.step("Проверка доступности Годы по ссылке")
    def open_years(self):
        """Открывает страницу Годы"""
        years_link = self.browser.find_element(By.CSS_SELECTOR, "a[href='/lists/categories/movies/7/']")
        years_link.click()

    @allure.step("Проверка доступности Критика по ссылке")
    def open_critics(self):
        """Отрывает страницу отзывов"""
        critics_link = self.browser.find_element(By.CSS_SELECTOR, "a[href='/lists/categories/movies/18/']")
        critics_link.click()

    @allure.step("Проверка сериалов на странице фильмов по ссылке")
    def open_incoming(self):
        """Открывает страницу поступлений за фильмы"""
        incoming_link = self.browser.find_element(By.CSS_SELECTOR, "a[href='/lists/categories/movies/5/']")
        incoming_link.click()

    