from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class LoginPage(BasePage):
    USERNAME = (By.ID, "email-2")
    PASSWORD = (By.ID, "field")
    LOGIN_BUTTON = (By.XPATH, "//a[@wized='loginButton']")


    def login(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.USERNAME)
        )
        self.input_text(self.username, *self.USERNAME)
        self.input_text(self.password, *self.PASSWORD)
        self.click(*self.LOGIN_BUTTON)
        sleep(5)

