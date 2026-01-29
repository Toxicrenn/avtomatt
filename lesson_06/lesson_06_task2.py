from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://uitestingplayground.com/textinput')

text_field = driver.find_element(By.CSS_SELECTOR, '#newButtonName')

text = 'SkyPro'

text_field.send_keys(text)

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(button)

driver.quit()