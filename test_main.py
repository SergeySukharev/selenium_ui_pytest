
def test_title(browser, base_url):
    browser.get(base_url)
    page_title = browser.title
    assert page_title == 'Your Store'


def test_search(browser, base_url):
    browser.get(base_url)
    browser.find_element_by_tag_name('input')


def test_menu(browser, base_url):
    browser.get(base_url)
    element = browser.find_element_by_css_selector('div.collapse.navbar-collapse.navbar-ex1-collapse')
    assert element.find_elements_by_css_selector('a.dropdown-toggle')


def test_center_img(browser, base_url):
    browser.get(base_url)
    images = browser.find_elements_by_tag_name('img')
    assert len(images) == 29


def test_basket(browser, base_url):
    browser.get(base_url)
    browser.find_element_by_css_selector('#cart > button')


def test_feature(browser, base_url):
    browser.get(base_url)
    assert browser.find_elements_by_css_selector('#content > div.row > div:nth-child(1) > div')










