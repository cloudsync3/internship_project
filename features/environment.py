from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from app.application import Application

 #Firefox
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options
# from webdriver_manager.firefox import GeckoDriverManager


def browser_init(context):
    """
    :param context: Behave context
    """

    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)


    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'darianesterova_aszJix'
    # bs_key = 'Mapkzz4zFCk4kQtpPW45'
    # url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #      "os" : "Windows",
    #      "osVersion" : "11",
    #      'browserName': 'chrome',
    #      'sessionName': scenario_name,
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    # options = webdriver.ChromeOptions()
    # # options.add_argument("--headless=new")
    # # options.add_argument("--window-size=1920x1080")
    # # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=service, options=options)

    # Firefox
    # firefox_options = Options()
    # firefox_options.add_argument("--headless")
    # service = Service(GeckoDriverManager().install())
    # context.driver = webdriver.Firefox(service=service, options=firefox_options)


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    scenario_name = scenario.name
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, scenario):
    if hasattr(context, 'driver'):  # Check if 'driver' exists
        context.driver.quit()
