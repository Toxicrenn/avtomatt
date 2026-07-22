from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.remote.webdriver import WebDriver

class Delay_Field:
    def __init__(self, browser:WebDriver) -> None:
        """Заходит на сайт"""
        self._driver = browser
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    @allure.step("Ввести время {time} в секундомер")
    def test_calc(self, time: int) -> None:
        """Очищает поле и вводит время"""
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(time)
