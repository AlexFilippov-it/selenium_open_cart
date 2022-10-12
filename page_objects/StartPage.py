import time
import allure
from selenium_open_cart.page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class StartPage(BasePage):
    MY_ACCOUNT = (By.XPATH, "//*[text()='My Account']")
    CLICK_TO_REGISTER = (By.XPATH, "//*[text()='Register']")
    CURRENCY = (By.XPATH, "//*[text()='Currency']")
    CURRENCY_EURO = (By.XPATH, "//*[text()='€ Euro']")
    CURRENCY_POUND = (By.XPATH, "//*[text()='£ Pound Sterling']")
    CURRENCY_DOLLAR = (By.XPATH, "//*[text()='$ US Dollar']")

    @allure.issue('https://pytest.org',
                  'Pytest-flaky test retries shows like test steps')
    @allure.step("Go to register page")
    def go_to_register_page(self):
        self.driver.find_element(*self.MY_ACCOUNT).click()
        self.driver.find_element(*self.CLICK_TO_REGISTER).click()

    @allure.step("Choose currency Euro")
    def choose_currency_euro(self):
        self.driver.find_element(*self.CURRENCY).click()
        self.driver.find_element(*self.CURRENCY_EURO).click()
        time.sleep(1.5)

    @allure.step("Choose currency Pound")
    def choose_currency_pound(self):
        self.driver.find_element(*self.CURRENCY).click()
        self.driver.find_element(*self.CURRENCY_POUND).click()
        time.sleep(1.5)

    @allure.step("Choose currency Dollar")
    def choose_currency_dollar(self):
        self.driver.find_element(*self.CURRENCY).click()
        self.driver.find_element(*self.CURRENCY_DOLLAR).click()
        time.sleep(1.5)
