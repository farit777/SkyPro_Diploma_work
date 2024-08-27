from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.NAME, "q")
        self.search_button = (By.XPATH, "//button[@type='submit']")
        self.result_title = (By.CSS_SELECTOR, ".search_results .title")

    def search_for_movie(self, movie_name):
        self.driver.find_element(*self.search_input).send_keys(movie_name)
        self.driver.find_element(*self.search_button).click()

    def get_result_title(self):
        return self.driver.find_element(*self.result_title).text