from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from Shop_pages.Authorization import OpenWebsite
from Shop_pages.Shopping import Shopping
from Shop_pages.Checkout import Checkout
from Shop_pages.Form import Form

def test_shop():
    service = Service(executable_path=r"C:\Users\ari\Desktop\тест\geko\geckodriver.exe")
    firefox_options = Options()
    firefox_options.add_argument('--private')
    browser = webdriver.Firefox(
        service=service,
        options=firefox_options
    )

    open_website = OpenWebsite(browser)
    open_website.authorization()

    shopping = Shopping(browser)
    shopping.shopping()

    checkout = Checkout(browser)
    checkout.checkout()

    result = Form(browser)
    shopping_result = result.form()

    assert '$58.29' in shopping_result

#pytest lesson_07/test_shop.py 



    