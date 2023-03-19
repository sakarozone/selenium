import sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
options = Options()
path=sys.argv[1]
id=sys.argv[2]
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get(path)
element = driver.find_element(By.ID, id)
assert element.is_displayed()
if element.is_displayed():
    print("The element was found!")
else :
    print("The element was not found!")
driver.quit()