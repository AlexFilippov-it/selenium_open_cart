from page_objects.AdminPage import AdminPage
from page_objects.AdminPage import AddProduct
from page_objects.AdminPage import DeleteProduct
from page_objects.StartPage import StartPage
from page_objects.RegisterPage import PersonalDetails


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


def test_delete_product(browser):
    browser.get(browser.url + "admin")
    AdminPage(browser).insert_login()
    AdminPage(browser).insert_password()
    AdminPage(browser).click_to_button_login()
    AdminPage(browser).go_to_category()
    DeleteProduct(browser).select_product()
    DeleteProduct(browser).click_on_button_delete()
    DeleteProduct(browser).alert_accept()


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


def test_switching_currencies(browser):
    browser.get(browser.url)
    StartPage(browser).choose_currency_euro()
    StartPage(browser).choose_currency_pound()
    StartPage(browser).choose_currency_dollar()
