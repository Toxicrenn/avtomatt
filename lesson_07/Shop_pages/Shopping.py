from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.remote.webdriver import WebDriver

class Shopping:
    def __init__(self, browser:WebDriver) -> None:
        self._driver = browser

    @allure.step("Добавление товаров в корзину")
    def shopping(self) -> None:
        self._driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"
        ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"
        ).click()
        self._driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()
