from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Путь к chromedriver
service = Service(
    executable_path=r"D:\SKYPRO\TEST\Cours_4\chromedriver-win64\
        chromedriver-win64\chromedriver.exe")

# Запуск веб-драйвера
driver = webdriver.Chrome()

try:
    # Открыть сайт
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ожидание, пока появится текст
    # "Please wait until the images are loaded..."
    WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element((
            By.ID, "text"), "Please wait until the images are loaded...")
    )
    print("Текст 'Please wait until the images are loaded...' обнаружен.")

    # Ожидание, пока текст изменится на "Done!"
    WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
    )
    print("Текст изменился на 'Done!'")

    # Поиск изображений
    images = driver.find_elements(By.CSS_SELECTOR, '#image-container img')

    # Проверяем, что загружены все 4 изображения
    if len(images) == 4:
        # Ищем изображение с id "award"
        for image in images:
            if image.get_attribute("id") == "award":
                print("Изображение найдено:", image.get_attribute("src"))
                break
            # Выход из цикла после нахождения изображения с id "award"
    else:
        print(
            "Недостаточно изображений. Ожидалось 4, но найдено:", len(images))

finally:
    # Закрыть драйвер
    driver.quit()
