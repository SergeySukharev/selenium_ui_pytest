from BaseApp import BasePage
from selenium.webdriver.common.by import By


class OpenCartAddToCartLocators:
    LOCATOR_OPENCART_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#content > div.row > div:nth-child(1) > div > div.button-group > button:nth-child(1)")
    LOCATOR_OPENCART_ADD_TO_CART_ALERT = (By.CLASS_NAME, "alert alert-success alert-dismissible")
    LOCATOR_OPENCART_CART_BUTTON = (By.XPATH, '//*[@id="common-home"]/div[1]/a[2]')
    LOCATOR_OPENCART_CART_TOTAL = (By.CSS_SELECTOR, "#content > div.row > div > table > tbody > tr:nth-child(4) > td:nth-child(2)")
    LOCATOR_OPENCART_CART_BACK_TO_MAIN_BUTTON = (By.XPATH, '//*[@id="content"]/div[3]/div[1]/a')


class AddToCart(BasePage):

    def click_on_add_to_cart_button(self):
        return self.find_element(OpenCartAddToCartLocators.LOCATOR_OPENCART_ADD_TO_CART_BUTTON, time=2).click()

    def click_on_cart_button(self):
        button_1 = self.find_element(OpenCartAddToCartLocators.LOCATOR_OPENCART_CART_BUTTON, time=2)
        button_1.click()

    def check_alert(self):
        return self.find_element(OpenCartAddToCartLocators.LOCATOR_OPENCART_ADD_TO_CART_ALERT, time=2)

    @property
    def find_total(self):
        return self.find_element(OpenCartAddToCartLocators.LOCATOR_OPENCART_CART_TOTAL, time=2)

    def click_on_back_to_main_button(self):
        self.find_element(OpenCartAddToCartLocators.LOCATOR_OPENCART_CART_BACK_TO_MAIN_BUTTON, time=2).click()
