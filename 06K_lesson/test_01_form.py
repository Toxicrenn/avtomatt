from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    yield driver
    driver.quit()


first_name = "Иван"
last_name = "Петров"
address = "Ленина, 55-3"
email = "test@skypro.com"
phone_number = "+7985899998787"
zip_code = ""
city = "Москва"
country = "Россия"
job_position = "QA"
company = "SkyPro"


def test_form(driver):
    driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys(
        first_name
    )
    driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(last_name)
    driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys(address)
    driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(email)
    driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys(phone_number)
    driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys(zip_code)
    driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys(city)
    driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys(country)
    driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys(
        job_position
    )
    driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys(company)

    driver.find_element(By.CSS_SELECTOR, "button").click()

    zip_red = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code"))
    )
    assert "alert-danger" in zip_red.get_attribute("class")

    green_fields = [
        "#first-name",
        "#last-name",
        "#address",
        "#e-mail",
        "#phone",
        "#city",
        "#country",
        "#job-position",
        "#company",
    ]

    for field in green_fields:
        element = driver.find_element(By.CSS_SELECTOR, field)
        assert "alert-success" in element.get_attribute("class")
