import pytest
from selenium.common import NoSuchElementException

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from pages.SearchResultPage import SearchResultPage


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


# SEARCH ITEMS

@pytest.mark.parametrize("item", ["tees", "blue shirt", "hoodies"])
def test_search_for_item(browser, item):

    home_page = HomePage(browser)
    search_result_page = SearchResultPage(browser)

    home_page.load()
    home_page.search_item(item)

    assert search_result_page.get_title() == f"Search results for: '{item}'"
    with pytest.raises(NoSuchElementException):
        search_result_page.get_no_results_message()

    for term in search_result_page.get_related_search_terms():
        if_related_search_correct = False
        for search_term in item.split(" "):
            if search_term in term.text:
                if_related_search_correct = True
        assert if_related_search_correct

    assert search_result_page.get_number_of_searching_results() > 0


@pytest.mark.parametrize("item", ["abcde", "unicorn"])
def test_search_for_item_with_invalid_phrase(browser, item):

    home_page = HomePage(browser)
    search_result_page = SearchResultPage(browser)

    home_page.load()
    home_page.search_item(item)

    assert search_result_page.get_title() == f"Search results for: '{item}'"
    assert search_result_page.get_no_results_message() == "Your search returned no results."
