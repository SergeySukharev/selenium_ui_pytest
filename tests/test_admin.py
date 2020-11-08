

def test_search(browser, base_url):
    browser.get(f'{base_url}/admin')
    browser.find_element_by_css_selector('h1.panel-title')


def test_menu(browser, base_url):
    browser.get(f'{base_url}/admin')
    element = browser.find_element_by_css_selector('div.panel-body')
    assert element.find_elements_by_css_selector('div.form-group')


def test_center_img(browser, base_url):
    browser.get(f'{base_url}/admin')
    images = browser.find_elements_by_tag_name('div')
    assert len(images) == 15


def test_basket(browser, base_url):
    browser.get(f'{base_url}/admin')
    browser.find_element_by_css_selector('button.btn.btn-primary')


def test_feature(browser, base_url):
    browser.get(f'{base_url}/admin')
    browser.find_element_by_css_selector('#content > div > div > div > div > div.panel-body > form > div:nth-child(2) '
                                         '> span > a')
