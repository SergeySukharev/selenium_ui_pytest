from BaseApp import BasePage
from selenium.webdriver.common.by import By


class OpenCartUserRegestrationLocators:
    LOCATOR_OPENCART_USER_REGESTRATION_FIRST_NAME = (By.ID, "input-firstname")
    LOCATOR_OPENCART_USER_REGESTRATION_LAST_NAME =(By.ID, 'input-lastname')
    LOCATOR_OPENCART_USER_REGESTRATION_EMAIL = (By.ID, 'input-email')
    LOCATOR_OPENCART_USER_REGESTRATION_PHONE = (By.ID, 'input-telephone')
    LOCATOR_OPENCART_USER_REGESTRATION_PASSWORD = (By.ID, 'input-password')
    LOCATOR_OPENCART_USER_REGESTRATION_PASSWORD_CONFIRM = (By.ID, 'input-confirm')
    LOCATOR_OPENCART_USER_REGESTRATION_PRIVACY_CHECKBOX = (By.CSS_SELECTOR, '#content > form > div > div > input[type=checkbox]:nth-child(2)')
    LOCATOR_OPENCART_USER_REGESTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, '#content > form > div > div > input.btn.btn-primary')


class UserRegistrationForm(BasePage):

    def go_to_site(self):
        return self.driver.get(f'{self.base_url}/index.php?route=account/register')

    def send_registration_data(self, first_name, last_name, password, email, phone):
        login_1 = self.find_element(OpenCartUserRegestrationLocators.LOCATOR_OPENCART_USER_REGESTRATION_FIRST_NAME)
        self.send_data(login_1, first_name)
        login_2 = self.find_element(OpenCartUserRegestrationLocators.LOCATOR_OPENCART_USER_REGESTRATION_LAST_NAME)
        self.send_data(login_2, last_name)
        telephone = self.find_element(OpenCartUserRegestrationLocators.LOCATOR_OPENCART_USER_REGESTRATION_PHONE)
        self.send_data(telephone, phone)
        e_mail = self.find_element(OpenCartUserRegestrationLocators.LOCATOR_OPENCART_USER_REGESTRATION_EMAIL)
        self.send_data(e_mail, email)
        secret = self.find_element(OpenCartUserRegestrationLocators.LOCATOR_OPENCART_USER_REGESTRATION_PASSWORD)
        self.send_data(secret, password)
        confirm = self.find_element(OpenCartUserRegestrationLocators.LOCATOR_OPENCART_USER_REGESTRATION_PASSWORD_CONFIRM)
        self.send_data(confirm, password)

    def submit_check(self):
        checkbox = self.find_element(OpenCartUserRegestrationLocators.LOCATOR_OPENCART_USER_REGESTRATION_PRIVACY_CHECKBOX)
        checkbox.click()

    def submit_button(self):
        button = self.find_element(OpenCartUserRegestrationLocators.LOCATOR_OPENCART_USER_REGESTRATION_SUBMIT_BUTTON)
        button.click()
