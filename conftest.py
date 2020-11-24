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

    def collect_logs_and_close():
        # Логиирование производительности страницы
        with open("logs/performance.log", "w+") as f:
            for line in driver.get_log("performance"):
                f.write(str(line))
                f.write("\n")

        # Логи консоли браузера собирает WARNINGS, ERRORS
        with open("logs/browser.log", "w+") as f:
            for line in driver.get_log("browser"):
                f.write(str(line))
                f.write("\n")

        # Локальное логированеи драйвера
        with open("logs/driver.log", "w+") as f:
            for line in driver.get_log("driver"):
                f.write(str(line))
                f.write("\n")

        driver.quit()
    request.addfinalizer(collect_logs_and_close)
    return driver


def driver_factory(browser):
    if browser == 'chrome':
        caps = DesiredCapabilities.CHROME
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_experimental_option('w3c', False)
        caps['loggingPrefs'] = {'performance': 'ALL', 'browser': 'ALL'}
        driver = webdriver.Chrome(PATH_TO_CHROME, options=options, desired_capabilities=caps)
    elif browser == 'firefox':
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Firefox(executable_path=PATH_TO_FIREFOX, options=options)
    elif browser == 'ie':
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Ie(executable_path=PATH_TO_IE, options=options)
    return driver
