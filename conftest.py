import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
import sys

sys.path.append('/Users/apple/Documents/otus/lesson_8/')


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.8.106:8085/")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("~/Documents/otus/drivers"))
    parser.addoption("--log_level", action="store", default="DEBUG")


@pytest.fixture
def browser(request):
    # Сбор параметров запуска для pytest
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")
    log_level = request.config.getoption("--log_level")

    if browser == "chrome":
        service = ChromiumService(executable_path=drivers + "/chromedriver")
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FFService(executable_path=drivers + "/geckodriver")
        driver = webdriver.Firefox(service=service)
    else:
        driver = webdriver.Safari()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
