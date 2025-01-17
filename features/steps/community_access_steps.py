from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

USERNAME_INPUT = (By.ID, "email-2")
PASSWORD_INPUT = (By.ID, "field")
LOGIN_BUTTON = (By.ID, "loginButton")


@given('Open Reelly main page')
def open_main_page(context):
    context.driver.get('https://soft.reelly.io')
    sleep(3)


@when('Enter credentials and login to the app')
def login(context):
    context.app.login_page.login()
    sleep(3)


@then('Click on settings option')
def setting_option(context):
    context.app.main_page.setting_option()


@then('Click on support option')
def support_option(context):
    context.app.main_page.support_option()


@when('Switch to the new tab')
def switch_to_new_tab(context):
    context.app.main_page.switch_to_new_window()


@then('Verify the right Whatsapp page opens')
def verify_whatsapp_page(context):
    context.app.main_page.verify_whatsapp_page()


@then('Go back to previous page')
def go_back_previous_page(context):
    context.app.main_page.go_back_previous_page()


@when('Click on t.me news option')
def click_on_news_option(context):
    context.app.main_page.click_on_news_option()


@then('Verify the right page opens')
def verify_tele_news_page(context):
    context.app.main_page.verify_tele_news_page()










