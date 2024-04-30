from selenium import webdriver
import time
import pytest

from utilities.BaseClass import BaseClass
from TestData.loginData import loginData
from PageObjects.Login_page_objects import LoginObj


class TestLogin(BaseClass):

    def test_login(self):
        data = loginData()
        login = LoginObj(self.dr)

        login.getUsername().send_keys(data.cred["username"])
        login.getUsername().clear()
        login.getPassword().send_keys(data.cred["password"])
        login.getLoginButton().click()


