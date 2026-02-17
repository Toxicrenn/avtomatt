from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.remote.webdriver import WebDriver

class OpenWebsite:
    def __init__(self, browser:WebDriver) -> None:
        """Заходит на сайт"""
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/")

    @allure.step("Ввод пароля и логина")
    def authorization(self) -> None:
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(
            "standard_user"
        )
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(
            "secret_sauce"
        )
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()

        WebDriverWait(self._driver, 4).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
            )
        )
