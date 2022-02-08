from selenium import webdriver
import math
import time 

link = "https://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    #запускаем браузер
    browser = webdriver.Chrome()
    browser.get(link)
    
    #ищем значение Х и подставляем в формулу + записываем это значение в переменную У
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    #ищем поле и вводим значение 
    input1 = browser.find_element_by_id("answer").send_keys(y)
    
    #Отмечаем checkbox "I'm the robot"
    input2 = browser.find_element_by_id("robotCheckbox").click()
    
    #Выбираем radiobutton "Robots rule!"
    input3= browser.find_element_by_id("robotsRule").click()
    
    #Нажимаем на кнопку Submit.
    button = browser.find_element_by_css_selector(".btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()