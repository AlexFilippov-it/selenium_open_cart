import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
import sys
import logging
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

sys.path.append('/Users/apple/Documents/otus/lesson_8/')


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.8.100:8085/")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("~/Documents/otus/drivers"))
    parser.addoption("--log_level", action="store", default="DEBUG")


@pytest.fixture
def browser(request):
    # Сбор параметров запуска для pytest
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")
    log_level = request.config.getoption("--log_level")

    class MyListener(AbstractEventListener):
        logger = logging.getLogger(request.node.name)
        logger.setLevel(logging.DEBUG)
        ch = logging.FileHandler(
            filename=f"logs/{request.node.name}.log")
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(logging.Formatter('%(asctime)s %(name)s:%(levelname)s %(message)s'))
        logger.addHandler(ch)

        def before_navigate_to(self, url, driver):
            self.logger.info(f"I'm navigating to {url} and {driver.title}")

        def after_navigate_to(self, url, driver):
            self.logger.info(f"I'm on {url}")

        def before_navigate_back(self, driver):
            self.logger.info(f"I'm navigating back")

        def after_navigate_back(self, driver):
            self.logger.info(f"I'm back!")

        def before_find(self, by, value, driver):
            self.logger.info(f"I'm looking for '{value}' with '{by}'")

        def after_find(self, by, value, driver):
            self.logger.info(f"I've found '{value}' with '{by}'")

        def before_click(self, element, driver):
            self.logger.info(f"I'm clicking {element}")

        def after_click(self, element, driver):
            self.logger.info(f"I've clicked {element}")

        def before_execute_script(self, script, driver):
            self.logger.info(f"I'm executing '{script}'")

        def after_execute_script(self, script, driver):
            self.logger.info(f"I've executed '{script}'")

        def before_quit(self, driver):
            self.logger.info(f"I'm getting ready to terminate {driver}")

        def after_quit(self, driver):
            self.logger.info(f"Driver Quit")

    if browser == "chrome":
        service = ChromiumService(executable_path=drivers + "/chromedriver")
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FFService(executable_path=drivers + "/geckodriver")
        driver = webdriver.Firefox(service=service)
    else:
        driver = webdriver.Safari()

    driver = EventFiringWebDriver(driver, MyListener())
    driver.test_name = request.node.name
    driver.log_level = log_level

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
