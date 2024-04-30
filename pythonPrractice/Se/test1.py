import time

from selenium import webdriver
from selenium.webdriver.chrome.options import  Options

co = Options()
co.add_argument("--headless")
dr = webdriver.Chrome(options=co, executable_path="C:/Users/kp/Downloads/chromedriver_win32 (2)/chromedriver.exe")

dr.get("https://qa-pegasus2-apta.figmd.com/signup/login")
dr.get("https://google.com")
print(dr.title)
dr.find_element_by_name("TextField").send_keys("kavyaApta")
dr.find_element_by_name("password").send_keys("Abcd1234#")
dr.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[3]/div/div/div[2]/div[3]/div[1]/button").cl
dr.close()
dr.quit()
print("completed")

