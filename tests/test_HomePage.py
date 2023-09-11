from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage


def test_go_to_user_registration(browser):
    home_page = HomePage(browser)
    register_page = RegisterPage(browser)
    home_page.load()
    home_page.go_to_user_registration()
    assert register_page.get_title() == "Create New Customer Account", "You are on the wrong page."


def test_go_to_user_login(browser):
    home_page = HomePage(browser)
    login_page = LoginPage(browser)
    home_page.load()
    home_page.go_to_user_login()
    assert login_page.get_title() == "Customer Login", "You are on the wrong page."

