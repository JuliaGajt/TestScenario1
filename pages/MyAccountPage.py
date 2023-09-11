from selenium.webdriver.common.by import By


class MyAccountPage:

    username_and_email_info = (By.XPATH, "//div[contains(@class, 'information')]//p")
    after_successful_registration_message = (By.XPATH, "//div[contains(@class,'message-success')]/div")

    url = ""

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.url)

    def get_title(self) -> str:
        return self.browser.title

    def get_username_and_email_page_information(self) -> str:
        return self.browser.find_element(*self.username_and_email_info).text.replace("\n", " ")

    def get_successful_registration_message(self) -> str:
        return self.browser.find_element(*self.after_successful_registration_message).text
