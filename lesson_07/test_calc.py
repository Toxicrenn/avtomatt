from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Calc_pages.DelayField import Delay_Field
from Calc_pages.Buttons import Buttons
from Calc_pages.Result import Result
import allure

@allure.title("Тестирование калькулятора")
@allure.description("Проверка калькулятора на корректность расчета и ожидание указанного времени в таймере")
@allure.feature("Сalculation")
@allure.severity("Blocker")
def test_calc():
    chrome_options = Options()
    chrome_options.add_argument("--private")
    browser = webdriver.Chrome(options=chrome_options)
    delay_time = "45"

    with allure.step(f"Ввод времени {delay_time} в секундомер"):
        delay_field = Delay_Field(browser)
        delay_field.test_calc(delay_time)

    with allure.step("Ввод выражения в калькулятор"):
        buttons = Buttons(browser)
        buttons.click_buttons()

    with allure.step("Ожидание результата"):
        calc_result = Result(browser, delay_time)
        result = calc_result.waitng_results()
        
    with allure.step("Проверка корректности вычислений"):    
        assert result == "15"


# pytest lesson_07/test_calc.py
