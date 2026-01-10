from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_shop(driver):
    driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack'))
    )

    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
    driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container').click()

    WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkout'))
    )
    driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#first-name'))
    )
    driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Renata')
    driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Asadova')
    driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('140141')

    driver.find_element(By.CSS_SELECTOR, '#continue').click()

    summary_total = WebDriverWait(driver, 4).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.summary_total_label'))
    )
    result = summary_total.text

    assert '$58.29' in result













