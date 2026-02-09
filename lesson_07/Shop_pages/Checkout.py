from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Checkout:
    def __init__(self, browser):
        self._driver = browser

    def checkout(self):
        WebDriverWait(self._driver, 4).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout"))
        )
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()

        WebDriverWait(self._driver, 4).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#first-name"))
        )
