from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.title = (By.TAG_NAME, "title")
        self.top_rated_link = (By.LINK_TEXT, "Топ 250")

    def get_title(self):
        return self.driver.find_element(*self.title).get_attribute("innerText")

    def navigate_to_top_rated(self):
        self.driver.find_element(*self.top_rated_link).click()