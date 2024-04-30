import allure

from PageObjects.AgreementPage import AgreementPage
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
class TestLogin:
    pass
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_login(self):
    #     loginObj = LoginPage(self.dr, self.reg, self.filelocation)
    #     orgobj = loginObj.loginwithcurrectcredentials()
    #     orgobj.fillorganization()
    #     orgobj.addContact()
    #     orgobj.addTin()
    #     techobj = orgobj.clickNext()
    #     techobj.submitOrgData()
    #     clini = techobj.clickNext()
    #     clini.add_clinician()
    #     clini.add_location()
    #     agree = clini.clickNext()
    #     agree.signAgreement()

