from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
import allure

class MainPage:
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.url = "https://www.kinopoisk.ru/"

    @allure.step("Открываем главную страницу Кинопоиска")
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

    @allure.step("Переход на страницу фильмов")
    def go_to_movies(self):
        movies_link = self.browser.find_element(By.CSS_SELECTOR, "a[href='/lists/categories/movies/1/']")
        movies_link.click()