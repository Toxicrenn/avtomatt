from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class Form:
    def __init__(self, browser):
        self._driver = browser

    @allure.step("Ввод значений в поле для доставки")
    def form(self)->float:
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Renata")
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Asadova")
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("140141")

        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()

        summary_total = WebDriverWait(self._driver, 4).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.summary_total_label")
            )
        )

        result = summary_total.text
        return result
