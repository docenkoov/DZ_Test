from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")

    blue_button = driver.find_element(By.ID, "ajaxButton")
    blue_button.click()

    # Увеличиваем время ожидания до 60 секунд
    green_box_text = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.ID, "p.bg-success"))
    ).text

    print(green_box_text)

finally:
    driver.quit()
