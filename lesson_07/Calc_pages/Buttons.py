from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.remote.webdriver import WebDriver

class Buttons:

    def __init__(self, browser:WebDriver) -> None:
        """Заходит на сайт"""
        self._driver = browser

    @allure.step("Ввести в калькулятор выражение: 7+8=")
    def click_buttons(self) -> None:
        """Вводит значения в калькулятор"""
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()
