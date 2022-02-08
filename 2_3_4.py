from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

driver = webdriver.Chrome()
driver.get(link)

# Нажимаем кнопку "Хочу отправиться в волшебное путешествие"
driver.find_element_by_css_selector('button.btn').click()

# Переключаемся на модальное окно
confirm = driver.switch_to.alert

# Принимаем confirm
confirm.accept()

# Получаем строковое значение x
x = driver.find_element_by_css_selector('#input_value').text

# Получаем результат формулы
calculation_result = calc(x)

# Передаем результат в поле ввода
driver.find_element_by_css_selector('#answer').send_keys(calculation_result)

# Нажимаем кнопку "Отправить"
driver.find_element_by_css_selector('button.btn').click()

time.sleep(15)