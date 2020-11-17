from Opencart import Search, AdminLoginLogout, AddToCart
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


def test_admin_login(browser, base_url):
    opencart_admin_page = AdminLoginLogout(browser, base_url)
    opencart_admin_page.go_to_site()
    opencart_admin_page.login()
    assert opencart_admin_page.title == 'Dashboard'
    opencart_admin_page.logout()
    assert opencart_admin_page.title == 'Administration'


def test_add_to_cart(browser,base_url):
    opencart_main_page = AddToCart(browser, base_url)
    opencart_main_page.go_to_site()
    opencart_main_page.click_on_add_to_cart_button()
    #opencart_main_page.check_alert()
    opencart_main_page.click_on_cart_button()
    assert opencart_main_page.title == "Shopping Cart"
    assert opencart_main_page.find_total == "£454.10"
    opencart_main_page.click_on_back_to_main_button()
    assert opencart_main_page.title == "Your Store"
