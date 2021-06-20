import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_tag_name('span[id="input_value"]')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    checkbox1 = browser.find_element_by_id('robotCheckbox')
    checkbox1.click()
    radiobutton1 = browser.find_element_by_id('robotsRule')
    radiobutton1.click()
    button = browser.find_element_by_css_selector('.btn')
    button.click()
finally:
    time.sleep(10)
    browser.quit()