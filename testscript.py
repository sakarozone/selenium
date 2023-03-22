from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get("http://www.seleniumframework.com/Practiceform/")
driver.find_element_by_id("alert").click()
try:
    WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

    alert = driver.switch_to.alert
    alert.accept()
    print("Alert has been raised")
except TimeoutException:
    print("No alert")