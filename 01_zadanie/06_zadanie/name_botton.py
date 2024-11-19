from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка драйвера (убедитесь,
# что у вас установлен соответствующий драйвер, например, chromedriver)
driver = webdriver.Chrome()

try:
    # Переход на страницу
    driver.get("http://uitestingplayground.com/textinput")

    # Находим поле ввода по его имени и вводим текст "SkyPro"
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")

    # Нажимаем на синюю кнопку
    blue_button = driver.find_element(By.ID, "updatingButton")
    blue_button.click()

    # Ожидаем, пока текст кнопки обновится, и получаем его
    button_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "updatingButton"))
    ).text

    # Выводим текст кнопки в консоль
    print(button_text)

finally:
    # Закрываем драйвер
    driver.quit()
