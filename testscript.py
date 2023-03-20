from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get("http://www.seleniumframework.com/Practiceform/")
element = driver.find_element(By.ID, "button1")
assert element.is_displayed()
if element.is_displayed():
    print("The button was found!")
driver.quit()