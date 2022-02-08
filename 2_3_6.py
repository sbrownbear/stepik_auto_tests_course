from selenium import webdriver
from math import log, sin
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

browser.find_element_by_css_selector('button.trollface').click()
time.sleep(1)

# Переключиться на новую вкладку
browser.switch_to.window(browser.window_handles[1])

# решить капчу для роботов
browser.find_element_by_css_selector('input#answer').send_keys(
  str(log(abs(12*sin(int(browser.find_element_by_id('input_value').text))))))
browser.find_element_by_css_selector('button.btn.btn-primary').click()