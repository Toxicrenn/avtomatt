from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OpenWebsite:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/")

    def authorization(self):
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()

        WebDriverWait(self._driver, 4).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack'))
    )

    