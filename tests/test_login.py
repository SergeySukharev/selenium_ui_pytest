

def test_search(browser, base_url):
    browser.get(f'{base_url}/index.php?route=account/login')
    assert browser.find_elements_by_tag_name('div')


def test_menu(browser, base_url):
    browser.get(f'{base_url}/index.php?route=account/login')
    element = browser.find_element_by_css_selector('#content > div > div:nth-child(2) > div')
    assert element.find_elements_by_css_selector('div.form-group')


def test_center_img(browser, base_url):
    browser.get(f'{base_url}/index.php?route=account/login')
    images = browser.find_elements_by_css_selector('a.list-group-item')
    assert len(images) == 13


def test_basket(browser, base_url):
    browser.get(f'{base_url}/index.php?route=account/login')
    browser.find_element_by_css_selector('input.btn.btn-primary')


def test_feature(browser, base_url):
    browser.get(f'{base_url}/index.php?route=account/login')
    assert browser.find_elements_by_tag_name('p')
