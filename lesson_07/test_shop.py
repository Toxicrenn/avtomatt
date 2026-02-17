from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from Shop_pages.Authorization import OpenWebsite
from Shop_pages.Shopping import Shopping
from Shop_pages.Checkout import Checkout
from Shop_pages.Form import Form
import allure

@allure.title("Тестирование магазина")
@allure.description("Проверка корректности суммы заказа")
@allure.feature("Shopping")
@allure.severity("Blocker")
def test_shop():
    service = Service(executable_path=r"C:\Users\ari\Desktop\тест\geko\geckodriver.exe")
    firefox_options = Options()
    firefox_options.add_argument("--private")
    browser = webdriver.Firefox(service=service, options=firefox_options)

    open_website = OpenWebsite(browser)
    with allure.step("Авторизация на сайте"):
        open_website.authorization()

    with allure.step("Пополнение корзины"):
        shopping = Shopping(browser)
        shopping.shopping()

    with allure.step("Переход в корзину"):
        checkout = Checkout(browser)
        checkout.checkout()

    with allure.step("Оформление доставки"):
        result = Form(browser)
        shopping_result = result.form()
    
    with allure.step("Проверка суммы заказа"):
        assert "$58.29" in shopping_result


# pytest lesson_07/test_shop.py
