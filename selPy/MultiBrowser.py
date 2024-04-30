import time
from selenium import webdriver

#driver = webdriver.Firefox(executable_path="K:/geckodriver.exe")
#driver.get("https://www.google.com")
#print(driver.title)
#driver.maximize_window()

driver = webdriver.Chrome(executable_path="K:/chromedriver.exe")
driver.get("https://www.facebook.com")
print(driver.title)
driver.maximize_window()
time.sleep(10)
driver.find_element_by_name('websubmit').click()