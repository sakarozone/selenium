import sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
options = Options()
path=sys.argv[1]
id=sys.argv[2]
options.add_argument("--headless=new")
driver = webdriver.Firefox(options=options)
driver.get(path)
element = driver.find_element(By.ID, id)
assert element.is_displayed()
if element.is_displayed():
    print("The button was found!")
driver.quit()