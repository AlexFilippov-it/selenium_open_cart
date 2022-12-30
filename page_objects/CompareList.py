from selenium_open_cart.page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
import time
import allure
from selenium_open_cart.data_users.data import get_login_user
from selenium_open_cart.data_users.data import get_pass_user
from selenium.webdriver.common.keys import Keys


class CompareListPages(BasePage):
    MAIN_MENU = (By.XPATH, "//*[text()='Components']")
    CLICK_TO_MONITORS_CATEGORY = (By.XPATH, "//*[text()='Monitors (2)']")
    CLICK_TO_FIRST_PRODUCT = (By.XPATH, "//div[contains(@class, 'button-group')]//child::*[2]//child::*")
    CLICK_TO_SECOND_PRODUCT = (By.XPATH, "//*[@id='content']/div[3]/div[2]/div/div[2]/div[2]/button[2]")
    CLICK_TO_WISH_LIST = (By.XPATH, "//*[text()='Wish List (2)']")
    NAME_FILD = (By.NAME, "email")
    PASSWORD_FILD = (By.NAME, "password")
    BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FIRST_PRODUCT_IN_WISH_LIST = (By.XPATH, "//*[@id='content']/div[1]/table/tbody/tr[1]/td[6]/a")
    SECOND_PRODUCT_IN_WISH_LIST = (By.XPATH, "//*[@id='content']/div[1]/table/tbody/tr[1]/td[6]/a")

    @allure.issue('https://pytest.org',
                  'Pytest-flaky test retries shows like test steps')
    @allure.step("Go to register page")
    def go_to_catalog_page(self):
        self.driver.find_element(*self.MAIN_MENU).click()
        self.driver.find_element(*self.CLICK_TO_MONITORS_CATEGORY).click()
        time.sleep(0.5)

    @allure.step("Choose two products")
    def choose_two_products(self):
        self.driver.find_element(*self.CLICK_TO_FIRST_PRODUCT).click()
        time.sleep(1.5)
        self.driver.find_element(*self.CLICK_TO_SECOND_PRODUCT).click()
        time.sleep(1.5)

    @allure.step("Click to Wish list")
    def click_to_wish_list(self):
        self.driver.find_element(*self.CLICK_TO_WISH_LIST).click()
        time.sleep(0.5)

    @allure.step("Login in user panel")
    def login_in_user_panel(self):
        self.driver.find_element(*self.NAME_FILD).clear()
        self.driver.find_element(*self.NAME_FILD).send_keys(*get_login_user())
        time.sleep(0.5)
        self.driver.find_element(*self.PASSWORD_FILD).clear()
        self.driver.find_element(*self.PASSWORD_FILD).send_keys(*get_pass_user())
        self.driver.find_element(*self.PASSWORD_FILD).send_keys(Keys.ENTER)
        time.sleep(1.5)

    @allure.step("Delete products from Wish List")
    def delete_first_product(self):
        self.driver.find_element(*self.FIRST_PRODUCT_IN_WISH_LIST).click()

    def delete_second_product(self):
        self.driver.find_element(*self.SECOND_PRODUCT_IN_WISH_LIST).click()
