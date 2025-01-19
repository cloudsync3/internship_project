from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class LoginPage(BasePage):
    # USERNAME = (By.ID, "email-2")
    USERNAME = (By.CSS_SELECTOR, "input[data-name='Email 2']")
    PASSWORD = (By.ID, "field")
    LOGIN_BUTTON = (By.XPATH, "//a[@wized='loginButton']")


    def login(self):
        sleep(5)
        # WebDriverWait(self.driver, 20).until(
        #     EC.visibility_of_element_located(self.USERNAME)
        # )
        self.input_text(self.username, *self.USERNAME)
        sleep(2)
        self.input_text(self.password, *self.PASSWORD)
        sleep(2)
        self.click(*self.LOGIN_BUTTON)


