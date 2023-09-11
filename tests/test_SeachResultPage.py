import pytest
from selenium.common import NoSuchElementException

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.MyWishListPage import MyWishListPage
from pages.SearchResultPage import SearchResultPage


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


@pytest.mark.parametrize("item", ["abcde", "unicorn"])
def test_search_for_item_with_invalid_phrase(browser, item):

    home_page = HomePage(browser)
    search_result_page = SearchResultPage(browser)

    home_page.load()
    home_page.search_item(item)

    assert search_result_page.get_title() == f"Search results for: '{item}'"
    assert search_result_page.get_no_results_message() == "Your search returned no results."


@pytest.mark.parametrize("item", ["Aero Daily Fitness Tee", "Selene Yoga Hoodie"])
def test_0_add_item_to_wish_list_through_search_being_logged_in(browser, item):

    home_page = HomePage(browser)
    login_page = LoginPage(browser)
    search_result_page = SearchResultPage(browser)
    my_wish_list_page = MyWishListPage(browser)

    home_page.load()
    home_page.go_to_user_login()
    login_page.login_user("test.automation@gmail.com", "TestAutomation1")
    home_page.search_item(item)

    search_result_page.add_item_to_wish_list(item)

    assert my_wish_list_page.get_title() == "My Wish List"
    assert my_wish_list_page.get_added_to_wish_list_message() == f"{item} has been added to your Wish List. Click here to continue shopping."
    assert my_wish_list_page.get_item_from_wish_list(item)


@pytest.mark.parametrize("item", ["Aero Daily Fitness Tee", "Selene Yoga Hoodie"])
def test_add_item_to_wish_list_through_search_being_logged_out(browser, item):
    home_page = HomePage(browser)
    login_page = LoginPage(browser)
    search_result_page = SearchResultPage(browser)

    home_page.load()
    home_page.search_item(item)
    search_result_page.add_item_to_wish_list(item)

    assert login_page.get_title() == "Customer Login"
    assert login_page.get_error_message() == "You must login or register to add items to your wishlist."


@pytest.mark.parametrize("item, size, color, if_log_to_system", [("Aero Daily Fitness Tee", "M", "Yellow", True),
                                               ("Selene Yoga Hoodie", "XS", "Purple", False)])
def test_1_add_item_to_basket_through_search(browser, item, size, color, if_log_to_system):
    home_page = HomePage(browser)
    login_page = LoginPage(browser)
    search_result_page = SearchResultPage(browser)

    home_page.load()

    if if_log_to_system:
        home_page.go_to_user_login()
        login_page.login_user("test.automation@gmail.com", "TestAutomation1")

    home_page.search_item(item)
    search_result_page.add_item_to_basket(item, size, color)

    assert search_result_page.get_title() == f"Search results for: '{item}'"
    assert search_result_page.get_added_to_cart_message() == f"You added {item} to your shopping cart."


@pytest.mark.parametrize("item", ["Aero Daily Fitness Tee", "Selene Yoga Hoodie"])
def test_add_item_to_wish_list_category_tab_being_logged_in(browser, item):

    # TODO
    raise Exception("Not done yet.")
