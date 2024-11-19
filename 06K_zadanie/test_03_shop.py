import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def setup():
    # Инициализация драйвера
    print("Настройка драйвера...")
    driver = webdriver.Chrome()
    # Убедитесь, что у вас установлен Chrome WebDriver
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()  # Закрытие браузера после завершения теста
    print("Драйвер завершил свою работу.")


def test_purchase(setup):
    driver = setup

    # Авторизация
    print("Авторизация на сайте...")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    print("Авторизация завершена.")

    # Добавление товаров в корзину
    print("Добавление товаров в корзину...")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    print("Товары добавлены в корзину.")

    # Переход в корзину
    print("Переход в корзину...")
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Переход к checkout
    print("Переход к оформлению заказа...")
    driver.find_element(By.ID, "checkout").click()

    # Заполнение формы
    print("Заполнение формы для оформления заказа...")
    driver.find_element(By.ID, "first-name").send_keys("Ольга")
    driver.find_element(By.ID, "last-name").send_keys("Доценко")
    driver.find_element(By.ID, "postal-code").send_keys("172400")
    driver.find_element(By.ID, "continue").click()
    print("Форма успешно заполнена.")

    # Чтение итоговой стоимости
    print("Чтение итоговой стоимости заказа...")
    total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_element.text
    total_amount = total_text.split()[-1]  # Извлекаем сумму из текста

    # Проверка итоговой суммы
    print(f"Ожидаемая сумма: $58.29, Фактическая сумма: {total_amount}")
    assert total_amount == "$58.29"


# Если файл запускается как скрипт, можно вызывать pytest
if __name__ == "__main__":
    pytest.main()
