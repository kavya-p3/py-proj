import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions

from TestData.LoginData import loginData
from TestData.RegistrationData import *
from Utilities.BaseClass import BaseClass


class RegistrationPage:
    def __init__(self, dr, reg,location):
        self.dr = dr
        self.reg = reg
        self.filelocation = location+ '\\'
        self.data = RegistrationData()

    firstname = (By.XPATH, '//input[@placeholder="Enter First Name"]')
    lastname = (By.XPATH, '//input[@placeholder="Enter Last Name"]')
    email_address = (By.XPATH, '//input[@placeholder="Enter Email Address"]')
    confirm_email_address = (By.XPATH, '//input[@placeholder="Enter Confirm Email Address"]')
    contact_number = (By.XPATH, '//input[@placeholder="Enter Contact No"]')
    username = (By.XPATH, '//input[@placeholder="Enter User Name"]')
    organization_name = (By.XPATH, '//input[@placeholder="Enter data..."]')
    success_registration_mesg = (By.XPATH, '//p[text()="Email has been sent to your registered email address."]')
    resend_email_button = (By.XPATH, '//span[text()="RESEND EMAIL"]')
    submit = (By.XPATH, '//span[text()="Submit"]')
    tin = (By.XPATH, '//label[text()="TIN"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    confirm_tin = (By.XPATH, '//label[text()="Confirm TIN"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    mips_checkbox = (By.XPATH, '//input[@type="checkbox"]')


    def fillRegistrationForm(self):

        wait1 = wait.WebDriverWait(self.dr, 10)
        wait1.until(expected_conditions.presence_of_element_located((RegistrationPage.firstname)))

        self.dr.find_element(*RegistrationPage.firstname).send_keys(self.data.reg['first_name'])
        self.dr.find_element(*RegistrationPage.lastname).send_keys(self.data.reg['last_name'])
        email_address = self.reg + "_" + self.data.reg['email_address']
        self.dr.find_element(*RegistrationPage.email_address).send_keys(email_address)
        self.dr.find_element(*RegistrationPage.confirm_email_address).send_keys(
            email_address)
        self.dr.find_element(*RegistrationPage.contact_number).send_keys(self.data.reg['contact_no'])
        self.dr.find_element(*RegistrationPage.organization_name).send_keys(
            'hns' + " " + self.data.reg['org_name'])
        username = self.reg + "_" + self.data.reg['username']

        self.dr.find_element(*RegistrationPage.username).send_keys(username)
        if 'elixir' in self.reg or 'polaris' in self.reg :
            tin= str(random.randrange(100000000,999999999))
            self.dr.find_element(*RegistrationPage.tin).send_keys(tin)
            self.dr.find_element(*RegistrationPage.confirm_tin).send_keys(tin)
            if self.reg != 'polaris':
                self.dr.find_element(*RegistrationPage.mips_checkbox).click()

        self.dr.get_screenshot_as_file(self.filelocation + 'Registration'+self.reg+'.png')
        wait2 = wait.WebDriverWait(self.dr, 30)
        wait2.until(expected_conditions.presence_of_element_located((RegistrationPage.resend_email_button)))
        assert self.dr.find_element(*RegistrationPage.resend_email_button)
        f = open("registeredusers.txt", "a")
        f.write('\n'+username+"-"+self.reg)
        f.close()


