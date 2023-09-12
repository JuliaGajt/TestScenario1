import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ProductPage:

    url = "https://magento.softwaretestingboard.com/"
    add_to_wish_list_button = (By.CSS_SELECTOR, "a[class*='towishlist']")
    add_to_basket_button = (By.CSS_SELECTOR, "button[title='Add to Cart']")

    select_size_or_color_button = "div[option-label='']"
    available_sizes = (By.CSS_SELECTOR, "div[id*='size']")
    shopping_cart_link_product_added = (By.XPATH, "//a[.='shopping cart']")
    added_to_cart_message = (By.CSS_SELECTOR, "div[data-ui-id='message-success'] > div")
    product_availability = (By.CSS_SELECTOR, "div[title='Availability'] > span")

    def __init__(self, browser):
        self.browser = browser

    def load(self, product: str):
        self.browser.get(self.url + product.replace(" ", "-").lower() + ".html")

    def get_title(self):
        return self.browser.title

    def get_message_added_to_basket(self):
        return self.browser.find_element(*self.added_to_cart_message).text

    def go_to_shopping_cart_with_success_link(self):
        self.browser.find_element(*self.shopping_cart_link_product_added).click()

    def get_availability_of_product(self):
        return self.browser.find_element(*self.product_availability).text

    def get_possible_sizes_of_product(self):
        return self.browser.find_elements(*self.available_sizes)

    def add_product_to_wish_list(self):
        add_to_WL = self.browser.find_element(*self.add_to_wish_list_button)
        ActionChains(self.browser).pause(1).move_to_element(add_to_WL).pause(2).click().perform()
        ActionChains(self.browser).reset_actions()

    def add_product_to_basket(self, size, color):

        if size != "":
            size_btn = self.browser.find_element(By.CSS_SELECTOR, self.select_size_or_color_button[:-2] + size + self.select_size_or_color_button[-2:])
            ActionChains(self.browser).pause(1).move_to_element(size_btn).pause(3).click().pause(2).perform()
            ActionChains(self.browser).reset_actions()

        if color != "":
            color_btn = self.browser.find_element(By.CSS_SELECTOR, self.select_size_or_color_button[:-2] + color + self.select_size_or_color_button[-2:])
            ActionChains(self.browser).move_to_element(color_btn).pause(3).click().perform()
            ActionChains(self.browser).reset_actions()

        add_to_basket = self.browser.find_element(*self.add_to_basket_button)
        ActionChains(self.browser).move_to_element(add_to_basket).pause(2).click().perform()
        ActionChains(self.browser).reset_actions()
