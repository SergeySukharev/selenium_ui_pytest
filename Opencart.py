from BaseApp import BasePage
from selenium.webdriver.common.by import By


class OpenCartLocators:
    LOCATOR_OPENCART_SEARCH_FIELD = (By.CSS_SELECTOR, "#search > input")
    LOCATOR_OPENCART_SEARCH_BUTTON = (By.CSS_SELECTOR, "#search > span > button")
    LOCATOR_OPENCART_SEARCH_RESULTS = (By.CLASS_NAME, "product-thumb")
    LOCATOR_OPENCART_ADMIN_LOGIN = (By.ID, "input-username")
    LOCATOR_OPENCART_ADMIN_PASS = (By.ID, "input-password")
    LOCATOR_OPENCART_ADMIN_BUTTON = (By.TAG_NAME, "button")
    LOCATOR_OPENCART_ADMIN_LOGOUT_BUTTON = (By.CSS_SELECTOR, "#header > div > ul > li:nth-child(2) > a")


class Search(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(OpenCartLocators.LOCATOR_OPENCART_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(OpenCartLocators.LOCATOR_OPENCART_SEARCH_BUTTON, time=2).click()

    def search_results(self):
        return self.find_elements(OpenCartLocators.LOCATOR_OPENCART_SEARCH_RESULTS, time=2)


class AdminLoginLogout(BasePage):

    def go_to_site(self):
        return self.driver.get(f'{self.base_url}/admin')

    def login(self):
        login = self.find_element(OpenCartLocators.LOCATOR_OPENCART_ADMIN_LOGIN)
        login.click()
        login.clear()
        login.send_keys('Admin')
        password = self.find_element(OpenCartLocators.LOCATOR_OPENCART_ADMIN_PASS, time=2)
        password.click()
        password.clear()
        password.send_keys('Admin')
        button = self.find_element(OpenCartLocators.LOCATOR_OPENCART_ADMIN_BUTTON, time=2)
        button.click()

    def logout(self):
        logout = self.find_element(OpenCartLocators.LOCATOR_OPENCART_ADMIN_LOGOUT_BUTTON, time=2)
        logout.click()
