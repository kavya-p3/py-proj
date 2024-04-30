from selenium import webdriver


def test_setup():
    global dr
    dr = webdriver.Chrome(executable_path='C:/Users/kp/PycharmProjects/Sem/Drivers/chromedriver.exe')
    dr.implicitly_wait(10)
    dr.maximize_window()


def test_login():
    dr.get("https://opensource-demo.orangehrmlive.com/")

    dr.find_element_by_id('txtUsername').send_keys('Admin')
    dr.find_element_by_id('txtUsername').clear()
    dr.find_element_by_id('txtPassword').send_keys('admin123')
    dr.find_element_by_id('btnLogin').click()


def test_teardown():
    dr.close()
    dr.quit()
    print("test completed")
