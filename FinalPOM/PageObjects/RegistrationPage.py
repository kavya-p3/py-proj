import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions

from TestData.LoginData import LoginData
from TestData.RegistrationData import *
from Utilities.BaseClass import BaseClass


class RegistrationPage:
    def __init__(self, dr):
        self.dr = dr


    firstname = (By.XPATH, '//input[@placeholder="Enter First Name"]')
    lastname = (By.XPATH, '//input[@placeholder="Enter Last Name"]')
    email_address = (By.XPATH, '//input[@placeholder="Enter Email Address"]')
    confirm_email_address = (By.XPATH, '//input[@placeholder="Enter Confirm Email Address"]')
    contact_number = (By.XPATH, '//input[@placeholder="Enter Contact No"]')
    username = (By.XPATH, '//input[@placeholder="Enter User Name"]')
    organization_name = (By.XPATH, '//input[@placeholder="Enter data..."]')
    acep_org_name = (By.XPATH, '(//input[@placeholder="Enter data..."])[2]')
    success_registration_mesg = (By.XPATH, '//p[text()="Email has been sent to your registered email address."]')
    resend_email_button = (By.XPATH, '//span[text()="RESEND EMAIL"]')
    submit = (By.XPATH, '//span[text()="Submit"]')
    tin = (By.XPATH, '//label[text()="TIN"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    confirm_tin = (By.XPATH, '//label[text()="Confirm TIN"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    mips_checkbox = (By.XPATH, '//input[@type="checkbox"]')
    #Acep specific
    org_type = (By.XPATH, '//div[text()="Select Organization Type"]/ancestor::div//input[@id="react-select-2-input"]')
    zip = (By.XPATH,'(//label[text()="Zip Code"]/ancestor::div/div/input)[2]')
    #Validation
    same_orgName_message=(By.XPATH,'//p[text()="Organization with a similar name already exist."]')
    submit = (By.XPATH, '//span[text()="Submit"]')
    orgErrormesg = (By.XPATH,"//p[contains(text(),'Only alphabets, numbers, and special characters')]")

    # def fillRegistrationForm(self):
    #
    #     wait1 = wait.WebDriverWait(self.dr, 10)
    #     wait1.until(expected_conditions.presence_of_element_located((RegistrationPage.firstname)))
    #
    #     self.dr.find_element(*RegistrationPage.firstname).send_keys(self.data.reg['first_name'])
    #     self.dr.find_element(*RegistrationPage.lastname).send_keys(self.data.reg['last_name'])
    #     email_address = self.reg + "_" + self.data.reg['email_address']
    #     self.dr.find_element(*RegistrationPage.email_address).send_keys(email_address)
    #     self.dr.find_element(*RegistrationPage.confirm_email_address).send_keys(
    #         email_address)
    #     self.dr.find_element(*RegistrationPage.contact_number).send_keys(self.data.reg['contact_no'])
    #     self.dr.find_element(*RegistrationPage.organization_name).send_keys(
    #         self.reg + " " + self.data.reg['org_name'])
    #     username = self.reg + "_" + self.data.reg['username']
    #
    #     self.dr.find_element(*RegistrationPage.username).send_keys(username)
    #     if self.reg in ['polaris', 'emds-elixir', 'unifirmd-elixir', 'flexmedical-elixir','ecw-elixir','compulink-elixir']:
    #         self.dr.find_element(*RegistrationPage.tin).send_keys(self.data.reg['tin'])
    #         self.dr.find_element(*RegistrationPage.confirm_tin).send_keys(self.data.reg['tin'])
    #         if self.reg != 'polaris':
    #             self.dr.find_element(*RegistrationPage.mips_checkbox).click()
    #
    #     self.dr.get_screenshot_as_file(self.filelocation + 'Registration'+self.reg+'.png')
    #     wait2 = wait.WebDriverWait(self.dr, 30)
    #     wait2.until(expected_conditions.presence_of_element_located((RegistrationPage.resend_email_button)))
    #     assert self.dr.find_element(*RegistrationPage.resend_email_button)
    #     f = open("registeredusers.txt", "a")
    #     f.write('\n'+username+"-"+self.reg)
    #     f.close()
    def enterFirstname(self,name):
        self.dr.find_element(*RegistrationPage.firstname).send_keys(name)

    def enterLastName(self,name):
        self.dr.find_element(*RegistrationPage.lastname).send_keys(name)

    def enterEmailAddressAndConfirmEmailAddress(self,email):
        self.dr.find_element(*RegistrationPage.email_address).send_keys(email)
        upper=email.upper()
        self.dr.find_element(*RegistrationPage.confirm_email_address).send_keys(upper)

    def enterContactNumber(self,num):
        self.dr.find_element(*RegistrationPage.contact_number).send_keys(num)

    def enterOrganizationName(self,name):

        self.dr.find_element(*RegistrationPage.organization_name).send_keys(name)
    def enterAcepOrganizationName(self,name):
        self.dr.find_element(*RegistrationPage.acep_org_name).send_keys(name)
    def enterUserName(self,name):
        self.dr.find_element(*RegistrationPage.username).send_keys(name)

    def enterTinAndConfirmTin(self,tin):
        self.dr.find_element(*RegistrationPage.tin).send_keys(tin)
        self.dr.find_element(*RegistrationPage.confirm_tin).send_keys(tin)

    def clickMipsCheckbox(self):
        self.dr.find_element(*RegistrationPage.mips_checkbox).click()

    def enterZip(self,zip):
        self.dr.find_element(*RegistrationPage.zip).send_keys(zip)

    def enterOrgType(self):
        self.dr.find_element(*RegistrationPage.org_type).send_keys('Phy')
        act = ActionChains(self.dr)
        act.key_down(Keys.ENTER).perform()

    def clickSubmit(self):
        self.dr.find_element(*RegistrationPage.submit).click()
