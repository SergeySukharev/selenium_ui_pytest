

def test_search(browser, base_url):
    browser.get(f'{base_url}index.php?route=product/product&path=20&product_id=44')
    browser.find_element_by_tag_name('h1')


def test_menu(browser, base_url):
    browser.get(f'{base_url}index.php?route=product/product&path=20&product_id=44')
    element = browser.find_element_by_css_selector('#content > div > div.col-sm-8 > ul.thumbnails')
    assert element.find_elements_by_css_selector('a.thumbnail')


def test_center_img(browser, base_url):
    browser.get(f'{base_url}index.php?route=product/product&path=20&product_id=44')
    images = browser.find_elements_by_tag_name('button')
    assert len(images) == 11


def test_basket(browser, base_url):
    browser.get(f'{base_url}index.php?route=product/product&path=20&product_id=44')
    browser.find_element_by_css_selector('#button-cart')


def test_feature(browser, base_url):
    browser.get(f'{base_url}index.php?route=product/product&path=20&product_id=44')
    assert browser.find_elements_by_css_selector('button.btn.btn-default')
