from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure

class MoviesPage:
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.url = "https://www.kinopoisk.ru/lists/categories/movies/1/"

    @allure.step("Открываем страницу фильмов Кинопоиска")
    def open(self):
        self.browser.get(self.url)

    @allure.step("Закрыть модальное окно, если оно открыто")
    def close_modal_if_open(self):
        try:
            modal_close_button = self.browser.find_element(By.CSS_SELECTOR, "body > div.ReactModalPortal > div > div > div > div:nth-child(1) > div.styles_buttonContainer__R98ro > button.style_button__PNtXT.style_buttonSize48__7RF4w.style_secondaryTransparent__ehaDu.style_buttonDark__beFpy.style_fullWidth__Kw7rX")
            modal_close_button.click()
        except Exception as e:
            allure.attach(self.browser.get_screenshot_as_png(), name="Modal Close Error", attachment_type=allure.attachment_type.PNG)
            print("Модальное окно не найдено или не открыто.")

    @allure.step("Проверка доступности жанров")
    def open_genres(self):
        genres_link = self.browser.find_element(By.CSS_SELECTOR, "a[href='/lists/categories/movies/8/']")
        genres_link.click()
        # genre_name = self.browser.find_element(By.CSS_SELECTOR, "span.styles_name__G_1mq").text
        # assert genre_name == "Комедии", "Жанр не найден"

    @allure.step("Проверка доступности стран")
    def open_countries(self):
        countries_link = self.browser.find_element(By.CSS_SELECTOR, "a[href='/lists/categories/movies/9/']")
        countries_link.click()
        # country_name = self.browser.find_element(By.CSS_SELECTOR, "span.styles_name__G_1mq").text
        # assert country_name == "Россия", "Страна не найдена"

    @allure.step("Проверка доступности Годы")
    def open_countries(self):
        countries_link = self.browser.find_element(By.CSS_SELECTOR, "a[href='/lists/categories/movies/7/']")
        countries_link.click()

    @allure.step("Проверка доступности Критика")
    def open_critics(self):
        countries_link = self.browser.find_element(By.CSS_SELECTOR, "a[href='/lists/categories/movies/18/']")
        countries_link.click()

    @allure.step("Проверка сериалов на странице фильмов")
    def open_series(self):
        countries_link = self.browser.find_element(By.CSS_SELECTOR, "a[href='/lists/categories/movies/3/']")
        countries_link.click()

    @allure.step("Проверка сериалов на странице фильмов")
    def open_incoming(self):
        countries_link = self.browser.find_element(By.CSS_SELECTOR, "a[href='/lists/categories/movies/5/']")
        countries_link.click()

    