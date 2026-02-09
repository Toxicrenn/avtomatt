from time import sleep

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# зайти на сайт
driver.get("http://the-internet.herokuapp.com/login")

# ввести имя пользователя
input_username = driver.find_element(By.CSS_SELECTOR, 'input[id="username"]')

username = "tomsmith"

input_username.send_keys(username)

sleep(1.5)

# ввести пароль
input_password = driver.find_element(By.CSS_SELECTOR, 'input[id="password"]')

password = "SuperSecretPassword!"

input_password.send_keys(password)

sleep(1.5)

# нажать на кнопку login
button = driver.find_element(By.CSS_SELECTOR, "button.radius")

button.click()

# вывести текст
text = driver.find_element(By.CSS_SELECTOR, 'div[id="flash"]').text

print(text)

driver.quit()
