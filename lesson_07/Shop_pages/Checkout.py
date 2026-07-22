from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.remote.webdriver import WebDriver

class Checkout:
    def __init__(self, browser:WebDriver) -> None:
        self._driver = browser

    @allure.step("Нажать кнопку checkout")
    def checkout(self) -> None:
        WebDriverWait(self._driver, 4).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout"))
        )
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()

        WebDriverWait(self._driver, 4).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#first-name"))
        )
