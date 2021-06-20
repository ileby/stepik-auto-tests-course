import os
import time

from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('1')
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys('2')
    input3 = browser.find_element_by_name('email')
    input3.send_keys('3')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'yes.txt')
    input4 = browser.find_element_by_name('file')
    input4.send_keys(file_path)
    button = browser.find_element_by_css_selector('.btn')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
