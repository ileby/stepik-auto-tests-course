from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import  math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button1 = browser.find_element_by_id("book").click()
x = int(browser.find_element_by_id('input_value').text)
x = calc(x)
input1 = browser.find_element_by_id('answer')
input1.send_keys(x)
button2 = browser.find_element_by_id('solve')
button2.click()
