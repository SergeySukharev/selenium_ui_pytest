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
    LOCATOR_OPENCART_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#content > div.row > div:nth-child(1) > div > div.button-group > button:nth-child(1)")
    LOCATOR_OPENCART_ADD_TO_CART_ALERT = (By.CLASS_NAME, "alert alert-success alert-dismissible")
    LOCATOR_OPENCART_CART_BUTTON = (By.XPATH, '//*[@id="cart"]/button')
    LOCATOR_OPENCART_CART_BUTTON_2 = (By.CSS_SELECTOR, "fa fa-shopping-cart")
    LOCATOR_OPENCART_CART_TOTAL = (By.CSS_SELECTOR, "#content > div.row > div > table > tbody > tr:nth-child(4) > td:nth-child(2)")
    LOCATOR_OPENCART_CART_BACK_TO_MAIN_BUTTON = (By.CLASS_NAME, "btn btn-default")
    LOCATOR_OPENCART_PRODUCT_CARD_H1 = (By.XPATH, '//*[@id="content"]/div/div[2]/h1')
    LOCATOR_OPENCART_PRODUCT_CARD_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    LOCATOR_OPENCART_PRODUCT_CARD_ADD_TO_CART_ALERT = (By.XPATH, '//*[@id="product-product"]/div[1]')
    LOCATOR_OPENCART_USER_REGESTRATION_FIRST_NAME = (By.ID, "input-firstname")
    LOCATOR_OPENCART_USER_REGESTRATION_LAST_NAME =(By.ID, 'input-lastname')
    LOCATOR_OPENCART_USER_REGESTRATION_EMAIL = (By.ID, 'input-email')
    LOCATOR_OPENCART_USER_REGESTRATION_PHONE = (By.ID, 'input-telephone')
    LOCATOR_OPENCART_USER_REGESTRATION_PASSWORD = (By.ID, 'input-password')
    LOCATOR_OPENCART_USER_REGESTRATION_PASSWORD_CONFIRM = (By.ID, 'input-confirm')
    LOCATOR_OPENCART_USER_REGESTRATION_PRIVACY_CHECKBOX = (By.CSS_SELECTOR, '#content > form > div > div > input[type=checkbox]:nth-child(2)')
    LOCATOR_OPENCART_USER_REGESTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, '#content > form > div > div > input.btn.btn-primary')


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


class AddToCart(BasePage):

    def click_on_add_to_cart_button(self):
        return self.find_element(OpenCartLocators.LOCATOR_OPENCART_ADD_TO_CART_BUTTON, time=2).click()

    def click_on_cart_button(self):
        self.find_element(OpenCartLocators.LOCATOR_OPENCART_CART_BUTTON, time=2).click()
        self.find_element(OpenCartLocators.LOCATOR_OPENCART_CART_BUTTON_2, time=2).click()

    def check_alert(self):
        return self.find_element(OpenCartLocators.LOCATOR_OPENCART_ADD_TO_CART_ALERT, time=2)

    @property
    def find_total(self):
        return self.find_element(OpenCartLocators.LOCATOR_OPENCART_CART_TOTAL, time=2)

    def click_on_back_to_main_button(self):
        self.find_element(OpenCartLocators.LOCATOR_OPENCART_CART_BACK_TO_MAIN_BUTTON, time=2).click()


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
        return self.find_element(OpenCartLocators.LOCATOR_OPENCART_PRODUCT_CARD_H1, time=2)

    def click_on_add_to_cart_button(self):
        return self.find_element(OpenCartLocators.LOCATOR_OPENCART_PRODUCT_CARD_ADD_TO_CART_BUTTON, time=2).click()

    def add_to_cart_alert(self):
        return self.find_element(OpenCartLocators.LOCATOR_OPENCART_PRODUCT_CARD_ADD_TO_CART_ALERT)


class UserRegistrationForm(BasePage):

    def go_to_site(self):
        return self.driver.get(f'{self.base_url}/index.php?route=account/register')

    def send_registration_data(self, first_name, last_name, password, email, phone):
        login_1 = self.find_element(OpenCartLocators.LOCATOR_OPENCART_USER_REGESTRATION_FIRST_NAME)
        login_1.send_keys(first_name)
        login_2 = self.find_element(OpenCartLocators.LOCATOR_OPENCART_USER_REGESTRATION_LAST_NAME)
        login_2.send_keys(last_name)
        telepohone = self.find_element(OpenCartLocators.LOCATOR_OPENCART_USER_REGESTRATION_PHONE)
        telepohone.send_keys(phone)
        e_mail = self.find_element(OpenCartLocators.LOCATOR_OPENCART_USER_REGESTRATION_EMAIL)
        e_mail.send_keys(email)
        secret = self.find_element(OpenCartLocators.LOCATOR_OPENCART_USER_REGESTRATION_PASSWORD)
        secret.send_keys(password)
        confirm = self.find_element(OpenCartLocators.LOCATOR_OPENCART_USER_REGESTRATION_PASSWORD_CONFIRM)
        confirm.send_keys(password)

    def submit_check(self):
        checkbox = self.find_element(OpenCartLocators.LOCATOR_OPENCART_USER_REGESTRATION_PRIVACY_CHECKBOX)
        checkbox.click()

    def submit_button(self):
        button = self.find_element(OpenCartLocators.LOCATOR_OPENCART_USER_REGESTRATION_SUBMIT_BUTTON)
        button.click()









