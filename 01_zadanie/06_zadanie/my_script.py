from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome()

wait = WebDriverWait(driver, 30, 10)

driver.maximize_window()
driver.get("http://uitestingplayground.com/ajax")
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
text_from_content = wait.until(EC.visibility_of_element_located((
    By.CSS_SELECTOR, '.bg-success'))).text
print(text_from_content)
