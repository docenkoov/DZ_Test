from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")

# Укажите путь к вашему chromedriver
chrome_driver_path = r"D:\SKYPRO\
    TEST\Cours_4\chromedriver-win64\chromedriver.exe"

# Инициализация веб-драйвера
driver = webdriver.Chrome()

try:
    # Открываем страницу
    driver.get("http://uitestingplayground.com/dynamicid")

    # Небольшая задержка для завершения загрузки страницы
    time.sleep(5)

    # Находим синюю кнопку и кликаем на нее
    blue_button = driver.find_element(
        By.XPATH, "//button[contains(@class, 'btn btn-primary')]")
    blue_button.click()

    # Небольшая задержка для визуального наблюдения
    time.sleep(5)

finally:
    # Закрываем драйвер
    driver.quit()
