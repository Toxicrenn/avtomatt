from selenium import webdriver
from Shop_pages.Authorization import OpenWebsite
from Shop_pages.Shopping import Shopping
from Shop_pages.Checkout import Checkout
from Shop_pages.Form import Form

def test_shop():
    browser = webdriver.Chrome()

    open_website = OpenWebsite(browser)
    open_website.authorization()

    shopping = Shopping(browser)
    shopping.shopping()

    checkout = Checkout(browser)
    checkout.checkout()

    result = Form(browser)
    shopping_result = result.form()

    assert '$58.29' in shopping_result

#pytest lesson_07/shop.py 



    