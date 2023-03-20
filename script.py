import sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
options = Options()
arr = sys.argv[1]
print(type(arr))
arr.replace('[\'', '')
arr.replace('\']', '')
# path=arr[0]
print(arr)

# options.headless = True
# driver = webdriver.Firefox(options=options)
# driver.get(path)
# length=len(arr)
# print('lengthis',length)
# for i in range(1,length):
#     try:
#         element = driver.find_element(By.ID, arr[i])
#         assert element.is_displayed()
#         if element.is_displayed():
#             print("The element ",arr[i], " was found!")
#     except NoSuchElementException:
#         print("The element ",arr[i]," was not found!")

# driver.quit()