import time

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions

from PageObjects.TechnicalSurveyPage import TechnicalSurveyPage
from TestData.OrganizationData import OrganizationData
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from Utilities.BaseClass import BaseClass


class OrganizationPage:
    def __init__(self, dr, reg,location):
        self.dr = dr
        self.reg = reg
        self.filelocation = location + '\\'

    # Organization details section
    number_Street = (By.XPATH,
                     '//label[text()="Number & Street"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    building_floor_suite = (By.XPATH,
                            '//label[text()="Building/Suite/Floor"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    zip = (By.XPATH,
           '//label[text()="Zip Code"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    organization_save_button = (By.XPATH, '//button/span[text()="SAVE"]')
    # additional organization section fields
    type = (By.XPATH, '//input[@id="react-select-2-input"]')

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Contact details section
    add_contact_button = (By.XPATH, "//span[text()='ADD CONTACT']")
    contact_first_name = (By.XPATH,
                          '//label[text()="First Name"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    contact_last_name = (By.XPATH,
                         '//label[text()="Last Name"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    contact_middle_name = (By.XPATH,
                           '//label[text()="Middle Name"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    contact_email_address = (By.XPATH,
                             '//label[text()="Email Address"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input[@placeholder="Enter data..."]')
    contact_phone_number = (By.XPATH,
                            '//label[text()="Phone No"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    contact_phone_extn = (By.XPATH,
                          '//label[text()="Phone No Extn"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    contact_alternate_number = (By.XPATH,
                                '//label[text()="Alternate Phone No"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    contact_alternate_extn = (By.XPATH,
                              '//label[text()="Alternate Phone No Extn"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    contact_save_button = (By.XPATH, '//button/span[text()="Save"]')
    # additional contact section fields
    contact_role = (By.XPATH,
                    '//div[text()="Select Role"]/ancestor::div[@class="select__value-container select__value-container--is-multi css-1hwfws3"]/div/div/input')
    contact_type = (By.XPATH,
                    '//div[text()="Select Contact Type"]/ancestor::div[@class="select__value-container css-1hwfws3"]/div/div/input')

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # tin details section
    add_tin_button = (By.XPATH, "//span[text()='ADD TAX IDENTIFICATION NUMBER']")
    tin_number = (By.XPATH, '//label[contains(text(),"Tax Identification Number")]/following-sibling::div/input')
    valid_from = (By.XPATH, '//label[text()="Valid From"]/following-sibling::div/input')
    valid_to = (By.XPATH, '//label[text()="Valid To"]/following-sibling::div/input')
    validation_to_date = (By.XPATH, '//p[text()="Valid To date should be greater than or equal to Jan 01 2021"]')
    tin_save = (By.XPATH, '//span[text()="Save"]')

    # common
    success_mesg = (By.XPATH, '//div[contains(text(),"Data")]')
    next = (By.XPATH, '//span[text()="Next"]')
    body = (By.TAG_NAME,"body")
    data = OrganizationData()

    def fillorganization(self):
        wait2 = wait.WebDriverWait(self.dr, 15)
        wait2.until(expected_conditions.presence_of_element_located((OrganizationPage.number_Street)))
        self.dr.find_element(*OrganizationPage.number_Street).send_keys(OrganizationPage.data.org['number&street'])
        self.dr.find_element(*OrganizationPage.building_floor_suite).send_keys(
            OrganizationPage.data.org['building/suite/floor'])
        self.dr.find_element(*OrganizationPage.zip).send_keys(OrganizationPage.data.org['zipcode'])

        if self.reg in ['hns', 'polaris', 'emds', 'compulink', 'aan']:
            self.dr.find_element(*OrganizationPage.type).send_keys(OrganizationPage.data.org['type'])
            act = ActionChains(self.dr)
            act.key_down(Keys.ENTER).perform()
        time.sleep(4)

        self.dr.find_element(*OrganizationPage.organization_save_button).click()
        wait2.until((expected_conditions.presence_of_element_located((OrganizationPage.success_mesg))))
        self.dr.get_screenshot_as_file(self.filelocation + 'Organization.png')
        assert OrganizationPage.success_mesg

    def addContact(self):

        self.dr.find_element(*OrganizationPage.add_contact_button).click()
        self.dr.find_element(*OrganizationPage.contact_first_name).send_keys(OrganizationPage.data.contact['FirstName'])
        self.dr.find_element(*OrganizationPage.contact_middle_name).send_keys(
            OrganizationPage.data.contact['MiddleName'])
        self.dr.find_element(*OrganizationPage.contact_last_name).send_keys(OrganizationPage.data.contact['LastName'])
        self.dr.find_element(*OrganizationPage.contact_email_address).send_keys(
            OrganizationPage.data.contact['email_address'])
        self.dr.find_element(*OrganizationPage.contact_phone_number).send_keys(
            OrganizationPage.data.contact['phone_number'])
        self.dr.find_element(*OrganizationPage.contact_phone_extn).send_keys(
            OrganizationPage.data.contact['phone_extn'])
        self.dr.find_element(*OrganizationPage.contact_alternate_number).send_keys(
            OrganizationPage.data.contact['alternate_number'])
        self.dr.find_element(*OrganizationPage.contact_alternate_extn).send_keys(
            OrganizationPage.data.contact['alt_extn'])
        self.dr.find_element(*OrganizationPage.contact_role).send_keys(OrganizationPage.data.contact['Role'])
        act1 = ActionChains(self.dr)
        act1.key_down(Keys.ENTER).perform()
        if self.reg in ['apta', 'acog', 'aan']:
            self.dr.find_element(*OrganizationPage.contact_type).send_keys(OrganizationPage.data.contact['Type'])
            act2 = ActionChains(self.dr)
            act2.key_down(Keys.ENTER).perform()

        self.dr.find_element(*OrganizationPage.contact_save_button).click()
        wait2 = wait.WebDriverWait(self.dr, 15)
        wait2.until(expected_conditions.presence_of_element_located((OrganizationPage.success_mesg)))
        self.dr.get_screenshot_as_file(self.filelocation + 'ADDContact.png')
        assert OrganizationPage.success_mesg

    def editContact(self):
        pass

    def deleteContact(self):
        pass

    def addTin(self):

        wait2 = wait.WebDriverWait(self.dr, 15)
        wait3 = wait.WebDriverWait(self.dr, 10, poll_frequency=1,
                                   ignored_exceptions=[ElementNotVisibleException, ElementNotInteractableException,NoSuchElementException])
        wait2.until(expected_conditions.presence_of_element_located((OrganizationPage.add_tin_button)))
        self.dr.find_element(*OrganizationPage.add_tin_button).click()
        wait1 = wait.WebDriverWait(self.dr, 10)
        wait1.until(expected_conditions.presence_of_element_located((OrganizationPage.tin_number)))

        self.dr.find_element(*OrganizationPage.tin_number).send_keys(OrganizationPage.data.tin['tin_number'])
        wait3.until(expected_conditions.presence_of_element_located((OrganizationPage.valid_from)))
        self.dr.find_element(*OrganizationPage.valid_from).send_keys(OrganizationPage.data.tin['valid_from'])
        self.dr.find_element(*OrganizationPage.valid_to).send_keys(OrganizationPage.data.tin['valid_to'])
        self.dr.find_element(*OrganizationPage.tin_save).click()
        wait2 = wait.WebDriverWait(self.dr, 15)
        wait2.until(expected_conditions.presence_of_element_located((OrganizationPage.success_mesg)))
        self.dr.get_screenshot_as_file(self.filelocation + 'ADDTin.png')
        self.dr.find_element(*OrganizationPage.body).screenshot(self.filelocation + 'ADDTin2.png')
        assert OrganizationPage.success_mesg

    def editTin(self):
        pass

    def deleteTin(self):
        pass

    def clickNext(self):
        time.sleep(10)

        # wait3 = wait.WebDriverWait(self.dr, 20, poll_frequency=1,
        #                            ignored_exceptions=[ElementNotVisibleException, ElementNotInteractableException,ElementClickInterceptedException,NoSuchElementException])
        # wait3.until(expected_conditions.element_to_be_clickable((OrganizationPage.add_tin_button)))

        self.dr.find_element(*OrganizationPage.next).click()

        techSurvey = TechnicalSurveyPage(self.dr, self.reg, self.filelocation)
        return techSurvey

    def checkTinValidationMessage(self):
        wait2 = wait.WebDriverWait(self.dr, 15)
        wait2.until(expected_conditions.presence_of_element_located((OrganizationPage.add_tin_button)))
        self.dr.find_element(*OrganizationPage.add_tin_button).click()
        wait1 = wait.WebDriverWait(self.dr, 10)
        wait1.until(expected_conditions.presence_of_element_located((OrganizationPage.tin_number)))
        self.dr.find_element(*OrganizationPage.tin_number).send_keys(OrganizationPage.data.tin['tin_number'])
        wait1.until(expected_conditions.presence_of_element_located((OrganizationPage.valid_from)))
        self.dr.find_element(*OrganizationPage.valid_from).send_keys(OrganizationPage.data.tin['valid_from'])
        self.dr.find_element(*OrganizationPage.valid_to).send_keys(OrganizationPage.data.tin['valid_to'])
        self.dr.find_element(*OrganizationPage.tin_save).click()
        assert self.dr.find_element(*OrganizationPage.validation_to_date)
        self.dr.get_screenshot_as_file(self.filelocation + 'TinValidationMessage'+self.reg+'.png')




