from selenium.webdriver.common.by import By

class cartPage():

    selector_btn        = (By.CSS_SELECTOR, '.button-2 product-box-add-to-cart-button')
    selector_cart       = (By.CSS_SELECTOR, 'cart-label')
    selector_cart_qty   = (By.CSS_SELECTOR, 'cart-qty')

    selector_books      = (By.CSS_SELECTOR, "a[href='/books']")
    selector_computers  = (By.CSS_SELECTOR, "a[href='/computers']")

class cartData():
    qty                 = "(1)"
    empty_qty           = "(0)"
    city                = "Test Aplikasi Kamu"
    address             = "Jalan Test Aplikasi Kamu"
    zip                 = "12345"
    phone_number        = "081234567890"
    error_minus_qty     = "Quantity should be positive"

    checkout_success    = "Your order has been successfully processed!"