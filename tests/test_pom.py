from Search import Search
from AdminLoginLogout import AdminLoginLogout
from AddToCart import AddToCart
from ProductCard import ProductCard
from UserRegistrationForm import UserRegistrationForm
import pytest


@pytest.mark.parametrize('value', ['MacBook', 'iPod'])
def test_opencart_search(browser, base_url, value):
    opencart_main_page = Search(browser, base_url)
    opencart_main_page.go_to_site()
    opencart_main_page.enter_word(value)
    opencart_main_page.click_on_the_search_button()
    elements = opencart_main_page.search_results()
    for elem in elements:
        assert value in elem.text


@pytest.mark.parametrize('admin_login, admin_password', [('admin', 'admin')])
def test_admin_login(browser, base_url, admin_login, admin_password):
    opencart_admin_page = AdminLoginLogout(browser, base_url)
    opencart_admin_page.go_to_site()
    opencart_admin_page.login(admin_login, admin_password)
    assert opencart_admin_page.title == 'Dashboard'
    opencart_admin_page.logout()
    assert opencart_admin_page.title == 'Administration'


def test_add_to_cart(browser, base_url):
    opencart_main_page = AddToCart(browser, base_url)
    opencart_main_page.go_to_site()
    opencart_main_page.click_on_add_to_cart_button()
    opencart_main_page.click_on_cart_button()
    assert opencart_main_page.title == "Shopping Cart"
    opencart_main_page.click_on_back_to_main_button()
    assert opencart_main_page.title == "Your Store"


PRODUCT_CARDS_URLS = {
    "MacBook": "index.php?route=product/product&product_id=43",
    "Iphone": "index.php?route=product/product&product_id=40"
}


@pytest.mark.parametrize("urls", list(PRODUCT_CARDS_URLS.values()))
def test_product_card(browser, base_url, urls):
    product_card_page = ProductCard(browser, base_url, urls)
    product_card_page.go_to_site()
    assert product_card_page.find_product_name.text == product_card_page.title
    product_card_page.click_on_add_to_cart_button()
    product_card_page.add_to_cart_alert()


USERS = [
    {
        "FirstName": "Aleksey",
        "LastName": "Ivanov",
        "e_mail": "ivano@mail.ru",
        "phone": "89240083321",
        "password": "Pa$$w0rd"
    }
]


@pytest.mark.parametrize("users", USERS)
def test_user_registration(browser, base_url, users):
    user_registration_page = UserRegistrationForm(browser, base_url)
    user_registration_page.go_to_site()
    user_registration_page.send_registration_data(users['FirstName'], users['LastName'], users["password"],
                                                  users["e_mail"], users["phone"])
    user_registration_page.submit_check()
    user_registration_page.submit_button()
