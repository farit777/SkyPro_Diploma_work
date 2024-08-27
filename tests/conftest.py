import pytest
from selenium import webdriver

@pytest.fixture(scope='module')
def browser():
    options = webdriver.ChromeOptions()
    options.browser_version = 'stable'
    options.platform_name = 'any'
    #options.accept_insecure_certs = True
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(4)
    browser.maximize_window()

    yield browser

    browser.quit()



# def FireFox_options():
#     options = webdriver.FirefoxOptions()
#     options.browser_version = 'stable'
#     driver = webdriver.Firefox(options=options)

# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# @pytest.fixture(scope="module")
# def setup():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.get("https://www.kinopoisk.ru")
#     yield driver
#     driver.quit()