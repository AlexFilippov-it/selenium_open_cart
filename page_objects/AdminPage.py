from selenium.webdriver.common.by import By
from selenium_open_cart.page_objects.BasePage import BasePage
from selenium_open_cart.test_data.data import get_login
from selenium_open_cart.test_data.data import get_pass
import time


class AdminPage(BasePage):
    USERNAME_FILD = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_FILD = (By.NAME, "password")
    BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    CHOICE_PARENT_CATEGORY = (By.XPATH, "//*[text()=' Catalog']")
    CHOICE_CHILD_CATEGORY = (By.XPATH, "//*[@id='collapse1']/li[2]/a")

    def insert_login(self):
        self.driver.find_element(*self.USERNAME_FILD).clear()
        self.driver.find_element(*self.USERNAME_FILD).send_keys(*get_login())

    def insert_password(self):
        self.driver.find_element(*self.PASSWORD_FILD).clear()
        self.driver.find_element(*self.PASSWORD_FILD).send_keys(*get_pass())

    def click_to_button_login(self):
        self.driver.find_element(*self.BUTTON).click()
        time.sleep(0.5)

    def go_to_category(self):
        self.driver.find_element(*self.CHOICE_PARENT_CATEGORY).click()
        time.sleep(0.5)
        self.driver.find_element(*self.CHOICE_CHILD_CATEGORY).click()


class AddProduct(BasePage):
    CLICK_TO_ICON = (By.XPATH, "//div[contains(@class, 'pull-right')]/a")
    ADD_TITLE = (By.XPATH, "//*[@id='input-name1']")
    ADD_DESCRIPTION = (By.XPATH, "//*[@id='language1']/div[2]/div/div/div[3]/div[2]")
    ADD_TAG_TITLE = (By.XPATH, "//*[@id='input-meta-title1']")
    ADD_TAG_DESCRIPTION = (By.XPATH, "//*[@id='input-meta-description1']")
    GO_TO_TAB_DATA = (By.XPATH, "//*[@id='form-product']/ul/li[2]/a")
    ADD_MODEL_PRODUCT = (By.XPATH, "//*[@id='input-model']")
    CLICK_TO_SAFE_PRODUCT = (By.XPATH, "//*[@id='content']/div[1]/div/div/button/i")

    def go_to_create_product(self):
        self.driver.find_element(*self.CLICK_TO_ICON).click()

    def add_title_product(self):
        self.driver.find_element(*self.ADD_TITLE).send_keys("Title product random")

    def add_description_product(self):
        self.driver.find_element(*self.ADD_DESCRIPTION) \
            .send_keys("Text of Description")

    def add_tag_title(self):
        self.driver.find_element(*self.ADD_TAG_TITLE) \
            .send_keys("Title product tag")

    def add_tag_description(self):
        self.driver.find_element(*self.ADD_TAG_DESCRIPTION) \
            .send_keys("Title product description")

    def go_to_tab_data(self):
        self.driver.find_element(*self.GO_TO_TAB_DATA).click()

    def add_model_product(self):
        self.driver.find_element(*self.ADD_MODEL_PRODUCT).send_keys("model1")

    def click_to_safe_product(self):
        self.driver.find_element(*self.CLICK_TO_SAFE_PRODUCT).click()


class DeleteProduct(BasePage):
    SELECT_PRODUCT = (By.XPATH, "//*[text()='Title product random']//..//input")
    BUTTON_DELETE_PRODUCT = (By.XPATH, "//button[@class='btn btn-danger']")

    def select_product(self):
        self.driver.find_element(*self.SELECT_PRODUCT).click()

    def click_on_button_delete(self):
        self.driver.find_element(*self.BUTTON_DELETE_PRODUCT).click()

    def alert_accept(self):
        alert = self.driver.switch_to.alert
        time.sleep(1)
        alert.accept()
        time.sleep(1)
