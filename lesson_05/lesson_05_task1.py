from time import sleep

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#зайти на сайт
driver.get('http://uitestingplayground.com/classattr')

#кликнуть на синюю кнопку
blue_button = 'button.btn-primary'

button = driver.find_element(By.CSS_SELECTOR, blue_button)

button.click()

sleep(5)
