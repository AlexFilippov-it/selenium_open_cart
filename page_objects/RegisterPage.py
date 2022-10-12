import time
from selenium.webdriver.common.by import By
from selenium_open_cart.page_objects.BasePage import BasePage
import allure
from selenium.common.exceptions import NoSuchElementException


class PersonalDetails(BasePage):
    FILD_FIRST_NAME = (By.XPATH, "//*[@id='input-firstname']")
    FILD_LAST_NAME = (By.XPATH, "//*[@id='input-lastname']")
    EMAIL = (By.XPATH, "//*[@id='input-email']")
    TEL = (By.XPATH, "//*[@id='input-telephone']")
    PASSWORD = (By.XPATH, "//*[@id='input-password']")
    CONFIRM_PASSWORD = (By.XPATH, "//*[@id='input-confirm']")
    NEWS_SUBSCRIBE = (By.XPATH, "//input[@type='radio'][@name='newsletter'][@value='1']")
    AGREE_TO_PRIVACY_POLICE = (By.XPATH, "//input[@type='checkbox'][@name='agree'][@value='1']")
    BUTTON_CONTINUE = (By.XPATH, "//input[@type='submit'][@class='btn btn-primary']")

    @allure.step("Wrote first name")
    def write_first_name(self):
        self.driver.find_element(*self.FILD_FIRST_NAME).clear()
        self.driver.find_element(*self.FILD_FIRST_NAME).send_keys("Test user")

    @allure.step("Wrote last name")
    def write_last_name(self):
        self.driver.find_element(*self.FILD_LAST_NAME).clear()
        self.driver.find_element(*self.FILD_LAST_NAME).send_keys("Test Last Name")

    @allure.step("Wrote email")
    def write_email(self):
        self.driver.find_element(*self.EMAIL).clear()
        self.driver.find_element(*self.EMAIL).send_keys("test_user@gmail.com")

    @allure.step("Wrote telephone")
    def write_telephone(self):
        self.driver.find_element(*self.TEL).clear()
        self.driver.find_element(*self.TEL).send_keys("+79259999999")

    @allure.step("Wrote password")
    def write_password(self):
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys("14253647")

    @allure.step("Wrote confirm password")
    def write_confirm_password(self):
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys("14253647")

    @allure.step("Added news subscribe")
    def news_subscribe_add(self):
        self.driver.find_element(*self.NEWS_SUBSCRIBE).click()

    @allure.step("Agree privacy policy")
    def agree_privacy_policy(self):
        self.driver.find_element(*self.AGREE_TO_PRIVACY_POLICE).click()
        time.sleep(4)

    @allure.step("Clicked to continue")
    def click_to_continue(self):
        try:
            self.driver.find_element(*self.BUTTON_CONTINUE).click()
        except NoSuchElementException as e:
            allure.attach(body=self.driver.get_screenshot_as_png(),
                          name="screenshot_image",
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(e.msg)
