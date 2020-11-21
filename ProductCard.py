from BaseApp import BasePage
from selenium.webdriver.common.by import By


class OpenCartProductCartLocators:
    LOCATOR_OPENCART_PRODUCT_CARD_H1 = (By.XPATH, '//*[@id="content"]/div/div[2]/h1')
    LOCATOR_OPENCART_PRODUCT_CARD_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    LOCATOR_OPENCART_PRODUCT_CARD_ADD_TO_CART_ALERT = (By.XPATH, '//*[@id="product-product"]/div[1]')


class ProductCard(BasePage):

    def __init__(self, driver, base_url, page_url):
        super().__init__(driver, base_url)
        self.driver = driver
        self.base_url = base_url
        self.page_url = page_url

    def go_to_site(self):
        return self.driver.get(f"{self.base_url}/{self.page_url}")

    @property
    def find_product_name(self):
        return self.find_element(OpenCartProductCartLocators.LOCATOR_OPENCART_PRODUCT_CARD_H1, time=2)

    def click_on_add_to_cart_button(self):
        return self.find_element(OpenCartProductCartLocators.LOCATOR_OPENCART_PRODUCT_CARD_ADD_TO_CART_BUTTON, time=2).click()

    def add_to_cart_alert(self):
        return self.find_element(OpenCartProductCartLocators.LOCATOR_OPENCART_PRODUCT_CARD_ADD_TO_CART_ALERT)
