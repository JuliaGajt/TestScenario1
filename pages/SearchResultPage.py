from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class SearchResultPage:
    related_search_terms = (By.CSS_SELECTOR, "div[class='search results'] dd > a")
    no_results_information = (By.CSS_SELECTOR, "div[class*='notice'] > div")
    added_to_cart_message = (By.CSS_SELECTOR, "div[data-ui-id='message-success'] > div")

    add_item_to_wish_list_button = """//a[contains(.,'')]/parent::*/following-sibling::div[@class='product-item-inner']
                                        //a[@title='Add to Wish List']"""

    add_item_to_basket_button = """//a[contains(.,'')]/parent::*/following-sibling::div[@class='product-item-inner']
                                        //button[@title='Add to Cart']"""

    item_name_card = "//a[contains(.,'')]/parent::*"

    select_size_of_item = """//a[contains(.,'')]/parent::*/following-sibling::div[contains(@class,'swatch-opt')]
                                        //div[contains(@id,'option-label-size') and @option-label='']"""

    select_color_of_item = """//a[contains(.,'')]/parent::*/following-sibling::div[contains(@class,'swatch-opt')]
                                        //div[contains(@id,'option-label-color') and @option-label='']"""

    shopping_cart_link_product_added = (By.XPATH, "//a[.='shopping cart']")

    results_of_searching = (By.CSS_SELECTOR, "li[class='item product product-item']")
    link_to_item_from_search_results = "img[class='product-image-photo'][alt='']"

    def __init__(self, browser):
        self.browser = browser

    def load(self, item):
        self.browser.get(f"https://magento.softwaretestingboard.com/catalogsearch/result/?q={item}")

    def get_title(self):
        return self.browser.title

    def get_related_search_terms(self):
        return self.browser.find_elements(*self.related_search_terms)

    def get_no_results_message(self):
        return self.browser.find_element(*self.no_results_information).text

    def get_added_to_cart_message(self):
        return self.browser.find_element(*self.added_to_cart_message).text

    def go_to_shopping_cart_with_success_link(self):
        self.browser.find_element(*self.shopping_cart_link_product_added).click()

    def add_item_to_wish_list(self, item):

        item_name_element = self.browser.find_element(By.XPATH,
                                                      self.item_name_card[:16] + item + self.item_name_card[16:])
        ActionChains(self.browser).move_to_element(item_name_element).pause(2).perform()
        ActionChains(self.browser).reset_actions()

        add_to_wish_list = self.browser.find_element(By.XPATH, self.add_item_to_wish_list_button[:16] + item +
                                                     self.add_item_to_wish_list_button[16:])
        ActionChains(self.browser).move_to_element(add_to_wish_list).pause(2).click().perform()
        ActionChains(self.browser).reset_actions()

    def add_item_to_basket(self, item, size, color):

        # move to products so they are visible
        item_name_element = self.browser.find_element(By.XPATH,
                                                      self.item_name_card[:16] + item + self.item_name_card[16:])
        ActionChains(self.browser).move_to_element(item_name_element).pause(2).perform()
        ActionChains(self.browser).reset_actions()

        # select size of product
        if size != "":
            size_button = self.browser.find_element(By.XPATH, self.select_size_of_item[:16] + item +
                                                    self.select_size_of_item[16:-2] + size + self.select_size_of_item[-2:])
            ActionChains(self.browser).move_to_element(size_button).pause(2).click().perform()
            ActionChains(self.browser).reset_actions()

        # select color of product
        if color != "":
            color_button = self.browser.find_element(By.XPATH,
                                                     self.select_color_of_item[:16] + item + self.select_color_of_item
                                                     [16:-2] + color + self.select_color_of_item[-2:])

            ActionChains(self.browser).move_to_element(color_button).pause(2).click().perform()
            ActionChains(self.browser).reset_actions()

        # add to basket
        add_to_basket_button = self.browser.find_element(By.XPATH, self.add_item_to_basket_button[:16]
                                                         + item + self.add_item_to_basket_button[16:])
        ActionChains(self.browser).move_to_element(add_to_basket_button).pause(2).click().perform()

        self.browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.CONTROL + Keys.HOME)

    def get_number_of_searching_results(self):
        return len(self.browser.find_elements(*self.results_of_searching))

    def got_to_product_page(self, item):
        self.browser.find_element(By.CSS_SELECTOR, self.link_to_item_from_search_results[:-2] + item + self.link_to_item_from_search_results[-2:]).click()

