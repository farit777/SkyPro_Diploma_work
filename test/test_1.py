from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from page.AuthPage import AuthPage
from time import sleep

# def test_first():
#     driver = webdriver.Firefox()
#     driver.implicitly_wait(4)
#     driver.maximize_window()

#     auth_page = AuthPage(driver)
#     auth_page.go()

#     sleep(5)

def test_capabilities():
    options = webdriver.ChromeOptions()
    options.browser_version = 'stable'
    #options.platform_name = 'any'
    #options.accept_insecure_certs = True
    driver = webdriver.Chrome(options=options)

    #driver.get("https://www.selenium.dev/")
    driver.get("https://www.kinopoisk.ru/")
    sleep(10)
    driver.quit()

def test_basic_options():
    options = webdriver.FirefoxOptions()
    options.browser_version = 'stable'
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.kinopoisk.ru/")
    sleep(5)
    driver.quit()