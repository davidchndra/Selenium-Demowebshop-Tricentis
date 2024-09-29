from selenium.webdriver.common.by import By

class registerPage():

    selector_gender = (By.ID, 'gender-male')
    selector_firstname = (By.ID, 'FirstName')
    selector_lastname = (By.ID, 'LastName')
    selector_email = (By.ID, 'Email')
    selector_password = (By.ID, 'Password')
    selector_repeat_password = (By.ID, 'ConfirmPassword')
    selector_button = (By.ID, 'register-button')

    selector_success_register = (By.CSS_SELECTOR, '.page-title h1')
    selector_error_register = (By.CSS_SELECTOR, '[field-validation-error]')

    selector_error_first = (By.CSS_SELECTOR, '[data-valmsg-for="FirstName"]')
    selector_error_last = (By.CSS_SELECTOR, '[data-valmsg-for="LastName"]')
    selector_error_email = (By.CSS_SELECTOR, '[data-valmsg-for="Email"]')
    selector_short_password = (By.CSS_SELECTOR, '[data-valmsg-for="Password"]')
    selector_mismatch_password = (By.CSS_SELECTOR, '[data-valmsg-for="ConfirmPassword"]')


class registerData():
    first_name              = "David"
    last_name               = "TAK Batch 7"
    empty_name              = ""

    valid_email             = "davidtak_register6@gmail.com"
    invalid_email           = "david_testgmail.com"
    empty_email             = ""

    valid_password          = "password123"
    short_password          = "short"
    empty_password          = ""

    success_register        = "Register"

    error_first_name        = "First name is required."
    error_last_name         = "Last name is required."
    error_email             = "Wrong email"
    error_short_password    = "The password should have at least 6 characters."
    error_mismatch_password = "The password and confirmation password do not match."

    success_message         = "Welcome to our store"
    unsuccessful_message    = "Login was unsuccessful."