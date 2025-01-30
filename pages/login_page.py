from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class LoginPage(BasePage):
    USERNAME = (By.ID, "email-2")
    # USERNAME = (By.CSS_SELECTOR, "input[data-name='Email 2']")
    PASSWORD = (By.ID, "field")
    LOGIN_BUTTON = (By.XPATH, "//a[@wized='loginButton']")


    def login(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.USERNAME)
        )
        self.input_text(self.username, *self.USERNAME)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PASSWORD)
        )
        self.input_text(self.password, *self.PASSWORD)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()


