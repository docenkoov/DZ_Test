from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element((
            By.ID, "text"), "Please wait until the images are loaded...")
    )
    print("Текст 'Please wait until the images are loaded...' обнаружен.")

    WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
    )
    print("Текст изменился на 'Done!'")
    images = driver.find_elements(By.CSS_SELECTOR, '#image-container img')

    if len(images) == 4:
        for image in images:
            if image.get_attribute("id") == "award":
                print("Изображение найдено:", image.get_attribute("src"))
                break
    else:
        print(
            "Недостаточно изображений. Ожидалось 4, но найдено:", len(images))

finally:
    driver.quit()
