from selenium.webdriver.common.by import By


class Delay_Field:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    def test_calc(self, time):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(time)
