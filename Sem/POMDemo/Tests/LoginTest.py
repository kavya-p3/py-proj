import unittest

from selenium import webdriver
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POMDemo.Pages.homePage import HomePage
from POMDemo.Pages.loginPage import LoginPage


class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome(executable_path = 'C:/Users/kp/PycharmProjects/Sem/Drivers/chromedriver.exe')
        cls.dr.implicitly_wait(10)
        cls.dr.maximize_window()


    def test_login_valid(self):

        dr = self.dr
        dr.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(dr)
        login.enter_username("Admin")
        login.enter_password('admin123')
        login.click_loginbutton()
        home = HomePage(dr)
        home.click_welcome()
        home.click_logout()


        # self.dr.find_element_by_id('txtUsername').send_keys('Admin')
        # self.dr.find_element_by_id('txtPassword').send_keys('admin123')
        # self.dr.find_element_by_id('btnLogin').click()
        # self.dr.find_element_by_id('welcome').click()
        # time.sleep(3)
        # self.dr.find_element_by_link_text('Logout').click()

    @classmethod
    def tearDownClass(cls):
        cls.dr.close()
        cls.dr.quit()
        print("DONNEEE")


if __name__=='__main__':
    unittest.main()
