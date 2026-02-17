from selenium.webdriver.common.by import By
import allure

class Buttons:

    def __init__(self, browser):
        self._driver = browser
        
    @allure.step("ВВести в калькулятор выражение: 7+8=")
    def click_buttons(self):
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()
