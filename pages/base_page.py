from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.username = "dasha.nesterova@yahoo.com"
        self.password = "Chukcha5323!"


    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def get_current_window_handle(self):
        window = self.driver.current_window_handle
        print('Current window ', window)
        return window

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print('All windows: ', all_windows)
        self.driver.switch_to.window(all_windows[1])
        print('Current window ', self.driver.current_window_handle)

    def verify_partial_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url in actual_url, f'Expected partial url {expected_url} not in actual{actual_url}'

    def close_current_tab_and_go_back(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def wait_and_click(self, *locator):
         self.wait.until(
         EC.element_to_be_clickable(locator),
         message = f'Element by {locator} not clickable'
         ).click()

    def wait_for_element_visible(self, *locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by {locator} not visible'
        )

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    def close(self):
        self.driver.close()

