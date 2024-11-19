from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class DataTypesPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    # Локаторы элементов
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '.form-control[name="first-name"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '[name="last-name"]')
    ADDRESS_INPUT = (By.CSS_SELECTOR, '.form-control[name="address"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, '.form-control[name="e-mail"]')
    PHONE_NUMBER_INPUT = (By.CSS_SELECTOR, '.form-control[name="phone"]')
    ZIP_CODE_INPUT = (By.CSS_SELECTOR, '.form-control[name="zip-code"]')
    CITY_INPUT = (By.CSS_SELECTOR, '.form-control[name="city"]')
    COUNTRY_INPUT = (By.CSS_SELECTOR, '.form-control[name="country"]')
    JOB_POSITION_INPUT = (
        By.CSS_SELECTOR, '.form-control[name="job-position"]')
    COMPANY_INPUT = (By.CSS_SELECTOR, '.form-control[name="company"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '.btn.btn-outline-primary.mt-3')

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def fill_first_name(self, first_name):
        input_element = self.driver.find_element(*self.FIRST_NAME_INPUT)
        input_element.clear()
        input_element.send_keys(first_name)

    def fill_last_name(self, last_name):
        input_element = self.driver.find_element(*self.LAST_NAME_INPUT)
        input_element.clear()
        input_element.send_keys(last_name)

    def fill_address(self, address):
        input_element = self.driver.find_element(*self.ADDRESS_INPUT)
        input_element.clear()
        input_element.send_keys(address)

    def fill_email(self, email):
        input_element = self.driver.find_element(*self.EMAIL_INPUT)
        input_element.clear()
        input_element.send_keys(email)

    def fill_phone_number(self, phone_number):
        input_element = self.driver.find_element(*self.PHONE_NUMBER_INPUT)
        input_element.clear()
        input_element.send_keys(phone_number)

    def fill_zip_code(self, zip_code):
        input_element = self.driver.find_element(*self.ZIP_CODE_INPUT)
        input_element.clear()
        input_element.send_keys(zip_code)

    def fill_city(self, city):
        input_element = self.driver.find_element(*self.CITY_INPUT)
        input_element.clear()
        input_element.send_keys(city)

    def fill_country(self, country):
        input_element = self.driver.find_element(*self.COUNTRY_INPUT)
        input_element.clear()
        input_element.send_keys(country)

    def fill_job_position(self, job_position):
        input_element = self.driver.find_element(*self.JOB_POSITION_INPUT)
        input_element.clear()
        input_element.send_keys(job_position)

    def fill_company(self, company):
        input_element = self.driver.find_element(*self.COMPANY_INPUT)
        input_element.clear()
        input_element.send_keys(company)

    def click_submit_button(self):
        button_element = self.driver.find_element(*self.SUBMIT_BUTTON)
        # Прокрутим страницу до кнопки
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", button_element)
        # Подождём полсекунды, чтобы элемент стал доступным
        time.sleep(0.5)
        # Используем ActionChains для надёжного клика
        ActionChains(self.driver).move_to_element(
            button_element).pause(0.1).click().perform()
