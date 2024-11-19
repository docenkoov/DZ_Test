import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.data_types_page import DataTypesPage


@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_fill_and_submit_form(browser):
    page = DataTypesPage(browser)
    page.load()

    page.fill_first_name('Иван')
    page.fill_last_name('Петров')
    page.fill_address('Ленина, 55-3')
    page.fill_email('test@skypro.com')
    page.fill_phone_number('+7985899998787')
    # Оставляем поле zip_code пустым
    page.fill_city('Москва')
    page.fill_country('Россия')
    page.fill_job_position('QA')
    page.fill_company('SkyPro')

    # Прокручиваем до кнопки Submit перед кликом
    submit_button = browser.find_element(*page.SUBMIT_BUTTON)
    browser.execute_script("arguments[0].scrollIntoView();", submit_button)

    page.click_submit_button()

    # Проверяем, что поле Zip Code подсвечено красным
    zip_code_input = browser.find_element(
        By.CSS_SELECTOR, '.form-control[name="zip-code"]')
    assert 'is-invalid' in zip_code_input.get_attribute(
        'class'), "Поле Zip Code не подсвечено красным."

    # Проверяем, что остальные поля подсвечены зеленым
    fields_to_check = [
        page.FIRST_NAME_INPUT,
        page.LAST_NAME_INPUT,
        page.ADDRESS_INPUT,
        page.EMAIL_INPUT,
        page.PHONE_NUMBER_INPUT,
        page.CITY_INPUT,
        page.COUNTRY_INPUT,
        page.JOB_POSITION_INPUT,
        page.COMPANY_INPUT
    ]

    for field_locator in fields_to_check:
        element = browser.find_element(*field_locator)
        assert 'is-valid' in element.get_attribute('class'), f"Поле {
            element.get_attribute('name')} не подсвечено зеленым."
