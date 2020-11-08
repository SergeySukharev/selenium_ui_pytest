

def test_search(browser, base_url):
    browser.get(f'{base_url}/index.php?route=product/category&path=20')
    browser.find_element_by_tag_name('input')


def test_menu(browser, base_url):
    browser.get(f'{base_url}/index.php?route=product/category&path=20')
    element = browser.find_element_by_css_selector('#content')
    assert element.find_elements_by_css_selector('#content > div:nth-child(7) > div:nth-child(1)')


def test_center_img(browser, base_url):
    browser.get(f'{base_url}/index.php?route=product/category&path=20')
    images = browser.find_elements_by_tag_name('button')
    assert len(images) == 45


def test_basket(browser, base_url):
    browser.get(f'{base_url}/index.php?route=product/category&path=20')
    browser.find_element_by_css_selector('#input-sort')


def test_feature(browser, base_url):
    browser.get(f'{base_url}/index.php?route=product/category&path=20')
    assert browser.find_elements_by_css_selector('#list-view')

