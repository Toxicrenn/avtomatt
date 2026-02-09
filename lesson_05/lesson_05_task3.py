from time import sleep

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# зайти на сайт
driver.get("http://the-internet.herokuapp.com/inputs")

# ввести в поле текст sky
input_selector = 'input[type="number"]'

input_field = driver.find_element(By.CSS_SELECTOR, input_selector)

text = "Sky"

input_field.send_keys(text)

sleep(5)
# ввести в поле текст pro
input_field.clear()

text = "Pro"

input_field.send_keys(text)

sleep(5)
driver.quit()
