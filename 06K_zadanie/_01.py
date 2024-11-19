from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def test_1():
    # Инициализация драйвера Chrome
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    try:
        # Открытие веб-страницы
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Заполнение полей формы
        driver.find_element(
            By.CSS_SELECTOR, '.form-control[name="first-name"]').send_keys(
                'Иван')
        driver.find_element(
            By.CSS_SELECTOR, '[name="last-name"]').send_keys('Петров')
        driver.find_element(
            By.CSS_SELECTOR, '.form-control[name="address"]').send_keys(
                'Ленина, 55-3')
        driver.find_element(
            By.CSS_SELECTOR, '.form-control[name="e-mail"]').send_keys(
                'test@skypro.com')
        driver.find_element(
            By.CSS_SELECTOR, '.form-control[name="phone"]').send_keys(
                '+7985899998787')
        driver.find_element(
            By.CSS_SELECTOR, '.form-control[name="zip-code"]').send_keys('')
        # Оставляем пустым
        driver.find_element(
            By.CSS_SELECTOR, '.form-control[name="city"]').send_keys('Москва')
        driver.find_element(
            By.CSS_SELECTOR, '.form-control[name="country"]').send_keys(
                'Россия')
        driver.find_element(
            By.CSS_SELECTOR, '.form-control[name="job-position"]').send_keys(
                'QA')
        driver.find_element(
            By.CSS_SELECTOR, '.form-control[name="company"]').send_keys(
                'SkyPro')

        # Ожидание, пока кнопка станет кликабельной
        button = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '.btn.btn-outline-primary.mt-3'))
        )

        # Прокрутка к кнопке
        driver.execute_script("arguments[0].scrollIntoView(true);", button)

        # Использование ActionChains для клика
        actions = ActionChains(driver)
        actions.move_to_element(button).click().perform()

        # Ожидание появления результатов
        WebDriverWait(driver, 40).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#zip-code')))

        # Проверка результатов
        assert 'alert-danger' in driver.find_element(
            By.CSS_SELECTOR, '#zip-code').get_attribute("class")
        assert 'success' in driver.find_element(
            By.CSS_SELECTOR, '#first-name').get_attribute("class")
        assert 'success' in driver.find_element(
            By.CSS_SELECTOR, '#last-name').get_attribute("class")
        assert 'success' in driver.find_element(
            By.CSS_SELECTOR, '#address').get_attribute("class")
        assert 'success' in driver.find_element(
            By.CSS_SELECTOR, '#e-mail').get_attribute("class")
        assert 'success' in driver.find_element(
            By.CSS_SELECTOR, '#phone').get_attribute("class")
        assert 'success' in driver.find_element(
            By.CSS_SELECTOR, '#city').get_attribute("class")

    finally:
        # Обеспечение корректного закрытия драйвера
        driver.quit()
