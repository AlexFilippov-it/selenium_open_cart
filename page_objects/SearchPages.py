from selenium_open_cart.page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
import time
import allure
from selenium_open_cart.data_users.data import get_login_user
from selenium_open_cart.data_users.data import get_pass_user
from selenium.webdriver.common.keys import Keys


class SearchPages(BasePage):
    MAIN_SEARCH_FIELD = (By.XPATH, "//*[@id='search']/input")
    CLICK_TO_SEARCH_ICON = (By.XPATH, "//*[@id='search']/span/button")
    CLICK_TO_SEARCH_IN_PRODUCT_DESCRIPTION = (By.XPATH, "//*[@id='description']")
    CLICK_TO_BUTTON_SEARCH = (By.XPATH, "//*[@id='button-search']")
    CLICK_TO_CHANGE_LIST = (By.XPATH, "//*[@id='list-view']/i")
    CLICK_TO_SORT_BY = (By.XPATH, "//*[@id='input-sort']")
    CHOSE_HIGH_LOW_PRICE = (By.XPATH, "//*[@id='input-sort']/option[5]")
    CLICK_TO_SORT_SHOW = (By.XPATH, "//*[@id='input-limit']")
    CLICK_TO_SORT_SHOW_25 = (By.XPATH, "//*[@id='input-limit']/option[2]")
    CLICK_TO_COMPARE_FIRST = (By.XPATH, "//button[contains(@data-original-title, 'Compare this Product')]/i")
    CLICK_TO_COMPARE_SECOND = (By.XPATH, "//*[@id='content']/div[3]/div[2]/div/div[2]/div[2]/button[3]/i")
    CLICK_TO_COMPARE_PRODUCT = (By.XPATH, "//div[contains(@class,'form-group')]/a")
    CLICK_TO_REMOVE_FIRST_PRODUCT = (By.XPATH, "//*[@id='content']/table/tbody[3]/tr/td[3]/a")
    CLICK_ADD_PRODUCT_TO_CART = (By.XPATH, "//input[@class='btn btn-primary btn-block']")
    CLICK_CART = (By.XPATH, "//*[@id='cart-total']")
    CLICK_GO_TO_CART = (By.XPATH, "//*[@id='cart']/ul/li[2]/div/p/a[1]")

    @allure.issue('https://pytest.org',
                  'Pytest-flaky test retries shows like test steps')
    @allure.step("Write word Apple")
    def write_apple_and_search(self):
        self.driver.find_element(*self.MAIN_SEARCH_FIELD).send_keys("apple")
        self.driver.find_element(*self.CLICK_TO_SEARCH_ICON).click()
        time.sleep(1.5)

    @allure.step("Choose show in description")
    def search_in_description(self):
        self.driver.find_element(*self.CLICK_TO_SEARCH_IN_PRODUCT_DESCRIPTION).click()
        time.sleep(0.5)
        self.driver.find_element(*self.CLICK_TO_BUTTON_SEARCH).click()
        time.sleep(0.5)

    @allure.step("Check search page")
    def check_search_page(self):
        self.driver.find_element(*self.CLICK_TO_CHANGE_LIST).click()
        time.sleep(0.5)
        self.driver.find_element(*self.CLICK_TO_SORT_BY).click()
        time.sleep(0.5)
        self.driver.find_element(*self.CHOSE_HIGH_LOW_PRICE).click()
        time.sleep(0.5)
        self.driver.find_element(*self.CLICK_TO_SORT_SHOW).click()
        time.sleep(0.5)
        self.driver.find_element(*self.CLICK_TO_SORT_SHOW_25).click()
        time.sleep(0.5)

    @allure.step("Add to compare")
    def add_to_compare(self):
        self.driver.find_element(*self.CLICK_TO_COMPARE_FIRST).click()
        time.sleep(1.5)
        self.driver.find_element(*self.CLICK_TO_COMPARE_SECOND).click()
        time.sleep(1.5)
        self.driver.find_element(*self.CLICK_TO_COMPARE_PRODUCT).click()
        time.sleep(1.5)

    @allure.step("Click remove for first product")
    def remove_first_product(self):
        self.driver.find_element(*self.CLICK_TO_REMOVE_FIRST_PRODUCT).click()
        time.sleep(1.5)

    @allure.step("Click add to Cart for second product")
    def add_to_cart_second_product(self):
        self.driver.find_element(*self.CLICK_ADD_PRODUCT_TO_CART).click()
        time.sleep(3.5)
        self.driver.find_element(*self.CLICK_CART).click()
        time.sleep(3.5)
        self.driver.find_element(*self.CLICK_GO_TO_CART).click()
        time.sleep(5.5)
