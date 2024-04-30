from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'Pixel3XL'
desired_caps['app'] = ('C:/Users/kp/Downloads/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
ele = dr.find_element_by_id('com.code2lead.kwad:id/EnterValue')
ele.click()