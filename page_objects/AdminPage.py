from selenium.webdriver.common.by import By
from selenium_open_cart.page_objects.BasePage import BasePage
from selenium_open_cart.data_users.data import get_login
from selenium_open_cart.data_users.data import get_pass
import time
import allure
from selenium.common.exceptions import NoSuchElementException


class AdminPage(BasePage):
    USERNAME_FILD = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_FILD = (By.NAME, "password")
    BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    CHOICE_PARENT_CATEGORY = (By.XPATH, "//*[text()=' Catalog']")
    CHOICE_CHILD_CATEGORY = (By.XPATH, "//*[@id='collapse1']/li[2]/a")

    @allure.step("Looked for Username fild")
    def insert_login(self):
        self.driver.find_element(*self.USERNAME_FILD).clear()
        self.driver.find_element(*self.USERNAME_FILD).send_keys(*get_login())

    @allure.step("Looked for Password fild")
    def insert_password(self):
        self.driver.find_element(*self.PASSWORD_FILD).clear()
        self.driver.find_element(*self.PASSWORD_FILD).send_keys(*get_pass())

    @allure.step("Did click on Button")
    def click_to_button_login(self):
        try:
            self.driver.find_element(*self.BUTTON).click()
            time.sleep(0.5)
        except NoSuchElementException as e:
            allure.attach(body=self.driver.get_screenshot_as_png(),
                          name="screenshot_image",
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(e.msg)

    @allure.step("Choice category")
    def go_to_category(self):
        try:
            self.driver.find_element(*self.CHOICE_PARENT_CATEGORY).click()
            time.sleep(0.5)
        except NoSuchElementException as e:
            allure.attach(body=self.driver.get_screenshot_as_png(),
                          name="screenshot_image",
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(e.msg)
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

    @allure.step("Do click to icon")
    def go_to_create_product(self):
        self.driver.find_element(*self.CLICK_TO_ICON).click()

    @allure.step("Added title product")
    def add_title_product(self):
        self.driver.find_element(*self.ADD_TITLE).send_keys("Title product random")

    @allure.step("Added description product")
    def add_description_product(self):
        self.driver.find_element(*self.ADD_DESCRIPTION) \
            .send_keys("Text of Description")

    @allure.step("Added tag title")
    def add_tag_title(self):
        self.driver.find_element(*self.ADD_TAG_TITLE) \
            .send_keys("Title product tag")

    @allure.step("Added tag description")
    def add_tag_description(self):
        self.driver.find_element(*self.ADD_TAG_DESCRIPTION) \
            .send_keys("Title product description")

    @allure.step("Go to another tab")
    def go_to_tab_data(self):
        self.driver.find_element(*self.GO_TO_TAB_DATA).click()

    @allure.step("Added model product")
    def add_model_product(self):
        self.driver.find_element(*self.ADD_MODEL_PRODUCT).send_keys("model1")

    @allure.step("Click to safe product")
    def click_to_safe_product(self):
        try:
            self.driver.find_element(*self.CLICK_TO_SAFE_PRODUCT).click()
        except NoSuchElementException as e:
            allure.attach(body=self.driver.get_screenshot_as_png(),
                          name="screenshot_image",
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(e.msg)


class DeleteProduct(BasePage):
    SELECT_PRODUCT = (By.XPATH, "//*[text()='Title product random']//..//input")
    BUTTON_DELETE_PRODUCT = (By.XPATH, "//button[@class='btn btn-danger']")

    @allure.link('https://webformyself.com/kak-udalit-vse-tovary-v-opencart/',
                 name='How is delete product from OpenCart')
    @allure.step("Select product")
    def select_product(self):
        self.driver.find_element(*self.SELECT_PRODUCT).click()

    @allure.step("Click on button delete")
    def click_on_button_delete(self):
        self.driver.find_element(*self.BUTTON_DELETE_PRODUCT).click()

    @allure.step("Switch to alert and accepted")
    def alert_accept(self):
        try:
            alert = self.driver.switch_to.alert
            time.sleep(1)
            alert.accept()
            time.sleep(1)
        except NoSuchElementException as e:
            allure.attach(body=self.driver.get_screenshot_as_png(),
                          name="screenshot_image",
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(e.msg)
