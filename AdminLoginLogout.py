from BaseApp import BasePage
from selenium.webdriver.common.by import By


class OpenCartAdminPageLocators:
    LOCATOR_OPENCART_ADMIN_LOGIN = (By.ID, "input-username")
    LOCATOR_OPENCART_ADMIN_PASS = (By.ID, "input-password")
    LOCATOR_OPENCART_ADMIN_BUTTON = (By.TAG_NAME, "button")
    LOCATOR_OPENCART_ADMIN_LOGOUT_BUTTON = (By.CSS_SELECTOR, "#header > div > ul > li:nth-child(2) > a")


class AdminLoginLogout(BasePage):

    def go_to_site(self):
        return self.driver.get(f'{self.base_url}/admin')

    def login(self, admin_login, admin_password):
        login = self.find_element(OpenCartAdminPageLocators.LOCATOR_OPENCART_ADMIN_LOGIN)
        self.send_data(login, admin_login)
        password = self.find_element(OpenCartAdminPageLocators.LOCATOR_OPENCART_ADMIN_PASS, time=2)
        self.send_data(password, admin_password)
        button = self.find_element(OpenCartAdminPageLocators.LOCATOR_OPENCART_ADMIN_BUTTON, time=2)
        button.click()

    def logout(self):
        logout = self.find_element(OpenCartAdminPageLocators.LOCATOR_OPENCART_ADMIN_LOGOUT_BUTTON, time=2)
        logout.click()
