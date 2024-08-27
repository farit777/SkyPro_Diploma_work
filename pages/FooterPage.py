from selenium.webdriver.common.by import By

class FooterPage:
    def __init__(self, driver):
        self.driver = driver
        self.footer_links = (By.CSS_SELECTOR, "footer a")

    def get_footer_links(self):
        return self.driver.find_elements(*self.footer_links)