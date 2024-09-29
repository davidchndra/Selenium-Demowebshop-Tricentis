import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObject.login import loginPage, loginData
from pageObject.cart import cartPage, cartData

class cartCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://demowebshop.tricentis.com/"

    def test_001_add_to_cart(self):
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-login').click()
        get_url0 = driver.current_url
        self.assertIn("/login", get_url0)

        driver.find_element(*loginPage.selector_email).send_keys(loginData.valid_email)
        driver.find_element(*loginPage.selector_password).send_keys(loginData.valid_password)
        driver.find_element(*loginPage.selector_button).click()

        driver.find_element(*cartPage.selector_books).click()
        get_url1 = driver.current_url
        self.assertIn("/books", get_url1)

        driver.find_element(By.XPATH, "//div[@class='product-item']//img[@title='Show details for Fiction']").click()
        get_url2 = driver.current_url
        self.assertIn("/fiction", get_url2)

        driver.find_element(By.XPATH, "//input[@id='add-to-cart-button-45']").click()
        driver.find_element(By.XPATH, "//li[@id='topcartlink']//a[@class='ico-cart']").click()

        get_url3 = driver.current_url
        self.assertIn("/cart", get_url3)

    def test_002_empty_cart(self):
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-login').click()
        get_url0 = driver.current_url
        self.assertIn("/login", get_url0)

        driver.find_element(*loginPage.selector_email).send_keys(loginData.valid_email)
        driver.find_element(*loginPage.selector_password).send_keys(loginData.valid_password)
        driver.find_element(*loginPage.selector_button).click()

        driver.find_element(By.XPATH, "//li[@id='topcartlink']//a[@class='ico-cart']").click()

        driver.find_element(By.XPATH, "//tr[@class='cart-item-row']//td[@class='remove-from-cart']//input[@name='removefromcart']").click()
        driver.find_element(By.XPATH, "//div[@class='buttons']//div[@class='common-buttons']//input[@name='updatecart']").click()

        cart_qty = driver.find_element(By.XPATH, "//li[@id='topcartlink']/a//span[@class='cart-qty']").text
        self.assertIn(cartData.empty_qty, cart_qty)

    def test_003_add_to_cart_minus_qty(self):
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-login').click()
        get_url0 = driver.current_url
        self.assertIn("/login", get_url0)

        driver.find_element(*loginPage.selector_email).send_keys(loginData.valid_email)
        driver.find_element(*loginPage.selector_password).send_keys(loginData.valid_password)
        driver.find_element(*loginPage.selector_button).click()

        self.driver.find_element(*cartPage.selector_books).click()
        self.assertIn("/books", self.driver.current_url)

        book_detail_xpath = "//div[@class='product-item']//img[@title='Show details for Fiction']"
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, book_detail_xpath))).click()
        self.assertIn("/fiction", self.driver.current_url)

        quantity_input = self.driver.find_element(By.XPATH, "//div[@class='add-to-cart']//input[@id='addtocart_45_EnteredQuantity']")
        quantity_input.clear()
        quantity_input.send_keys("-100")
        self.driver.find_element(By.ID, 'add-to-cart-button-45').click()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'bar-notification')))
        err_msg = self.driver.find_element(By.XPATH, "//div[@id='bar-notification']//p[@class='content']").text
        self.assertIn(cartData.error_minus_qty, err_msg)

    def test_004_checkout(self):
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-login').click()
        get_url0 = driver.current_url
        self.assertIn("/login", get_url0)

        driver.find_element(*loginPage.selector_email).send_keys(loginData.valid_email)
        driver.find_element(*loginPage.selector_password).send_keys(loginData.valid_password)
        driver.find_element(*loginPage.selector_button).click()

        driver.find_element(*cartPage.selector_books).click()
        get_url1 = driver.current_url
        self.assertIn("/books", get_url1)

        driver.find_element(By.XPATH, "//div[@class='product-item']//img[@title='Show details for Fiction']").click()
        get_url2 = driver.current_url
        self.assertIn("/fiction", get_url2)

        driver.find_element(By.XPATH, "//input[@id='add-to-cart-button-45']").click()
        driver.find_element(By.XPATH, "//li[@id='topcartlink']//a[@class='ico-cart']").click()

        get_url3 = driver.current_url
        self.assertIn("/cart", get_url3)
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='termsofservice']")))
        driver.find_element(By.XPATH, "//input[@id='termsofservice']").click()
        driver.find_element(By.XPATH, "//button[@id='checkout']").click()

        get_url4 = driver.current_url
        self.assertIn("/onepagecheckout", get_url4)

        driver.find_element(By.XPATH, "//select[@id='BillingNewAddress_CountryId']/option[@value='1']")
        driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_City']").click()
        driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_City']").send_keys(cartData.city)
        driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_Address1']").click()
        driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_Address1']").send_keys(cartData.address)
        driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_ZipPostalCode']").click()
        driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_ZipPostalCode']").send_keys(cartData.zip)
        driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_PhoneNumber']").click()
        driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_PhoneNumber']").send_keys(cartData.phone_number)

        driver.find_element(By.XPATH, "//input[@onclick='Billing.save()']").click()
        driver.find_element(By.XPATH, "//input[@onclick='Billing.save()']").click()

        driver.find_element(By.XPATH, "//input[@id='PickUpInStore']").click()
        driver.find_element(By.XPATH, "//input[@onclick='Shipping.save()']").click()
        driver.find_element(By.XPATH, "//input[@class='button-1 payment-method-next-step-button']").click()
        driver.find_element(By.XPATH, "//input[@class='button-1 payment-info-next-step-button']").click()
        driver.find_element(By.XPATH, "//input[@value='Confirm']").click()

        get_url5 = driver.current_url
        self.assertIn("/checkout/completed/", get_url5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()