import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


PATH_TO_CHROME = 'drivers/chromedriver.exe'
PATH_TO_FIREFOX = 'drivers/geckodriver.exe'
PATH_TO_IE = 'drivers/IEDriverServer.exe'


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://demo.opencart.com",
        help="Request base url"
    )
    parser.addoption(
        "--browser",
        action="store",
        default='chrome',
        help="Browser to use"
    )


@pytest.fixture(scope="module")
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    driver = driver_factory(request.config.getoption("--browser"))
    driver.maximize_window()
    # driver.implicitly_wait(5)
    request.addfinalizer(driver.quit)
    return driver


def driver_factory(browser):
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = webdriver.Chrome(PATH_TO_CHROME, options=options)
    elif browser == 'firefox':
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Firefox(executable_path=PATH_TO_FIREFOX, options=options)
    elif browser == 'ie':
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Ie(executable_path=PATH_TO_IE, options=options)
    return driver


