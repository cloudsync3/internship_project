from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class MainPage(BasePage):

    SETTINGS_BTN = (By.CSS_SELECTOR, "[href='/settings']")
    SUPPORT_BTN = (By.CSS_SELECTOR, "a[href*='https://api.whatsapp.com/']")
    WHATSAPP_VERIFY = (By.CSS_SELECTOR, "#action-button")
    TME_NEWS = (By.XPATH, "//a[@href='https://t.me/reellydxb' and contains(@class, 'page-setting-block')]")
    TELEGRAM_BTN = (By.XPATH, "//a[@href='https://t.me/reellydxb']")

    def open_main(self):
        self.open_url('https://soft.reelly.io')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SETTINGS_BTN)
        )


    def setting_option(self):
        # self.driver.find_element(*self.SETTINGS_BTN).click()
        # sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SETTINGS_BTN)
        ).click()


    def support_option(self):
        # self.driver.find_element(*self.SUPPORT_BTN).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUPPORT_BTN)
        ).click()


    def switch_to_new_tab(self):
        sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def verify_whatsapp_page(self):
        # self.driver.find_element(*self.WHATSAPP_VERIFY)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.WHATSAPP_VERIFY)
        )

    def go_back_previous_page(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(2)

    def click_on_news_option(self):
        # self.wait_for_element_visible(*self.TME_NEWS)
        # self.scroll_to_element(self.TME_NEWS)
        # self.driver.find_element(*self.TME_NEWS).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.TME_NEWS)
        ).click()

    def verify_tele_news_page(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: "t.me/reellydxb" in driver.current_url
        )
        assert "t.me/reellydxb" in self.driver.current_url, f"Expected 't.me/reellydxb' in URL but got '{self.driver.current_url}'"
        print(f"Verified Telegram page opened: {self.driver.current_url}")






