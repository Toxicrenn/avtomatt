from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.remote.webdriver import WebDriver

class Result:
    def __init__(self, browser:WebDriver, delay_time:int) -> None:
        """Заходит на сайт"""
        self._driver = browser
        self._time = delay_time

    @allure.step("Ожидание результата расчета")
    def waitng_results(self) -> str:
        """Ожидает завершения расчета и возвращает результат"""
        WebDriverWait(self._driver, self._time).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
        )
        result = self._driver.find_element(By.CSS_SELECTOR, "div.screen").text
        return result
