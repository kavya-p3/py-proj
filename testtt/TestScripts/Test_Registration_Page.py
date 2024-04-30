from TestData.LoginData import loginData
from PageObjects.LoginPage import *
from PageObjects.OrganizationPage import *
from selenium import webdriver
import pytest
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from Utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
class TestRegistration:


        def test_Registration(self):
            loginObj = LoginPage(self.dr, self.reg, self.filelocation)
            regObj = loginObj.clickRegisterNewUserLink()
            regObj.fillRegistrationForm()

