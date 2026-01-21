from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Calc_pages.DelayField import Delay_Field
from Calc_pages.Buttons import Buttons
from Calc_pages.Result import Result

def test_calc():
    chrome_options = Options()
    chrome_options.add_argument('--private')
    browser = webdriver.Chrome(
        options=chrome_options
    )
    delay_time = '45'

    delay_field = Delay_Field(browser)
    delay_field.test_calc(delay_time)

    buttons = Buttons(browser)
    buttons.click_buttons()

    calc_result = Result(browser, delay_time)
    result = calc_result.waitng_results()
    assert result == '15'





#pytest lesson_07/test_calc.py