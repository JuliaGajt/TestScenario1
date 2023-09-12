import pytest

from pages.LoginPage import LoginPage
from pages.MyAccountPage import MyAccountPage
from pages.MyWishListPage import MyWishListPage
from pages.ProductPage import ProductPage
from pages.SearchResultPage import SearchResultPage
from pages.ShoppingCartPage import ShoppingCartPage


# ADD ITEM FROM SEARCH RESULTS TO WISHLIST

@pytest.mark.parametrize("item", ["Aero Daily Fitness Tee", "Selene Yoga Hoodie"])
def test_add_item_to_wish_list_through_search_being_logged_out(browser, item):

    login_page = LoginPage(browser)
    search_result_page = SearchResultPage(browser)

    search_result_page.load(item)

    assert search_result_page.get_number_of_searching_results() > 0
    search_result_page.add_item_to_wish_list(item)

    assert login_page.get_title() == "Customer Login"
    assert login_page.get_error_message() == "You must login or register to add items to your wishlist."


@pytest.mark.parametrize("item", ["Aero Daily Fitness Tee", "Selene Yoga Hoodie"])
def test_add_item_to_wish_list_through_search_being_logged_in(browser, item):

    login_page = LoginPage(browser)
    search_result_page = SearchResultPage(browser)
    my_wish_list_page = MyWishListPage(browser)

    login_page.load()
    login_page.login_user("test.automation@gmail.com", "TestAutomation1")

    search_result_page.load(item)

    assert search_result_page.get_number_of_searching_results() > 0

    search_result_page.add_item_to_wish_list(item)

    assert my_wish_list_page.get_title() == "My Wish List"
    assert my_wish_list_page.get_added_to_wish_list_message() == f"{item} has been added to your Wish List. Click here to continue shopping."
    assert my_wish_list_page.get_item_from_wish_list(item)


# ADD ITEM FROM SEARCH RESULTS TO BASKET

@pytest.mark.parametrize("item, size, color, if_log_to_system", [("Aero Daily Fitness Tee", "M", "Yellow", True),
                                               ("Selene Yoga Hoodie", "XS", "Purple", False)])
def test_add_item_to_basket_through_search(browser, item, size, color, if_log_to_system):
    login_page = LoginPage(browser)
    search_result_page = SearchResultPage(browser)
    shopping_cart_page = ShoppingCartPage(browser)

    if if_log_to_system:
        login_page.load()
        login_page.login_user("test.automation@gmail.com", "TestAutomation1")

    search_result_page.load(item)

    assert search_result_page.get_number_of_searching_results() > 0

    search_result_page.add_item_to_basket(item, size, color)

    assert search_result_page.get_title() == f"Search results for: '{item}'"
    assert search_result_page.get_added_to_cart_message() == f"You added {item} to your shopping cart."

    search_result_page.go_to_shopping_cart_with_success_link()
    assert item in shopping_cart_page.get_products_in_shopping_cart()


# GO TO ITEM FROM SEARCH RESULT PAGE

@pytest.mark.parametrize("item, if_logged", [("Aero Daily Fitness Tee", True), ("Selene Yoga Hoodie", False)])
def test_got_to_item_from_search_results(browser, item, if_logged):

    login_page = LoginPage(browser)
    search_result_page = SearchResultPage(browser)
    product_page = ProductPage(browser)
    my_account_page = MyAccountPage(browser)

    if if_logged:
        login_page.load()
        login_page.login_user("test.automation@gmail.com", "TestAutomation1")

        assert my_account_page.get_title() == "My Account"
        assert my_account_page.get_username_and_email_page_information() == "Test Automation test.automation@gmail.com"

    search_result_page.load(item)

    assert search_result_page.get_number_of_searching_results() > 0

    search_result_page.got_to_product_page(item)

    assert product_page.get_title() == item, "You are on the wrong page."
    assert product_page.get_availability_of_product().lower() == "in stock"
    assert len(product_page.get_possible_sizes_of_product()) > 0


