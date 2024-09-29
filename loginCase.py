import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObject.login import loginPage, loginData

class registerCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://demowebshop.tricentis.com/"

    def test_001_login_with_valid_data(self):
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-login').click()
        get_url1 = driver.current_url
        self.assertIn("/login", get_url1)

        driver.find_element(*loginPage.selector_email).send_keys(loginData.valid_email)
        driver.find_element(*loginPage.selector_password).send_keys(loginData.valid_password)
        driver.find_element(*loginPage.selector_button).click()

        indicator = driver.find_element(*loginPage.selector_logout).text
        self.assertIn(loginData.logout_message, indicator)

    def test_002_login_with_wrong_password(self):
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-login').click()
        get_url1 = driver.current_url
        self.assertIn("/login", get_url1)

        driver.find_element(*loginPage.selector_email).send_keys(loginData.valid_email)
        driver.find_element(*loginPage.selector_password).send_keys(loginData.invalid_password)
        driver.find_element(*loginPage.selector_button).click()

        indicator = driver.find_element(*loginPage.selector_error_msg).text
        self.assertIn(loginData.error_message, indicator)

    def test_003_login_with_invalid_email_format(self):
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-login').click()
        get_url1 = driver.current_url
        self.assertIn("/login", get_url1)

        driver.find_element(*loginPage.selector_email).send_keys(loginData.invalid_email)
        driver.find_element(*loginPage.selector_password).send_keys(loginData.valid_password)
        driver.find_element(*loginPage.selector_button).click()

        indicator = driver.find_element(*loginPage.selector_error_email).text
        self.assertIn(loginData.error_email_format, indicator)
        
    def test_004_login_with_empty_password(self):
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-login').click()
        get_url1 = driver.current_url
        self.assertIn("/login", get_url1)

        driver.find_element(*loginPage.selector_email).send_keys(loginData.invalid_email)
        driver.find_element(*loginPage.selector_button).click()
    
    def test_005_login_with_empty_email(self):
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-login').click()
        get_url1 = driver.current_url
        self.assertIn("/login", get_url1)

        driver.find_element(*loginPage.selector_password).send_keys(loginData.valid_password)
        driver.find_element(*loginPage.selector_button).click()

        indicator = driver.find_element(*loginPage.selector_error_msg).text
        self.assertIn(loginData.error_message, indicator)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()