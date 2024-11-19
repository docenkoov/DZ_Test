from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Найти строку поиска и ввести "Selenium"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")

# Нажать Enter для выполнения поиска
search_box.send_keys(Keys.RETURN)

driver.quit()
