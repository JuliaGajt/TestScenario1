
import pytest
from pages.MyAccountPage import MyAccountPage
from pages.RegisterPage import RegisterPage


@pytest.mark.parametrize("firstname, lastname, email, password",
                         [("Test1", "Something1", "test3.Something1@gcail.com", "SomeGoodPassword1"),
                          ("Test2", "Something2", "test4.Something2@gcail.com", "SomeGoodPassword2")])
def test_register_new_user(browser, firstname, lastname, email, password):
    register_page = RegisterPage(browser)
    my_account_page = MyAccountPage(browser)
    register_page.load()

    assert register_page.get_title() == "Create New Customer Account", "You are on the wrong page."

    register_page.register_new_user(firstname, lastname, email, password)

    assert my_account_page.get_title() == "My Account"
    assert my_account_page.get_username_and_email_page_information() == f"{firstname} {lastname} {email}"
    assert my_account_page.get_successful_registration_message() == "Thank you for registering with Main Website Store."


@pytest.mark.parametrize("firstname, lastname, email, password", [("Test1", "Something", "", "SomeGoodPassword1"),
                                                                  ("Test2", "", "test4.Something@gmanil.com",
                                                                   "SomeGoodPassword2")])
def test_register_new_user_fail(browser, firstname, lastname, email, password):
    register_page = RegisterPage(browser)
    register_page.load()

    assert register_page.get_title() == "Create New Customer Account", "You are on the wrong page."
    register_page.register_new_user(firstname, lastname, email, password)

    assert register_page.get_title() == 'Create New Customer Account'

    if firstname == '': assert register_page.get_firstname_error() == "This is a required field."
    if lastname == '': assert register_page.get_lastname_error() == "This is a required field."
    if email == '': assert register_page.get_email_error() == "This is a required field."
    if password == '':
        assert register_page.get_password_error() == "This is a required field."
        assert register_page.get_password_confirmation_error() == "This is a required field."
