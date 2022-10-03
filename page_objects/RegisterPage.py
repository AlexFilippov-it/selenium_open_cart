import time

from selenium.webdriver.common.by import By
from selenium_open_cart.page_objects.BasePage import BasePage


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

    def write_first_name(self):
        self.driver.find_element(*self.FILD_FIRST_NAME).clear()
        self.driver.find_element(*self.FILD_FIRST_NAME).send_keys("Test user")

    def write_last_name(self):
        self.driver.find_element(*self.FILD_LAST_NAME).clear()
        self.driver.find_element(*self.FILD_LAST_NAME).send_keys("Test Last Name")

    def write_email(self):
        self.driver.find_element(*self.EMAIL).clear()
        self.driver.find_element(*self.EMAIL).send_keys("test_user@gmail.com")

    def write_telephone(self):
        self.driver.find_element(*self.TEL).clear()
        self.driver.find_element(*self.TEL).send_keys("+79259999999")

    def write_password(self):
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys("14253647")

    def write_confirm_password(self):
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys("14253647")

    def news_subscribe_add(self):
        self.driver.find_element(*self.NEWS_SUBSCRIBE).click()

    def agree_privacy_policy(self):
        self.driver.find_element(*self.AGREE_TO_PRIVACY_POLICE).click()
        time.sleep(4)

    def click_to_continue(self):
        self.driver.find_element(*self.BUTTON_CONTINUE).click()
