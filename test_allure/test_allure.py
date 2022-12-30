from selenium_open_cart.page_objects.AdminPage import AdminPage
from selenium_open_cart.page_objects.AdminPage import AddProduct
from selenium_open_cart.page_objects.AdminPage import DeleteProduct
from selenium_open_cart.page_objects.StartPage import StartPage
from selenium_open_cart.page_objects.RegisterPage import PersonalDetails
from selenium_open_cart.page_objects.CompareList import CompareListPages
from selenium_open_cart.page_objects.SearchPages import SearchPages
import allure
from allure_commons.types import Severity


@allure.story('Check search field')
def test_check_search_fild(browser):
    browser.get(browser.url)
    SearchPages(browser).write_apple_and_search()
    SearchPages(browser).search_in_description()
    SearchPages(browser).check_search_page()
    SearchPages(browser).add_to_compare()
    SearchPages(browser).remove_first_product()
    SearchPages(browser).add_to_cart_second_product()


@allure.story('Check products in Wish List')
def test_check_products_in_wish_list(browser):
    browser.get(browser.url)
    CompareListPages(browser).go_to_catalog_page()
    CompareListPages(browser).choose_two_products()
    CompareListPages(browser).click_to_wish_list()
    CompareListPages(browser).login_in_user_panel()
    CompareListPages(browser).delete_first_product()
    CompareListPages(browser).delete_second_product()


@allure.feature('Authorization and add product')
def test_login_page_check_elements(browser):
    browser.get(browser.url + "admin")
    AdminPage(browser).insert_login()
    AdminPage(browser).insert_password()
    AdminPage(browser).click_to_button_login()
    AdminPage(browser).go_to_category()
    AddProduct(browser).go_to_create_product()
    AddProduct(browser).add_title_product()
    AddProduct(browser).add_description_product()
    AddProduct(browser).add_tag_title()
    AddProduct(browser).add_tag_description()
    AddProduct(browser).go_to_tab_data()
    AddProduct(browser).add_model_product()
    AddProduct(browser).click_to_safe_product()


@allure.story('Delete product')
def test_delete_product(browser):
    browser.get(browser.url + "admin")
    AdminPage(browser).insert_login()
    AdminPage(browser).insert_password()
    AdminPage(browser).click_to_button_login()
    AdminPage(browser).go_to_category()
    DeleteProduct(browser).select_product()
    DeleteProduct(browser).click_on_button_delete()
    DeleteProduct(browser).alert_accept()


@allure.severity(severity_level=Severity.BLOCKER)
@allure.story('Add new user')
def test_registration_user(browser):
    browser.get(browser.url)
    StartPage(browser).go_to_register_page()
    PersonalDetails(browser).write_first_name()
    PersonalDetails(browser).write_last_name()
    PersonalDetails(browser).write_email()
    PersonalDetails(browser).write_telephone()
    PersonalDetails(browser).write_password()
    PersonalDetails(browser).write_confirm_password()
    PersonalDetails(browser).news_subscribe_add()
    PersonalDetails(browser).agree_privacy_policy()
    PersonalDetails(browser).click_to_continue()


@allure.story('Switching currencies')
def test_switching_currencies(browser):
    browser.get(browser.url)
    StartPage(browser).choose_currency_euro()
    StartPage(browser).choose_currency_pound()
    StartPage(browser).choose_currency_dollar()
