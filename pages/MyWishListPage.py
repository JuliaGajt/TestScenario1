from selenium.webdriver.common.by import By


class MyWishListPage:

    url = ""
    message_added_to_wishlist = (By.CSS_SELECTOR, "div[data-ui-id='message-success'] > div")
    item_in_wish_list = "//a[@title='' and @class='product-item-link']"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.url)

    def get_title(self):
        return self.browser.title

    def get_added_to_wish_list_message(self):
        return self.browser.find_element(*self.message_added_to_wishlist).text

    def get_item_from_wish_list(self, item):
        return self.browser.find_element(By.XPATH, self.item_in_wish_list[:12] + item + self.item_in_wish_list[12:])

