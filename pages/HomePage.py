from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class HomePage:

    register_account_button = (By.XPATH, "//a[.='Create an Account']")
    login_account_button = (By.XPATH, "//a[contains(., 'Sign In')]")

    search_input = (By.ID, "search")

    url = "https://magento.softwaretestingboard.com/"

    def __init__(self, browser: webdriver):
        self.browser = browser

    def get_page_title(self):
        return self.browser.title

    def load(self):
        self.browser.get(self.url)

    def go_to_user_registration(self):
        self.browser.find_element(*self.register_account_button).click()

    def go_to_user_login(self):
        self.browser.find_element(*self.login_account_button).click()

    def search_item(self, item):
        self.browser.find_element(*self.search_input).send_keys(item + Keys.ENTER)
