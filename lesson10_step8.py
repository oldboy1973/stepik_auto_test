from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Говорим браузеру ожидать до 20 секунд
    # пока в элементе с id="price" текст
    # станет равным "$100"
    WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    # кликаем по этому элементу - кнопке
    # это вызывает редирект
    button = browser.find_element_by_id('book')
    button.click()
    # Определяем x
    span = browser.find_element_by_id('input_value')
    x = int(span.text)
    value = calc(x)
    # Заполняем поле вычисленным значением
    input = browser.find_element_by_id('answer')
    input.send_keys(value)
    # Подтверждаем
    submit = browser.find_element_by_css_selector('button[type="submit"]')
    submit.click()
finally:
    time.sleep(10)
    browser.quit()