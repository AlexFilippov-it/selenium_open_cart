import time

from selenium.webdriver.common.by import By
from selenium_open_cart.page_objects.BasePage import BasePage


class StartPage(BasePage):
    MY_ACCOUNT = (By.XPATH, "//*[text()='My Account']")
    CLICK_TO_REGISTER = (By.XPATH, "//*[text()='Register']")
    CURRENCY = (By.XPATH, "//*[text()='Currency']")
    CURRENCY_EURO = (By.XPATH, "//*[text()='€ Euro']")
    CURRENCY_POUND = (By.XPATH, "//*[text()='£ Pound Sterling']")
    CURRENCY_DOLLAR = (By.XPATH, "//*[text()='$ US Dollar']")

    def go_to_register_page(self):
        self.driver.find_element(*self.MY_ACCOUNT).click()
        self.driver.find_element(*self.CLICK_TO_REGISTER).click()

    def choose_currency_euro(self):
        self.driver.find_element(*self.CURRENCY).click()
        self.driver.find_element(*self.CURRENCY_EURO).click()
        time.sleep(1.5)

    def choose_currency_pound(self):
        self.driver.find_element(*self.CURRENCY).click()
        self.driver.find_element(*self.CURRENCY_POUND).click()
        time.sleep(1.5)

    def choose_currency_dollar(self):
        self.driver.find_element(*self.CURRENCY).click()
        self.driver.find_element(*self.CURRENCY_DOLLAR).click()
        time.sleep(1.5)
