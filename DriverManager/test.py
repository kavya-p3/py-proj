from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import keyword

dr = webdriver.Chrome(ChromeDriverManager().install())
dr.get("https://qa-pegasus2-apta.figmd.com/signup/login")
time.sleep(15)
dr.find_element_by_name("TextField").send_keys("kavyaApta6")
dr.find_element_by_name("password").send_keys("Abcd1234#")
#dr.find_element_by_css_selector("button.MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary").click()
#dr.find_element_by_class_name("MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary").click()
#dr.find_element_by_class_name("MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary").get_attribute()
dr.find_element_by_xpath("//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary']").click()
time.sleep(20)
pname = dr.find_element_by_xpath("//body/div[@id='root']/div/div/div/main/div/div/div/div/div/div/div/div/div/div[@id='panel1c-content']/div/div/div/div/div/div[1]/div[1]/div[1]/div[1]/input[1]")
pnumber = dr.find_element_by_xpath("//body/div[@id='root']/div/div/div/main/div/div/div/div/div/div/div/div/div/div[@id='panel1c-content']/div/div/div/div/div/div[2]/div[1]/div[1]/div[1]/input[1]")
pbuilding = dr.find_element_by_xpath("//body//div[@id='root']//div//div//div//div//div//div//div//div//div//div//div[2]//div[2]//div[1]//div[1]//input[1]")
pzipcode = dr.find_element_by_xpath("//body//div[@id='root']//div//div//div//div//div//div//div//div//div//div//div[2]//div[3]//div[1]//div[1]//input[1]")
save = dr.find_element_by_xpath("//body/div[@id='root']/div/div/div/main/div/div/div/div/div/div/div/div/div/div[@id='panel1c-content']/div/div/div/div/div/div/button[1]")
pname.send_keys(Keys.CONTROL+"a")
pname.send_keys(Keys.DELETE)
pnumber.send_keys(Keys.CONTROL+"a")
pnumber.send_keys(Keys.DELETE)
pbuilding.send_keys(Keys.CONTROL+"a")
pbuilding.send_keys(Keys.DELETE)
pzipcode.clear()
pname.send_keys("Hosp\' \" , & . -")
pnumber.send_keys("6th floor (B2.1) wing symphony it park nanded city")
pbuilding.send_keys("Pandurang layout sinhagad")
pzipcode.send_keys("12345")
save.click()
success = dr.find_element_by_xpath("//body/div[@id='root']/div/div/div/div[2]")

