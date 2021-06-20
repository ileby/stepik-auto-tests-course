import time
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element_by_css_selector('.trollface')
    button1.click()
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
    x = int(browser.find_element_by_id('input_value').text)
    x = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(x)
    button2 = browser.find_element_by_css_selector('.btn')
    button2.click()
finally:
    time.sleep(10)
    browser.quit()