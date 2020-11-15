from BaseApp import BasePage
from selenium.webdriver.common.by import By


class OpencartSearchLocators:
    LOCATOR_OPENCART_SEARCH_FIELD = (By.CSS_SELECTOR, "#search > input")
    LOCATOR_OPENCART_SEARCH_BUTTON = (By.CSS_SELECTOR, "#search > span > button")
    LOCATOR_OPENCART_SEARCH_RESULTS = (By.CLASS_NAME, "product-thumb")


class Search(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(OpencartSearchLocators.LOCATOR_OPENCART_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(OpencartSearchLocators.LOCATOR_OPENCART_SEARCH_BUTTON, time=2).click()

    def search_results(self):
        return self.find_elements(OpencartSearchLocators.LOCATOR_OPENCART_SEARCH_RESULTS, time=2)
