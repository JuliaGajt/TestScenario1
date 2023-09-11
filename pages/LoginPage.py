from selenium.webdriver.common.by import By


class LoginPage:

    url = "https://magento.softwaretestingboard.com/customer/account/login/"

    email_input = (By.ID, "email")
    password_input = (By.XPATH, "//input[@id='pass' and @title='Password']")
    login_button = (By.XPATH, "//*[@id='send2' and contains(@class,'login primary')]")

    error_message = (By.CSS_SELECTOR, "div[data-ui-id='message-error'] > div")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.url)

    def get_title(self):
        return self.browser.title

    def login_user(self, email, password):

        self.browser.find_element(*self.email_input).send_keys(email)
        self.browser.find_element(*self.password_input).send_keys(password)
        self.browser.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.browser.find_element(*self.error_message).text

