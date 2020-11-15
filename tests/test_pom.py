from Opencart import Search, AdminLoginLogout
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

