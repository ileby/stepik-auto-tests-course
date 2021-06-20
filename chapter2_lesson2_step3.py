import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = int(browser.find_element_by_id('num1').text)
    num2 = int(browser.find_element_by_id('num2').text)
    sum1 = str(num1 + num2)
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(sum1)
    button = browser.find_element_by_css_selector('.btn').click()
finally:
    time.sleep(10)
    browser.quit()