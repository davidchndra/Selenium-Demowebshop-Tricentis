from selenium.webdriver.common.by import By

class loginPage():
    
    selector_email = (By.ID, 'Email')
    selector_password = (By.ID, 'Password')
    selector_button = (By.CSS_SELECTOR, '.login-button')

    selector_error_msg = (By.CSS_SELECTOR, '.validation-summary-errors')
    selector_error_email = (By.CSS_SELECTOR, '.field-validation-error')

    selector_invalid_email = (By.CSS_SELECTOR, 'span[for="Email"]')

    selector_logout = (By.CSS_SELECTOR, '.ico-logout')

class loginData():

    valid_email             = "davidtak_register5@gmail.com"
    invalid_email           = "david_testgmail.com"
    empty_email             = ""

    valid_password          = "password123"
    invalid_password        = "invalidpassword123"
    short_password          = "short"
    empty_password          = ""

    logout_message          = "Log out"

    error_email_format      = "Please enter a valid email address."
    error_message           = "Login was unsuccessful. Please correct the errors and try again."
