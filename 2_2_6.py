from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

#Открыть страницу http://SunInJuly.github.io/execute_script.html.
link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

#Посчитать математическую функцию от x
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#Считать значение для переменной x
unknown = browser.find_element_by_id("input_value")
x = unknown.text
y = calc(x)
  
#Проскроллить станицу вниз
browser.execute_script("window.scrollBy(0, 100);")

#Ввести ответ в текстовое поле
field = browser.find_element_by_css_selector("input.form-control")
input = field.send_keys(y)

#Выбрать checkbox "Подтверждаю, что являюсь роботом"
option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
option1.click()

option1 = browser.find_element_by_css_selector("[for='robotsRule']").click() 
button = browser.find_element_by_css_selector("button.btn").click() 
time.sleep(1)