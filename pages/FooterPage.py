from selenium.webdriver.common.by import By

class FooterPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.kinopoisk.ru/'
        self.footer_links = (By.CSS_SELECTOR, 'a.footer__content-link')

    def go(self):
        self.driver.get(self.url)
        
    def get_footer_links(self):
        
        return self.driver.find_elements(self.footer_links)