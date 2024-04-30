from PageObjects.LoginPage import *
from PageObjects.OrganizationPage import *
from selenium import webdriver
import pytest
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from Utilities.BaseClass import BaseClass
from TestData.LoginData import LoginData



class TestLogin(BaseClass):




    def test_login_with_incorrect_credentails(self):
        loginObj = LoginPage(self.dr)
        loginObj.enterUsername(LoginData.cred[self.reg + 'username'])

        loginObj.enterPassword('123456')

        loginObj.clickLogin()

        message = loginObj.validation_message
        wait1 = wait.WebDriverWait(self.dr, 10)
        wait1.until(expected_conditions.presence_of_element_located((loginObj.validation_message)))
        self.dr.get_screenshot_as_file(self.filelocation + 'LoginValidation' + self.reg + '.png')
        assert loginObj.validation_message

    def test_login_with_correct_credentails(self):
        loginObj = LoginPage(self.dr)
        loginObj.enterUsername(LoginData.cred[self.reg+'username'])

        loginObj.enterPassword(LoginData.cred[self.reg+'password'])
        self.dr.get_screenshot_as_file(self.filelocation + 'LoginScreen' + self.reg + '.png')
        objOrg=loginObj.clickLogin()
        wait1 = wait.WebDriverWait(self.dr, 20)
        wait1.until(expected_conditions.presence_of_element_located((objOrg.organization_save_button)))
        self.dr.get_screenshot_as_file(self.filelocation + 'LoginSuccess' + self.reg + '.png')


