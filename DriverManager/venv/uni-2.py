import unittest
import HtmlTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):
    def test_ser(self):
        self.dr = webdriver.Chrome(ChromeDriverManager().install())
        self.dr.implicitly_wait(10)
        self.dr.maximize_window()
        self.dr.get("https://www.amazon.in/")
        self.dr.find_element_by_id('twotabsearchtextbox').send_keys('auto')
        self.dr.find_element_by_class_name('nav-input').click()


if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output='C:/Users/kp/PycharmProjects/DriverManager/venv/reportss',verbosity=2))