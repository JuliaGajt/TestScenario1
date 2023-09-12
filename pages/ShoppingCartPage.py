from selenium.webdriver.common.by import By


class ShoppingCartPage:

    url = "https://magento.softwaretestingboard.com/checkout/cart/"
    products_on_cart = (By.XPATH, "//*[@class='product-item-name']/a[not(@data-bind)]")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.url)

    def get_title(self):
        return self.browser.title

    def get_products_in_shopping_cart(self):
        return [product.text for product in self.browser.find_elements(*self.products_on_cart)]

