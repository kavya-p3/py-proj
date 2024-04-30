from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions

from PageObjects.OrganizationPage import OrganizationPage
from PageObjects.RegistrationPage import RegistrationPage
from TestData.LoginData import loginData
from Utilities.BaseClass import BaseClass


class LoginPage:
    def __init__(self, dr,reg,filelocation):
        self.dr = dr
        self.reg = reg
        self.filelocation = filelocation+'\\'

    username = (By.NAME, "TextField")
    password = (By.NAME, "password")
    loginbutton = (By.XPATH, "//span[text()='Login']")
    continuebutton = (By.XPATH, '//span[text()="Continue"]')
    register_here_link = (By.XPATH, '//span[text()="Register here"]')
    aan_nonmember_link =(By.XPATH,'//span[text()="Signup as a non member"]')
    data = loginData()




    def loginwithcurrectcredentials(self):

        wait2 = wait.WebDriverWait(self.dr, 15)
        wait2.until(expected_conditions.presence_of_element_located((LoginPage.username)))
        self.dr.find_element(*LoginPage.username).send_keys(LoginPage.data.cred[self.reg + 'username'])
        if self.reg == 'aan':
            self.dr.find_element(*LoginPage.continuebutton).click()
        wait1 = wait.WebDriverWait(self.dr, 10)
        wait1.until(expected_conditions.presence_of_element_located((LoginPage.password)))
        self.dr.find_element(*LoginPage.password).send_keys(LoginPage.data.cred[self.reg + 'password'])

        self.dr.get_screenshot_as_file(self.filelocation+'Login.png')
        self.dr.find_element(*LoginPage.loginbutton).click()
        orgObject = OrganizationPage(self.dr,self.reg,self.filelocation)
        return orgObject

    def clickRegisterNewUserLink(self):
        wait2 = wait.WebDriverWait(self.dr, 15)
        if self.reg == 'aan':
            wait2.until(expected_conditions.presence_of_element_located((LoginPage.aan_nonmember_link)))
            self.dr.find_element(*LoginPage.aan_nonmember_link).click()
        else:
            wait2.until(expected_conditions.presence_of_element_located((LoginPage.register_here_link)))
            self.dr.find_element(*LoginPage.register_here_link).click()
        regObj = RegistrationPage(self.dr, self.reg, self.filelocation)

        return regObj


