from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    try:
        delay_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        delay_input.send_keys("45")

        button_7 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#c0"))
        )
        button_7.click()

        button_plus = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#add"))
        )
        button_plus.click()

        button_8 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#c1"))
        )
        button_8.click()

        button_equals = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#equals"))
        )
        button_equals.click()

        result = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#result"))
        )

        assert result.text == "15", f"Ожидалось 15, но получено {result.text}"

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_calculator()
