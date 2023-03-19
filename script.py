import sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
options = Options()
path=sys.argv[1]
id=sys.argv[2]
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get(path)
element = driver.find_element(By.ID, id)
assert element.is_displayed()
try:
    if element.is_displayed():
        print("The element was found!")
except NoSuchElementException:
    print("The element was not found!")
driver.quit()