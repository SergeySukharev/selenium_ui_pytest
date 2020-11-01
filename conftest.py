import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


PATH_TO_CHROME = 'drivers/chromedriver.exe'
PATH_TO_FIREFOX = 'drivers/geckodriver.exe'
PATH_TO_IE = 'drivers/IEDriverServer.exe'


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://demo.opencart.com/",
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


@pytest.fixture(scope="module")
def browser(request):
    if request.config.getoption("--browser") == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("--start-maximized")
        wd = webdriver.Chrome(PATH_TO_CHROME, options=options)
        yield wd
        wd.quit()
    elif request.config.getoption("--browser") == 'firefox':
        options = Options()
        options.add_argument("--headless")
        wd = webdriver.Firefox(executable_path=PATH_TO_FIREFOX, options=options)
        wd.maximize_window()
        yield wd
        wd.quit()
    elif request.config.getoption("--browser") == 'ie':
        capabilities = DesiredCapabilities.INTERNETEXPLORER
        capabilities["acceptInsecureCerts"] = True
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        wd = webdriver.Ie(executable_path=PATH_TO_IE, options=options, capabilities=capabilities)
        yield wd
        wd.quit()
