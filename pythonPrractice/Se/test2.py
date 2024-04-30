from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

dr = webdriver.Chrome(ChromeDriverManager().install())
dr.get("Https://google.com")
