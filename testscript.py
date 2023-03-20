from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.seleniumframework.com/Practiceform/")
element = driver.find_element(By.ID, "button1")
assert element.is_displayed()
if element.is_displayed():
    print("The button was found!")
driver.quit()