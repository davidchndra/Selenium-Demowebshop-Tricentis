import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObject.register import registerPage, registerData

class registerCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://demowebshop.tricentis.com/"

    def test_001_register_with_valid_data(self):
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-register').click()
        get_url1 = driver.current_url
        self.assertIn("/register", get_url1)

        driver.find_element(*registerPage.selector_gender).click()
        driver.find_element(*registerPage.selector_firstname).send_keys(registerData.first_name)
        driver.find_element(*registerPage.selector_lastname).send_keys(registerData.last_name)
        driver.find_element(*registerPage.selector_email).send_keys(registerData.valid_email)
        driver.find_element(*registerPage.selector_password).send_keys(registerData.valid_password)
        driver.find_element(*registerPage.selector_repeat_password).send_keys(registerData.valid_password)
        driver.find_element(*registerPage.selector_button).click()

        success_message = driver.find_element(*registerPage.selector_success_register).text
        self.assertIn(registerData.success_register, success_message)

    def test_002_register_with_registered_email(self): #negative case
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-register').click()
        get_url1 = driver.current_url
        self.assertIn("/register", get_url1)
        
        driver.find_element(*registerPage.selector_gender).click()
        driver.find_element(*registerPage.selector_firstname).send_keys(registerData.first_name)
        driver.find_element(*registerPage.selector_lastname).send_keys(registerData.last_name)
        driver.find_element(*registerPage.selector_email).send_keys(registerData.valid_email)
        driver.find_element(*registerPage.selector_password).send_keys(registerData.valid_password)
        driver.find_element(*registerPage.selector_repeat_password).send_keys(registerData.valid_password)
        driver.find_element(*registerPage.selector_button).click()

        self.assertIn("/register", get_url1)

    def test_003_register_with_empty_gender(self): #positive case
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-register').click()
        get_url1 = driver.current_url
        self.assertIn("/register", get_url1)
        
        driver.find_element(*registerPage.selector_firstname).send_keys(registerData.first_name)
        driver.find_element(*registerPage.selector_lastname).send_keys(registerData.last_name)
        driver.find_element(*registerPage.selector_email).send_keys(registerData.valid_email)
        driver.find_element(*registerPage.selector_password).send_keys(registerData.valid_password)
        driver.find_element(*registerPage.selector_repeat_password).send_keys(registerData.valid_password)
        driver.find_element(*registerPage.selector_button).click()

        success_message = driver.find_element(*registerPage.selector_success_register).text
        self.assertIn(registerData.success_register, success_message)

    def test_004_register_with_empty_last_name(self): #negative case
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-register').click()
        get_url1 = driver.current_url
        self.assertIn("/register", get_url1)

        driver.find_element(*registerPage.selector_gender).click()
        driver.find_element(*registerPage.selector_firstname).send_keys(registerData.first_name)
        # driver.find_element(*registerPage.selector_lastname).send_keys(registerData.last_name)
        driver.find_element(*registerPage.selector_email).send_keys(registerData.valid_email)
        driver.find_element(*registerPage.selector_password).send_keys(registerData.valid_password)
        driver.find_element(*registerPage.selector_repeat_password).send_keys(registerData.valid_password)
        driver.find_element(*registerPage.selector_button).click()


        error_message = driver.find_element(*registerPage.selector_error_last).text
        self.assertIn(registerData.error_last_name, error_message)

    def test_005_register_with_invalid_email_format(self): #negative case
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-register').click()
        get_url1 = driver.current_url
        self.assertIn("/register", get_url1)

        driver.find_element(*registerPage.selector_gender).click()
        driver.find_element(*registerPage.selector_firstname).send_keys(registerData.first_name)
        driver.find_element(*registerPage.selector_lastname).send_keys(registerData.last_name)
        driver.find_element(*registerPage.selector_email).send_keys(registerData.invalid_email)
        driver.find_element(*registerPage.selector_password).send_keys(registerData.valid_password)
        driver.find_element(*registerPage.selector_repeat_password).send_keys(registerData.valid_password)
        driver.find_element(*registerPage.selector_button).click()

        error_message = driver.find_element(*registerPage.selector_error_email).text
        self.assertIn(registerData.error_email, error_message)

    def test_006_register_with_short_password(self): #negative case
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-register').click()
        get_url1 = driver.current_url
        self.assertIn("/register", get_url1)

        driver.find_element(*registerPage.selector_gender).click()
        driver.find_element(*registerPage.selector_firstname).send_keys(registerData.first_name)
        driver.find_element(*registerPage.selector_lastname).send_keys(registerData.last_name)
        driver.find_element(*registerPage.selector_email).send_keys(registerData.invalid_email)
        driver.find_element(*registerPage.selector_password).send_keys(registerData.short_password)
        driver.find_element(*registerPage.selector_repeat_password).send_keys(registerData.short_password)
        driver.find_element(*registerPage.selector_button).click()

        error_message = driver.find_element(*registerPage.selector_short_password).text
        self.assertIn(registerData.error_short_password, error_message)

    def test_007_register_with_mismatch_password(self): #negative case
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-register').click()
        get_url1 = driver.current_url
        self.assertIn("/register", get_url1)

        driver.find_element(*registerPage.selector_gender).click()
        driver.find_element(*registerPage.selector_firstname).send_keys(registerData.first_name)
        driver.find_element(*registerPage.selector_lastname).send_keys(registerData.last_name)
        driver.find_element(*registerPage.selector_email).send_keys(registerData.invalid_email)
        driver.find_element(*registerPage.selector_password).send_keys(registerData.short_password)
        driver.find_element(*registerPage.selector_repeat_password).send_keys("mismatchpassword")
        driver.find_element(*registerPage.selector_button).click()

        error_message = driver.find_element(*registerPage.selector_mismatch_password).text
        self.assertIn(registerData.error_mismatch_password, error_message)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()