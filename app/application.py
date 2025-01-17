from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.login_page import LoginPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(driver)
        self.base_page = BasePage(driver)
        self.login_page = LoginPage(driver)