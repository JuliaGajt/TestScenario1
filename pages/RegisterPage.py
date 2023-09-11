from selenium.webdriver.common.by import By


class RegisterPage:

    firstname_input_field = (By.ID, "firstname")
    lastname_input_field = (By.ID, "lastname")
    email_input_field = (By.ID, "email_address")
    password_input_field = (By.ID, "password")
    password_confirmation_input_field = (By.ID, "password-confirmation")

    submit_account = (By.XPATH, "//button[@title='Create an Account']")

    firstname_error = (By.ID, "firstname-error")
    lastname_error = (By.ID, "lastname-error")
    email_error = (By.ID, "email_address-error")
    password_error = (By.ID, "password-error")
    password_confirmation_error = (By.ID, "password-confirmation-error")

    url = "https://magento.softwaretestingboard.com/customer/account/create/"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.url)

    def get_title(self):
        return self.browser.title

    def register_new_user(self, firstname, lastname, email, password):

        self.browser.find_element(*self.firstname_input_field).send_keys(firstname)
        self.browser.find_element(*self.lastname_input_field).send_keys(lastname)
        self.browser.find_element(*self.email_input_field).send_keys(email)
        self.browser.find_element(*self.password_input_field).send_keys(password)
        self.browser.find_element(*self.password_confirmation_input_field).send_keys(password)
        self.browser.find_element(*self.submit_account).click()

    def get_firstname_error(self):
        return self.browser.find_element(*self.firstname_error).text

    def get_lastname_error(self):
        return self.browser.find_element(*self.lastname_error).text

    def get_email_error(self):
        return self.browser.find_element(*self.email_error).text

    def get_password_error(self):
        return self.browser.find_element(*self.password_error).text

    def get_password_confirmation_error(self):
        return self.browser.find_element(*self.password_confirmation_error).text
