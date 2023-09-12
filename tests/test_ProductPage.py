import pytest

from pages.LoginPage import LoginPage
from pages.MyWishListPage import MyWishListPage
from pages.ProductPage import ProductPage
from pages.ShoppingCartPage import ShoppingCartPage


@pytest.mark.parametrize("product", ["Tiffany Fitness Tee", "Proteus Fitness Jackshirt"])
def test_add_product_to_wish_list_logged_out(browser, product):
    product_page = ProductPage(browser)
    login_page = LoginPage(browser)

    product_page.load(product)
    assert product_page.get_title() == product, "You are on the wrong page."
    assert product_page.get_availability_of_product().lower() == "in stock"
    assert len(product_page.get_possible_sizes_of_product()) > 0

    product_page.add_product_to_wish_list()

    assert login_page.get_title() == "Customer Login"
    assert login_page.get_error_message() == "You must login or register to add items to your wishlist."


@pytest.mark.parametrize("product", ["Tiffany Fitness Tee", "Proteus Fitness Jackshirt"])
def test_add_product_to_wish_list_logged_in(browser, product):

    product_page = ProductPage(browser)
    login_page = LoginPage(browser)
    my_wish_list_page = MyWishListPage(browser)

    login_page.load()
    login_page.login_user("test.automation@gmail.com", "TestAutomation1")

    product_page.load(product)
    assert product_page.get_title() == product, "You are on the wrong page."
    assert product_page.get_availability_of_product().lower() == "in stock"
    assert len(product_page.get_possible_sizes_of_product()) > 0

    product_page.add_product_to_wish_list()

    assert my_wish_list_page.get_title() == "My Wish List"
    assert my_wish_list_page.get_added_to_wish_list_message() == f"{product} has been added to your Wish List. Click here to continue shopping."
    assert my_wish_list_page.get_item_from_wish_list(product)


@pytest.mark.parametrize("product, size, color, if_logged", [("Tiffany Fitness Tee", "M", "Blue", True),
                                                      ("Proteus Fitness Jackshirt", "L", "Orange", False)])
def test_add_product_to_basket(browser, product, size, color, if_logged):

    product_page = ProductPage(browser)
    shopping_cart_page = ShoppingCartPage(browser)
    login_page = LoginPage(browser)

    if if_logged:
        login_page.load()
        login_page.login_user("test.automation@gmail.com", "TestAutomation1")

    product_page.load(product)

    assert product_page.get_title() == product, "You are on the wrong page."
    assert product_page.get_availability_of_product().lower() == "in stock"
    assert len(product_page.get_possible_sizes_of_product()) > 0

    product_page.add_product_to_basket(size, color)

    assert product_page.get_title() == product, "You are on the wrong page."
    assert product_page.get_message_added_to_basket() == f"You added {product} to your shopping cart."

    product_page.go_to_shopping_cart_with_success_link()
    assert product in shopping_cart_page.get_products_in_shopping_cart()




