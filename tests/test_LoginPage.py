import pytest

from pages.LoginPage import LoginPage
from pages.MyAccountPage import MyAccountPage


@pytest.mark.parametrize("username, email, password", [("Test Automation", "test.automation@gmail.com",
                                                        "TestAutomation1")])
def test_login_to_page(browser, username, email, password):

    login_page = LoginPage(browser)
    my_account_page = MyAccountPage(browser)

    login_page.load()
    login_page.login_user(email, password)

    assert my_account_page.get_title() == "My Account"
    assert my_account_page.get_username_and_email_page_information() == f"{username} {email}"
