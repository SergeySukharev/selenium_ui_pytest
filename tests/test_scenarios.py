from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_admin_login_logout(browser, base_url):
    browser.get(f'{base_url}/admin')
    browser.find_element_by_id('input-username').send_keys('Admin')
    browser.find_element_by_id('input-password').send_keys('Admin')
    browser.find_element_by_tag_name('button').click()

    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.title_is("Dashboard"))
    el = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div/ul/li[2]/a')))

    el.click()
    wait.until(EC.title_is("Administration"))


def test_admin_goods_table(browser, base_url):
    browser.get(f'{base_url}/admin')
    browser.find_element_by_id('input-username').send_keys('Admin')
    browser.find_element_by_id('input-password').send_keys('Admin')
    browser.find_element_by_tag_name('button').click()

    wait = WebDriverWait(browser, 10, poll_frequency=1)
    browser.find_element_by_css_selector('#menu-catalog > a').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "collapse1"] / li[2] / a'))).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#content > div.container-fluid > div > '
                                                            'div.col-md-9.col-md-pull-3.col-sm-12 > div > '
                                                            'div.panel-body')))
