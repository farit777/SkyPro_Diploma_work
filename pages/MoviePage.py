from selenium.webdriver.common.by import By

class MoviePage:
    def __init__(self, driver):
        self.driver = driver

    def is_page_loaded(self):
        return "Титаник" in self.driver.title